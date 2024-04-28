#!/bin/bash

if [ ! $1 ]; then
    port=22
else
    port=$1
fi

user=root
ip=$your_server_ip

ssh $user@$ip -p $port

#expect version
###!/usr/bin/expect
#set timeout 3
#set user root
#set ip $ip
#spawn ssh ${user}@${ip}
##expect "password:"
##send "$your_passwd\r"
#interact
