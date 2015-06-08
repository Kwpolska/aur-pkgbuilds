mkaur() {
    pkg=$1
    ssh aur4.archlinux.org setup-repo $1
    git clone ssh+git://aur4.archlinux.org/$1.git/
    cd $1
    cp ~/git/aur-pkgbuilds/$1/* .
}

cpaur() {
    pkg=$1
    cd $1
    cp ~/git/aur-pkgbuilds/$1/* .
}

commitaur() {
    mksrcinfo
    git add .
    git commit -asm $1
    git push -u origin master
    cd ..
}
