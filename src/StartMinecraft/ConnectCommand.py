def cncmd(command:str,arg:dict):
    cmd=command
    for cmdarg in arg.keys():
        cmd+=f" {cmdarg} {arg[cmdarg]}"
    return cmd
