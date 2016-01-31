'''
This is the delegate file for the capstone project.
This will create the class that delegates how information is passed between the different modules of the application.
'''

## Imports
# Build in modules
import multiprocessing # Allows access to multiprocessing
import time # Allows access to time
# Custom modules

# Delegate class
class Delegate():
    # Initiating the class
    def __init__(self,queue_SC,queue_UI):
        print('__init__ - delegate - accessed')
        self.queue_SC = queue_SC
        self.queue_UI = queue_UI

    def run(self):
        print('run - delegate - accessed')
        delegateRun = True
        while delegateRun:
            # print('delegate loop running')
            forwardMovement = self.queue_UI.get()
            self.queue_SC.put(forwardMovement)

