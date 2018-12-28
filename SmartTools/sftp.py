# coding: utf-8
# paramiko可以理解成一个围绕SSH网络概念的纯python接口
# 使用paramiko实现一个类似于sftp可以批量上传下载文件批量执行命令的小工具

import paramiko 
import os
import re
import threading
from stat import S_ISDIR
from time import sleep

class LinuxInstance(object):
    """远程linux实例类"""
    def __init__(self,ip,username,password,timeout=300):
        """初始化类属性"""
        self.ip = ip
        self.username = username
        self.password = password
        self.timeout = timeout
        self.t =''
        self.chanel = ''
        self.try_time = 3

    def connect(self):
        """连接远端服务器的方法"""
        while True:
            try:
                self.t = paramiko.Transport(sock=(self.ip,22))
                self.t.connect(username=self.username,password=self.password)
                self.chanel = self.t.open_session()
                self.chanel.settimeout(self.timeout)
                self.chanel.get_pty()
                self.chanel.invoke_shell()
                """如果没有异常返回连接成功"""
                print(u'连接%s成功' % self.ip)
                # 将接收到的网络数据解码为str类型
                print(self.chanel.recv(65535).decode('utf-8'))
                return
            except Exception as e:
                if self.try_time != 0:
                    print(u'连接%s失败,请重试!!!' % self.ip)
                    self.try_times -= 1
                else:
                    print(u'三次失败自动退出')
                    exit(1)
    
    def close(self):
        """断开连接方法"""
        self.chanel.close()
        self.t.close()

    def ssh2(self,cmd):
        """通过ssh连接远端服务器执行命令"""
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(self.ip,22,username=self.username,password=self.password)
            for m in cmd:
                stdin, stdout, stderr = ssh.exec_command(m)
                out = stdout.readlines()
                for o in out:
                    print (o)
            print('%s\tOK\n' % self.ip)
            ssh.close()
        except:
            print('%s\tError\n' % self.ip)

    def __get_all_files_in_local_dir(self,local_dir):
        """获取本地指定目录及其子目录下的所有文件条目"""
        # 创建所有文件条目的空列表
        all_files = list()
        # 获取指定目录下的所有文件条目列表
        files = os.listdir(local_dir)  
        for x in files:
            # 拼接文件条目绝对路径
            filename = os.path.join(local_dir,x)
            # 如果是目录则递归处理
            if os.path.isdir(filename):
                all_files.extend(self.__get_all_files_in_local_dir(filename))
            else:
                all_files.append(filename)
        return all_files

    
    def __get_all_files_in_remote_dir(self,sftp,remote_dir):
        """获取远端指定目录及其子目录的下的所有文件"""
        # 保存所有文件列表
        all_files  = list()
        # 去掉字符串最后的‘/’
        if remote_dir[-1] == '/':
            remote_dir = remote_dir[0:-1]
        # 获取当前目录下的所有目录包括属性值
        files = sftp.listdir_attr(remote_dir)
        for x in files:
            # 获取远程目录下的所有目录文件及完整路径
            filename = remote_dir + '/' +x.filename
            # 如果是目录则递归处理该目录，这里用到了stat库中S_ISDIR
            if S_ISDIR(x.st_mode):
                all_files.extend(self.__get_all_files_in_remote_dir(sftp,filename))
            else:
                all_files.append(filename)
        return all_files

    def sftp_upload_single_file(self,local_single_file_path,remote_single_file_path):
        try:
            t = paramiko.Transport(sock=(self.ip,22))
            t.connect(username=self.username,password=self.password)
            sftp = paramiko.SFTPClient.from_transport(t)
            sftp.put(local_single_file_path,remote_single_file_path)
        except Exception as e:
            print(e)

    def sftp_download_single_file(self,remote_single_file_path,local_single_path):
        try:
            t = paramiko.Transport(sock=(self.ip,22))
            t.connect(username=self.username,password=self.password)
            sftp = paramiko.SFTPClient.from_transport(t)
            sftp.get(remote_single_file_path,local_single_path)
        except Exception as e:
            print(e)
            
    def sftp_put_dir(self, local_dir, remote_dir):
        t = paramiko.Transport(sock=(self.ip,22))
        t.connect(username=self.username,password=self.password)
        sftp = paramiko.SFTPClient.from_transport(t)
        # 去掉路径字符串最后的“/”
        if remote_dir[-1] == '/':
            remote_dir = remote_dir[0:-1]

        for root, dirs, files in os.walk(local_dir):
            for filespath in files:
                local_file_catag = os.path.join(root,filespath)
                a = local_file_catag.replace(local_dir,'')
                remote_file_catag = remote_dir + a
                try:
                    sftp.put(local_file_catag, remote_file_catag)
                except Exception as e:
                    sftp.mkdir(os.path.split(remote_file_catag)[0])
                    sftp.put(local_file_catag,remote_file_catag)
                print (u'上传本地文件: %s ==> 远端服务器%s: %s...' % (local_file_catag,self.ip,remote_file_catag))
            for name in dirs:
                local_path = os.path.join(root,name)
                a = local_path.replace(local_dir,'')
                remote_path = remote_dir + a
                try:
                    sftp.mkdir(remote_path)
                    print("创建远程文件夹:"%remote_path)
                except Exception as e:
                    print(e) 
                  
    def sftp_get_dir(self, remote_dir, local_dir):
        t = paramiko.Transport(sock=(self.ip,22))
        t.connect(username=self.username, password=self.password)
        sftp = paramiko.SFTPClient.from_transport(t)
        # 获取远端主机上的目录及其子目录下的所有文件
        all_files = self.__get_all_files_in_remote_dir(sftp, remote_dir)
        # 依次get每个文件
        for x in all_files:
            filename = x.split('/')[-1]
            local_filename = os.path.join(local_dir,filename)
            print (u'下载文件 %s 到本地 %s 中......'% (filename,local_dir))
            sftp.get(x,local_filename)

