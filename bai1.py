import tkinter as tk
from math import sqrt

def tinh_toan(phep_tinh):
    try:
        so1 = float(so_nhap1.get())
        if phep_tinh != 'sqrt':  # 'sqrt' chỉ cần so1
            so2 = float(so_nhap2.get())
        if phep_tinh == 'cong':
            ket_qua.set(so1 + so2)
        elif phep_tinh == 'tru':
            ket_qua.set(so1 - so2)
        elif phep_tinh == 'nhan':
            ket_qua.set(so1 * so2)
        elif phep_tinh == 'chia':
            ket_qua.set(so1 / so2)
        elif phep_tinh == 'sqrt':
            ket_qua.set(sqrt(so1))
    except Exception as e:
        ket_qua.set("Lỗi")

window = tk.Tk()
window.title("Máy Tính")

# Biến lưu trữ kết quả
ket_qua = tk.StringVar()

# Định nghĩa và đặt các widget bằng grid
tk.Label(window, text="Số thứ nhất:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
so_nhap1 = tk.Entry(window)
so_nhap1.grid(row=0, column=1, padx=5, pady=5)

tk.Label(window, text="Số thứ hai:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
so_nhap2 = tk.Entry(window)
so_nhap2.grid(row=1, column=1, padx=5, pady=5)

tk.Button(window, text="Cộng", command=lambda: tinh_toan('cong')). grid(row=3, column=0, sticky="w", padx=5, pady=5)
tk.Button(window, text="Trừ", command=lambda: tinh_toan ('tru' )). grid(row=3, column=1, sticky="w", padx=5, pady=5)
tk.Button(window, text="Căn Bậc Hai", command=lambda: tinh_toan('sqrt')).grid (row=3, column=2, sticky="w", padx=5, pady=5)
tk.Button(window, text="Nhân", command=lambda: tinh_toan('nhan')). grid(row=3, column=3, sticky="w", padx=5, pady=5)
tk.Button(window, text="Chia", command=lambda: tinh_toan('chia')). grid(row=3, column=4, sticky="w", padx=5, pady=5)

tk.Label(window, text="Kết quả:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
tk.Label(window, textvariable=ket_qua).grid(row=2, column=1, sticky="w", padx=5, pady=5)

window.mainloop()
