#! /bin/bash

case $1 in
    insert)
        [ -d ~/.2fa/$2 ] && rm -r ~/.2fa/$2
        mkdir ~/.2fa/$2
        echo -n $3 > ~/.2fa/$2/key
        gpg2 -r "x" -e ~/.2fa/$2/key
        rm ~/.2fa/$2/key
        ;;
    generate)
        code=$(gpg2 -d ~/.2fa/$2/key.gpg)
        echo $(oathtool -b --totp $code)
        ;;
    *)
        ;;
esac

exit