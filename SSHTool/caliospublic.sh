#!/bin/bash

if [ ! $1 ]; then
    port=22
else
    port=$1
fi

user=root
ip=116.62.46.72

ssh $user@$ip -p $port


#expect version
###!/usr/bin/expect
#set timeout 3
#set user root
#set ip 116.62.46.72
#spawn ssh ${user}@${ip}
##expect "password:"
##send "123456\r"
#interact
