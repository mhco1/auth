#!/bin/bash

PS3='Please enter your choice: '
options=("otp" "pass")
select opt in "${options[@]}"
do
    case $opt in
        "otp")
            #echo "you chose choice 1"
            python ./otp/otp.py
            ;;
        "pass")
            #echo "you chose choice 2"
            python ./pass/pass.py
            ;;
        *) echo "invalid option $REPLY";;
    esac
done