# For the fucking GUI :v

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

window = tk.Tk()

window.configure(bg="white")
window.geometry("300x200")
window.title("Vector Length, Angle, and Dot Calculator")

# frame input

input_frame = ttk.Frame(window)

# layouting (Grid, Pack, Place)

input_frame.pack(padx=10,pady=10,fill="x",expand=True)

# component


# entry nama depan

nama_depan_label = ttk.Label(input_frame, text="Input Nama Depan : ")
nama_depan_label.pack(fill="x",expand=True)

NAMA_DEPAN = tk.StringVar()

nama_depan_entry = ttk.Entry(input_frame, textvariable=NAMA_DEPAN)
nama_depan_entry.pack(fill="x", expand=True)

# entry nama belakang
nama_belakang_label = ttk.Label(input_frame, text="Input Nama Belakang : ")
nama_belakang_label.pack(fill="x",expand=True)

NAMA_BELAKANG = tk.StringVar()

nama_belakang_entry = ttk.Entry(input_frame, textvariable=NAMA_BELAKANG)
nama_belakang_entry.pack(fill="x", expand=True)

# button

def tombol_click():
	showinfo(title="mwehehe", message=NAMA_DEPAN.get()+NAMA_BELAKANG.get())

tombol_sapa = ttk.Button(input_frame, text="Sapa Gua", command=tombol_click)
tombol_sapa.pack(fill='x', expand=True)

# colorchooser







window.mainloop()