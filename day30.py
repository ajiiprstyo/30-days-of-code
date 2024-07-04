from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QComboBox, QMessageBox

class CalculatorWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Perhitungan Pajak")
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        self.price_label = QLabel("Harga:")
        self.price_input = QLineEdit()
        layout.addWidget(self.price_label)
        layout.addWidget(self.price_input)

        self.tax_label = QLabel("Pajak:")
        self.tax_combobox = QComboBox()
        self.tax_combobox.addItems(["10%", "15%", "20%"])
        layout.addWidget(self.tax_label)
        layout.addWidget(self.tax_combobox)

        self.calculate_button = QPushButton("Hitung Pajak")
        self.calculate_button.clicked.connect(self.calculate_tax)
        layout.addWidget(self.calculate_button)

        self.result_label = QLabel("")
        layout.addWidget(self.result_label)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def calculate_tax(self):
        try:
            price = float(self.price_input.text())
            tax_percentage = float(self.tax_combobox.currentText().strip('%')) / 100
            total_price = price + (price * tax_percentage)
            self.result_label.setText(f"Total harga beserta pajak: ${total_price:.2f}")
        except ValueError:
            QMessageBox.warning(self, "Peringatan", "Masukkan harga dengan format angka yang benar.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalculatorWindow()
    window.show()
    sys.exit(app.exec_())
  
