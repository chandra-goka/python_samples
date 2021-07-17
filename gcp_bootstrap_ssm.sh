#!/usr/bin/env bash

request_cmd=$([[ -x "$(command -v curl)" ]] && echo "curl_request" || echo "wget_request")
download_cmd=$([[ -x "$(command -v curl)" ]] && echo "curl -sSO" || echo "wget -q")

GOSS_ENDPOINT="https://api.goss.vdo.manage.rackspace.com/v1.0/instance/goss"

JWT_TOKEN="{jwt_token}"

UNABLE_TO_ACTIVATE=1
JOB_RETRIEVE_FAILURE=2
NO_JOB_FOUND=3
OS_UNSUPPORTED=4

find_value() {
  local key="$1"
  if [[ -f /etc/centos-release ]]; then
      [[ "${key}" == "ID" ]] && echo "centos" && return
      if [[ "${key}" == "VERSION_ID" ]]; then
        local version
        version=$(awk '{ for (i=1; i<=NF; ++i) { if ($i ~ /[0-9]/) print $i } }' /etc/centos-release)
        IFS='.' read -ra versionArr <<< "$version"
        echo "${versionArr[0]}.${versionArr[1]}"
        return
      fi
  fi
  if [[ -f /etc/redhat-release ]]; then
      [[ "${key}" == "ID" ]] && echo "rhel" && return
      [[ "${key}" == "VERSION_ID" ]] && awk '{ for (i=1; i<=NF; ++i) { if ($i ~ /[0-9]/) print $i } }' /etc/redhat-release && return
  fi
  [[ -f /etc/os-release ]] && awk "/^$key=/" /etc/os-release | sed "s/\($key=\"\?\|\"$\)//g" && return
}

distro=$(find_value ID)
distro_version=$(find_value VERSION_ID)

has_instance_id() {
  regfile="/var/lib/amazon/ssm/Vault/Store/RegistrationKey"
  if [[ -f "$regfile" ]] && \
    [[ $(grep -c '"instanceID":"mi-' "$regfile") -eq 1 ]]; then
    my_id=$(ssm-cli get-instance-information | sed 's/"[:|,]"/ /g' | awk '{print $2}')
    if [[ $my_id == mi-* ]]; then
      return 0
    else
      return 1
    fi
  fi
  return 1
}

