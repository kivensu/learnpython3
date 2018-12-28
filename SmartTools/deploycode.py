# coding: utf-8
# fabric code deploy tool

from fabric.api import *
from fabric.colors  import *
import time

env.user = 'root'
env.hosts = ['192.168.103.155','192.168.103.156']
# 密码略去
env.password = ''

env.project_name = 'Server'
env.project_code_source = '/Users/suboyang/Documents/repository/fengji/Server/'
env.project_tar_source = '/Users/suboyang/Documents/repository/fengji/releases/'
env.project_pack_name = 'release'

env.deploy_project_root = '/data/wwwroot/'
env.deploy_release_dir = 'release'
env.deploy_current_dir = 'current'
env.deploy_version = time.strftime("%Y-%m-%d_%H:%M:%S")+"_V1"

@runs_once
def input_versionid():
    return prompt("Please input this project rollback version ID: ",default="")

@task
@runs_once
def tar_source():
    print (yellow("Creating source package..."))
    with lcd(env.project_code_source):
        local("tar -zcf %s.tar.gz ." % (env.project_tar_source + env.project_pack_name))
    print (green("Creating source package success!"))

@task
def put_package():
    print (yellow("Start put source package..."))
    with settings(warn_only=True):
        run ("mkdir -p %s"%(env.deploy_project_root + env.deploy_release_dir + "/" + env.project_name + "/" + env.deploy_version))
        run ("mkdir -p %s"%(env.deploy_project_root + env.deploy_current_dir + "/" + env.project_name))
    env.deploy_full_path = env.deploy_project_root + env.deploy_release_dir +'/'+ env.project_name + '/' +env.deploy_version
    with settings(warn_only=True):
        result = put(env.project_tar_source + env.project_pack_name + ".tar.gz", env.deploy_full_path)
    if result.failed and not("Put file failed, Continue[Y/N]?"):
        abort("Aborting file put task!")
    with cd(env.deploy_full_path):
        run ("tar -zxf %s.tar.gz" %(env.project_pack_name))
        run ("rm -rf %s.tar.gz" %(env.project_pack_name))
    print(green("Put && Untar source code package success!"))

@task
def make_symlink():
    print(yellow("Update current symlink"))
    env.deploy_full_path = env.deploy_project_root + env.deploy_release_dir + "/" + env.project_name + "/" + env.deploy_version
    with settings(warn_only=True):
        run("rm -rf %s"%(env.deploy_project_root + env.deploy_current_dir + "/" + env.project_name))
        run("ln -s %s %s"%(env.deploy_full_path, env.deploy_project_root + env.deploy_current_dir + "/"+env.project_name))
    print (green("Update symlink success!"))

@task
def rollback():
    print(yellow("Rollback project version"))
    versionid = input_versionid()
    if versionid == '':
        abort("Project version ID error,abort!")

    env.deploy_full_path=env.deploy_project_root + env.deploy_release_dir + "/"+ env.project_name +"/" + versionid
    run("rm -rf %s" % env.deploy_project_root + env.deploy_current_dir + "/" + env.project_name)
    run("sleep 1")
    run("ln -s %s %s" % (env.deploy_full_path ,env.deploy_project_root + env.deploy_current_dir + "/" + env.project_name))
    print (green("Rollback successs!"))

@task
def go():
    tar_source()
    put_package()
    make_symlink()
    rollback()