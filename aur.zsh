mkaur() {
    pkg=$1
    ssh aur.archlinux.org setup-repo $1
    git submodule add ssh+git://aur.archlinux.org/$1.git/
    cd $1
}

cpaur() {
    pkg=$1
    cd $1
}

commitaur() {
    makepkg --printsrcinfo > .SRCINFO
    git add .
    git commit -asm "$1"
    git push -u origin master
    cd ..
}

commitaurgh() {
    commitaur "$1"
    ./UPDATE-REQUIREMENTS.py
    git add .
    git commit -asm "$1"
    git push
}
