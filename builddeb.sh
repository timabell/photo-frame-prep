#!/bin/bash
version=$1
packagename="photoframeprep_${version}_all.deb"
mkdir -p packaging/photoframeprep/DEBIAN/
mkdir -p packaging/photoframeprep/usr/bin/
cp photo-frame-prep.py packaging/photoframeprep/usr/bin/photo-frame-prep
cd packaging/
sed s/#version#/$version/ control > photoframeprep/DEBIAN/control
echo "fakeroot dpkg -b photoframeprep $packagename"
fakeroot dpkg -b photoframeprep $packagename
lintian $packagename
