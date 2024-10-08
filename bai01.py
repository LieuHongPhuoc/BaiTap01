import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox

# Tạo cửa sổ chính
window = tk.Tk()
window.title("Python GUI")
window.configure(bg="lightyellow")


# Tạo hàm thoát ứng dụng
def exit_app():
    window.quit()

#Tạo hộp thoại thông báo
def hop_thong_bao():
    messagebox.showinfo("Python message Info Box", "A Python GUI created using tkinter: The year is 2022.")

#Tạo hộp thoại cảnh báo
def hop_canh_bao():
    messagebox.showwarning("Python message Warning Box", "A Python GUI created using tkinter: Warning :There might be a bug in this code.")

#Tạo hộp thoại báo lỗi
def hop_bao_loi():
    messagebox.showerror("Python message Error Box", "A Python GUI created using tkinter: Error :Houston ~ we DO have a serious PROBLEM!.")

#tạo hộp yes ,no, cancel
def hop_ask():
    messagebox.askyesnocancel("Python message Multi Choice Box", "Are you sure you really wish do this ?")

# Tạo hộp tkinter để thông báo
def hop_tk():
    messagebox.showinfo(window1=tk.Tk(), bg = "lightgreen")

# Tạo Menu Bar
menu_bar = tk.Menu(window)

# Tạo Menu File
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New")
file_menu.add_separator() # Đường gạch phân cách
file_menu.add_command(label="Exit", command=exit_app)  # Nút Exit thoát ứng dụng
menu_bar.add_cascade(label="File", menu=file_menu)

# Gán menu bar vào cửa sổ chính
window.config(menu=menu_bar)

# Tạo Menu Help
menu_help = tk.Menu(menu_bar,tearoff= 0)

menu_help.add_command(label="About1",command=hop_thong_bao)  # Tạo mục About thông báo

menu_help.add_command(label="About2",command=hop_canh_bao) # Tạo mục About cảnh báo

menu_help.add_command(label="About3",command=hop_bao_loi) # Tạo mục About báo lỗi

menu_help.add_command(label="About4",command=hop_ask)

menu_help.add_command(label="About5",command=hop_tk)

menu_bar.add_cascade(label="Help", menu= menu_help)

# Tạo Notebook để chứa các tab
notebook = ttk.Notebook(window)
notebook.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Tạo hai frame cho Tab1 và Tab2
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)

# Thêm các tab vào Notebook
notebook.add(tab1, text="Tab1")
notebook.add(tab2, text="Tab2")

# --- Tab 1: Chứa các phần từ LabelFrame "Mighty Python" đến ScrolledText ---

# Tạo LabelFrame "Mighty Python" để chứa nội dung
frame_tab1 = tk.LabelFrame(tab1, text="Mighty Python", padx=10, pady=10, fg="blue")
frame_tab1.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="ew")

# Tạo Label và Entry cho tên
label_name = tk.Label(frame_tab1, text="Enter your name:")
label_name.grid(row=1, column=0, padx=5, pady=5, sticky="w")

entry_name = tk.Entry(frame_tab1, width=20)
entry_name.grid(row=2, column=0, padx=5, pady=5, sticky="w")

# Tạo Label và ComboBox cho số
label_number = tk.Label(frame_tab1, text="Choose a number:")
label_number.grid(row=1, column=1, padx=5, pady=5, sticky="w")

number_options = ["1", "2", "3", "4", "5"]
combobox_number = ttk.Combobox(frame_tab1, values=number_options)
combobox_number.set("")
combobox_number.grid(row=2, column=1, padx=5, pady=5, sticky="w")

# Tạo ScrolledText
scrolled_text = ScrolledText(frame_tab1, width=40, height=10)
scrolled_text.grid(row=4, column=0, columnspan=3, padx=10, pady=5, sticky="ew")

# Tạo Button để thực hiện hành động (Đưa nút Click Me vào Tab1)
def on_click():
    name = entry_name.get()
    number = combobox_number.get()
    options_selected = []
    
    if chk_var1.get():
        options_selected.append("Option 1")
    if chk_var2.get():
        options_selected.append("Option 2")
    
    options_text = ", ".join(options_selected) if options_selected else "No options"
    selected_color = color_var.get()
    
    if name and number:
        button_click.config(text=f"Hello {name} {number} ({options_text})", bg=selected_color)
        scrolled_text.insert(tk.END, f"Hello {name} {number} ({options_text})\n")
    else:
        button_click.config(text="Hãy nhập tên và chọn số")

button_click = tk.Button(frame_tab1, text="Click Me!", command=on_click)
button_click.grid(row=2, column=2, padx=5, pady=5, sticky="w")


# --- Tab 2: Chứa LabelFrame "The Snake" và phần còn lại ---

# Tạo LabelFrame "The Snake" cho Tab2
frame_tab2 = tk.LabelFrame(tab2, text="The Snake", padx=10, pady=10, fg="green")
frame_tab2.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="ew")

# Tạo Checkboxes
chk_var1 = tk.BooleanVar()
chk_var2 = tk.BooleanVar()
chk_var3 = tk.BooleanVar()

def disable_checkbox():
    checkbox1.config(state=tk.DISABLED)

checkbox1 = tk.Checkbutton(frame_tab2, text="Disable", variable=chk_var1, command=disable_checkbox)
checkbox1.grid(row=1, column=0, padx=5, pady=5, sticky="w")

checkbox2 = tk.Checkbutton(frame_tab2, text="UnChecked", variable=chk_var2)
checkbox2.grid(row=1, column=1, padx=5, pady=5, sticky="w")

checkbox3 = tk.Checkbutton(frame_tab2, text="Enable", variable=chk_var3)
checkbox3.grid(row=1, column=2, padx=5, pady=5, sticky="w")

# Tạo Radio Buttons để chọn màu
color_var = tk.StringVar(value="none")

# Tạo LabelFrame mục tiêu để thay đổi màu
target_frame = tk.LabelFrame(frame_tab2, text="Change My Color", padx=10, pady=10, fg="black")
target_frame.grid(row=3, column=0, columnspan=3, padx=10, pady=10, sticky="ew")

# Hàm thay đổi màu của target_frame khi nhấn Radio Button
def change_color():
    selected_color = color_var.get()
    target_frame.config(bg=selected_color)

radio1 = tk.Radiobutton(frame_tab2, text="Blue", variable=color_var, value="blue", command=change_color)
radio1.grid(row=2, column=0, padx=5, pady=5, sticky="w")

radio2 = tk.Radiobutton(frame_tab2, text="Gold", variable=color_var, value="gold", command=change_color)
radio2.grid(row=2, column=1, padx=5, pady=5, sticky="w")

radio3 = tk.Radiobutton(frame_tab2, text="Red", variable=color_var, value="red", command=change_color)
radio3.grid(row=2, column=2, padx=5, pady=5, sticky="w")


# Hiển thị cửa sổ
window.mainloop()
