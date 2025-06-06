#!/bin/bash
# Run on macOS to set up passwordless SSH to the EC2 instance.
# Usage: ./configure_ssh_mac_to_ec2.sh user@ec2-host

KEY=~/.ssh/things3_ec2
ssh-keygen -t rsa -b 4096 -f "$KEY" -N ""
ssh-copy-id -i "$KEY" "$1"
