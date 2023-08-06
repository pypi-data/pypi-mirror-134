#!/bin/sh

set -ex

mkdir -p dist
if ! test -e /.dockerenv; then
  exec docker run --rm -it -v $(pwd):/mnt/host/rql quay.io/pypa/manylinux_2_24_x86_64 sh /mnt/host/rql/$0
fi

cd /mnt/host
VERSION=6.2.0

curl -L https://github.com/Gecode/gecode/archive/refs/tags/release-$VERSION.tar.gz | tar -xzf -

cd gecode-release-$VERSION
./configure
make -j2
make install

PYBINS="/opt/python/cp37*/bin /opt/python/cp38*/bin /opt/python/cp39*/bin"

mkdir -p /wheelhouse
# Compile wheels
for PYBIN in $PYBINS; do
    "${PYBIN}/pip" wheel --use-feature=in-tree-build /mnt/host/rql -w /wheelhouse
done

# Bundle external shared libraries into the wheels
for whl in /wheelhouse/rql*.whl; do
    auditwheel repair "$whl" -w /wheelhouse
done

# Install packages and test
for PYBIN in $PYBINS; do
    "${PYBIN}/pip" install pytest
    "${PYBIN}/pip" install rql --no-index -f /wheelhouse
    echo "************  test on $PYBIN"
    (cd "/mnt/host"; "${PYBIN}/py.test" rql)
done
mv /wheelhouse/rql*manylinux*.whl /mnt/host/rql/dist/
