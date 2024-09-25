from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_About(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 650)
        MainWindow.setMinimumSize(QtCore.QSize(1100, 650))
        MainWindow.setMaximumSize(QtCore.QSize(1100, 650))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.aboutSayfaLabel = QtWidgets.QLabel(self.centralwidget)
        self.aboutSayfaLabel.setGeometry(QtCore.QRect(28, 55, 271, 71))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(28)
        self.aboutSayfaLabel.setFont(font)
        self.aboutSayfaLabel.setObjectName("aboutSayfaLabel")
        
        self.geriButton = QtWidgets.QPushButton(self.centralwidget)
        self.geriButton.setGeometry(QtCore.QRect(20, 20, 100, 40))
        self.geriButton.setObjectName("geriButton")
        self.geriButton.setText("Geri")

        self.centralLabel = QtWidgets.QLabel(self.centralwidget)
        self.centralLabel.setGeometry(QtCore.QRect(50, 150, 1000, 450))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(18)
        self.centralLabel.setFont(font)
        self.centralLabel.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.centralLabel.setWordWrap(True)
        self.centralLabel.setObjectName("centralLabel")
        
        # Bilgileri buraya ekleyin
        self.centralLabel.setText("""
Uygulama İsmi: PDR App<br><br> 
Yapımcı: Muhammet Emirhan Sümer<br><br>                             
Version: Kararlı 1.1<br><br>
Yapımı: 07.06.2024<br><br>
Son Güncelleme: 21.09.2024
""")

        self.logoLabel = QtWidgets.QLabel(self.centralwidget)
        self.logoLabel.setGeometry(QtCore.QRect(350, -70, 700, 700))
        self.logoLabel.setPixmap(QtGui.QPixmap("img/ykfl.png"))
        self.logoLabel.setScaledContents(True) 
        self.logoLabel.setObjectName("logoLabel")

        self.tarihLabel = QtWidgets.QLabel(self.centralwidget)
        self.tarihLabel.setGeometry(QtCore.QRect(20, 600, 1061, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tarihLabel.setFont(font)
        self.tarihLabel.setObjectName("tarihLabel")
        self.tarihLabel.setAlignment(QtCore.Qt.AlignRight)
        self.tarihLabel.setText("07.06.2024")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1100, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Uygulama Bilgisi"))
        self.aboutSayfaLabel.setText(_translate("MainWindow", "Uygulama Bilgisi"))