#!/bin/bash

set -e

NAME="altinkaynak-calc-extension.oxt"

echo "Altinkaynak Calc Extension build"

rm -f "$NAME"

zip -r "$NAME" \
    Addons.xcu \
    description.xml \
    META-INF \
    pythonpath \
    README.md \
    LICENSE

echo "Oluşturuldu: $NAME"
