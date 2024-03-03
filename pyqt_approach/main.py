# importing the required module  
import sys
from PyQt5.QtCore import Qt, QSize, QRect
from PyQt5.QtWidgets import QApplication, QLabel, QSizePolicy, QScrollArea, QMessageBox, QMainWindow, QMenu, QAction, qApp, QFileDialog, QToolBar
from PyQt5.QtGui import QImage, QPixmap, QPalette, QPainter, QIcon, QKeySequence
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter

class QImageViewer(QMainWindow):
    # defining the initializing function
    def __init__(self):
        super().__init__()
        # configuring the window
        self.setWindowTitle('Pratyaksa - Spatial Data Analysis Tool')
        # configuring the width and height of the window  
        self.window_width, self.window_height = self.geometry().width(), self.geometry().height()
        # setting the icon of the window
        self.setWindowIcon(QIcon('./utils/icon.png'))
        # using the resize() to set the size of the application  
        self.resize(self.window_width * 2, self.window_height * 2)
        # creating an object of the QPrinter class
        self.printerObj = QPrinter()
        # setting the initial scale factor
        self.scale_factor = 0.0
        # creating an object of the QLabel class to display the label
        self.image_label = QLabel()
        # setting the background color of the label to display the image using the setBackgoundRole() method and QPalette class
        self.image_label.setBackgroundRole(QPalette.Base)
        # setting the size policy of the label using the setSizePolicy() method and QSizePolicy class
        self.image_label.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        #setting the setScaledContents() method to True to manually adjust the aspect ratio of the image in the application
        self.image_label.setScaledContents(True)
        # creating an object of the QScrollArea class to display the scroll area
        self.scroll_area = QScrollArea()
        # setting the background color of the scroll to discplay the background using the setBackgoundRole() method and QPalette class 
        self.scroll_area.setBackgroundRole(QPalette.Dark)
        # setting the scrolling area to the image label using the setWidget() method  
        self.scroll_area.setWidget(self.image_label) 
        # setting the visibility of the scrolling area with the help of the setVisible() method  
        self.scroll_area.setVisible(False)
        # setting the central widget to the scroll area using the setCentralWidget() method 
        self.setCentralWidget(self.scroll_area)

        #--------------------------------------  
        # Creating a File Menu  
        #--------------------------------------  
        self.filemenu = self.menuBar().addMenu('&File')  
        #--------------------------------------  
        # Creating a File Toolbar  
        #--------------------------------------  
        self.filetoolbar = QToolBar('File')  
        self.filetoolbar.setIconSize(QSize(30, 30))  
        self.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.filetoolbar)
        # creating the menu options
        # calling the user defined makeAction() method to create the action for the menu options
        self.open_doc_opt = self.makeAction(self, 'utils/openImage.ico', 'Open Image...', 'Open Image...', self.openImage)
        # using the setShortcut() method to set a shortcut to execute the 'Open' command  
        self.open_doc_opt.setShortcut(QKeySequence.Open)
        # calling the user-defined makeAction() method to create the action to print the file  
        self.print_opt = self.makeAction(self, './utils/printer.ico', 'Print', 'Print', self.printImage)
        #using the setShortcut() method to set a shortcut to execute the 'Print' command
        self.print_opt.setShortcut(QKeySequence.Print)
        # initially disabling the action by setting the value of setEnabled() method to False  
        self.print_opt.setEnabled(False)
        # using the addActions() method to add all the created actions to the 'File' menu and toolbar 
        self.filemenu.addActions([self.open_doc_opt, self.print_opt])
        self.filetoolbar.addActions([self.open_doc_opt, self.print_opt])  
        # adding the separator  
        self.filemenu.addSeparator()  
        # calling the user-defined makeAction() method to create the action to close the application  
        self.exit_opt = self.makeAction(self, '', 'Exit', 'Exit', self.close) 
        # using the setShortcut() method to set a shortcut to execute the 'Close' command  
        self.print_opt.setShortcut(QKeySequence.Close)
        # using the addActions() method to add all the created actions to the 'File' menu and toolbar  
        self.filemenu.addActions([self.exit_opt])

        #--------------------------------------  
        # Creating a View Menu  
        #--------------------------------------  
        self.viewmenu = self.menuBar().addMenu('&View')  
        #--------------------------------------  
        # Creating an View Tool bar  
        #--------------------------------------  
        self.viewtoolbar = QToolBar('Edit')  
        self.viewtoolbar.setIconSize(QSize(30, 30))  
        self.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.viewtoolbar) 
        self.zoomIN_opt = self.makeAction(self, './utils/zoomIn.ico', 'Zoom In (25%)', 'Zoom In (25%)', self.zoom_in)
        # calling the user-defined makeAction() method to create the action to zoom in the image
        self.zoomIN_opt.setShortcut(QKeySequence.ZoomIn)
        # initially disabling the action by setting the value of setEnabled() method to False
        self.zoomIN_opt.setEnabled(False)
        # calling the user-defined makeAction() method to create the action to zoom out the image  
        self.zoomOUT_opt = self.makeAction(self, './utils/zoomOut.ico', 'Zoom Out (25%)', 'Zoom Out (25%)', self.zoom_out) 
        # using the setShortcut() method to set a shortcut to execute the 'Zoom Out' command  
        self.zoomOUT_opt.setShortcut(QKeySequence.ZoomOut)  
        # initially disabling the action by setting the value of setEnabled() method to False  
        self.zoomOUT_opt.setEnabled(False)  
        # calling the user-defined makeAction() method to create the action to set the normal size of the image  
        self.normalSize_opt = self.makeAction(self, '', 'Normal Size', 'Normal Size', self.normal_size)
        # using the setShortcut() method to set a shortcut to execute the 'Normal Size' command
        self.normalSize_opt.setShortcut(QKeySequence('Ctrl+S'))
        # initially disabling the action by setting the value of setEnabled() method to False
        self.normalSize_opt.setEnabled(False)
        # setting the initial value of setCheckable() method to True
        self.normalSize_opt.setCheckable(True)
        # using the addActions() method to add all the created actions to the 'View' menu and toolbar  
        self.viewmenu.addActions([self.zoomIN_opt, self.zoomOUT_opt, self.normalSize_opt])
        self.viewtoolbar.addActions([self.zoomIN_opt, self.zoomOUT_opt])  
        # adding the separator  
        self.viewmenu.addSeparator()  
        self.viewtoolbar.addSeparator()  
        # calling the user-defined makeAction() method to create the action to fit the image to the window  
        self.fitToWindow_opt = self.makeAction(self, './utils/fitToWindow.ico', 'Fit To Window', 'Fit To Window', self.fit_to_window)
        # using the setShortcut() method to set a shortcut to execute the 'Fit To Window' command
        self.fitToWindow_opt.setShortcut(QKeySequence('Ctrl+F'))
        # initially disabling the action by setting the value of setEnabled() method to False
        self.fitToWindow_opt.setEnabled(False)
        # using the addActions() method to add all the created actions to the 'View' menu and toolbar
        self.viewmenu.addActions([self.fitToWindow_opt])
        self.viewtoolbar.addActions([self.fitToWindow_opt])

        # Dictionary to store loaded images for caching
        self.image_cache = {}

    # defining the required methods of the class
    # defining the method to open the image file
    def openImage(self):
        # creating an object of the QFileDialog.Options class  
        selections = QFileDialog.Options()  
        # calling the getOpenFileName() method to browse the image from the directory  
        file_name, _ = QFileDialog.getOpenFileName(  
            self,  
            'QFileDialog.getOpenFileName()',  
            '',  
            'Images (*.png *.jpeg *.jpg *.bmp *.gif)',  
            options = selections  
            )  
        # if the file name is not an empty string  
        if file_name:  
            pixmap = self.loadImage(file_name)
            if pixmap:
                self.image_label.setPixmap(pixmap)
                # enabling the visibility of the scroll area  
                self.scroll_area.setVisible(True)  
                # enabling the "Print" action  
                self.print_opt.setEnabled(True)  
                # calling the fit_to_window() method  
                self.fit_to_window()  
                # enabling the "Fit To Window" action  
                self.fitToWindow_opt.setEnabled(True)  
                # calling the update_actions() method  
                self.update_actions()  

                # if the "Fit To Window" action is not checked  
                if not self.fitToWindow_opt.isChecked():  
                    # calling the adjustSize() method to adjust the size of the image  
                    self.image_label.adjustSize() 

    def loadImage(self, file_name):
        # Load image from cache if already loaded
        if file_name in self.image_cache:
            return self.image_cache[file_name]

        # Load image and cache it
        image = QImage(file_name)
        if not image.isNull():
            pixmap = QPixmap.fromImage(image)
            self.image_cache[file_name] = pixmap
            return pixmap
        else:
            QMessageBox.information(self, 'Image Viewer', 'Cannot load %s.' % file_name)  
            return None

    #defining the method to print the image
    def printImage(self):
        # creating an object of the QPrintDialog class to print the image  
        print_dialog = QPrintDialog(self.printerObj, self)  
        # if the dialog is accepted  
        if print_dialog.exec_():  
            the_painter = QPainter(self.printerObj)  
            # creating a rectangle to place the image  
            rectangle = the_painter.viewport()  
            # defining the size of the image  
            the_size = self.image_label.pixmap().size()  
            # scaling the image to the Aspect Ratio  
            the_size.scale(rectangle.size(), Qt.KeepAspectRatio)  
            # setting the viewport of the image by calling the setViewport() method
            the_painter.setViewport(rectangle.x(), rectangle.y(), the_size.width(), the_size.height())  
            # calling the setWindow() method  
            the_painter.setWindow(self.image_label.pixmap().rect())  
            # calling the drawPixmap() method  
            the_painter.drawPixmap(0, 0, self.image_label.pixmap())

    #defining the zoom in on the image
    def zoom_in(self):
        # calling the scale_image() method to scale the image  
        self.scale_image(1.25)

    #defining the zoom out on the image
    def zoom_out(self):
        # calling the scale_image() method to scale the image  
        self.scale_image(0.8)

    #defining the method to set the normal size of the image
    def normal_size(self):
        #calling the adjustSize() method to adjust the size of the image
        self.image_label.adjustSize()
        #setting the scale factor to 1.0
        self.scale_factor = 1.0

    #defining the method to fit the image to the window
    def fit_to_window(self):
        #retriving the boolean value from the "Fit to window" action
        fitToWindow = self.fitToWindow_opt.isChecked()
        #configuring the scroll area to resizable
        self.scroll_area.setWidgetResizable(fitToWindow)
        #if the retrived value is False, calling the user-defined normal_size() method
        if not fitToWindow:
            self.normal_size()
        # calling the user defined update_actions() method
        self.update_actions()

    #defining the method to scale the image  
    def update_actions(self):
        # enabling the "Zoom In", "Zoom Out", and "Normal Size" actions, if the "Fir To Window" is unchecked
        self.zoomIN_opt.setEnabled(not self.fitToWindow_opt.isChecked()) 
        self.zoomOUT_opt.setEnabled(not self.fitToWindow_opt.isChecked())  
        self.normalSize_opt.setEnabled(not self.fitToWindow_opt.isChecked())   

    # defining the method to scale the image  
    def scale_image(self, sf):
        # defining the scaling factor of the image  
        self.scale_factor *= sf  
        # using the resize() method to resize the image as per the scaling factor 
        self.image_label.resize(self.scale_factor * self.image_label.pixmap().size())  
        # calling the user-defined adjust_scroll_bar() method to adjust the scrollbar as per the scaling factor  
        self.adjust_scroll_bar(self.scroll_area.horizontalScrollBar(), sf)
        self.adjust_scroll_bar(self.scroll_area.verticalScrollBar(), sf)  
        # toggling the "Zoom In" and "Zoom Out" actions as per the scaling factor   
        self.zoomIN_opt.setEnabled(self.scale_factor < 3.0)  
        self.zoomOUT_opt.setEnabled(self.scale_factor > 0.333)

    #defining the method to adjust the scrollbar
    def adjust_scroll_bar(self, scroll_bar, sf):  
        # setting the value of the scrollbar to the minimum value  
        scroll_bar.setValue(int(sf * scroll_bar.value() + ((sf - 1) * scroll_bar.pageStep() / 2)))

    #defining the method to create the action for the menu options
    def makeAction(self, parent, icon, name, tip, method):  
        # creating an object of the QAction class to create the action for the menu options  
        the_action = QAction(QIcon(icon), name, parent)  
        # setting the status tip of the action using the setStatusTip() method  
        the_action.setStatusTip(tip)  
        # connecting the action to the method using the triggered.connect() method  
        the_action.triggered.connect(method)  
        # returning the action  
        return the_action

# main function  
if __name__ == '__main__':  

    # creating an object of the QApplication class  

    the_app = QApplication(sys.argv)  

    # creating an object of the Application class  
    imageViewerApp = QImageViewer()  

    # using the show() method to display the window  
    imageViewerApp.show()  

    # using the exit() function of the sys module to close the application  
    sys.exit(the_app.exec_())
