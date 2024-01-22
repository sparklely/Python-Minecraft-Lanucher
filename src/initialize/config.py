import yaml
from initialize.g_vars import lanucher

def init_config():
    with open("../config.yml",'w') as config:
        config=yaml.safe_load(config)
        lanucher.MinecraftPath=config['lanucher']['MinecraftPath']

