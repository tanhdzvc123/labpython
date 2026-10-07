
danh_sach_phong = [
    {"ma_phong": "101", "loai_phong": "Don", "gia": 300000, "trang_thai": "Trong", "ten_khach": ""},
    {"ma_phong": "102", "loai_phong": "Doi", "gia": 500000, "trang_thai": "Trong", "ten_khach": ""},
    {"ma_phong": "201", "loai_phong": "VIP", "gia": 800000, "trang_thai": "Da dat", "ten_khach": "Nguyen Van A"}
]


lich_su_giao_dich = []

def nhap_so_nguyen_an_toan(thong_bao):
    """Hàm hỗ trợ nhập số nguyên an toàn bằng try-except[cite: 3]"""
    while True:
        try:
            val = int(input(thong_bao))
            return val
        except ValueError:
            print("❌ Lỗi: Dữ liệu nhập vào phải là số nguyên! Vui lòng nhập lại.")


def hien_thi_danh_sach_phong():
    """Chức năng 1: Hiển thị danh sách toàn bộ phòng[cite: 3]"""
    print("\n--- DANH SÁCH TOÀN BỘ PHÒNG ---")
    if not danh_sach_phong:
        print("Chưa có phòng nào trong hệ thống.")
        return

    print(f"{'Mã phòng':<10} | {'Loại phòng':<12} | {'Giá/đêm (VNĐ)':<15} | {'Trạng thái':<12} | {'Khách đang ở':<20}")
    print("-" * 75)
    for p in danh_sach_phong:
        khach = p["ten_khach"] if p["ten_khach"] else "-"
        print(f"{p['ma_phong']:<10} | {p['loai_phong']:<12} | {p['gia']:<15,} | {p['trang_thai']:<12} | {khach:<20}")


def xem_phong_trong():
    """Chức năng 2: Xem nhanh các phòng đang trống[cite: 3]"""
    print("\n--- DANH SÁCH PHÒNG ĐANG TRỐNG ---")
    phong_trong = [p for p in danh_sach_phong if p["trang_thai"] == "Trong"]
    
    if not phong_trong:
        print("Hiện tại không có phòng nào trống!")
        return

    print(f"{'Mã phòng':<10} | {'Loại phòng':<12} | {'Giá/đêm (VNĐ)':<15}")
    print("-" * 45)
    for p in phong_trong:
        print(f"{p['ma_phong']:<10} | {p['loai_phong']:<12} | {p['gia']:<15,}")


def them_phong_moi():
    """Chức năng 3: Thêm phòng mới[cite: 3]"""
    print("\n--- THÊM PHÒNG MỚI ---")
    ma_phong = input("Nhập mã phòng mới: ").strip()
    
    for p in danh_sach_phong:
        if p["ma_phong"] == ma_phong:
            print("❌ Lỗi: Mã phòng này đã tồn tại!")
            return

    loai_phong = input("Nhập loại phòng (ví dụ: Don, Doi, VIP): ").strip()
    gia = nhap_so_nguyen_an_toan("Nhập giá phòng/đêm (VNĐ): ")
    
    phong_moi = {
        "ma_phong": ma_phong,
        "loai_phong": loai_phong,
        "gia": gia,
        "trang_thai": "Trong",
        "ten_khach": ""
    }
    danh_sach_phong.append(phong_moi)
    print(f"✅ Thêm phòng {ma_phong} thành công!")


def dat_phong():
    """Chức năng 4: Đặt phòng cho khách (Trống -> Đã đặt)[cite: 3]"""
    print("\n--- ĐẶT PHÒNG KHÁCH SẠN ---")
    ma_phong = input("Nhập mã phòng cần đặt: ").strip()
    
    for p in danh_sach_phong:
        if p["ma_phong"] == ma_phong:
            if p["trang_thai"] == "Da dat":
                print("❌ Phòng này đã có khách đặt rồi!")
                return
            
            ten_khach = input("Nhập tên khách hàng đặt phòng: ").strip()
            if not ten_khach:
                print("❌ Tên khách hàng không được để trống!")
                return
            
            p["trang_thai"] = "Da dat"
            p["ten_khach"] = ten_khach
            print(f"✅ Đặt phòng {ma_phong} cho khách {ten_khach} thành công!")
            return

    print("❌ Không tìm thấy mã phòng này!")


