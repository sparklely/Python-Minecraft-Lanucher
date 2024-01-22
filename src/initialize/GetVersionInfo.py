import os
from initialize.g_vars import lanucher

# 获取所有版本列表
def init_GetAllVerList():
    lanucher.MinecraftVersions=os.listdir(lanucher.MinecraftPath)