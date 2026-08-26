ho_ten = input("Nhap ho ten: ")
nam_sinh = int(input("Nhap nam sinh: "))
diem_tb = float(input("Nhap diem trung binh: "))
"""
Vì hàm mặc định luôn nhận dữ liệu dưới dạng chuỗi (). 
cần dùng để biểu diễn số nguyên nên phải ép kiểu bằng , còn là số thực nên phải ép kiểu bằng .
là dữ liệu dạng chữ nên giữ nguyên kiểu chuỗi và không cần ép kiểu.input()strnam_sinhint()diem_tbfloat()ho_ten
"""
print("Python", "la", "ngon", "ngu", "lap", "trinh", sep ="-")
print("Dong 1", end= "|")
print("Dong 2")


print("Python", "la", "ngon", "ngu", "lap", "trinh", sep =",")
print("Python", "la", "ngon", "ngu", "lap", "trinh", sep ="\n")
print("Python", "la", "ngon", "ngu", "lap", "trinh", sep ="`")
"""
sep dùng để quy định ký tự ngăn cách giữa các giá trị trong hàm . 
Khi , các giá trị được ngăn cách bằng dấu gạch ngang; khi , các giá trị được ngăn cách bằng dấu phẩy; khi , mỗi giá trị được in trên một dòng mới.print()sep="-"sep=", "sep="\n"
end dùng để quy định ký tự kết thúc sau khi hàm thực hiện xong. 
Mặc định nên chương trình sẽ xuống dòng. Khi dùng, lệnh tiếp theo sẽ được in trên cùng một dòng và ngăn cách bằng ký tự nhiên.print()end="\n"end=" | "print()
"""
# f-string
print(f"Ho ten: {ho_ten} - Nam sinh: {nam_sinh}- DTB:{diem_tb: .2f}")
# str.fomat()
print("Ho ten:{} - Nam sinh: {} - DTB: {:.2f}".format(ho_ten, nam_sinh, diem_tb))
#toán tử %
print("Ho ten: %s - Nam sinh: %d - DTB: %.2f" %(ho_ten, nam_sinh, diem_tb))
"""
Python khuyến khích sử dụng f-string vì cú pháp ngắn gọn, dễ đọc, dễ viết và cho phép chèn trực tiếp biến hoặc biểu thức vào trong chuỗi. 
So với và toán tử , f-string giúp chương trình rõ ràng và thuận tiện hơn.str.format()%
"""
# Chu thich mot dong: khai bao thong tin sinh vien
"""
Chu thich/docstring nhieu dong:
Chuong trinh quan ly diem sinh vien - Buoi 2
"""
ho_ten = "Tran Thi B" # bien luu ho ten

s1 = 'Xin chao'
s2 = "Ban co khoe khong?"
s3 = '''Day la
mot chuoi
nhieu dong'''
s4 = "Duong dan: C:\\Python\\data"
s5 = r"Duong dan raw: C:\Python\data"
s6 = "Toi ten la \"Nam\", con ban ten gi?"
print(s1); print(s2); print(s3); print(s4); print(s5); print(s6)
"""
s4 là chuỗi thông thường nên ký tự có thể được Python hiểu là ký tự escape, vì vậy cần dùng để biểu diễn một dấu gạch chéo ngược.
 là raw string, có tiền tố , nên các ký tự được giữ nguyên. 
 Raw string thường được sử dụng khi làm việc với đường dẫn trên Windows hoặc các chuỗi có nhiều ký tự .
 """