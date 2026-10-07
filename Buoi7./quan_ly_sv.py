import sys

class SinhVien:

  def __init__(self, ma_sv, ho_ten, diem_toan, diem_van, diem_anh):
    self.ma_sv = ma_sv
    self.ho_ten = ho_ten
    self.diem_toan = diem_toan
    self.diem_van = diem_van
    self.diem_anh = diem_anh
    self.dtb = round((diem_toan + diem_van + diem_anh) / 3, 2)
    self.xep_loai = self.tinh_xep_loai()

  def tinh_xep_loai(self):
    if self.dtb >= 8.0:
      return "Giỏi"
    elif self.dtb >= 6.5:
      return "Khá"
    elif self.dtb >= 5.0:
      return "Trung bình"
    else:
      return "Yếu"

  def hien_thi_thong_tin(self):
    print(
        f"Mã SV: {self.ma_sv:<6} | Họ tên: {self.ho_ten:<18} | Toán:"
        f" {self.diem_toan:<4} | Văn: {self.diem_van:<4} | Anh:"
        f" {self.diem_anh:<4} | ĐTB: {self.dtb:<4} | Loại: {self.xep_loai}"
    )


class QuanLySinhVien:

  def __init__(self):
    self.danh_sach = []

  def xem_danh_sach(self):
    print("\n" + "=" * 70)
    print("                DANH SÁCH SINH VIÊN HIỆN CÓ")
    print("=" * 70)
    if not self.danh_sach:
      print("-> Hiện chưa có sinh viên nào trong hệ thống.")
    else:
      for sv in self.danh_sach:
        sv.hien_thi_thong_tin()
    print("=" * 70)

  def nhap_diem_hop_le(self, ten_mon):
    """Hàm bổ trợ bắt lỗi try-except khi nhập điểm từng môn"""
    while True:
      try:
        diem_input = input(f"   + Nhập điểm {ten_mon}: ")
        diem = float(diem_input)
        if 0.0 <= diem <= 10.0:
          return diem
        else:
          print("   -> LỖI: Điểm phải nằm trong khoảng từ 0.0 đến 10.0!")
      except ValueError:
        print("   -> LỖI: Dữ liệu không hợp lệ, vui lòng nhập số thực (float)!")

  def them_sinh_vien(self):
    print("\n--- THÊM SINH VIÊN MỚI ---")
    while True:
      ma_sv = input("   + Nhập mã sinh viên mới: ").strip()
      if any(sv.ma_sv.lower() == ma_sv.lower() for sv in self.danh_sach):
        print(f"   -> LỖI: Mã sinh viên '{ma_sv}' đã tồn tại! Vui lòng nhập mã khác.")
      elif not ma_sv:
        print("   -> LỖI: Mã sinh viên không được để trống!")
      else:
        break

    ho_ten = input("   + Nhập họ và tên sinh viên: ").strip()

    diem_toan = self.nhap_diem_hop_le("Toán")
    diem_van = self.nhap_diem_hop_le("Văn")
    diem_anh = self.nhap_diem_hop_le("Tiếng Anh")

    sv_moi = SinhVien(ma_sv, ho_ten, diem_toan, diem_van, diem_anh)
    self.danh_sach.append(sv_moi)
    print(f"-> Đã thêm thành công sinh viên '{ho_ten}' (Mã: {ma_sv}).")

  def tim_kiem_sinh_vien(self):
    print("\n--- TÌM KIẾM SINH VIÊN ---")
    tu_khoa = input("Nhập Mã SV hoặc Tên SV cần tìm: ").strip().lower()
    ket_qua = [
        sv
        for sv in self.danh_sach
        if tu_khoa in sv.ma_sv.lower() or tu_khoa in sv.ho_ten.lower()
    ]

    if ket_qua:
      print(f"-> Tìm thấy {len(ket_qua)} sinh viên phù hợp:")
      for sv in ket_qua:
        sv.hien_thi_thong_tin()
    else:
      print(f"-> Không tìm thấy sinh viên nào khớp với từ khóa '{tu_khoa}'.")

  def xoa_sinh_vien(self):
    print("\n--- XÓA SINH VIÊN ---")
    ma_sv = input("Nhập mã sinh viên cần xóa: ").strip()
    for sv in self.danh_sach:
      if sv.ma_sv.lower() == ma_sv.lower():
        self.danh_sach.remove(sv)
        print(f"-> Đã xóa thành công sinh viên có mã '{ma_sv}'.")
        return
    print(f"-> Không tìm thấy sinh viên có mã '{ma_sv}' để xóa.")

  def thong_ke_bao_cao(self):
    print("\n" + "=" * 50)
    print("             BÁO CÁO THỐNG KÊ HỌC TẬP")
    print("=" * 50)
    tong_sv = len(self.danh_sach)
    if tong_sv == 0:
      print("-> Chưa có dữ liệu sinh viên để thống kê.")
      return

    gioi = sum(1 for sv in self.danh_sach if sv.xep_loai == "Giỏi")
    kha = sum(1 for sv in self.danh_sach if sv.xep_loai == "Khá")
    tb = sum(1 for sv in self.danh_sach if sv.xep_loai == "Trung bình")
    yeu = sum(1 for sv in self.danh_sach if sv.xep_loai == "Yếu")

    dtb_chung = sum(sv.dtb for sv in self.danh_sach) / tong_sv

    print(f"1. Tổng số sinh viên quản lý : {tong_sv} sinh viên")
    print(f"2. Điểm trung bình toàn khóa  : {dtb_chung:.2f}")
    print("3. Phân loại học lực:")
    print(f"   - Số lượng Giỏi         : {gioi} ({gioi/tong_sv*100:.1f}%)")
    print(f"   - Số lượng Khá          : {kha} ({kha/tong_sv*100:.1f}%)")
    print(
        f"   - Số lượng Trung bình   : {tb} ({tb/tong_sv*100:.1f}%)"
    )
    print(f"   - Số lượng Yếu          : {yeu} ({yeu/tong_sv*100:.1f}%)")
    print("=" * 50)

def main():
  qlsv = QuanLySinhVien()

  while True:
    print("\n" + "       MENU QUẢN LÝ SINH VIÊN          " )
    print("1. Xem danh sách sinh viên")
    print("2. Thêm sinh viên mới vào hệ thống")
    print("3. Tìm kiếm sinh viên theo tên / mã")
    print("4. Xóa sinh viên")
    print("5. Xem báo cáo thống kê")
    print("0. Thoát chương trình")
    print("*" * 64)

    chon = input("Vui lòng chọn chức năng (0-5): ").strip()

    if chon == "1":
      qlsv.xem_danh_sach()
    elif chon == "2":
      qlsv.them_sinh_vien()
    elif chon == "3":
      qlsv.tim_kiem_sinh_vien()
    elif chon == "4":
      qlsv.xoa_sinh_vien()
    elif chon == "5":
      qlsv.thong_ke_bao_cao()
    elif chon == "0":
      print("\n-> Cảm ơn bạn đã sử dụng chương trình. Tạm biệt!")
      break
    else:
      print("-> Lựa chọn không hợp lệ, vui lòng chọn số từ 0 đến 5.")

if __name__ == "__main__":
  main()