#######JOSEPH VUSUMZI DUDA#######
#DEVELOPED IN 2023
#This is a guessing game application using PyQt5
#It allows users to guess a random number between 1 and 10
#Users can change the background color and picture displayed    
#The application has a simple GUI with buttons and labels
#It uses a grid layout to organize the interface    
#It includes features for guessing, changing settings, and starting a new game
#Assumes you have PyQt5 installed and a pictures named 'mickey.gif' and 'pluto.gif' in the same directory
#Error handling is minimal and assumes correct user input



import sys                         # imports standard Python sys module
from PyQt5.QtWidgets import *       # imports PyQt5 widget modules
from PyQt5.QtGui import *          # imports PyQt5 GUI modules
from random import*              # imports random  module

class my_widget(QWidget):                   # define class for widget which inherits from QWidget
    def __init__(self,parent=None):           # constructor object method 
        QWidget.__init__(self,parent)            # calling QWidget constructor
        self.setWindowTitle('Guessing game')    # Set Window title
        self.setGeometry(300, 300, 500,350)   # set Geometry for window
        
        # creating picture part widget  window default
        picture_widget=QWidget() # create window object for picture
        self.mickey_pic=QPixmap('mickey.gif')
        self.pic_widget=QLabel(self)
        self.pic_widget.setPixmap(self.mickey_pic)
        picture_widget=self.pic_widget
        #creating interface part widget window
        interface_widget=QWidget()                   # create window object for interface grid
        interface_label=QLabel('Interface:')          # create label
        interface_label.setFont(QFont('Times',18))   # set fornt
        
        picture_label=QLabel('Picture:')               # create picture label
        self.picture_checkbox=QComboBox()            # create combo box for pictures
        self.picture_checkbox.addItem('Mickey')       # add item Mickey to picture combo box
        self.picture_checkbox.addItem('Pluto')      # add item Pluto to picture combo box
        
        colour_label=QLabel('Colour:')
        self.colour_checkbox=QComboBox()   # create combobox for colors
        self.colours=['white','black','cyan','darkCyan','red','darkRed','magenta','darkMagenta','green','darkGreen','yellow','darkYellow','blue','darkBlue','gray','darkGray','lightGray']                                     # create list of colors
        for j in self.colours:
            self.colour_checkbox.addItem(j)                         # add all colors to the combo box for colors
        self.change_button=QPushButton('Change')                    # create change button
        self.change_button.clicked.connect(self.change_clicked)     # connect change button to change_clicked function
        
        self.close_button=QPushButton('Close')                      # create close button
        self.close_button.clicked.connect(self.close_clicked)       # connect close button to close_clicked function
        
        self.new_game_button=QPushButton('New Game')                # create new game button
        self.new_game_button.clicked.connect(self.new_game_clicked) # connect new game button to new_game_clicked function
        #interface grid
        grid_interface=QGridLayout()                               # create grid layout
        grid_interface.addWidget(interface_label,0,0)                # add label in position 0,0
        grid_interface.addWidget(picture_label,1,0)                   # add label in position 1,0
        grid_interface.addWidget(self.picture_checkbox,1,1)            # add color combo box in position 1,1
        grid_interface.addWidget(colour_label,2,0)                      # add label in position 2,0
        grid_interface.addWidget(self.colour_checkbox,2,1)              # add picture combo box in position 2,1
        grid_interface.addWidget(self.change_button,2,2)              # add change button in position 2,2
        grid_interface.addWidget(self.close_button,3,0)             # add change button in position 3,0
        grid_interface.addWidget(self.new_game_button,3,1)        # add change button in position 3,1
        interface_widget.setLayout(grid_interface)              # set grid layout as interface_widget’s layout
        
        #Create Guess Widget Window
        guesses_widget=QWidget()                               # create window object for guesses grid
        self.guesses_label=QLabel('Guesses:')                  # set window title for guesses grid
        self.guesses_label.setFont(QFont('Times',18))          # set font size
        
        self.guesses_1_label=QLabel('')             # create guess 1 label
        self.guesses_1_label_user_input=QLabel('')           # set label to be empty
        self.guesses_1_label_user_reply=QLabel('')            # set label to be empty
        self.guesses_2_label=QLabel('')                # create guess 2 label
        self.guesses_2_label_user_input=QLabel('')              # set label to be empty
        self.guesses_2_label_user_reply=QLabel('')               # set label to be empty
        self.guesses_3_label=QLabel('')                 # create guess 3 label
        self.guesses_3_label_user_input=QLabel('')             # set label to be empty
        self.guesses_3_label_user_reply=QLabel('')           # set label to be empty
        self.guess_input=QLineEdit()                       # create line edit
        self.guess_button=QPushButton('Guess')           # create guess button
        self.guess_button.clicked.connect(self.guess_clicked)                 # link guess botton to guess_clicked function
        
        #guess grid
        self.guess_grid=QGridLayout()                                    # create grid layout
        self.guess_grid.addWidget(self.guesses_label,0,0)                 # add label in position 0,0
        self.guess_grid.addWidget(self.guesses_1_label,1,0)                # add label in position 1,0
        self.guess_grid.addWidget(self.guesses_1_label_user_input,1,1)      # add label in position 1,1
        self.guess_grid.addWidget(self.guesses_1_label_user_reply,1,2)       # add label in position 1,2
        self.guess_grid.addWidget(self.guesses_2_label,2,0)                   # add label in position 2,0
        self.guess_grid.addWidget(self.guesses_2_label_user_input,2,1)         # add label in position 2,1
        self.guess_grid.addWidget(self.guesses_2_label_user_reply,2,2)        # add label in position 2,2
        self.guess_grid.addWidget(self.guesses_3_label,3,0)                  # add label in position 3,0
        self.guess_grid.addWidget(self.guesses_3_label_user_input,3,1)      # add label in position 3,1
        self.guess_grid.addWidget(self.guesses_3_label_user_reply,3,2)     # add label in position 3,2
        self.guess_grid.addWidget(self.guess_input,4,1)                   # add label in position4,1
        self.guess_grid.addWidget(self.guess_button,4,2)                 # add label in position 4,2
        guesses_widget.setLayout(self.guess_grid)                       # set grid layout as guesses_widget’s layout
        #main window
        self.vertical_widget=QWidget()                            # create window object for guesses grid and interface grid
        self.main_vertical=QVBoxLayout()                          # create vertical layyout
        self.main_vertical.addWidget(guesses_widget)
        self.main_vertical.addWidget(interface_widget)
        self.vertical_widget.setLayout(self.main_vertical)        # set vertical layout as vertical_widget’s layout
        
        self.main_horizontal=QHBoxLayout(self)                    # create horizontal layout
        self.main_horizontal.addWidget(picture_widget)
        self.main_horizontal.addWidget(self.vertical_widget)
        self.setLayout(self.main_horizontal)                      # set horizontal layout as widget’s layout

        
    def change_clicked(self):                                     # define function linked to change button
        #changing colours
        colour=self.colour_checkbox.currentText()                 # get current/selected color
        self.setPalette(QPalette(QColor(colour)))                 # set background to selected color
        self.setAutoFillBackground(True)        
        #changing pictures
        picture=self.picture_checkbox.currentText()               # get current/selected picture
        self.pic_widget.setPixmap(QPixmap(picture+'.gif'))        # set picture to selected picture
        
    def close_clicked(self):  # define function linked to close button
        self.close()            # close the window
       
    def new_game_clicked(self):                       # define function linked to new game button
        #function to make all messages and numbers for guesses to be empty again            self.guesses_2_label.setText('Guess 2:')
        self.guesses_1_label.setText('')
        self.guesses_1_label_user_input.setText('')   # set label to be empty
        self.guesses_1_label_user_reply.setText('')   # set label to be empty
         
        self.guesses_2_label.setText('')
        self.guesses_2_label_user_input.setText('')   # set label to be empty
        self.guesses_2_label_user_reply.setText('')   # set label to be empty
               
        self.guesses_3_label_user_input.setText('')   # set label to be empty
        self.guesses_3_label_user_reply.setText('')   # set label to be empty
        self.guesses_3_label.setText('')   
    def guess_clicked(self):                               # define function linked to guess button 
        # function to show appropiate messages after guessing
        random_number=randint(1,10)  # generate random integers from 1 to 10 inclusive
        guessed_num = int(self.guess_input.displayText())  # get guessed number from the guess_input QLineEdit
        
        if self.guesses_1_label_user_input.text()=='':     # check if label to display input for guess 1 is empty or not
            if guessed_num>random_number:                  # check if user guessed input is greater than randomised integer
                message='Too High'       
            elif guessed_num<random_number:                # check if user guessed input is lesser than randomised integer
                message='Too Low'     
            elif guessed_num==random_number:               # check if user guessed input is equal to randomised integer
                message='Correct!'         
            self.guesses_1_label.setText('Guess 1:')
            self.guesses_2_label.setText('')
            self.guesses_3_label.setText('')            
            self.guesses_1_label_user_input.setText(str(guessed_num))    #update label value which shows user input for guess 1
            self.guesses_1_label_user_reply.setText(message)             #update label value which shows appropriate message for guess 3
            
        elif self.guesses_2_label_user_input.text()=='' and self.guesses_1_label_user_reply.text()!='Correct!':    # check if label to display input for guess 2 is empty or not
            if guessed_num>random_number:                   # check if user guessed input is greater than randomised integer
                message='Too High'        
            elif guessed_num<random_number:                 # check if user guessed input is lesser than randomised integer
                message='Too Low'   
            elif guessed_num==random_number:                # check if user guessed input is equal to randomised integer
                message='Correct!'            
            self.guesses_2_label.setText('Guess 2:')
            self.guesses_3_label.setText('')
            self.guesses_2_label_user_input.setText(str(guessed_num))   # update label value which shows user input for guess 2
            self.guesses_2_label_user_reply.setText(message)            # update label value which shows appropriate message for guess 3
            
        elif self.guesses_3_label_user_input.text()=='' and self.guesses_2_label_user_reply.text()!='Correct!'and self.guesses_1_label_user_reply.text()!='Correct!':    # check if label to display input for guess 3 is empty or not
            if guessed_num>random_number:                   # check if user guessed input is greater than randomised integer
                message='Too Big'        
            elif guessed_num<random_number:                 # check if user guessed input is lesser than randomised integer
                message='Too small'   
            elif guessed_num==random_number:                # check if user guessed input is equal to randomised integer
                message='Correct!'            
            self.guesses_3_label.setText('Guess 3:')
            self.guesses_3_label_user_input.setText(str(guessed_num))   # update label value which shows user input for guess 3
            self.guesses_3_label_user_reply.setText(message)      # update label value which shows appropriate message for guess 3
def main():                      # define main function
    app=QApplication(sys.argv)     # imports PyQt5 widget modules
    game_widget=my_widget()         # create window object
    game_widget.show()              # show window
    sys.exit(app.exec_())         # start executing main app event loop

main()                           #call the main function