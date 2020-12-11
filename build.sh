python -m pip install --user pyinstaller
pyinstaller -F main.py -i ./icon.ico
rm -r build
rm main.spec
echo "Build complete"
