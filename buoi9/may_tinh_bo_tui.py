import tkinter as tk

# Khoi tao cua so chinh
cua_so = tk.Tk()
cua_so.title("May tinh bo tui")
cua_so.geometry("320x400")
cua_so.resizable(False, False)

bieu_thuc = ""


def nhap_ky_tu(ky_tu):
    global bieu_thuc
    bieu_thuc += str(ky_tu)
    hien_thi.delete(0, tk.END)
    hien_thi.insert(0, bieu_thuc)


def tinh_ket_qua():
    global bieu_thuc
    try:
        ket_qua = str(eval(bieu_thuc))
        hien_thi.delete(0, tk.END)
        hien_thi.insert(0, ket_qua)
        bieu_thuc = ket_qua
    except ZeroDivisionError:
        hien_thi.delete(0, tk.END)
        hien_thi.insert(0, "Loi: Chia cho 0")
        bieu_thuc = ""
    except Exception:
        hien_thi.delete(0, tk.END)
        hien_thi.insert(0, "Loi bieu thuc")
        bieu_thuc = ""


def xoa_man_hinh():
    global bieu_thuc
    bieu_thuc = ""
    hien_thi.delete(0, tk.END)


# Man hinh hien thi (Entry)
hien_thi = tk.Entry(
    cua_so, font=("Arial", 20), justify="right", bd=10, relief=tk.FLAT
)
hien_thi.grid(row=0, column=0, columnspan=4, padx=10, pady=15, sticky="we")

# Danh sach cac nut
cac_nut = [
    ("7", 1, 0),
    ("8", 1, 1),
    ("9", 1, 2),
    ("/", 1, 3),
    ("4", 2, 0),
    ("5", 2, 1),
    ("6", 2, 2),
    ("*", 2, 3),
    ("1", 3, 0),
    ("2", 3, 1),
    ("3", 3, 2),
    ("-", 3, 3),
    ("0", 4, 0),
    (".", 4, 1),
    ("+", 4, 3),
]

# Tạo các nút số và phép tính (0-9, +, -, *, /)
for text, row, col in cac_nut:
    tk.Button(
        cua_so,
        text=text,
        font=("Arial", 14),
        width=5,
        height=2,
        command=lambda t=text: nhap_ky_tu(t),
    ).grid(row=row, column=col, padx=5, pady=5)

# Nút Xóa (C)
tk.Button(
    cua_so,
    text="C",
    font=("Arial", 14),
    width=5,
    height=2,
    bg="#f44336",
    fg="white",
    command=xoa_man_hinh,
).grid(row=4, column=2, padx=5, pady=5)

# Nút Bằng (=) để tính kết quả
tk.Button(
    cua_so,
    text="=",
    font=("Arial", 14),
    width=23,
    height=2,
    bg="#4CAF50",
    fg="white",
    command=tinh_ket_qua,
).grid(row=5, column=0, columnspan=4, padx=5, pady=10)

if __name__ == "__main__":
    cua_so.mainloop()