#! /bin/bash

case $1 in
    tree)
        tree -J ~/.password-store
        ;;
    insert)
        (echo $3; echo $3) |  pass insert $2
        ;;
    remove)
        (echo 'y') | pass rm -r $2
        ;;
    copy)
        echo -n $(pass $2) | xclip -selection c | echo ''
        ;;
    *)
        echo -n "no option"
        ;;
esac

exit