import csdl_chat_lieu as db

def tao_du_lieu_mau():
    db.khoi_tao_db()
    
    danh_sach_vai = [
        ("Cotton", "Trắng", 150.0, 45000, "Công ty Dệt May 1"),
        ("Kate", "Xanh dương", 80.5, 35000, "Vải Sợi Miền Nam"),
        ("Denim", "Đen", 200.0, 75000, "Tổng kho Tân Bình"),
        ("Lụa", "Đỏ đô", 50.0, 120000, "Tơ Lụa Hà Đông"),
        ("Kaki", "Be", 120.0, 50000, "Đại lý Vải Thành Công")
    ]
    
    # Thêm từng loại vào CSDL
    for ten, mau, soluong, gia, ncc in danh_sach_vai:
        db.them_chat_lieu(ten, mau, soluong, gia, ncc)
        
    print("Đã thêm dữ liệu mẫu thành công vào file 'chat_lieu.db'!")

if __name__ == "__main__":
    tao_du_lieu_mau()