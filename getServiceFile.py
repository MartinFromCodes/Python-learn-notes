#!/usr/local/bin/python  
# encoding:utf-8  
  
import paramiko  
import os  
  
HOST_IP='192.168.1.2'  
REMOTE_PATH='/home'  
REMOTE_FILENAME='typecho.db'  
LOCAL_PATH='/usr/nginx/www/build/usr/'  
USERNAME='root'  
PASSWORD='123123'  
  
def remote_scp(host_ip,remote_path,local_path,file_name,username,password):  
    t = paramiko.Transport((host_ip,22))  
    t.connect(username=username, password=password) # 登录远程服务器  
    sftp = paramiko.SFTPClient.from_transport(t)  # sftp传输协议  
    src = remote_path+'/'+file_name  
    des = local_path+'/'+file_name  
    sftp.get(src,des)  
    t.close()  
  
  
if not os.path.isdir(LOCAL_PATH):  
    os.makedirs(LOCAL_PATH)  
if not os.path.isfile(LOCAL_PATH+'/'+REMOTE_FILENAME):  
    fp=open(LOCAL_PATH+'/'+REMOTE_FILENAME,'w')  
    fp.close()  
  
remote_scp(HOST_IP,REMOTE_PATH,LOCAL_PATH,REMOTE_FILENAME,USERNAME,PASSWORD)  
