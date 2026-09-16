tu_dien_anh_viet = {
    "hello": "xin chào",
    "book": "quyển sách",
    "table": "cái bàn",
}

print(tu_dien_anh_viet.get("hello","Khong tim thay tu nay"))
print(tu_dien_anh_viet.get("computer", "Khong tim thay tu nay"))

tu_dien_anh_viet["computer"] = "may tinh"

tu_dien_anh_viet.pop("table")
print("Tu dien hien tai:")
for tu_anh, tu_viet in tu_dien_anh_viet.items():
    print(f"{tu_anh}"- {tu_viet})