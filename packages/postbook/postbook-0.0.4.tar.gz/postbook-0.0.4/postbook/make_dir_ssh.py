
import paramiko
import pickle
import os
def make_dir(dir_path):
    current_directory = os.getcwd()
    with open(f"{current_directory}/.plog","rb") as f:
        meta_data = pickle.load(f)
    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(meta_data['ip_address'],22,username=meta_data['username'],password=meta_data['password'],timeout=4)
    (stdin, stdout, stderr) = s.exec_command(f'mkdir site/{dir_path}')
    for line in stdout.readlines():
        print (line)

    s.close()
    return dir_path