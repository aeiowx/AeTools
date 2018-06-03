import paramiko  
from paramiko import SSHClient
from scp import SCPClient
import threading  
import os
import sys
import time

paramiko.util.log_to_file('paramiko.log')
#default_path='rsa_key/xd_id_rsa'
remote_file_path = '/tmp/numlockx_1.2-7_amd64.deb'
local_file_path = 'update_files/numlockx_1.2-7_amd64.deb'

ip_file = "ip_list.txt"
result_file = "result.txt"

fail_cnt=0
success_cnt=0

def run_update(ip,username):  
    install_deb = 'sudo -S dpkg -i %s'%remote_file_path
    rm_deb = 'rm %s'%remote_file_path
    cmd = [install_deb, rm_deb]
    passwd = '???'

    global fail_cnt
    global success_cnt
    
    result_fp=open(result_file, 'a+')

    try:  
        #default_path = os.path.join(os.environ['HOME'], '.ssh', 'id_rsa')
        #key=paramiko.RSAKey.from_private_key_file(default_path)
        ssh = paramiko.SSHClient()  
#       ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  
        ssh.connect(ip,22,username,passwd,timeout=5)

        print 'device: %s is available, send update files\n'%(ip)  
        try:
            scp = SCPClient(ssh.get_transport())
        except Exception as e:  
            print e  

        scp.put(local_file_path, remote_file_path, True)  
        scp.close()

        print '%s: run update cmd\n'%(ip)  
        for m in cmd:  
            stdin, stdout, stderr = ssh.exec_command(m)  
            if cmp(m, install_deb) == 0:
                stdin.write("%s\r"%passwd)
            out = stdout.readlines()  
            for o in out:  
                print o,  
            out = stderr.readlines()
            for o in out:  
                print o,  
        ssh.close()  

        success_cnt+=1
        result_fp.write("device:%s, update success!, total success cnt %d\n"%ip, success_cnt)

    except :  
        fail_cnt+=1
#   print 'device: ip %s, update fail, total fail time %d\n'%(ip, fail_cnt)  
        result_fp.write("device:%s, update faile!\n"%ip)

    result_fp.close()

if __name__=='__main__':  
    username = "???"  
    threads = []   
    print "Deb package installer begin......" 
    print "start time %s"%time.ctime() 
    
    result_fp = open(result_file, 'a+')
    result_fp.write("start time %s\n"%time.ctime())
    result_fp.close()

    ip_list_p = open(ip_file, 'r')
    ip_start = ip_list_p.readline()
    ip_end = ip_list_p.readline()
    ip_list_p.close()

    if ip_start == "":
        ip_start="192.168.1.1"
        ip_end=ip_start

    if ip_end == "":
        ip_end=ip_start

    ip_start_args = "".join(ip_start.strip('\n'))
    ip_end_args = "".join(ip_end.strip('\n'))

    ip_prefix = '.'.join(ip_start_args.split('.')[:-1]) 
    start = '.'.join(ip_start_args.split('.')[3:]) 
    end = '.'.join(ip_end_args.split('.')[3:]) 

    print 'prefix %s, range(%s, %s)'%(ip_prefix, start, end)

    threads = []
    for i in range(int(start), int(end)+1):  
        ip = ip_prefix + '.%s'%str(i)  
        a=threading.Thread(target=run_update,args=(ip,username))   
        threads.append(a)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    time.sleep(20)

    result_fp = open(result_file, 'a+')
    result_fp.write("Success num: %d, fail num %d\n"%(success_cnt, fail_cnt))
    result_fp.write("end time %s\n"%time.ctime())
    result_fp.close()