if __name__ == '__main__':
    get_or_put = str(input("Do you want to upload or download files?(upload or download): "))
    # 密码略去
    host_lists = [['192.168.103.155','root','']]
    if get_or_put == 'download':
        judge_single_file = str(input("Do you want to download single file or some files?(single or some): "))
        remote_path = str(input("Please input your remote path: "))
        local_path = str(input("Please input your local path: "))
        if judge_single_file == 'single':
            for a in host_lists:
                host = LinuxInstance(a[0],a[1],a[2])
                host.connect()
                host.sftp_download_single_file(remote_path,local_path)
                host.close()
        elif judge_single_file == 'some':
            for a in host_lists:
                host = LinuxInstance(a[0],a[1],a[2])
                host.connect()
                host.sftp_get_dir(remote_path,local_path)
                host.close()
        else:
            print("input error!")

    elif get_or_put == 'upload':
        judge_single_file = str(input("Do you want to download single file or some files?(single or some): "))
        remote_path = str(input("Please input your remote path: "))
        local_path = str(input("Please input your local path: "))
        if judge_single_file == 'single':
            for a in host_lists:
                host = LinuxInstance(a[0],a[1],a[2])
                host.connect()
                host.sftp_upload_single_file(local_path,remote_path)
                host.close()
        elif judge_single_file == 'some':
            for a in host_lists:
                host = LinuxInstance(a[0],a[1],a[2])
                host.connect()
                host.sftp_put_dir(local_path,remote_path)
                host.close()
        else:
            print("input error!")

    else:
        exec_cmd_option = str(input("Do you want to exec cmd? (yes or no)"))
        cmd =[]
        cmd_input=str(input("Please input you cmd: "))
        cmd.append(cmd_input)
        if exec_cmd_option == 'yes':
            for a in host_lists:
                host = LinuxInstance(a[0],a[1],a[2])
                host.connect()
                task=threading.Thread(host.ssh2(cmd))
                host.close()
        else:
            exit()
        exit()
