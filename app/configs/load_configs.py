import yaml
import os
from os import path


yaml.warnings({'YAMLLoadWarning': False})
CONFIG_FILE = 'sql_config.yml'
CONFIG_PATH_DIR = path.join(os.getcwd(), 'configs', CONFIG_FILE)


def get_configs():
    
    with open(CONFIG_PATH_DIR, 'r') as stream:
        configs = yaml.load(stream)
        
    host, port = configs['host'], configs['port']
    user, pwd = configs['user'], configs['pwd']
    database, sql = configs['database'], configs['sql']
    
    return host, port, user, pwd, database, sql
    

load_configs = get_configs()
HOST, PORT = load_configs[:2]
USER, PWD = load_configs[2:4]
DB, SQL = load_configs[4:]

CONN_STRING = "{0}+mysqlconnector://{1}:{2}@{3}:{4}/{5}"\
    .format(SQL, USER, PWD, HOST, PORT, DB)
