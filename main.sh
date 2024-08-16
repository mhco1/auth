#!/bin/bash

PS3='Please enter your choice: '
options=("otp" "pass")
select opt in "${options[@]}"
do
    case $opt in
        "otp")
            python ./otp/otp.py
            break
            ;;
        "pass")
            python ./pass/pass.py
            break
            ;;
        *) echo "invalid option $REPLY";;
    esac
done