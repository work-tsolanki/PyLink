from PyQt5 import QtWidgets, QtCore
import sys
import ctypes


class Application():

    def __init__(self):

        self.app = QtWidgets.QApplication(sys.argv)
        main_window = QtWidgets.QWidget()

        #fetching Width x Height of Window
        try:
            user32 = ctypes.windll.user32
            user32.SetProcessDPIAware() 
            width = user32.GetSystemMetrics(0)  
            height = user32.GetSystemMetrics(1)
        except AttributeError:
            QtWidgets.QMessageBox.warning(self.app, "Error", "Couldn't fetch resolution. Set to default")
            main_window.setGeometry(0,0, 1920, 1080)
        else:
            main_window.setGeometry(0,0, width, height)
            

        
        
        main_window.show()
        self.app.exec_()
        
        
        
app = Application()
