import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QFormLayout, QMessageBox
)

class CuaSoDangNhap(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Form Dang Nhap")
        self.resize(320, 150)

        # Tao cac o nhap va nut bam
        self.o_nhap_tai_khoan = QLineEdit()
        self.o_nhap_mat_khau = QLineEdit()
        self.o_nhap_mat_khau.setEchoMode(QLineEdit.Password)
        
        self.nut_dang_nhap = QPushButton("Dang nhap")

        # Sap xep giao dien
        layout = QFormLayout()
        layout.addRow(QLabel("Tai khoan:"), self.o_nhap_tai_khoan)
        layout.addRow(QLabel("Mat khau:"), self.o_nhap_mat_khau)
        layout.addRow(self.nut_dang_nhap)
        self.setLayout(layout)

        # Ket noi signal - slot
        self.nut_dang_nhap.clicked.connect(self.xu_ly_dang_nhap)

    def xu_ly_dang_nhap(self):
        tai_khoan = self.o_nhap_tai_khoan.text()
        mat_khau = self.o_nhap_mat_khau.text()

        if tai_khoan == "" or mat_khau == "":
            QMessageBox.critical(self, "Loi", "Vui long nhap day du tai khoan va mat khau.")
            return

        QMessageBox.information(self, "Thanh cong", f"Xin chao {tai_khoan}, dang nhap thanh cong!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    cua_so = CuaSoDangNhap()
    cua_so.show()
    sys.exit(app.exec_())