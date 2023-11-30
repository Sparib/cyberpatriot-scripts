#!/bin/bash
# CURRENT_USERS=$(awk -F: '($3>=1000)&&($1!="nobody"){print $1}' /etc/passwd)
# WANTED_USERS=$(cat ~/Desktop/)
whoami
echo "$SUDO_USER"
echo "$HOME/Desktop"
logname