def tra_phong_thanh_toan():
    """Chức năng 5: Trả phòng / thanh toán[cite: 3]"""
    print("\n--- TRẢ PHÒNG & THANH TOÁN ---")
    ma_phong = input("Nhập mã phòng trả: ").strip()
    
    for p in danh_sach_phong:
        if p["ma_phong"] == ma_phong:
            if p["trang_thai"] == "Trong":
                print("❌ Phòng này hiện đang trống, không thể trả!")
                return
            
            # Nhập số đêm ở
            while True:
                so_dem = nhap_so_nguyen_an_toan("Nhập số đêm khách đã ở: ")
                if so_dem > 0:
                    break
                print("❌ Số đêm ở phải lớn hơn 0!")

            tong_tien = so_dem * p["gia"]
            ten_khach = p["ten_khach"]

            # Lưu vào lịch sử giao dịch[cite: 3]
            giao_dich = {
                "ma_phong": ma_phong,
                "ten_khach": ten_khach,
                "so_dem": so_dem,
                "thanh_tien": tong_tien
            }
            lich_su_giao_dich.append(giao_dich)

            # Cập nhật trạng thái phòng về "Trong"[cite: 3]
            p["trang_thai"] = "Trong"
            p["ten_khach"] = ""

            print("-" * 35)
            print("✅ XÁC NHẬN THANH TOÁN SUCCESSFUL!")
            print(f"Khách hàng: {ten_khach}")
            print(f"Phòng: {ma_phong} | Số đêm: {so_dem}")
            print(f"Tổng thành tiền: {tong_tien:,} VNĐ")
            print("-" * 35)
            return

    print("❌ Không tìm thấy mã phòng này!")


def thong_ke_doanh_thu():
    """Chức năng 6: Thống kê tổng doanh thu từ các lượt trả phòng[cite: 3]"""
    print("\n--- THỐNG KÊ DOANH THU ---")
    if not lich_su_giao_dich:
        print("Chưa có giao dịch trả phòng nào được ghi nhận.")
        return

    tong_doanh_thu = sum(gd["thanh_tien"] for gd in lich_su_giao_dich)
    
    print(f"{'Mã phòng':<10} | {'Tên khách':<20} | {'Số đêm':<10} | {'Thành tiền (VNĐ)':<15}")
    print("-" * 65)
    for gd in lich_su_giao_dich:
        print(f"{gd['ma_phong']:<10} | {gd['ten_khach']:<20} | {gd['so_dem']:<10} | {gd['thanh_tien']:<15,}")
    
    print("-" * 65)
    print(f"👉 TỔNG DOANH THU: {tong_doanh_thu:,} VNĐ")

def main():
    while True:
        print("\n========================================")
        print("  QUẢN LÝ ĐẶT PHÒNG KHÁCH SẠN MINI")
        print("========================================")
        print("1. Hiển thị danh sách toàn bộ phòng")
        print("2. Xem nhanh các phòng đang trống")
        print("3. Thêm phòng mới")
        print("4. Đặt phòng cho khách")
        print("5. Trả phòng / Thanh toán")
        print("6. Thống kê tổng doanh thu")
        print("0. Thoát chương trình")
        print("========================================")
        
        chon = nhap_so_nguyen_an_toan("Mời chọn chức năng (0-6): ")

        if chon == 1:
            hien_thi_danh_sach_phong()
        elif chon == 2:
            xem_phong_trong()
        elif chon == 3:
            them_phong_moi()
        elif chon == 4:
            dat_phong()
        elif chon == 5:
            tra_phong_thanh_toan()
        elif chon == 6:
            thong_ke_doanh_thu()
        elif chon == 0:
            print("Cảm ơn bạn đã sử dụng chương trình! Tạm biệt.")
            break
        else:
            print("❌ Lựa chọn không hợp lệ, vui lòng chọn từ 0 đến 6.")
if __name__ == "__main__":
    main()