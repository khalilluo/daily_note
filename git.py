import sys,os

userName='khalilluo'
password='8703007j'

gitignore='''
venv
.idea
__pycache__
'''

def exeCmd(cmd):
    cmds=cmd.split('\n')
    for c in cmds:
        os.system(c)

if __name__ == '__main__':
    print('git init directory: ',sys.argv[1])
    dir=sys.argv[1]
    if os.path.exists(f'{dir}/.git'):#已经初始化
        pass
    else:
        with open('.gitignore', 'w') as f:
            f.write(gitignore)
        url=input('input github repository URL: ')
        if url=='':
            exit(0)
        suffix=url.replace('https://','')
        https=f'https://{userName}:{password}@{suffix}.git'
        cmd=f'''
            git init
            git remote add origin {https}
            '''
        exeCmd(cmd)
    #公操作
    cmd='''
        git add -A
        git commit -m "commit"
        git push origin master
        '''
    exeCmd(cmd)