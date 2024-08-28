#!/bin/bash

case $1 in
    init)
        pass init $2
        mkdir ~/.password-store/auth
        mkdir ~/.password-store/pass
        ;;
    tree)
        tree -J ~/.password-store/$2
        ;;
    insert)
        (echo $3; echo $3) |  pass insert $2
        ;;
    remove)
        (echo 'y') | pass rm -r $2
        [ ! -d ~/.password-store/$3 ] && mkdir ~/.password-store/$3
        ;;
    get)
        pass $2
        ;;
    copy-key)
        echo -n $(pass $2) | xclip -selection c | echo ''
        ;;
    copy-user)
        echo -n $2 | xclip -selection c | echo ''
        ;;
    generate-key)
        pwgen -$2 $3 1
        ;;
    generate-key-code)
        key=$(pass $2)
        code=$(oathtool -b --totp $key)
        echo -n $code | xclip -selection c | echo -n $code
        ;;
    *)
        echo -n "no option"
        ;;
esac