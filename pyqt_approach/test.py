        # #--------------------------------------  
        # # Creating a Tools Menu  
        # #--------------------------------------  
        # self.Toolsmenu = self.menuBar().addMenu('&Tools')  
        # #--------------------------------------  
        # # Creating a Tools Toolbar  
        # #--------------------------------------  
        # self.Toolstoolbar = QToolBar('Tools')  
        # self.Toolstoolbar.setIconSize(QSize(30, 30))  
        # self.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.Toolstoolbar)
        # # creating the menu options
        # # calling the user defined makeAction() method to create the action for the menu options
        # self.hand_opt = self.makeAction(self, './utils/hand.ico', 'Hand Tool', 'Hand Tool', self.hand)
        # # using the setShortcut() method to set a shortcut to execute the 'Open' command  
        # self.hand_opt.setShortcut(QKeySequence.Hand)
        # # calling the user-defined makeAction() method to create the action to print the file  
        # self.draw_opt = self.makeAction(self, './utils/paint.ico', 'Draw Tool', 'Draw Tool', self.draw)
        # #using the setShortcut() method to set a shortcut to execute the 'Print' command
        # self.draw_opt.setShortcut(QKeySequence.Draw)
        # # initially disabling the action by setting the value of setEnabled() method to False  
        # self.draw_opt.setEnabled(False)
        # # using the addActions() method to add all the created actions to the 'File' menu and toolbar 
        # self.toolsmenu.addActions([self.hand_opt, self.draw_opt])
        # self.toolstoolbar.addActions([self.hand_opt, self.draw_opt])  
        # # adding the separator  
        # self.toolsmenu.addSeparator()  
        # # calling the user-defined makeAction() method to create the action to close the application  
        # self.circle_opt = self.makeAction(self, './utils/circle.ico', 'Circle Tool', 'Circle Tool', self.close) 
        # # using the setShortcut() method to set a shortcut to execute the 'Close' command  
        # self.circle_opt.setShortcut(QKeySequence.Circle)
        # # using the addActions() method to add all the created actions to the 'File' menu and toolbar  
        # self.toolsmenu.addActions([self.cirle_opt])

