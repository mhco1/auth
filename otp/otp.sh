#! /bin/bash

case $1 in
    insert)
        [ -d ~/.2fa/$2 ] && rm -r ~/.2fa/$2
        mkdir ~/.2fa/$2
        echo -n $3 > ~/.2fa/$2/key
        gpg2 -q -r "x" -e ~/.2fa/$2/key
        rm ~/.2fa/$2/key
        ;;
    remove)
        rm -r ~/.2fa/$2
        ;;
    generate)
        key=$(gpg2 -q -d ~/.2fa/$2/key.gpg)
        code=$(oathtool -b --totp $key)
        echo -n $code | xclip -selection c | echo -n $code
        ;;
    *)
        ;;
esac

exit