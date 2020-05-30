import platform as plf

profiles = [
    'architecture',
    'mac_ver',
    'machine',
    'node',
    'platform',
    'processor',
    'python_build',
    'python_compiler',
    'python_version',
    'release',
    'system',
    'uname',
    'version',
]

for profile in profiles:
    if hasattr(plf, profile):
        print(profile+ ": " + str(getattr(plf, profile)()))
