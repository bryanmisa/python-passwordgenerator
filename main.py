import sys
import string
import random
from PyQt5 import *
from PyQt5.QtWidgets import QDialog, QApplication,QMessageBox
from PasswordGeneratorGUI import Ui_Form
from PasswordGeneratorGUI import *


class AppWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.show()

 

    def generate_password(self) :
        
        lowercase = ""
        uppercase = ""
        numbers = ""
        special_characters = ""
        result = ''
        pass_length = 0

           
        if self.ui.numbers_cb.isChecked():
            numbers = string.digits
            
        if self.ui.specialcharacter_cb.isChecked() :
            special_characters = string.punctuation           

       
        if self.ui.radioButton_6.isChecked() :
            pass_length = 6
        
        elif self.ui.radioButton_8.isChecked() :
                pass_length = 8
        
        elif self.ui.radioButton_12.isChecked() :
                pass_length = 12

        elif self.ui.radioButton_16.isChecked() :
            pass_length = 16

        elif self.ui.radioButton_24.isChecked() :
            pass_length = 24

        else :
            pass_length = 4

        result  =  numbers + special_characters + string.ascii_lowercase + string.ascii_uppercase

        passw = ''.join(random.sample(result, pass_length))
                         
        self.ui.showpassword_tb.setText(passw)

        
if __name__ == "__main__":        
    app = QApplication(sys.argv)
    w = AppWindow()
    w.show()
    sys.exit(app.exec_())