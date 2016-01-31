'''
This is the system controller file for the capstone project.
This will be where most of the processing of commands is handled.
'''

## Imports
# Build in modules

# Custom modules

# System controller class
class SystemController():
    # Initiating the class
    def __init__(self,queue_SC):
        print('__init__ - systemController - accessed')
        # Sets up the queue between the delegate and the system controller
        self.queue_SC = queue_SC

    def run(self):
        print('run - systemController - accessed')
        systemControllerRun = True
        while systemControllerRun:
            # print('delegate loop running')
            propCommand = self.queue_SC.get()

            for i in propCommand:
                print(i)