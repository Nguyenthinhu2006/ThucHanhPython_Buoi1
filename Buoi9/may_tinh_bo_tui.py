import tkinter as tk

def bam_nut(gia_tri):
    hien_tai = entry_man_hinh.get()
    entry_man_hinh.insert(tk.END, gia_tri)

def xoa_man_hinh():
    entry_man_hinh.delete(0, tk.END)

def tinh_ket_qua():
    try:
        bieu_thuc = entry_man_hinh.get()
        ket_qua = eval(bieu_thuc)
        entry_man_hinh.delete(0, tk.END)
        entry_man_hinh.insert(0, str(ket_qua))
    except Exception:
        entry_man_hinh.delete(0, tk.END)
        entry_man_hinh.insert(0, "Lỗi")

cua_so = tk.Tk()
cua_so.title("Máy tính bỏ túi")
cua_so.geometry("320x400")
cua_so.resizable(False, False)

entry_man_hinh = tk.Entry(cua_so, font=("Arial", 20), justify="right", bd=8, relief=tk.SUNKEN)
entry_man_hinh.grid(row=0, column=0, columnspan=4, padx=10, pady=15, sticky="we")

danh_sach_nut = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 3)
]

for (text, row, col) in danh_sach_nut:
    btn = tk.Button(
        cua_so, text=text, font=("Arial", 14, "bold"), width=5, height=2,
        command=lambda t=text: bam_nut(t)
    )
    btn.grid(row=row, column=col, padx=5, pady=5)

btn_xoa = tk.Button(
    cua_so, text="C", font=("Arial", 14, "bold"), width=5, height=2,
    bg="#ff6666", fg="white", command=xoa_man_hinh
)
btn_xoa.grid(row=4, column=2, padx=5, pady=5)

btn_bang = tk.Button(
    cua_so, text="=", font=("Arial", 14, "bold"), width=22, height=2,
    bg="#4CAF50", fg="white", command=tinh_ket_qua
)
btn_bang.grid(row=5, column=0, columnspan=4, padx=5, pady=10)

if __name__ == "__main__":
    cua_so.mainloop()