#!/bin/bash

case $1 in
    tree)
        tree -J $2
        ;;
    set-pass)
        echo -n $3 | gpg --encrypt -r x > $2/pass
        ;;
    get-pass)
        echo -n $(gpg --decrypt $2/pass)
        ;;
    gen-pass)
        echo -n $(pwgen -$2 $3 1)
        ;;
    set-auth)
        echo -n $3 | gpg --encrypt -r x > $2/token
        ;;
    get-auth)
        echo -n $(gpg --decrypt $2/token)
        ;;
    gen-auth)
        echo -n $(oathtool -b --totp $(echo -n $2 | xxd -ps -r))
        ;;
    *)
        echo -n "no option"
        ;;
esac