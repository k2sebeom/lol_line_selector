python -m pip install --user pyinstaller
pyinstaller -F main.py -i ./icon.ico
RMDIR /q /s build
DEL main.spec
ECHO "Build Complete"
