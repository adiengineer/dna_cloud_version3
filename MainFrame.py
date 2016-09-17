import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import time

class EncodeThread(QThread):

    signalStatus = pyqtSignal(str)

    def run(self):
        count = 0
        while count <= 100:
            time.sleep(1)
            count += 20
            self.signalStatus.emit(str(count))
        self.signalStatus.emit('Idle.')


class EncodeUI(QFrame):
  
    def __init__(self,parent,height,width):
        QWidget.__init__(self, parent)
        self.initUI(height,width)
        self.height1 = height
        self.width1 = width
        self.noOfFiles = 0
        
    def initUI(self,height,width):
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.setWindowTitle('Encode Files')
        self.setAcceptDrops(True)
        self.layout.setAlignment(Qt.AlignTop)
        self.setStyleSheet("background-color: rgb(255,255,255); margin:5px; border:1px solid rgb(0, 0, 0);")
        self.setFixedWidth(width*2)

    
    def dragEnterEvent(self, e):
        if e.mimeData().hasUrls:
            e.accept()
        else:
            e.ignore() 

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls:
            event.setDropAction(Qt.CopyAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls:
            event.setDropAction(Qt.CopyAction)
            event.accept()
            for url in event.mimeData().urls():
                linkToFile = str(url.toLocalFile())
                textView = QLabel(linkToFile)
                textView.setStyleSheet("background-color: rgb(255,255,255); margin:5px; border:0px solid rgb(0, 0, 0);")
                scroll = QScrollArea()
                scroll.setWidget(textView)
                scroll.setWidgetResizable(True)
                scroll.setFixedWidth(250)
                scroll.setFixedHeight(40)
                scroll.setHorizontalScrollBarPolicy( Qt.ScrollBarAlwaysOff )
                scroll.setVerticalScrollBarPolicy( Qt.ScrollBarAlwaysOff ) 
                self.progress = QProgressBar(self)
                self.progress.setValue(0)
                self.progress.setAlignment(Qt.AlignCenter);
                self.layout.addWidget(scroll,self.noOfFiles,0)
                self.layout.addWidget(self.progress,self.noOfFiles,1)
                self.noOfFiles = self.noOfFiles + 1
                self.startEncoding()
        else:
            event.ignore()

    def startEncoding(self):
       self.thread = EncodeThread()
       self.thread.signalStatus.connect(self.updateStatus)
       self.thread.start()
    def updateStatus(self,status):
       if status != 'Idle.':
          self.progress.setValue(int(status))
       else:
          self.thread.wait()

class MainWindow(QWidget):
   
  def __init__(self,parent=None):
        QWidget.__init__(self, parent)
        self.initUI()

  def initUI(self):
        layout = QHBoxLayout()
        height = self.frameGeometry().height()
        width = self.frameGeometry().width()
        print width
        self.encodeUI = EncodeUI(self,height,width/2)
        self.decodeUI = EncodeUI(self,height,width/2)
        layout.addWidget(self.encodeUI)
        layout.addWidget(self.decodeUI)
        self.setLayout(layout)
        self.setWindowTitle('DNA 3.0')

app = QApplication(sys.argv)
dna3Win = MainWindow()
dna3Win.showMaximized()
app.exec_() 
