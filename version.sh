function release(){
    gitdesc=$(git describe --tag | sed  's/^v//')
    desc_items=($(echo $gitdesc | tr '-'  ' ' ))
    desc_len=${#desc_items[@]}
    VERSION=${desc_items[0]}
    git_commit=$(git log -n 1 --pretty --format=%h)
    if [ $desc_len -ge 3 ];then
        release=${desc_items[-2]}.${desc_items[-1]}
    else
        release=0.$git_commit
    fi
    branch_info=($(git branch | grep '^*' | cut -d ' '  -f 2  | tr '-' " "))
    pypi_version=$VERSION.${desc_items[-2]}

    cat > dops/version.py <<EOF
VERSION_INFO = (
                ("program","dops"),
                ("version","$branch_info-$VERSION"),
                ("pypi","$pypi_version"),
                ("commit","$release"),
                ("buildTime","$(date +'%F %X')"),
)
EOF

}

case $1 in
    *)
    release
    ;;
esac