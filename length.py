# For the fucking GUI :v

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from vector_calc import length

window = tk.Tk()

window.configure(bg="white")
window.geometry("300x200")
window.title("Dot Calculator")

# frame input

input_frame = ttk.Frame(window)

# layouting (Grid, Pack, Place)

input_frame.pack(padx=10,pady=10,fill="x",expand=True)

# component


# entry nama depan

vector = tk.StringVar()

label = ttk.Label(input_frame, text="Masukkan vektor : ")
label.pack(fill="x",expand=True)

vector_label = ttk.Entry(input_frame, textvariable=vector)
vector_label.pack(pady=5,fill="x", expand=True)

def result():
	vec = list(map(int, vector.get().split(',')))

	showinfo(message=length(vec), title='Result')


run_btn = ttk.Button(input_frame, text="Calculate", command=result)
run_btn.pack(fill="x", expand=True)

window.mainloop()