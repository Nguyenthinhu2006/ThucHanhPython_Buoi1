
print("=== HOẠT ĐỘNG 3: ĐỊNH DANH & PEP8 ===")

# Bài tập 3.1: Soi lỗi đặt tên
"""
DANH SÁCH ĐỊNH DANH VÀ LÝ DO:
- 1diem: SAI (Bắt đầu bằng chữ số).
- gia-tri: SAI (Chứa dấu gạch ngang '-').
- tam_thoi: HỢP LỆ.
- Diem_TB: HỢP LỆ (Nhưng chưa chuẩn phong cách PEP8 cho biến).
- class: SAI (Trùng từ khóa reserved của Python).
- so luong: SAI (Chứa khoảng trắng).
- MAX_SPEED: HỢP LỆ (Đặt tên cho hằng số theo chuẩn PEP8).
- diemTB: HỢP LỆ (Nhưng là dạng camelCase, chưa chuẩn PEP8 cho biến).
- 2024_data: SAI (Bắt đầu bằng chữ số).
- tong$: SAI (Chứa ký tự đặc biệt '$').
- sinhVien1: HỢP LỆ (Nhưng chưa chuẩn PEP8 cho biến).
"""

# Bài tập 3.2: Áp dụng PEP8
ten = "Nguyen Van A"
diem_toan = 8.5
diem_van = 7.0
so_luong_mon_hoc = 2
MUC_LUONG_TOI_THIEU = 5000000

print("Bài 3.2 - Đã đặt lại tên biến theo PEP8:")
print(f"Họ tên: {ten}, Điểm Toán: {diem_toan}, Lương tối thiểu: {MUC_LUONG_TOI_THIEU}")
print("\n" + "="*50 + "\n")

print("=== HOẠT ĐỘNG 5: TOÁN TỬ ===")

# Bài tập 5.1: Toán tử số học
a = 17
b = 5

print("Bài 5.1 - Kết quả các phép toán số học:")
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a // b =", a // b)
print("a % b =", a % b)
print("a ** b =", a ** b)

# Bài tập 5.2: Toán tử so sánh & logic
diem = 6.5
tuoi = 20

print("\nBài 5.2 - Kiểm tra điều kiện logic:")
kieu_dieu_kien_1 = (diem >= 6.5) and (diem < 8.0)
print("- Điểm đạt loại Khá?:", kieu_dieu_kien_1)

kieu_dieu_kien_2 = (tuoi < 18) or (tuoi > 60)
print("- Tuổi chưa đủ 18 hoặc trên 60?:", kieu_dieu_kien_2)
print("- Phủ định điều kiện tuổi bằng 'not':", not kieu_dieu_kien_2)


# Bài tập 5.3: Toán tử gán & toán tử đặc biệt
print("\nBài 5.3 - Toán tử gán & đặc biệt:")
x = 10
x += 5
print("x sau += 5:", x)
x -= 3
print("x sau -= 3:", x)
x *= 2
print("x sau *= 2:", x)
x /= 4
print("x sau /= 4:", x)
x //= 2
print("x sau //= 2:", x)
x **= 3
print("x sau **= 3:", x)

danh_sach = [1, 2, 3, "python"]
print("3 có trong danh_sach không?:", 3 in danh_sach)

list1 = [1, 2, 3]
list2 = list1
print("list1 is list2?:", list1 is list2)


# Bài tập 5.4: Độ ưu tiên toán tử
print("\nBài 5.4 - Độ ưu tiên toán tử:")
print("2 + 3 * 4 ** 2 =", 2 + 3 * 4 ** 2)
print("(2 + 3) * 4 ** 2 =", (2 + 3) * 4 ** 2)
print("10 > 5 and 3 < 1 or not False =", 10 > 5 and 3 < 1 or not False)

print("\n" + "="*50 + "\n")


print("=== HOẠT ĐỘNG 6: BIẾN & DYNAMIC TYPING ===")

# Bài tập 6.1: Khai báo biến với nhiều kiểu dữ liệu
bien = 10
print(bien, type(bien))

bien = "Xin chao"
print(bien, type(bien))

bien = 3.14
print(bien, type(bien))

bien = True
print(bien, type(bien))

# Bài tập 6.2: Mini bài toán tổng hợp
print("\nBài 6.2 - Mini bài toán tổng hợp:")
ho_ten = "Nguyen Van A"
diem_toan = 8.0
diem_ly = 7.5
diem_hoa = 9.0

dtb = (diem_toan + diem_ly + diem_hoa) / 3

la_gioi = dtb >= 8.0
la_kha = dtb >= 6.5 and dtb < 8.0
la_trung_binh = dtb >= 5.0 and dtb < 6.5
la_yeu = dtb < 5.0

print(ho_ten, "- DTB:", round(dtb, 2))
print("Dat loai Gioi?", la_gioi)
print("Dat loai Kha?", la_kha)
print("Dat loai Trung binh?", la_trung_binh)
print("Dat loai Yeu?", la_yeu)
print("Kieu du lieu cua la_gioi:", type(la_gioi))