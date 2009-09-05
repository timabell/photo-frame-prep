#!/bin/bash
echo "version from first arg, eg 0.1"
version=$1 #get version from first arg
packagename="photoframeprep_${version}_all.deb"
packager="Tim Abell <tim@timwise.co.uk>"
date=$(/bin/date)
target="debian/photoframeprep"
rm -rf $target
mkdir -p $target/DEBIAN/
mkdir -p $target/usr/bin/
mkdir -p $target/usr/share/doc/photoframeprep/
mkdir -p $target/usr/share/pyshared/photoframeprep/
sed s/#version#/$version/ debian/control > $target/DEBIAN/control
sed "s/#packager#/$packager/" debian/copyright > $target/usr/share/doc/photoframeprep/copyright
sed -i "s/#date#/$date/"  $target/usr/share/doc/photoframeprep/copyright
cd debian/
gzip -c -9 changelog > ../$target/usr/share/doc/photoframeprep/changelog.gz
cd ..
cp photo-frame-prep.py $target/usr/bin/photo-frame-prep
cp gui.py $target/usr/share/pyshared/photoframeprep/
fakeroot dpkg -b $target $packagename
lintian $packagename
