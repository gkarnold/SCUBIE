'''
ASU Mechanical Engineering Capstone Project
Team: CARBON6
Members:
Galen Arnold
Nathan Tappendorf
Heidi Jimenez
Zach Washburn
Jordan Ames
Abram Langston

This is the main application file that will run the entire application
'''

## Imports
# Build in modules
from PyQt4 import QtGui, QtCore # Allows access to PyQt commands
import sys # Allows access to system commands
# Custom modules
import UI.UI as UI # Imports the UI from the UI folder


# Main function that loads and runs the application
def applicationMain():
    print('Application run')
    # Calls the UI launcher
    launchUI()


def launchUI():
    print('applicationMain - application - accessed')
    ## Loading and displaying the UI
    # Creates the GUI application
    print('Creating GUI application')
    app = QtGui.QApplication(sys.argv)
    # Creates the class instance defining what to display
    print('Creating an instance of the UI')
    ex = UI.UI()
    # Shows the class instance
    print('Showing the instance of the UI')
    ex.show()
    # Exits the program when the GUI application is exited
    sys.exit(app.exec_())

if __name__ == '__main__':
    applicationMain()