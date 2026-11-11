import sqlite3

def khoi_tao_db():
    conn = sqlite3.connect("chat_lieu.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS chat_lieu (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ten_vai TEXT NOT NULL,
            mau_sac TEXT NOT NULL,
            so_luong REAL NOT NULL,
            gia_tien REAL NOT NULL,
            nha_cung_cap TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def them_chat_lieu(ten_vai, mau_sac, so_luong, gia_tien, nha_cung_cap):
    conn = sqlite3.connect("chat_lieu.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO chat_lieu (ten_vai, mau_sac, so_luong, gia_tien, nha_cung_cap) 
        VALUES (?, ?, ?, ?, ?)
    """, (ten_vai, mau_sac, so_luong, gia_tien, nha_cung_cap))
    conn.commit()
    conn.close()

def lay_tat_ca():
    conn = sqlite3.connect("chat_lieu.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, ten_vai, mau_sac, so_luong, gia_tien, nha_cung_cap FROM chat_lieu")
    rows = cursor.fetchall()
    conn.close()
    return rows

def xoa_chat_lieu(record_id):
    conn = sqlite3.connect("chat_lieu.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM chat_lieu WHERE id = ?", (record_id,))
    conn.commit()
    conn.close()

def thong_ke_theo_loai_vai():
    conn = sqlite3.connect("chat_lieu.db")
    cursor = conn.cursor()
    cursor.execute("SELECT ten_vai, SUM(so_luong) FROM chat_lieu GROUP BY ten_vai")
    data = cursor.fetchall()
    conn.close()
    return data