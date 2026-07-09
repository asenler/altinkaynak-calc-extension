#!/bin/bash
set -e

APP="altinkaynak-calc-extension"
BUILD="build"
OXT="$BUILD/oxt"

echo "==> Cleaning..."
rm -rf "$BUILD"
mkdir -p "$OXT"

echo "==> Copying extension files..."

cp description.xml "$OXT/"
cp LICENSE "$OXT/"
cp README.md "$OXT/"

cp Addons.xcu "$OXT/" 2>/dev/null || true

mkdir -p "$OXT/META-INF"
cp META-INF/manifest.xml "$OXT/META-INF/" 2>/dev/null || true

mkdir -p "$OXT/python"

cp src/*.py "$OXT/python/"

echo "==> Creating OXT..."

(
    cd "$OXT"
    zip -qr "../${APP}.oxt" .
)

echo
echo "Done:"
echo "$BUILD/${APP}.oxt"
