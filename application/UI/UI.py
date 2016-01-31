'''
UI class file for the capstone project.
This file creates a UI class that imports and inherits the base UI class that is created by QT and pyuic4.
This class will be loaded and executed by the application to provide the user with a
'''

## Imports
# Build in modules
from PyQt4 import QtGui, QtCore # Allows access to PyQt commands
import sys # Allows access to system commands
import multiprocessing # Allows access to processes and their commands
import threading # Allows access to processes and their commands
from array import *
# Custom modules
import UIBase # Base UI that will be inherited
import delegate.delegate as delegate # Delegate for the application
import systemController.systemController as sc # System controller for the application

# UI class for the application that inherits from the base UI built with QT and pyuic4
class UI(UIBase.Ui_MainWindow):
    def __init__(self):
        print('__init__ - UI - accessed')
        # Initializes the QWidget superclass
        QtGui.QMainWindow.__init__(self)
        # Runs setupIU method upon initialization
        self.setupUi(self)
        # Runs the button functionality
        self.buttonFunctionality()

        # Creates queues
        self.queue_SC = multiprocessing.Queue()
        self.queue_UI = multiprocessing.Queue()

        # Initializes the delegate
        self.initializeDelegate(self.queue_SC,self.queue_UI)

        # Initializes the system controller
        self.initializeSystemController(self.queue_SC)

    # Method for defining the functionality of the buttons
    def buttonFunctionality(self):
        print('buttonFunctionality - UI - accessed')

        ## Set up slider controls
        # Movement sliders
        self.sliderMovementForward.valueChanged.connect(self.moveForward)
        self.sliderMovementVertical.valueChanged.connect(self.moveVertical)
        self.sliderMovementZRotation.valueChanged.connect(self.rotateZ)
        # Trim sliders
        self.sliderTrimHorizontal.valueChanged.connect(self.trimHorizontal)
        self.sliderTrimVertical.valueChanged.connect(self.trimVertical)

    def trimHorizontal(self,value):
        print('trimeHorizontal - UI - accessed')

    def trimVertical(self,value):
        print('trimVertial - UI - accessed')


    def moveForward(self,value):
        print('moveForward - UI - accessed')
        self.boxProp1.setText(str(value))
        self.boxProp2.setText(str(value))
        self.queue_UI.put(array('f',[1,value]))


    def moveVertical(self,value):
        print('moveVertical - UI - accessed')
        self.boxProp3.setText(str(value))
        self.boxProp4.setText(str(value))
        self.queue_UI.put(array('f',[2,value]))

    def rotateZ(self,value):
        print('rotateZ - UI - accessed')
        self.boxProp1.setText(str(value))
        self.boxProp2.setText(str(-value))
        self.queue_UI.put(array('f',[3,value]))

    def printValue(self,value):
        print(value)

    def initializeDelegate(self,queue_SC,queue_UI):
        print('initializeDelegate - UI - accessed')
        ## Starting the delegate
        # Creates an instance of the delegate
        # print('Creating delegate')
        self.delegate = delegate.Delegate(queue_SC,queue_UI)
        # Creates a thread from the delegate
        # print('Creating process for delegate')
        self.delegateThread = threading.Thread(target = self.delegate.run, args=())
        # Makes the delegate thread a not daemon process so it can spawn additional processes
        # print('Setting delegate process as not daemon')
        self.delegateThread.daemon = True
        # Starts the delegate thread
        # print('Starting the delegate process')
        self.delegateThread.start()

    def initializeSystemController(self,queue_SC):
        print('initializeSystemController - UI - accessed')
        ## Starting the system controller
        # Creates an instance of the system controller
        # print('Creating system controller')
        self.systemController = sc.SystemController(queue_SC)
        # Creates a thread for the system controller
        # print('Creating process for system controller')
        self.systemControllerThread = threading.Thread(target = self.systemController.run, args=())
        # Makes the system controller thread a not daemon process so it can spawn additional processes
        # print('Setting system controller process as not daemon')
        self.systemControllerThread.daemon = True
        # Starts the system controller thread
        # print('Starting the system controller process')
        self.systemControllerThread.start()


# Main function that loads and runs the UI for testing
def applicationMain():
    print('applicationMain - UI - accessed')
    ## Loading and displaying the UI
    # Creates the GUI application
    print('Creating GUI application')
    app = QtGui.QApplication(sys.argv)
    # Creates the class instance defining what to display
    print('Creating an instance of the UI')
    ex = UI()
    # Shows the class instance
    print('Showing the instance of the UI')
    ex.show()
    # Exits the program when the GUI application is exited
    sys.exit(app.exec_())

if __name__ == '__main__':
    applicationMain()