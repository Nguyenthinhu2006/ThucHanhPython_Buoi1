import csdl_sach as db

def tao_du_lieu_mau():
    # Khởi tạo bảng CSDL nếu chưa có
    db.tao_bang_neu_chua_co()
    
    # Danh sách dữ liệu mẫu để nhập thử
    danh_sach_sach = [
        ("Dac Nhan Tam", "Dale Carnegie", "Ky nang song"),
        ("Nha Gia Kim", "Paulo Coelho", "Tieu thuyet"),
        ("Luoc Su Thoi Gian", "Stephen Hawking", "Khoa hoc"),
        ("Dai Viet Su Ky Toan Thu", "Ngo Si Lien", "Lich su")
    ]
    
    # Thêm từng cuốn sách vào CSDL
    for ten, tg, tl in danh_sach_sach:
        db.them_sach(ten, tg, tl)
        
    print("Đã tạo và nhập dữ liệu mẫu thành công vào file 'tu_sach.db'!")

if __name__ == "__main__":
    tao_du_lieu_mau()