wget_request() {
  # $1 = url
  # $2 = header
  # $3 (optional) = HTTP Method
  optional_post_argument=$([[ $# -gt 2 ]] && echo '--post-data ""'|| echo "")
  wget -q --save-header -O- "$1" "--header=$2"
}


curl_request() {
  # $1 = url
  # $2 = header
  # $3 (optional) = HTTP Method
  optional_post_argument=$([[ $# -gt 2 ]] && echo "--request POST"|| echo "")
  curl --location -s -D - "$1" -H "$2" $optional_post_argument
}

send_error() {
  # $1 = error code

  echo "Sending error to goss with error code: $1"
  error_endpoint="$GOSS_ENDPOINT/error/$1"
  $request_cmd "$error_endpoint" "X-Auth-Token: $JWT_TOKEN" "POST"
}

install_generic() {
    local bin_url="$1"
    local install_cmd="$2"
    # The start/stop commands should be available globally
    svc_stop_cmd="$3"
    svc_start_cmd="$4"
    local svc_status_cmd="$5"
    if [[ $($svc_status_cmd) == 0 ]]; then
      echo "SSM Agent already installed"
    else
      [[ ! -d /tmp/ssm ]] && mkdir /tmp/ssm
      cd /tmp/ssm || :
      echo "Running: $download_cmd $bin_url"
      $download_cmd "${bin_url}"
      echo "Running $install_cmd"
      $install_cmd
      echo "Running $svc_start_cmd"
      $svc_start_cmd
      if [[ "$?" != 0 ]]; then
        echo "Failed to start the amazon-ssm-agent service."
        # This is likely due to the OS being unsupported
        send_error $OS_UNSUPPORTED
        exit 1
      fi

      echo "Running $svc_stop_cmd"
      $svc_stop_cmd
    fi
}

install_ubuntu() {
    local bin_url="https://s3.amazonaws.com/ec2-downloads-windows/SSMAgent/latest/debian_amd64/amazon-ssm-agent.deb"
    local install_cmd="dpkg -i /tmp/ssm/amazon-ssm-agent.deb"
    svc_stop_cmd="service amazon-ssm-agent stop"
    svc_start_cmd="service amazon-ssm-agent start"
    local svc_status_cmd="service amazon-ssm-agent status"
    install_generic "$bin_url" "$install_cmd" "$svc_stop_cmd" "$svc_start_cmd" "$svc_status_status"
}

install_rhel6() {
    local bin_url="https://s3.amazonaws.com/ec2-downloads-windows/SSMAgent/latest/linux_amd64/amazon-ssm-agent.rpm"
    local install_cmd="yum install -y /tmp/ssm/amazon-ssm-agent.rpm"
    svc_stop_cmd="stop amazon-ssm-agent"
    svc_start_cmd="start amazon-ssm-agent"
    local svc_status_status="service amazon-ssm-agent status"
    install_generic "$bin_url" "$install_cmd" "$svc_stop_cmd" "$svc_start_cmd" "$svc_status_status"
}

install_rhel7() {
    local bin_url="https://s3.amazonaws.com/ec2-downloads-windows/SSMAgent/latest/linux_amd64/amazon-ssm-agent.rpm"
    local install_cmd="yum install -y /tmp/ssm/amazon-ssm-agent.rpm"
    svc_stop_cmd="systemctl stop amazon-ssm-agent"
    svc_start_cmd="systemctl start amazon-ssm-agent"
    local svc_status_status="systemctl status amazon-ssm-agent"
    install_generic "$bin_url" "$install_cmd" "$svc_stop_cmd" "$svc_start_cmd" "$svc_status_status"
}

install_sles() {
    local bin_url="https://s3.amazonaws.com/ec2-downloads-windows/SSMAgent/latest/linux_amd64/amazon-ssm-agent.rpm"
    local install_cmd="rpm --install /tmp/ssm/amazon-ssm-agent.rpm"
    svc_stop_cmd="systemctl stop amazon-ssm-agent"
    svc_start_cmd="systemctl start amazon-ssm-agent"
    local svc_status_status="systemctl status amazon-ssm-agent"
    install_generic "$bin_url" "$install_cmd" "$svc_stop_cmd" "$svc_start_cmd" "$svc_status_status"
}

install_debian() {
    local bin_url="https://s3.amazonaws.com/ec2-downloads-windows/SSMAgent/latest/debian_amd64/amazon-ssm-agent.deb"
    local install_cmd="sudo dpkg -i /tmp/ssm/amazon-ssm-agent.deb"
    svc_stop_cmd="systemctl stop amazon-ssm-agent"
    svc_start_cmd="systemctl start amazon-ssm-agent"
    local svc_status_status="systemctl status amazon-ssm-agent"
    install_generic "$bin_url" "$install_cmd" "$svc_stop_cmd" "$svc_start_cmd" "$svc_status_status"
}

install_ssm() {
  case $distro in
      ubuntu)
          install_ubuntu
          ;;
      centos|rhel)
          if [[ "${distro_version}" == 6* ]]; then
            install_rhel6
          else
            install_rhel7
          fi
          ;;
      sles)
            install_sles
          ;;
      debian)
            install_debian
          ;;
      *)
          echo "Operating System unsupported."
          send_error $OS_UNSUPPORTED
          exit 1
          ;;
  esac
}

activate_ssm() {
  # $1 = activation_id
  # $2 = activation_code
  # $3 = region
  echo "Stopping the SSM agent."
  $svc_stop_cmd

  echo "Registering the SSM agent."
  amazon-ssm-agent -y -register -code "$2" -id "$1" -region "$3" > /dev/null

  echo "Starting the SSM agent."
  $svc_start_cmd

  if [[ "$?" != 0 ]]; then
    echo "Failed to start the amazon-ssm-agent service."
    send_error $OS_UNSUPPORTED
    exit 1
  fi
}

get_header_from_response() {
  # $1 Raw response from http request
  echo "$1" | sed '/^\s*$/q'
}

get_body_from_response() {
  # $1 Raw response from http request
  echo "$1" | sed '1,/^\s*$/d'
}

get_response_status_code() {
  echo "$1" | head -1 | grep -Eo '[0-9][0-9][0-9]'
}

get_job_location() {
  echo "$1" | tr -d '\r' | awk '/^[lL]ocation: /{print $2}'
}

get_job_count() {
  # $1 = Response JSON of GET job request
  echo "$1" | tr -d '\r' | grep -Eo "\"currentItemCount\":[0-9]+" | awk -F\: '{print $2}'
}

get_job_status() {
  # $1 = Response JSON of GET job request
  echo "$1" | tr -d '\r' | grep -Eo "\"status\":[^,]+" | head -1 | awk -F\: '{print $2}' | tr -d '"'
}

get_activation_id() {
  # $1 = Response JSON of GET job request
  echo "$1" | tr -d '\r' | grep -Eo "\"activation_id\":[^,]+" | head -1 | awk -F\: '{print $2}' | tr -d '"'
}

get_activation_code() {
  # $1 = Response JSON of GET job request
  echo "$1" | tr -d '\r' | grep -Eo "\"activation_code\":[^,]+" | head -1 | awk -F\: '{print $2}' | tr -d '"'
}

get_region() {
  # $1 = Response JSON of GET job request
  echo "$1" | tr -d '\r' | grep -Eo "\"region\":[^,]+" | head -1 | awk -F\: '{print $2}' | tr -d '"'
}

if has_instance_id; then
  echo "Instance Id already exists, do not re-run the activation."
  exit 0
fi

install_ssm

echo "Creating a GOSS job to create an activation code"

activation_endpoint="$GOSS_ENDPOINT/activate"

activation_job_response=$($request_cmd $activation_endpoint "X-Auth-Token: $JWT_TOKEN" "POST")

activation_status=$(get_response_status_code "$activation_job_response")

if [[ $activation_status != 2* ]]
then
  echo "Got a non-successful response when getting activation code."
  send_error $UNABLE_TO_ACTIVATE
  exit 1
fi
echo "Activation Job Response: $activation_job_response"
job_location=$(get_job_location "$activation_job_response")

# Up to 10 retries
for NUM in 1 2 3 4 5 6 7 8 9 10
do
  echo "Calling get job"
  echo "jwt_token: $JWT_TOKEN"
  echo "Job location: $job_location"
  job_response=$($request_cmd $job_location "X-Auth-Token: $JWT_TOKEN")
  echo "Job response: $job_status"
  job_status=$(get_response_status_code "$job_response")
  echo "Job status: $job_status"
  if [[ $job_status != 2* ]]
  then
    echo "Unable to get activation job response"
    send_error $JOB_RETRIEVE_FAILURE
    exit 1
  fi

  job_data=$(get_body_from_response "$job_response")

  if [[ $(get_job_count "$job_data")  -lt 1 ]]
  then
    echo "No jobs found, aborting."
    send_error $NO_JOB_FOUND
    exit 1
  fi

  status="$(get_job_status "$job_data")"

  if [ "$status" = "RUNNING" ]
  then
    echo "Job is still running..."
    # wait 10 seconds
    sleep 10
    continue
  fi

  if [ "$status" != "SUCCEEDED" ]
  then
    echo "Failed to get activation from GOSS"
    exit 1
  fi

  activation_id="$(get_activation_id "$job_data")"
  activation_code="$(get_activation_code "$job_data")"
  region="$(get_region "$job_data")"
  break
done

echo "Activation_id: $activation_id"
activate_ssm "$activation_id" "$activation_code" "$region"
