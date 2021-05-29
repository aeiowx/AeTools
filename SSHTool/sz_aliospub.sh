#!/usr/bin/expect
set filename [lindex $argv 0]
set timeout 3
set username root
set ip 116.62.46.72
spawn scp -r $filename $username@$ip:/tmp
#expect "password:"
#send "123456\r"
interact
