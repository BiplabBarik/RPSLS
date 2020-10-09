##############################################################################
############### Rock Paper Scissor Lizard Spock Arcade Game  #################
############### Author : Biplab Barik                        #################
############### Date   : Oct 2020                            #################
##############################################################################

#!/usr/bin/python

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5 import QtCore 
from PyQt5.QtGui import *
import sys
import webbrowser
import random
import mysql.connector

IDtoIconPath = [
     "Resources/Handsigns/sign_rock.png",
     "Resources/Handsigns/sign_paper.png",
     "Resources/Handsigns/sign_scissor.png",
     "Resources/Handsigns/sign_lizard.png",
     "Resources/Handsigns/sign_spock.png",
     ]

############################    GAME UI Engine     ###########################
class Ui(QtWidgets.QMainWindow):
     def __init__(self):
          super(Ui, self).__init__()
          
          #Load Main Page
          self.LoadMainPage()
          
          self.show()
     
     def LoadMainPage(self):
          uic.loadUi('Resources/UI_Files/MainGamePage.ui', self)
          self.main_widget = self.findChild(QtWidgets.QWidget, 'centralwidget')
          self.main_widget.setStyleSheet(
               "background-image: url(Resources/Background/BackgroundMain.jpg)")
          
          #Configure Buttons
          self.button_rps = self.findChild(QtWidgets.QPushButton, 'button_rps') 
          self.button_rps.clicked.connect(self.LoadRPSPage)
        
          self.button_rpsls = self.findChild(QtWidgets.QPushButton, 'button_rpsls')
          self.button_rpsls.clicked.connect(self.LoadRPSLSPage)
        
          self.button_rules = self.findChild(QtWidgets.QPushButton, 'button_rules')
          self.button_rules.clicked.connect(self.LoadRulesPage)
        
          self.button_authr = self.findChild(QtWidgets.QPushButton, 'button_author')
          self.button_authr.clicked.connect(self.OpenAuthorPage)
          
          #Configure Animation
          self.Anim_gif = QMovie('Resources/Animation/GIF_Background.gif')
        
          self.label_intro = self.findChild(QtWidgets.QLabel, 'welcome_label_gif')
          self.label_intro.setMovie(self.Anim_gif)
          self.label_rps_gif = self.findChild(QtWidgets.QLabel, 'rps_gif')
          self.label_rps_gif.setMovie(self.Anim_gif)
          self.label_rpsls_gif = self.findChild(QtWidgets.QLabel, 'rpsls_gif')
          self.label_rpsls_gif.setMovie(self.Anim_gif)
          self.label_rules_gif = self.findChild(QtWidgets.QLabel, 'rules_gif')
          self.label_rules_gif.setMovie(self.Anim_gif)
          
          self.Anim_gif.start()
          self.show()
     
     def LoadRPSPage(self):
          #Load Rock Paper Scissor Game Page
          uic.loadUi('Resources/UI_Files/RPSGamePage.ui', self)
        
          self.rps_gidget = self.findChild(QtWidgets.QWidget, 'widget_rps')
          self.rps_gidget.setStyleSheet(
               "background-image: url(Resources/Background/BackgroundBlue_Dark.jpg)")
        
          self.button_back = self.findChild(QtWidgets.QPushButton, 'button_back')
          self.button_back.clicked.connect(self.LoadMainPage)
          self.button_reset = self.findChild(QtWidgets.QPushButton, 'button_reset')
          self.button_reset.clicked.connect(self.ResetGame)
        
          self.button_rock = self.findChild(QtWidgets.QPushButton, 'button_rock')
          self.button_papr = self.findChild(QtWidgets.QPushButton, 'button_paper')
          self.button_sicr = self.findChild(QtWidgets.QPushButton, 'button_scissor')
          
          #Load Button commands
          self.button_rock.clicked.connect(lambda: self.RPS_PlyrImageSelect(0))
          self.button_papr.clicked.connect(lambda: self.RPS_PlyrImageSelect(1))
          self.button_sicr.clicked.connect(lambda: self.RPS_PlyrImageSelect(2))
        
          #Load Button Icons
          self.button_rock.setIcon(QIcon("Resources/Handsigns/sign_rock.png"));
          self.button_papr.setIcon(QIcon("Resources/Handsigns/sign_paper.png"));
          self.button_sicr.setIcon(QIcon("Resources/Handsigns/sign_scissor.png"));
          
          #Load Player Computer selection label
          self.label_comp = self.findChild(QtWidgets.QLabel, 'label_comp')
          self.label_plyr = self.findChild(QtWidgets.QLabel, 'label_plyr')
          
          #Result Label
          self.label_result = self.findChild(QtWidgets.QLabel, 'label_result')
          self.label_result.clear()
          
          self.show()
          
          
     def LoadRPSLSPage(self):
          #Load Rock Paper Scissor Lizard Spock Game Page
          uic.loadUi('Resources/UI_Files/RPSLSGamePage.ui', self)
        
          self.rps_gidget = self.findChild(QtWidgets.QWidget, 'widget_rpsls')
          self.rps_gidget.setStyleSheet(
               "background-image: url(Resources/Background/BackgroundRed_Dark.jpg)")
        
          self.button_back = self.findChild(QtWidgets.QPushButton, 'button_back')
          self.button_back.clicked.connect(self.LoadMainPage)
          self.button_reset = self.findChild(QtWidgets.QPushButton, 'button_reset')
          self.button_reset.clicked.connect(self.ResetGame)
        
          self.button_rock = self.findChild(QtWidgets.QPushButton, 'button_rock')
          self.button_papr = self.findChild(QtWidgets.QPushButton, 'button_papr')
          self.button_sicr = self.findChild(QtWidgets.QPushButton, 'button_sicr')
          self.button_lizr = self.findChild(QtWidgets.QPushButton, 'button_lizd')
          self.button_spok = self.findChild(QtWidgets.QPushButton, 'button_spok')
          
          #Load Button commands
          self.button_rock.clicked.connect(lambda: self.RPSLS_PlyrImageSelect(0))
          self.button_papr.clicked.connect(lambda: self.RPSLS_PlyrImageSelect(1))
          self.button_sicr.clicked.connect(lambda: self.RPSLS_PlyrImageSelect(2))
          self.button_lizr.clicked.connect(lambda: self.RPSLS_PlyrImageSelect(3))
          self.button_spok.clicked.connect(lambda: self.RPSLS_PlyrImageSelect(4))
        
          #Load Button Icons
          self.button_rock.setIcon(QIcon("Resources/Handsigns/sign_rock.png"));
          self.button_sicr.setIcon(QIcon("Resources/Handsigns/sign_scissor.png"));
          self.button_papr.setIcon(QIcon("Resources/Handsigns/sign_paper.png"));
          self.button_lizr.setIcon(QIcon("Resources/Handsigns/sign_lizard.png"));
          self.button_spok.setIcon(QIcon("Resources/Handsigns/sign_spock.png"));
          
          #Load Player Computer selection label
          self.label_comp = self.findChild(QtWidgets.QLabel, 'label_comp')
          self.label_plyr = self.findChild(QtWidgets.QLabel, 'label_plyr')
          
          #Result Label
          self.label_result = self.findChild(QtWidgets.QLabel, 'label_result')
          self.label_result.clear()
          
          self.show()
     
     #RPS Game
     def RPS_PlyrImageSelect(self,plyr_num):
          print("Player Option "+str(plyr_num))
          
          ImagePath = IDtoIconPath[plyr_num]
          self.plyr_pixmap = QPixmap(ImagePath)
          self.plyr_pixmap = self.plyr_pixmap.scaled(128,128)
          self.label_plyr.setPixmap(self.plyr_pixmap)
          
          #Generate Random
          comp_num = random.randint(0,2)
          self.RPS_CompImageSelect(comp_num);
          
          #Compute Result
          self.CalculateResultRPS(plyr_num,comp_num)
          
     def RPS_CompImageSelect(self,comp_num):
          print("Computer Option "+str(comp_num))
          
          ImagePath = IDtoIconPath[comp_num]
          self.comp_pixmap = QPixmap(ImagePath)
          self.comp_pixmap = self.comp_pixmap.scaled(128,128)
          self.label_comp.setPixmap(self.comp_pixmap)
     
     
     def CalculateResultRPS(self,plyr,comp):
          #Determine the Winner
          
          if ((plyr == 0 and comp == 2)
              or (plyr == 1 and comp == 0)
               or (plyr == 2 and comp == 1)):
               result_text = "Game Won"
               self.label_result.setStyleSheet("color : lightgreen;");
          elif comp == plyr :
               result_text = "Game Tied"
               self.label_result.setStyleSheet("color : white;");
          else :
               result_text = "Game Lost"
               self.label_result.setStyleSheet("color : red;");
               
          self.label_result.setText(result_text)
     
     
     
     #RPSLS Game
     def RPSLS_PlyrImageSelect(self,plyr_num):
          print("Player Option "+str(plyr_num))
          
          ImagePath = IDtoIconPath[plyr_num]
          self.plyr_pixmap = QPixmap(ImagePath)
          self.plyr_pixmap = self.plyr_pixmap.scaled(128,128)
          self.label_plyr.setPixmap(self.plyr_pixmap)
          
          #Generate Random
          comp_num = random.randint(0,4)
          self.RPSLS_CompImageSelect(comp_num);
          
          #Compute Result
          self.CalculateResultRPSLS(plyr_num,comp_num)
          
     def RPSLS_CompImageSelect(self,comp_num):
          print("Computer Option "+str(comp_num))
          
          ImagePath = IDtoIconPath[comp_num]
          self.comp_pixmap = QPixmap(ImagePath)
          self.comp_pixmap = self.comp_pixmap.scaled(128,128)
          self.label_comp.setPixmap(self.comp_pixmap)
          
     def CalculateResultRPSLS(self,plyr,comp):
          #Determine the Winner
          
          if ((plyr == 0 and comp == 2) or (plyr == 0 and comp == 3) or
              (plyr == 1 and comp == 0) or (plyr == 1 and comp == 4) or 
              (plyr == 2 and comp == 1) or (plyr == 2 and comp == 3) or
              (plyr == 3 and comp == 1) or (plyr == 3 and comp == 4) or
              (plyr == 4 and comp == 2) or (plyr == 4 and comp == 0)
              ):
               result_text = "Game Won"
               self.label_result.setStyleSheet("color : lightgreen;");
          elif comp == plyr :
               result_text = "Game Tied"
               self.label_result.setStyleSheet("color : white;");
          else :
               result_text = "Game Lost"
               self.label_result.setStyleSheet("color : red;");
               
          self.label_result.setText(result_text)
     
     def ResetGame(self):
          #Reset Game
          self.label_comp.clear()
          self.label_plyr.clear()
          self.label_result.clear()
          
     def LoadRulesPage(self):
          uic.loadUi('Resources/UI_Files/RulesPage.ui', self)
        
          self.rules_widget = self.findChild(QtWidgets.QWidget, 'widget_rules')
          self.rules_widget.setStyleSheet(
               "background-image: url(Resources/Background/BackgroundBlue_Dark.jpg)")
        
          self.button_back = self.findChild(QtWidgets.QPushButton, 'button_back')
          self.button_back.clicked.connect(self.LoadMainPage)
        
          self.label_rule_rps   = self.findChild(QtWidgets.QLabel , 'label_rule_rps')
          self.label_rule_rpsls = self.findChild(QtWidgets.QLabel , 'label_rule_rpsls')
          self.label_rule_rpsls.setHidden(True)
        
          self.rb_rule_rbs   = self.findChild(QtWidgets.QRadioButton , 'rb_rps')
          self.rb_rule_rbsls = self.findChild(QtWidgets.QRadioButton , 'rb_rpsls')
          self.rb_rule_rbs.setChecked(True);
        
          self.label_rule = self.findChild(QtWidgets.QLabel , 'label_ruleimage')
          self.pixmap = QPixmap("Resources/Rules/RPS.png")
          self.pixmap = self.pixmap.scaled(321,221)
          self.label_rule.setPixmap(self.pixmap)
        
          self.rb_rule_rbs.toggled.connect(self.RB_RPSSelected)
          self.rb_rule_rbsls.toggled.connect(self.RB_RPSLSSelected)
        
          self.show()
     
     
     def RB_RPSSelected(self):
          self.label_rule_rpsls.setHidden(True)
          self.label_rule_rps.setHidden(False)
        
          #Update Image
          self.pixmap = QPixmap("Resources/Rules/RPS.png")
          self.pixmap = self.pixmap.scaled(321,221)
          self.label_rule.setPixmap(self.pixmap)
     
     def RB_RPSLSSelected(self):
          self.label_rule_rps.setHidden(True)
          self.label_rule_rpsls.setHidden(False)
        
          #Update Image
          self.pixmap = QPixmap("Resources/Rules/RPSLS.png")
          self.pixmap = self.pixmap.scaled(321,221)
          self.label_rule.setPixmap(self.pixmap)
          
          
     def OpenAuthorPage(self):
          #Open WebBrowser Page
          webbrowser.open('https://github.com/BiplabBarik/')
          return


def main(): 
     GameApp = QtWidgets.QApplication(sys.argv)
     GameWindow = Ui()
     GameApp.exec_()

if __name__ == '__main__':
     main()
