#!/usr/bin/env bash

# script to ssh to a remote server
# syntax: ssh_to_remote_server.ssh <server IP address>

# Check if IP address argument is provided
if [ -z "$1" ]; then
  echo "Please provide the IP address of the remote server as an argument."
  exit 1
fi


# IP address of the remote server
remote_server="$1"

# SSH command to connect to the remote server using the private key
ssh -i ~/.ssh/school "$remote_server"
