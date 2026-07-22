@echo off

echo Cleaning old build...
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist

echo Building Wyvern...
pyinstaller --onedir --windowed --name Wyvern --icon=resources\app.ico main.py

echo Copying data folder...
xcopy data dist\Wyvern\data /E /I /Y

echo Copying resources folder...
xcopy resources dist\Wyvern\resources /E /I /Y

echo.
echo ==========================
echo Build Complete!
echo ==========================
pause