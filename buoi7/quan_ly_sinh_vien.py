
danh_sach_sv = [
    {"ma_sv": "SV01", "ten_sv": "Vũ Tuấn Anh", "gioi_tinh": "Nam", "diem_tb": 8.5, "xep_loai": "Gioi"},
    {"ma_sv": "SV02", "ten_sv": "Trần An Trung", "gioi_tinh": "Nu", "diem_tb": 9.2, "xep_loai": "Xuat sac"},
    {"ma_sv": "SV03", "ten_sv": "Lê Văn Tê", "gioi_tinh": "Nam", "diem_tb": 6.4, "xep_loai": "Trung binh"}
]


def nhap_so_thuc_an_toan(loi_nhac):
    """Bắt lỗi nhập điểm từ 0.0 đến 10.0"""
    while True:
        try:
            val = float(input(loi_nhac))
            if 0.0 <= val <= 10.0:
                return val
            print("❌ Lỗi: Điểm phải nằm trong khoảng từ 0.0 đến 10.0!")
        except ValueError:
            print("❌ Lỗi: Dữ liệu không hợp lệ, vui lòng nhập một số thực!")

def nhap_so_nguyen_an_toan(loi_nhac):
    """Bắt lỗi nhập lựa chọn menu"""
    while True:
        try:
            return int(input(loi_nhac))
        except ValueError:
            print("❌ Lỗi: Vui lòng nhập một số nguyên!")

def tinh_xep_loai(diem_tb):
    """Tự động tính xếp loại học lực dựa vào điểm trung bình"""
    if diem_tb >= 9.0:
        return "Xuat sac"
    elif diem_tb >= 8.0:
        return "Gioi"
    elif diem_tb >= 6.5:
        return "Kha"
    elif diem_tb >= 5.0:
        return "Trung binh"
    else:
        return "Yeu"

def tim_sv_theo_ma(ma_sv):
    for sv in danh_sach_sv:
        if sv["ma_sv"] == ma_sv:
            return sv
    return None

def hien_thi_danh_sach():
    print("\n" + "=" * 70)
    print(f"{'Ma SV':<10}{'Ho va Ten':<25}{'Gioi tinh':<12}{'Diem TB':<12}{'Xep loai':<15}")
    print("-" * 70)
    if not danh_sach_sv:
        print("-> Danh sách hiện đang trống.")
    else:
        for sv in danh_sach_sv:
            print(f"{sv['ma_sv']:<10}{sv['ten_sv']:<25}{sv['gioi_tinh']:<12}{sv['diem_tb']:<12.1f}{sv['xep_loai']:<15}")
    print("=" * 70)

def xem_sv_gioi():
    sv_gioi = [sv for sv in danh_sach_sv if sv["diem_tb"] >= 8.0]
    print("\n--- DANH SÁCH SINH VIÊN GIỎI & XUẤT SẮC (ĐTB >= 8.0) ---")
    if not sv_gioi:
        print("-> Không có sinh viên nào đạt loại Giỏi/Xuất sắc.")
        return
    for sv in sv_gioi:
        print(f"  {sv['ma_sv']} - {sv['ten_sv']} - ĐTB: {sv['diem_tb']} - Loại: {sv['xep_loai']}")

def them_sinh_vien():
    print("\n--- THÊM SINH VIÊN MỚI ---")
    ma_sv = input("Nhập mã sinh viên mới: ").strip().upper()
    if tim_sv_theo_ma(ma_sv) is not None:
        print(f"❌ Mã sinh viên {ma_sv} đã tồn tại!")
        return

    ten_sv = input("Nhập họ tên sinh viên: ").strip().title()
    gioi_tinh = input("Nhập giới tính (Nam/Nu): ").strip().title()
    diem_tb = nhap_so_thuc_an_toan("Nhập điểm trung bình (0-10): ")
    xep_loai = tinh_xep_loai(diem_tb)

    danh_sach_sv.append({
        "ma_sv": ma_sv, "ten_sv": ten_sv,
        "gioi_tinh": gioi_tinh, "diem_tb": diem_tb, "xep_loai": xep_loai
    })
    print(f"✅ Thêm sinh viên {ten_sv} thành công!")

def xoa_sinh_vien():
    print("\n--- XÓA SINH VIÊN ---")
    ma_sv = input("Nhập mã sinh viên cần xóa: ").strip().upper()
    sv = tim_sv_theo_ma(ma_sv)
    if sv is None:
        print(f"❌ Không tìm thấy sinh viên có mã {ma_sv}.")
        return
    
    danh_sach_sv.remove(sv)
    print(f"✅ Đã xóa sinh viên {sv['ten_sv']} ({ma_sv}) khỏi hệ thống.")

def thong_ke_lop():
    print("\n--- THỐNG KÊ LỚP HỌC ---")
    if not danh_sach_sv:
        print("-> Chưa có dữ liệu sinh viên.")
        return
    
    tong_diem = sum(sv["diem_tb"] for sv in danh_sach_sv)
    dtb_chung = tong_diem / len(danh_sach_sv)
    
    print(f"• Tổng số sinh viên: {len(danh_sach_sv)}")
    print(f"• Điểm trung bình chung của lớp: {dtb_chung:.2f}")

def hien_thi_menu():
    print("\n===== QUẢN LÝ SINH VIÊN =====")
    print("1. Hiển thị danh sách tất cả sinh viên")
    print("2. Xem danh sách sinh viên Giỏi/Xuất sắc")
    print("3. Thêm sinh viên mới")
    print("4. Xóa sinh viên")
    print("5. Thống kê lớp học")
    print("0. Thoát chương trình")

def chay_chuong_trinh():
    while True:
        hien_thi_menu()
        lua_chon = nhap_so_nguyen_an_toan("Mời chọn chức năng (0-5): ")
        if lua_chon == 1:
            hien_thi_danh_sach()
        elif lua_chon == 2:
            xem_sv_gioi()
        elif lua_chon == 3:
            them_sinh_vien()
        elif lua_chon == 4:
            xoa_sinh_vien()
        elif lua_chon == 5:
            thong_ke_lop()
        elif lua_chon == 0:
            print("Cảm ơn bạn đã sử dụng chương trình. Tạm biệt!")
            break
        else:
            print("❌ Lựa chọn không hợp lệ, vui lòng chọn từ 0 đến 5.")

if __name__ == "__main__":
    chay_chuong_trinh()