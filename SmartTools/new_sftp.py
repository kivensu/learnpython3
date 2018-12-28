# coding: utf-8
# usage: fab -f sftp004.py go
# fabric库更高级更简单
# 使用fabric实现文件传输并校验指纹

from fabric.api import *
from fabric.colors import *

env.user = 'root'
env.hosts = ['192.168.103.155']
# 密码略去
env.password = ''

@runs_once
@task

def tarfile():
    """本地打包任务函数"""
    print(yellow('tar file...'))
    # lcd()切换本地目录
    with lcd('/Users/suboyang/Documents/Ebooks/Life'):
        # local()执行本地命令
        local('tar czf timefriend.tar.gz timefriend.pdf')

@task
def putfile():
    """上传文件任务函数"""
    print(blue('put file...'))
    # run()执行远程命令
    run ('mkdir -p /tmp/log')
    # cd()切换远程目录
    with cd('/tmp/log'):
        with settings(warn_only=True):
            # 上传本地到远程
            result = put('/Users/suboyang/Documents/Ebooks/Life/timefriend.tar.gz','/tmp/log')
        if result.failed and not confirm('put file field,Continue[Y?N]?'):
            abort('Aborting file put task!')

@task
def checkfile():
    """校验文件任务函数"""
    print(red('check file...'))
    with settings(warn_only=True):
        # 执行本地MD5检验
        lmd5 = local('md5sum /Users/suboyang/Documents/Ebooks/Life/timefriend.tar.gz',capture=True).split(' ')[0]
        # 执行远程MD5检验
        rmd5 = run('md5sum /tmp/log/timefriend.tar.gz').split(' ')[0]
    if lmd5 == rmd5:
        print('OK')
    else:
        print('ERROR')

@task
def go():
    tarfile()
    putfile()
    checkfile()