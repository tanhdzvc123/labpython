import pandas as pd

# 1. Tạo file diem_sinh_vien.csv (nếu bạn chưa có file)
csv_content = """ho_ten,mon_hoc,diem
Nguyen Van A,Toan,8.5
Tran Thi B,Toan,6.0
Le Van C,Toan,9.0
Pham Thi D,Toan,4.5
Nguyen Van A,Ly,7.5
Tran Thi B,Ly,5.5
Le Van C,Ly,8.0
Pham Thi D,Ly,6.5
Nguyen Van A,Hoa,9.0
Tran Thi B,Hoa,6.5
Le Van C,Hoa,8.5
Pham Thi D,Hoa,5.0"""

with open("diem_sinh_vien.csv", "w", encoding="utf-8") as f:
    f.write(csv_content)


# --- Bài tập 2.1 – Đọc CSV & xem tổng quan ---
df = pd.read_csv("diem_sinh_vien.csv")
print(df.head())               
print("Shape:", df.shape)      
print("Columns:", df.columns.tolist()) 


# --- Bài tập 2.2 – Thống kê theo môn học ---
diem_trung_binh_mon = df.groupby("mon_hoc")["diem"].mean()
print(diem_trung_binh_mon)

print("Diem trung binh toan bo:", df["diem"].mean())
print("Diem cao nhat:", df["diem"].max())
print("Diem thap nhat:", df["diem"].min())


# --- Bài tập 2.3 – Tính DTB từng sinh viên & lọc đạt/không đạt ---
diem_tb_sv = df.groupby("ho_ten")["diem"].mean().round(2)
print(diem_tb_sv)

sinh_vien_dat = diem_tb_sv[diem_tb_sv >= 5.0]
sinh_vien_khong_dat = diem_tb_sv[diem_tb_sv < 5.0]

print("\nSinh vien dat:")
print(sinh_vien_dat)
print("\nSinh vien khong dat:")
print(sinh_vien_khong_dat)