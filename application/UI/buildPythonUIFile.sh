echo “This is a simple shell script that is used to update the base UI python file when changes are made in QT Designer”

cd /Users/galenarnold/Documents/Galen/Python/seniorDesign/UI
pyuic4 aquaUI_Base.ui > UIBase.py
osascript -e 'tell application "Terminal" to quit'