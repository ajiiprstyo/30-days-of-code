import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit, QMessageBox

class CurrencyConverter(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('USD to IDR Converter')
        
        # Membuat label input
        self.label = QLabel('Enter amount in USD:', self)
        
        # Membuat kotak teks input
        self.textbox = QLineEdit(self)
        
        # Membuat tombol konversi
        self.btn = QPushButton('Convert', self)
        self.btn.clicked.connect(self.convertCurrency)
        
        # Menyusun layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.textbox)
        vbox.addWidget(self.btn)
        
        self.setLayout(vbox)
        
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def convertCurrency(self):
        try:
            usd_amount = float(self.textbox.text())
            conversion_rate = 16385  # Nilai tukar USD ke IDR (dapat disesuaikan sesuai nilai tukar saat ini)
            idr_amount = usd_amount * conversion_rate
            QMessageBox.information(self, 'Conversion Result', f'{usd_amount} USD is equal to {idr_amount:.2f} IDR', QMessageBox.Ok)
        except ValueError:
            QMessageBox.warning(self, 'Input Error', 'Please enter a valid number', QMessageBox.Ok)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CurrencyConverter()
    sys.exit(app.exec_())
          
