#! /bin/bash

passArgs='';
count=0;

while IFS='\n' read -r l; do
    # echo ${l:4}
    if [[ $count > 0 ]]; then
        passArgs=$( echo $passArgs $count ${l:4} );
    fi
    count=$(($count+1));
done <<< $(pass);

dialog --menu "exemple list:" 15 40 $count $passArgs;

#echo $passArgs;