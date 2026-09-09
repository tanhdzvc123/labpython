# 1. Khai báo chuỗi họ tên thô
ho_ten_tho = "   nguyễN  văn   an  "

# 2. Xử lý chuẩn hóa bằng strip(), split(), join() và title()
ho_ten_sach = " ".join(ho_ten_tho.strip().split()).title()

# 3. In kết quả
print(ho_ten_sach)  # Kết quả: Nguyễn Văn An