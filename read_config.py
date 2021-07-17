from configparser import ConfigParser

cfg = ConfigParser()
cfg.read('app_config.ini')
cfg.read('prod_app_config.ini')

print ("Sections : ", cfg.sections())

for section in cfg.sections():
    print("SECTION -> ",section)
    print("-------------------")
    print('LOG_FILE_PATH - ' , cfg.get(section,'LOG_FILE_PATH'))
    print('SECRET_KEY - ', cfg.get(section,'SECRET_KEY'))
    print('SECRET_VALUE - ' , cfg.get(section,'SECRET_VALUE'))
    print('PORT - ' , cfg.get(section,'PORT'))
    print('APP_BASE_URL - ' , cfg.get(section,'APP_BASE_URL'))
    print('IS_DEBUG - ' , cfg.getboolean(section,'is_debug'))


