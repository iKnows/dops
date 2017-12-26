#!/usr/bin/env bash

set -o errexit

function version() {
    gitdesc=$(git describe --tag | sed  's/^v//')
    desc_items=($(echo $gitdesc | tr '-'  ' ' ))
    desc_len=${#desc_items[@]}
    VERSION=${desc_items[0]}
    if [ $desc_len -ge 3 ];then
        release=${desc_items[-2]}.${desc_items[-1]}
    else
        release=0
    fi
    branch_info=($(git branch | grep '^*' | cut -d ' '  -f 2  | tr '-' " "))
    git_commit=$(git log -n 1 --pretty --format=%h)

    cat > dops/version.py <<EOF
VERSION_INFO = (
                ("program","dops"),
                ("version","$branch_info-$VERSION"),
                ("commit","$release-$git_commit"),
                ("buildTime","$(date +'%F %X')"),
)
EOF
}


function pypi() {
    pip3 install twine

    python3 setup.py sdist bdist_wheel

    twine upload dist/*

    rm -rf ./build/
    rm -rf ./dist/
    rm -rf ./dops.egg-info/
}


case $1 in
    *)
        version
        # pypi
      ;;
esac
