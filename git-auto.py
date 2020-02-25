#!/usr/bin/python 
# -*- coding: utf-8 -*-
# 调用方法: python git-merge.py bugfix(source) 'fixbug'(commit) dev(target)
# 调用场景: 写完代码后, 自动提交，合并到dev
import sys
import os
import subprocess

sourceBranch = sys.argv[0] # 当前修改得分支
commitMsg = sys.argv[0] | 'python auto commit' # 默认提交信息 
targetBranch = sys.argv[2] | 'dev' # 需要合并得分支，默认用dev去合并
project_dir = 'D:/V7/Main/bos-dev-platform'  # git本地仓库路径

os.chdir(project_dir) # 转到当前目录

# git commit
subprocess.call(['git', 'add', '.'])
subprocess.call(['git', 'commit', '-m', commitMsg])
subprocess.call(['git', 'push', '--set-upstream', 'origin', sourceBranch]) # git push --set-upstream origin dev

# git merge
subprocess.call(['git', 'checkout',  targetBranch])
subprocess.call(['git', 'pull'])
subprocess.call(['git', 'merge', sourceBranch])
subprocess.call(['git', 'push', '-u', 'origin', targetBranch]) # git push -u origin dev


# git delete remote branch

# git push origin --delete branch
