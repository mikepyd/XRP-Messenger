#! /bin/bash

#echo "XRP Messenger "
GREEN="\e[92m"
BLUE="\e[94m"
printf "${GREEN}"
figlet XRP Messenger
printf "${BLUE}"
echo "Created by Michiel Odendaal"
STOP="\e[0m"
printf "${STOP}"

function countdown(){
   date1=$((`date +%s` + $1)); 
   while [ "$date1" -ge `date +%s` ]; do 
     echo -ne "$(date -u --date @$(($date1 - `date +%s`)) +%H:%M:%S)\r";
     sleep 0.1
   done
}

countdown 5

exec python3 main.py && exit

