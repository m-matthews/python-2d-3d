#!/usr/bin/env bash

DEST=~/.config/inkscape/extensions
echo "Updating Inkscape local extensions in folder '$DEST'."

echo "Removing existing py-2d-3d extensions."
rm $DEST/py2d*

echo "Installating latest py-2d-3d extensions."
cp py2d*.py $DEST
cp py2d*.inx $DEST

echo "Installation of py-2d-3d extensions for Inkscape complete."
echo "Restart Inkscape to ensure updates are available."
