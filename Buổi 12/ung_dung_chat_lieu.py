import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import csdl_chat_lieu as db

class UngDungQuanLyChatLieu:
    def __init__(self, root):
        self.root = root
        self.root.title("Phần mềm Quản lý Chất liệu Quần áo")
        self.root.geometry("650x550")
        
        # Khởi tạo CSDL
        db.khoi_tao_db()
        
        # --- Khung nhập liệu ---
        frm_input = tk.LabelFrame(root, text=" Thông tin chất liệu vải ", padx=10, pady=10)
        frm_input.pack(fill="x", padx=10, pady=10)
        
        tk.Label(frm_input, text="Tên vải:").grid(row=0, column=0, sticky="w", pady=4)
        self.cb_tenvai = ttk.Combobox(frm_input, values=["Cotton", "Kate", "Denim", "Lụa", "Kaki", "Len", "Voan"], width=28)
        self.cb_tenvai.grid(row=0, column=1, pady=4)
        self.cb_tenvai.current(0)
        
        tk.Label(frm_input, text="Màu sắc:").grid(row=1, column=0, sticky="w", pady=4)
        self.txt_mausac = tk.Entry(frm_input, width=30)
        self.txt_mausac.grid(row=1, column=1, pady=4)
        
        tk.Label(frm_input, text="Số lượng tồn (mét):").grid(row=2, column=0, sticky="w", pady=4)
        self.txt_soluong = tk.Entry(frm_input, width=30)
        self.txt_soluong.grid(row=2, column=1, pady=4)
        
        tk.Label(frm_input, text="Giá tiền / 1 mét (VNĐ):").grid(row=3, column=0, sticky="w", pady=4)
        self.txt_giatien = tk.Entry(frm_input, width=30)
        self.txt_giatien.grid(row=3, column=1, pady=4)
        
        tk.Label(frm_input, text="Nhà cung cấp:").grid(row=4, column=0, sticky="w", pady=4)
        self.txt_ncc = tk.Entry(frm_input, width=30)
        self.txt_ncc.grid(row=4, column=1, pady=4)
        
        tk.Button(frm_input, text="Thêm chất liệu", command=self.them_moi, bg="#4CAF50", fg="white", width=15).grid(row=5, column=1, sticky="e", pady=8)
        
        # --- Khung hiển thị danh sách ---
        frm_list = tk.Frame(root, padx=10)
        frm_list.pack(fill="both", expand=True, padx=10)
        
        self.listbox = tk.Listbox(frm_list, width=75, height=10)
        self.listbox.pack(side="left", fill="both", expand=True)
        
        scrollbar = tk.Scrollbar(frm_list, orient="vertical", command=self.listbox.yview)
        scrollbar.pack(side="right", fill="y")
        self.listbox.config(yscrollcommand=scrollbar.set)
        
        # --- Khung chức năng phụ ---
        frm_btn = tk.Frame(root, pady=10)
        frm_btn.pack(fill="x", padx=10)
        
        tk.Button(frm_btn, text="Xóa mục chọn", command=self.xoa_muc, bg="#f44336", fg="white", width=18).pack(side="left", padx=5)
        tk.Button(frm_btn, text="Biểu đồ tồn kho", command=self.thong_ke, bg="#2196F3", fg="white", width=18).pack(side="right", padx=5)
        
        self.tai_du_lieu()

    def tai_du_lieu(self):
        self.listbox.delete(0, tk.END)
        rows = db.lay_tat_ca()
        for r in rows:
            hien_thi = f"ID: {r[0]} | Vải: {r[1]} | Màu: {r[2]} | Tồn: {r[3]}m | Giá: {r[4]:,.0f}đ | NCC: {r[5]}"
            self.listbox.insert(tk.END, hien_thi)

    def them_moi(self):
        ten_vai = self.cb_tenvai.get()
        mau_sac = self.txt_mausac.get().strip()
        soluong_str = self.txt_soluong.get().strip()
        giatien_str = self.txt_giatien.get().strip()
        nha_cung_cap = self.txt_ncc.get().strip()
        
        if not mau_sac or not soluong_str or not giatien_str or not nha_cung_cap:
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ tất cả thông tin!")
            return
        
        try:
            soluong = float(soluong_str)
            gia_tien = float(giatien_str)
        except ValueError:
            messagebox.showerror("Lỗi", "Số lượng và giá tiền phải là kiểu số hợp lệ!")
            return
        
        db.them_chat_lieu(ten_vai, mau_sac, soluong, gia_tien, nha_cung_cap)
        messagebox.showinfo("Thành công", "Đã thêm loại chất liệu mới vào kho!")
        
        # Xóa trắng form nhập
        self.txt_mausac.delete(0, tk.END)
        self.txt_soluong.delete(0, tk.END)
        self.txt_giatien.delete(0, tk.END)
        self.txt_ncc.delete(0, tk.END)
        self.tai_du_lieu()

    def xoa_muc(self):
        try:
            selected_idx = self.listbox.curselection()[0]
            selected_text = self.listbox.get(selected_idx)
            record_id = int(selected_text.split("|")[0].replace("ID:", "").strip())
            
            db.xoa_chat_lieu(record_id)
            messagebox.showinfo("Thành công", "Đã xóa chất liệu khỏi danh mục!")
            self.tai_du_lieu()
        except IndexError:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn một dòng trong danh sách để xóa!")

    def thong_ke(self):
        data = db.thong_ke_theo_loai_vai()
        if not data:
            messagebox.showinfo("Thông báo", "Chưa có dữ liệu để thống kê!")
            return
        
        ten_vais = [row[0] for row in data]
        tong_soluongs = [row[1] for row in data]
        
        plt.figure(figsize=(7, 5))
        plt.bar(ten_vais, tong_soluongs, color=['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6'])
        plt.title("Thống kê tổng số lượng tồn kho theo loại vải (mét)")
        plt.xlabel("Loại vải")
        plt.ylabel("Tổng số lượng (m)")
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = UngDungQuanLyChatLieu(root)
    root.mainloop()