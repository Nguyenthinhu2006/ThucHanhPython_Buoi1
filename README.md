# Bài 1.1: Khai báo và truy cập
diem_so = [8.5, 7.0, 9.2, 6.5, 5.5]

print(diem_so[0])      # In phần tử đầu tiên -> Output: 8.5
print(diem_so[-1])     # In phần tử cuối cùng -> Output: 5.5
print(diem_so[1:4])    # Cắt từ vị trí 1 đến trước 4 -> Output: [7.0, 9.2, 6.5]
print(diem_so[::2])    # Lấy cách 1 phần tử (step = 2) -> Output: [8.5, 9.2, 5.5]
print(diem_so[::-1])   # Đảo ngược danh sách -> Output: [5.5, 6.5, 9.2, 7.0, 8.5]

# Bài 1.2: Các phương thức thường dùng
ten_sv = ["An", "Binh", "Chi"]

ten_sv.append("Dung")          # Thêm "Dung" vào cuối list
ten_sv.insert(1, "Em")         # Chèn "Em" vào vị trí chỉ số 1
print(ten_sv)

ten_sv.remove("Chi")           # Xóa phần tử có giá trị "Chi"
pop_ra = ten_sv.pop()          # Xóa và lấy ra phần tử cuối cùng ("Dung")
print(ten_sv, "- da xoa:", pop_ra)

ten_sv.sort()                  # Sắp xếp tăng dần theo bảng chữ cái
print(ten_sv)

ten_sv.reverse()               # Đảo ngược thứ tự danh sách hiện tại
print(ten_sv)

ten_sv.extend(["Giang", "Hoa"])# Nối thêm danh sách ["Giang", "Hoa"] vào cuối
print(ten_sv)


"""remove(x): Tìm và xóa phần tử đầu tiên trong List có giá trị bằng x.
 Phương thức này không trả về giá trị (trả về None). Nếu giá trị không tồn
 tại trong List, Python sẽ báo lỗi ValueError.

pop(i): Xóa phần tử tại vị trí chỉ số i (mặc định nếu không truyền i thì 
xóa phần tử cuối cùng). Phương thức này trả về giá trị của phần tử vừa bị xóa để có thể gán
vào biến hoặc sử dụng tiếp."""


# Bài 2.1: Duyệt list bằng vòng lặp for
diem_so = [8.5, 7.0, 9.2, 6.5, 5.5]
tong = 0

for diem in diem_so:
    print(diem)
    tong = tong + diem

print("Tong diem:", tong)
print("Diem trung binh:", round(tong / len(diem_so), 2))

# Bài 2.2: List lồng nhau (Ma trận)
ma_tran = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# In ra theo từng hàng
for hang in ma_tran:
    print(hang)

# In ra từng phần tử, duyệt theo hàng rồi theo cột
for hang in ma_tran:
    for phan_tu in hang:
        print(phan_tu, end=" ")
    print()
# code tính tổng các phần tử trong ma trận
tong_ma_tran = 0
for hang in ma_tran:
    for phan_tu in hang:
        tong_ma_tran += phan_tu

print("Tong tat ca phan tu trong ma tran:", tong_ma_tran)

# Bài 3.1 - Lọc số chẵn/lẻ
day_so = list(range(1, 21))

so_chan = [x for x in day_so if x % 2 == 0]
so_le = [x for x in day_so if x % 2 != 0]

print("So chan:", so_chan)
print("So le:", so_le)

# Bài 3.2 - Biến đổi phần tử
diem_so = [8.5, 7.0, 9.2, 6.5, 5.5]
diem_cong = [round(diem + 0.5, 2) for diem in diem_so]

print("Diem cong:", diem_cong)# Bài 4.1 - Khai báo & tính bất biến
toa_do = (3, 5)
print(toa_do, type(toa_do))

# Thử gán lại sẽ gây ra lỗi TypeError vì tuple là dữ liệu bất biến (immutable)
# toa_do[0] = 10 

# Bài 4.2 - Unpacking tuple
x, y = toa_do
print("x =", x, "- y =", y)

# Đổi giá trị 2 biến bằng unpacking (không cần biến tạm)
a, b = 10, 20
a, b = b, a
print("a =", a, "- b =", b)

# Bài 4.3 - Trả về nhiều giá trị từ một biểu thức
c, d = 17, 5
thuong_du = divmod(c, d)     # divmod trả về tuple (thuong, du)
thuong, du = thuong_du       # unpacking kết quả
print(f"{c} chia {d} duoc thuong {thuong}, du {du}")

#Hoạt động 5: Vận dụng Tuple & Yêu cầu tính khoảng cách tới (0,0)
import math

diem_a = (2, 3)
diem_b = (7, 8)

xa, ya = diem_a
xb, yb = diem_b

khoang_cach = math.sqrt((xb - xa) ** 2 + (yb - ya) ** 2)
print(f"Khoang cach giua {diem_a} va {diem_b} la: {round(khoang_cach, 2)}")

# Tính khoảng cách của từng điểm trong danh sách so với gốc tọa độ (0, 0)
cac_diem = [(0, 0), (3, 4), (6, 8)]

for diem in cac_diem:
    x, y = diem
    # Khoảng cách từ (x, y) đến (0, 0) là sqrt(x^2 + y^2)
    kc_goc = math.sqrt(x**2 + y**2)
    print(f"Khoang cach tu diem {diem} den goc toa do (0, 0) la: {round(kc_goc, 2)}")# BÀI 6: Mini project 1 - Quản lý danh sách sinh viên ---
danh_sach_sv = [(8.5, "An"), (7.0, "Binh"), (9.2, "Chi"), (6.5, "Dung")]

# Thêm sinh viên mới
danh_sach_sv.append((8.0, "Em"))

# Xóa một sinh viên
danh_sach_sv.remove((7.0, "Binh"))

# Sửa điểm cho sinh viên ở vị trí 0
danh_sach_sv[0] = (9.0, danh_sach_sv[0][1])

# Kiểm tra sinh viên có trong danh sách không
print("Chi co trong danh sach khong?", (9.2, "Chi") in danh_sach_sv)

# Sắp xếp theo điểm tăng dần
danh_sach_sv.sort()
print("Danh sach sau khi sap xep theo diem tang dan:")
for diem, ten in danh_sach_sv:
    print(f"{ten} - {diem}")

# Sắp xếp giảm dần
danh_sach_sv.sort(reverse=True)
print("Danh sach sau khi sap xep theo diem giam dan:")
for diem, ten in danh_sach_sv:
    print(f"{ten} - {diem}")# BÀI 7: Mini project 2 - Quản lý kho hàng ---
kho_hang = [
    ("Ban phim", 250000, 10),
    ("Chuot", 150000, 20),
    ("Man hinh", 2500000, 5)
]

# Thêm sản phẩm mới
kho_hang.append(("Tai nghe", 300000, 15))

# Xóa một sản phẩm
kho_hang.remove(("Chuot", 150000, 20))

# Hiển thị danh sách kho hàng
print("DANH SACH KHO HANG:")
for ten, gia, so_luong in kho_hang:
    print(f"{ten:<12} - Gia: {gia:>10,} - SL: {so_luong}")

# Tính tổng giá trị kho hàng bằng vòng lập cộng dồn
tong_gia_tri = 0
for ten, gia, so_luong in kho_hang:
    tong_gia_tri = tong_gia_tri + gia * so_luong

print(f"Tong gia tri kho hang: {tong_gia_tri:,} VND")
