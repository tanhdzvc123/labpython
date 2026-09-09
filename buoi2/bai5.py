# 1. Nhập thông tin từ người dùng
ho_ten = input("Nhap ho ten: ")
sdt = input("Nhap so dien thoai: ")
email = input("Nhap email: ")

# 2. Xử lý và kiểm tra dữ liệu
ho_ten_chuan = " ".join(ho_ten.strip().split()).title()  # Chuẩn hóa họ tên
sdt_hop_le = len(sdt) == 10                             # Kiểm tra SĐT đủ 10 ký tự (trả về True/False)
email_hop_le = "@" in email                             # Kiểm tra email chứa ký tự "@" (trả về True/False)

# 3. In kết quả ra màn hình
print(f"Ho ten (da chuan hoa): {ho_ten_chuan}")
print(f"So dien thoai hop le (du 10 ky tu)? {sdt_hop_le}")
print(f"Email hop le (co ky tu @)? {email_hop_le}")