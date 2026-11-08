import re

def tinh_toan(a, phep_tinh, b):
    if phep_tinh == "+":
        return a + b
    elif phep_tinh == "-":
        return a - b
    elif phep_tinh == "*":
        return a * b
    elif phep_tinh == "/":
        if b == 0:
            return "Loi: khong the chia cho 0"
        return a / b
    else:
        return "Phep tinh khong hop le"

def main():
    print("===== MAY TINH BO TUI (console) =====")
    while True:
        bieu_thuc = input("Nhap bieu thuc (vd: 5+3 hoac 5 + 3), hoac 'thoat' de dung: ").strip()
        if bieu_thuc.lower() == "thoat":
            print("Tam biet!")
            break
        
        # Dùng regex để tách số và toán tử (+, -, *, /) kể cả khi nhập liền nhau
        khop = re.match(r"^\s*([+-]?\d*\.?\d+)\s*([+\-*/])\s*([+-]?\d*\.?\d+)\s*$", bieu_thuc)
        
        if khop:
            a_str, phep_tinh, b_str = khop.groups()
            ket_qua = tinh_toan(float(a_str), phep_tinh, float(b_str))
            print("Ket qua:", ket_qua)
        else:
            print("Dinh dang khong hop le. Vi du dung: 5 + 3 hoac 5+3")

if __name__ == "__main__":
    main()