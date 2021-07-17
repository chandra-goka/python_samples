<#
    .SYNOPSIS
      Registers this host with ssm agent
    .DESCRIPTION
      Downloads the agent, installs it, must be run as Administrator
#>

$jwt_token = "{jwt_token}"

$error_codes = @{"UNABLE_TO_ACTIVATE"=1; "JOB_RETRIEVE_FAILURE"=2; "NO_JOB_FOUND"=3; "OS_UNSUPPORTED"=4;}

function Send-Error($error_code, $jwt_token)
{
    $error_url = "https://api.goss.vdo.manage.rackspace.com/v1.0/instance/goss/error/{0}" -f $error_code
    Invoke-WebRequest $error_url -Method POST -Headers @{'X-Auth-Token' = $jwt_token} -UseBasicParsing
}

if ($PSVersionTable.PSVersion.Major -lt 3) {
  echo "PowerShell version unsupported."
  exit 10
}

$supported = @("2012", "2016", "2019")

$isServer = (Get-CimInstance Win32_OperatingSystem | Select-Object -expand ProductType) -eq 3
$osName = Get-CimInstance Win32_OperatingSystem | Select-Object -expand Caption
$isVersionSupported = $null -ne ($supported | ? { $osName -match $_ })
$isSupported = ([Environment]::Is64BitOperatingSystem) -and $isServer -and $isVersionSupported

if(-Not $isSupported) {
  echo "Operating System version unsupported."
  Send-Error $error_codes.OS_UNSUPPORTED $jwt_token
  exit 10
}

$goss_access_url = "https://api.goss.vdo.manage.rackspace.com/v1.0/instance/goss/activate"
try {
    $access_job_response = Invoke-WebRequest $goss_access_url -Method POST -Headers @{'X-Auth-Token' = $jwt_token; 'Content-Type' = 'application/json'} -UseBasicParsing
} catch {
    echo "Unable to create activation for ssm."
    Send-Error $error_codes.UNABLE_TO_ACTIVATE $jwt_token
    exit 11
}
$job_location = $access_job_response.headers.Location

$status = "RUNNING"
$activation = $null
DO {
    Start-Sleep -s 10
    try {
        $job_status_response = Invoke-WebRequest $job_location -Method GET -Headers @{'X-Auth-Token' = $jwt_token} -UseBasicParsing
    } catch {
        echo "Failed to get job status while getting activation for SSM"
        Send-Error $error_codes.JOB_RETRIEVE_FAILURE $jwt_token
        exit 11
    }

        $job_json_response = ConvertFrom-Json $([String]::new($job_status_response.Content))
        $cnt = $job_json_response.data.currentItemCount

        if ($cnt -ne 1) {
            echo "Unexpected response from job status while activating SSM."
            Send-Error $error_codes.NO_JOB_FOUND $jwt_token
            exit 11
        }

        $status = $job_json_response.data.items[0].status
        $activation = $job_json_response.data.items[0].message
} While ($status -eq "RUNNING")

if ($status -ne "SUCCEEDED") {
    echo "Failed to create an activation for SSM"
    Send-Error $error_codes.UNABLE_TO_ACTIVATE $jwt_token
    exit 11
}

$activationcode = $activation.activation_code
$activationid = $activation.activation_id
$region = $activation.region


$dir = $env:TEMP + "\ssm"
New-Item -ItemType directory -Path $dir -Force
cd $dir

(New-Object System.Net.WebClient).DownloadFile("https://amazon-ssm-$region.s3.amazonaws.com/latest/windows_amd64/AmazonSSMAgentSetup.exe", $dir + "\AmazonSSMAgentSetup.exe")
Start-Process .\AmazonSSMAgentSetup.exe -ArgumentList @("/norestart", "/uninstall", "/q", "/log", "install.log") -Wait
Start-Process .\AmazonSSMAgentSetup.exe -ArgumentList @("/norestart", "/q", "/log", "install.log", "CODE=$activationcode", "ID=$activationid", "REGION=$region") -Wait
Get-Content ($env:ProgramData + "\Amazon\SSM\InstanceData\registration")
Get-Service -Name "AmazonSSMAgent"

cd $Env:ProgramFiles\Amazon\SSM
$output = .\ssm-cli.exe get-instance-information | ConvertFrom-Json
$managed_instance_id = $output.psobject.properties["instance-id"].value
echo "ssm_instance_id=$managed_instance_id"