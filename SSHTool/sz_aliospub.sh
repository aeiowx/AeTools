#!/usr/bin/expect
set filename [lindex $argv 0]
set timeout 3
set username root
set ip $your_server_ip
spawn scp -r $filename $username@$ip:/tmp
#expect "password:"
#send "$your_passwd\r"
interact
