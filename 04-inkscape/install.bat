@echo off

echo Updating Inkscape local extensions in folder '%APPDATA%\inkscape\extensions'.

echo Removing existing py-2d-3d extensions.

del /Q %APPDATA%\inkscape\extensions\py2d*.inx > NUL
del /Q %APPDATA%\inkscape\extensions\py2d*.py > NUL

echo Installating latest py-2d-3d extensions.

copy /Y py2d*.inx %APPDATA%\inkscape\extensions > NUL
copy /Y py2d*.py %APPDATA%\inkscape\extensions > NUL

echo Installation of py-2d-3d extensions for Inkscape complete.
echo Restart Inkscape to ensure updates are available.
