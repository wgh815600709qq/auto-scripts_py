# -*- coding: UTF-8 -*-
# 批量删除本地git分支脚本
import os
import subprocess
project_dir = 'D:/V7/bos-dev-platform'  # git本地仓库路径
ignore_branch_list = ['dev', 'master']  # 需要保留的本地分支

# 函数定义
def get_branches(project_dir):
    try:
        os.chdir(project_dir)        #转到工程路径下
    finally:
        print('执行结果：')
    branches_bytes = subprocess.check_output(["git", "branch"])
    #终端运行“git branch”命令，并且将终端的输出str转存到branches_bytes里
    branches_str = str(branches_bytes, encoding = "utf8")
    branches = branches_str.split('\n')
    #使用str的split方法将其按照'\n'分割
    branch_list = []
    for branch in branches[0:-1]:
        branch_list.append(branch.lstrip('* ')) # 去空格， *
    return branch_list

local_gitBranch_list = get_branches(project_dir)
# 遍历删除
for  branch in local_gitBranch_list:
    try:
        ignore_branch_list.index(branch)  # index方法没找到时候会报错
    except:
        print(branch)
        subprocess.call(['git', 'branch', '-D', branch])
print('batch delete has finished')