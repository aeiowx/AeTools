#### 使用方式
1. ip_list.txt文件里填上所要升级的机器IP范围，如
192.68.1.1
192.168.1.254

#### 流程图
```flow
st=>start: Start
e=>end
readfile=>operation: Read config file
confcheck=>condition: The right config?
defconf=>operation: Abort.
enumhost=>operation: Enumerate hosts list in config file.
sshconnect=>operation: Connect host.(Choose SSH authentication mode here)
connectret=>condition: Success or fail?
pushrun=>operation: Push files and run comands.(Use SCP and SSH)
resultwrite=>operation: Write result to file.
lasthost=>condition: Is last host?
 
 
st->readfile->confcheck
confcheck(yes)->enumhost->sshconnect->connectret
confcheck(no)->defconf->resultwrite->e
connectret(yes)->pushrun->lasthost
connectret(no)->resultwrite->e
lasthost(yes)->resultwrite->e
lasthost(no)->enumhost
```


