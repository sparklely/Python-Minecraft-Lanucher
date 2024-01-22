# 拼接启动指令
def cncmd(command:str,arg:dict):
    cmd=command
    # 获取传入词典所有key
    for cmdarg in arg.keys():
        # 遍历词典拼接启动参数
        cmd+=f" {cmdarg} {arg[cmdarg]}"
    # 返回启动指令
    return cmd
