import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLineEdit, QPushButton, QGridLayout, QVBoxLayout
)
from PyQt5.QtCore import Qt

class MayTinhBoTui(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("May Tinh Bo Tui - PyQt5")
        self.setFixedSize(300, 400)
        self.man_hinh = QLineEdit()
        self.man_hinh.setFixedHeight(50)
        self.man_hinh.setAlignment(Qt.AlignRight)
        self.man_hinh.setReadOnly(True)
        self.man_hinh.setStyleSheet("font-size: 24px; padding: 5px;")

        # 2. Danh sach cac nut tren may tinh
        danh_sach_nut = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['C', '0', '=', '+']
        ]

        grid_layout = QGridLayout()
        
        for hang_idx, hang in enumerate(danh_sach_nut):
            for cot_idx, nhan in enumerate(hang):
                nut = QPushButton(nhan)
                nut.setFixedHeight(60)
                nut.setStyleSheet("font-size: 18px; font-weight: bold;")
                
                # Ket noi su kien clicked voi ham xu ly
                nut.clicked.connect(self.xu_ly_bam_nut)
                
                grid_layout.addWidget(nut, hang_idx, cot_idx)

        layout_chinh = QVBoxLayout()
        layout_chinh.addWidget(self.man_hinh)
        layout_chinh.addLayout(grid_layout)
        self.setLayout(layout_chinh)

    def xu_ly_bam_nut(self):
        # Lay ten cua nut vua duoc bam
        nut_gui_tin_hieu = self.sender()
        gia_tri = nut_gui_tin_hieu.text()

        if gia_tri == "C":
            self.man_hinh.clear()
        elif gia_tri == "=":
            try:
                bieu_thuc = self.man_hinh.text()
                ket_qua = str(eval(bieu_thuc))
                self.man_hinh.setText(ket_qua)
            except Exception:
                self.man_hinh.setText("Loi")
        else:

            if self.man_hinh.text() == "Loi":
                self.man_hinh.clear()
            # Them ký tự vừa bấm vào màn hình
            self.man_hinh.setText(self.man_hinh.text() + gia_tri)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    cua_so = MayTinhBoTui()
    cua_so.show()
    sys.exit(app.exec_())