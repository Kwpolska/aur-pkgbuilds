# Maintainer: Chris Warrick <aur@chriswarrick.com>
pkgbase=python-yapsy
pkgname=('python-yapsy' 'python2-yapsy')
_pyname=Yapsy
pkgver=1.11.123
pkgrel=2
pkgdesc='Yet Another Plugin SYstem'
arch=('any')
url='http://yapsy.sourceforge.net/'
license=('BSD')
makedepends=('python' 'python2' 'python-setuptools' 'python2-setuptools')
options=(!emptydirs)
# `b` added upstream
source=("https://pypi.python.org/packages/source/${_pyname:0:1}/${_pyname}/${_pyname}-${pkgver}b.tar.gz")
md5sums=('7a8934158e9314c4f0f76606d082be8f')

prepare() {
  cd "${srcdir}/${_pyname}-${pkgver}"
  cp -r "${srcdir}/${_pyname}-${pkgver}" "${srcdir}/${_pyname}-${pkgver}-py2"
}

package_python-yapsy() {
  depends=('python' 'python-setuptools')
  cd "${srcdir}/${_pyname}-${pkgver}"
  python3 setup.py install --root="${pkgdir}/" --optimize=1
  install -D -m644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgbase}/LICENSE"
}

package_python2-yapsy() {
  depends=('python2' 'python2-setuptools')
  cd "${srcdir}/${_pyname}-${pkgver}-py2"
  python2 setup.py install --root="${pkgdir}/" --optimize=1
}

# vim:set ts=2 sw=2 et:
