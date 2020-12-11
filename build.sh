python -m pip install --user pyinstaller keyboard
pyinstaller -F main.py -i ./icon.ico
rm -r build
rm main.spec
echo "Build complete"
