from PyQt5 import QtWidgets
from pages.Anasayfa import Anasayfa
import pages.Version as Version
from pages.About import Ui_About
from pages.RandevuListele import Ui_Listele
import pages.RandevuEkle as RandevuEkle
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sqlite3
import datetime
import smtplib
import json
import locale

class AnaSayfa(QtWidgets.QMainWindow):
    locale.setlocale(locale.LC_TIME, 'tr_TR.UTF-8')

    def __init__(self):
        super().__init__()
        self.ui_anasayfa = Anasayfa()
        self.ui_anasayfa.setupUi(self)
        self.ui_anasayfa.randevuEkle.clicked.connect(self.openRandevuEkle)
        self.ui_anasayfa.randevuListele.clicked.connect(self.openRandevuListele)
        self.ui_anasayfa.about.clicked.connect(self.openAbout)
        self.ui_anasayfa.version.clicked.connect(self.openVersion)

    def openRandevuEkle(self):
        self.randevuEkleSayfasi = RandevuEkle.RandevuEkle()
        self.randevuEkleSayfasi.setupUi(self)
        self.randevuEkleSayfasi.kaydetButon.clicked.connect(self.kaydet)
        self.randevuEkleSayfasi.geriButton.clicked.connect(self.anaSayfayaGit)

    def openRandevuListele(self):
        self.ui_randevu_listele = Ui_Listele()
        self.ui_randevu_listele.setupUi(self)
        self.ui_randevu_listele.geriButton.clicked.connect(self.anaSayfayaGit)

    def openAbout(self):
        self.ui_about = Ui_About()
        self.ui_about.setupUi(self)
        self.ui_about.geriButton.clicked.connect(self.anaSayfayaGit)

    def openVersion(self):
        self.ui_version = Version.Ui_About()
        self.ui_version.setupUi(self)
        self.ui_version.geriButton.clicked.connect(self.anaSayfayaGit)

    def anaSayfayaGit(self):
        self.ui_anasayfa.setupUi(self)
        self.ui_anasayfa.randevuEkle.clicked.connect(self.openRandevuEkle)
        self.ui_anasayfa.randevuListele.clicked.connect(self.openRandevuListele)
        self.ui_anasayfa.about.clicked.connect(self.openAbout)
        self.ui_anasayfa.version.clicked.connect(self.openVersion)

    def sender(self, subject, message, fromEmail, toEmail, login_pwd):
        msg = MIMEMultipart()
        msg['From'] = fromEmail
        msg['To'] = toEmail
        msg['Subject'] = subject
        body = message
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromEmail, login_pwd)
        text = msg.as_string()
        server.sendmail(fromEmail, toEmail, text)
        server.quit()

    def kaydet(self):
        isim = self.randevuEkleSayfasi.isimLineEdit.text()
        soyisim = self.randevuEkleSayfasi.soyisimLineEdit.text()
        tarih = self.randevuEkleSayfasi.dateTimeEdit.dateTime().toString("dd-MM-yyyy")
        ders = self.randevuEkleSayfasi.dersSecComboBox.currentText()
        secilenSinif = self.randevuEkleSayfasi.sinifSecComboBox.currentText()
        secilenTarih = self.randevuEkleSayfasi.dateTimeEdit.date().toPyDate()
        suankiTarih = datetime.date.today()
        gunlar = {
    0: "Pazar",
    1: "Pazartesi",
    2: "Salı",
    3: "Çarşamba",
    4: "Perşembe",
    5: "Cuma",
    6: "Cumartesi"
}

        gunAdi = gunlar[secilenTarih.weekday()]

        if ders == "Ders Seçiniz" or secilenSinif == "Sınıf Seçiniz":
            QtWidgets.QMessageBox.warning(self.centralWidget(), "Hata", "Lütfen tüm alanları doldurun.")
            return

        if secilenTarih < suankiTarih:
            QtWidgets.QMessageBox.warning(self.centralWidget(), "Geçmiş Tarih", "Geçmiş bir zamana randevu ekleyemezsiniz.")
            return
        
        try:
            con = sqlite3.connect("db/veritabani.db")
            cursor = con.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS randevular (id INTEGER PRIMARY KEY, isim TEXT, soyisim TEXT, tarih TEXT, gun TEXT, sinif TEXT, ders TEXT)")
            cursor.execute("INSERT INTO randevular (isim, soyisim, tarih, gun, sinif, ders) VALUES (?, ?, ?, ?, ?, ?)", (isim, soyisim, tarih,gunAdi, secilenSinif, ders))
            cursor.execute("DELETE FROM randevular WHERE tarih < ?", (suankiTarih.strftime("%d-%m-%Y"),))
            con.commit()
            QtWidgets.QMessageBox.information(self.centralWidget(), "Randevu Eklendi", "Randevunuz başarıyla eklendi.")
        except Exception as e:
            QtWidgets.QMessageBox.warning(self.centralWidget(), "Hata", f"Veritabanına kaydedilemedi: {e}")
        finally:
            con.close()

        try:
            with open("config/config.json", encoding='utf-8') as file:
                config = json.load(file)

            senderMail = config['senderEmail']
            senderPassword = config['senderPassword']
            toEmail = "bordosec@gmail.com"
            subject = "Yeni Randevu Eklendi"
            message = f"""
            <html>
            <body>
                <h2 style="text-align: center;">Yeni bir randevu eklendi.</h2>
                <p style="font-size: 16px;"><strong>İsim:</strong> {isim}</p>
                <p style="font-size: 16px;"><strong>Soyisim:</strong> {soyisim}</p>
                <p style="font-size: 16px;"><strong>Sınıf:</strong> {secilenSinif}</p>
                <p style="font-size: 16px;"><strong>Gün:</strong> {gunAdi}</p>
                <p style="font-size: 16px;"><strong>Ders:</strong> {ders}</p>
                <p style="font-size: 16px;"><strong>Tarih:</strong> {tarih}</p>
            </body>
            </html>
            """

            msg = MIMEMultipart()
            msg['From'] = senderMail
            msg['To'] = toEmail
            msg['Subject'] = subject
            msg.attach(MIMEText(message, 'html'))

            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login(senderMail, senderPassword)
                server.sendmail(senderMail, toEmail, msg.as_string())
                
        except Exception as e:
                pass
            
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = AnaSayfa()
    MainWindow.show()
    sys.exit(app.exec_())
