
if [ ! $1 ]; then
    echo "Please enter an ip and a port number."
    exit
fi

if [ ! $2 ]; then
    echo "Please enter a port number."
    exit
fi

ip=$1
port=$2

ssh -CqTfnN -R 0.0.0.0:$port:127.0.0.1:22 root@$ip
