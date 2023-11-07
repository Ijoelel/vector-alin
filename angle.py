# For the fucking GUI :v

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from vector_calc import angle

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

vector1 = tk.StringVar()
vector2 = tk.StringVar()

label = ttk.Label(input_frame, text="Masukkan vektor : ")
label.pack(fill="x",expand=True)

vector1 = ttk.Entry(input_frame, textvariable=vector1)
vector1.pack(pady=5,fill="x", expand=True)

vector2 = ttk.Entry(input_frame, textvariable=vector2)
vector2.pack(pady=5,fill="x", expand=True)

def result():
	vec1 = list(map(int, vector1.get().split(',')))
	vec2 = list(map(int, vector2.get().split(',')))

	showinfo(message=angle(vec1, vec2), title='Result')


run_btn = ttk.Button(input_frame, text="Calculate", command=result)
run_btn.pack(fill="x", expand=True)

window.mainloop()