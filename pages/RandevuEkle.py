from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import pages.SınıfEkle as SınıfEkle

class RandevuEkle(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 650)
        MainWindow.setMinimumSize(QtCore.QSize(1100, 650))
        MainWindow.setMaximumSize(QtCore.QSize(1100, 650))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.randevuEkleSayfaLabel = QtWidgets.QLabel(self.centralwidget)
        self.randevuEkleSayfaLabel.setGeometry(QtCore.QRect(30, 70, 481, 41))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(28)
        self.randevuEkleSayfaLabel.setFont(font)
        self.randevuEkleSayfaLabel.setObjectName("randevuEkleSayfaLabel")

        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(200, 180, 321, 191))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setObjectName("gridLayout")

        # Set styles for line edits
        self.isimLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.isimLineEdit.setObjectName("isimLineEdit")
        self.isimLineEdit.setStyleSheet("""
            QLineEdit {
                border: 2px solid #888;
                padding: 5px;
                border-radius: 5px;
            }
        """)
        self.gridLayout.addWidget(self.isimLineEdit, 1, 1, 1, 1)

        self.isimLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(28)
        self.isimLabel.setFont(font)
        self.isimLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.isimLabel.setObjectName("isimLabel")
        self.gridLayout.addWidget(self.isimLabel, 1, 0, 1, 1)

        self.soyisimLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.soyisimLineEdit.setObjectName("soyisimLineEdit")
        self.soyisimLineEdit.setStyleSheet("""
            QLineEdit {
                border: 2px solid #888;
                padding: 5px;
                border-radius: 5px;

            }
        """)
        self.gridLayout.addWidget(self.soyisimLineEdit, 2, 1, 1, 1)

        self.soyisimLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(28)
        self.soyisimLabel.setFont(font)
        self.soyisimLabel.setObjectName("soyisimLabel")
        self.gridLayout.addWidget(self.soyisimLabel, 2, 0, 1, 1)

        self.kaydetButon = QtWidgets.QPushButton(self.centralwidget)
        self.kaydetButon.setGeometry(QtCore.QRect(450, 400, 201, 51))

        self.yenileButon = QtWidgets.QPushButton(self.centralwidget)
        self.yenileButon.setGeometry(QtCore.QRect(970, 20, 100, 40))
        self.yenileButon.setObjectName("yenileButon")
        self.yenileButon.clicked.connect(self.loadSinif)

        self.sınıfDüzenleButon = QtWidgets.QPushButton(self.centralwidget)
        self.sınıfDüzenleButon.setGeometry(QtCore.QRect(950, 570, 120, 40))
        self.sınıfDüzenleButon.setObjectName("sınıfDüzenleButon")

        self.sinifEkleWindow = None
        self.sınıfDüzenleButon.setText("Sınıf Düzenle")
        self.sınıfDüzenleButon.clicked.connect(self.runSinifEkle)

        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(590, 350, 250, 250))
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.hide()

        turkish_locale = QtCore.QLocale(QtCore.QLocale.Turkish, QtCore.QLocale.Turkey)
        self.calendarWidget.setLocale(turkish_locale)

        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setGeometry(QtCore.QRect(590, 295, 260, 30))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.dateTimeEdit.setDisplayFormat("dd.MM.yyyy") 
        self.dateTimeEdit.mousePressEvent = self.showCalendar
        self.calendarWidget.clicked.connect(self.updateDateTimeEdit)

        self.sinifSecComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.sinifSecComboBox.setGeometry(QtCore.QRect(590, 230, 121, 22))
        self.sinifSecComboBox.setObjectName("sinifSecComboBox")
        self.sinifSecComboBox.addItem("")

        self.dersSecComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.dersSecComboBox.setGeometry(QtCore.QRect(730, 230, 121, 22))
        self.dersSecComboBox.setObjectName("dersSecComboBox")
        self.dersSecComboBox.addItem("")
        for i in range(1, 9):
            self.dersSecComboBox.addItem(f"{i}. Ders")

        self.geriButton = QtWidgets.QPushButton(self.centralwidget)
        self.geriButton.setGeometry(QtCore.QRect(20, 20, 100, 40))
        self.geriButton.setObjectName("geriButton")
        self.geriButton.setText("Geri")
        self.geriButton.clicked.connect(self.close_sinifEkleWindow)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1440, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.connection = sqlite3.connect("db/siniflar.db")
        self.cursor = self.connection.cursor()

        self.cursor.execute("CREATE TABLE IF NOT EXISTS siniflar (sinif TEXT)")

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS randevular (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                isim TEXT,
                soyisim TEXT,
                ders TEXT,
                sinif TEXT,
                tarih TEXT
            )
        """)

        self.connection.commit()
        self.loadSinif()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Randevu Ekle"))
        self.randevuEkleSayfaLabel.setText(_translate("MainWindow", "RANDEVU EKLE"))
        self.isimLabel.setText(_translate("MainWindow", "İSİM"))
        self.soyisimLabel.setText(_translate("MainWindow", "SOYİSİM"))
        self.kaydetButon.setText(_translate("MainWindow", "KAYDET"))
        self.yenileButon.setText(_translate("MainWindow", "Yenile"))
        self.sinifSecComboBox.setItemText(0, _translate("MainWindow", "Sınıf Seçiniz"))
        self.dersSecComboBox.setItemText(0, _translate("MainWindow", "Ders Seçiniz"))

    def showCalendar(self):
        self.calendarWidget.show()

    def updateDateTimeEdit(self):
        selected_date = self.calendarWidget.selectedDate()
        now = QtCore.QDateTime.currentDateTime().date()

        if selected_date < now:
            QtWidgets.QMessageBox.warning(self.centralwidget, "Geçersiz Tarih", "Geçmiş bir tarih seçemezsiniz.")
            self.calendarWidget.hide()
        else:
            self.dateTimeEdit.setDate(selected_date)
            self.calendarWidget.hide()

    def close_sinifEkleWindow(self):
        if self.sinifEkleWindow:
            self.sinifEkleWindow.close()
            self.sinifEkleWindow = None

    def runSinifEkle(self):
        self.sinifEkleWindow = SınıfEkle.SinifEkle()
        self.sinifEkleWindow.show()

    def loadSinif(self):
        self.sinifSecComboBox.clear()
        self.sinifSecComboBox.addItem("Sınıf Seçiniz")

        self.cursor.execute("SELECT * FROM siniflar")
        siniflar = self.cursor.fetchall()
        for sinif in siniflar:
            self.sinifSecComboBox.addItem(sinif[0])

    def closeEvent(self, event):
        self.connection.close()
        event.accept()