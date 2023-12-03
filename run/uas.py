import tkinter as tk
from PIL import ImageTk, Image

import result_formula as rf

# List Anggota
anggota = {'Afrizal Luthfi Eka Arnatha' : 183, 'Sarah Nabila' : 195, 'Rizky Akbar Maulana' : 196, 'Diha Anfeu Nio Julaynda' : 212}


root = tk.Tk()
root.geometry("1366x768")
root.title('dot, length and angle calculator')

options_frame = tk.Frame(root, bg='#888888' )

def dot_page():
	dot_frame = tk.Frame(main_frame, bg="#ffffff")
	dot_frame.pack(padx=20, pady=20)

	title = tk.Label(dot_frame, text="Dot Calculator", font=('Bold', 18), bg="#ffffff")
	title.grid(row=0, columnspan=2)

	label_vector1 = tk.Label(dot_frame, text="Enter Vector 1:", font=('Bold', 14), bg="#ffffff")
	label_vector1.grid(row=1, column=0, padx=5, pady=(50, 0))

	vector1 = tk.Entry(dot_frame, font=14)
	vector1.grid(row=1, column=1, padx=5, pady=(50, 0))

	label_vector2 = tk.Label(dot_frame, text="Enter Vector 2:", font=('Bold', 14), bg="#ffffff")
	label_vector2.grid(row=2, column=0, padx=5, pady=10)

	vector2 = tk.Entry(dot_frame, font=14)
	vector2.grid(row=2, column=1, padx=5, pady=10)

	def result():
		v1 = vector1.get().split(',')
		v2 = vector2.get().split(',')

		def set_image():

			img = tk.PhotoImage(file = rf.formula("dot", v1, v2))

			img_label.config(image=img, bd=0)
			img_label.image=img

		canvas = tk.Canvas(dot_frame, width=1100, height=275, bg="white", highlightthickness=0)
		canvas.grid(row=4, columnspan=2, padx=10, pady=10)

		img_label = tk.Label(dot_frame)
		img_label.grid(row=4, columnspan=2, padx=10, pady=10)

		set_image()

	result_button = tk.Button(dot_frame, text='Calculate', command=lambda: result())
	result_button.grid(row=3,columnspan=2,  pady = (20, 0))

def length_page():
	length_frame = tk.Frame(main_frame, bg="#ffffff")

	length_frame.pack(padx=20, pady=20)
	title = tk.Label(length_frame, text="Length Calculator", font=('Bold', 18), bg="#ffffff")
	title.grid(row=0, columnspan=2)

	label_vector = tk.Label(length_frame, text="Enter Vector:", font=('Bold', 14), bg="#ffffff")
	label_vector.grid(row=1, column=0, padx=5, pady=(50, 0))

	vector = tk.Entry(length_frame, font=14)
	vector.grid(row=1, column=1, padx=5, pady=(50, 0))

	def result():
		v = vector.get().split(',')

		canvas = tk.Canvas(length_frame, width=1100, height=275, bg="white", highlightthickness=0)
		canvas.grid(row=4, columnspan=2, padx=10, pady=10)

		img_label = tk.Label(length_frame)
		img_label.grid(row=4, columnspan=2, padx=10, pady=10)

		def set_image():

			img = tk.PhotoImage(file = rf.formula("length", v))

			img_label.config(image=img, bd=0)
			img_label.image=img

		set_image()

	result_button = tk.Button(length_frame, text='Calculate', command=lambda: result())
	result_button.grid(row=3,columnspan=2,  pady = (20, 0))

def angle_page():
	angle_frame = tk.Frame(main_frame, bg="#ffffff")
	angle_frame.pack(padx=20, pady=20)

	title = tk.Label(angle_frame, text="Angle Calculator", font=('Bold', 18), bg="#ffffff")
	title.grid(row=0, columnspan=2)

	label_vector1 = tk.Label(angle_frame, text="Enter Vector 1:", font=('Bold', 14), bg="#ffffff")
	label_vector1.grid(row=1, column=0, padx=5, pady=(50, 0))

	vector1 = tk.Entry(angle_frame, font=14)
	vector1.grid(row=1, column=1, padx=5, pady=(50, 0))

	label_vector2 = tk.Label(angle_frame, text="Enter Vector 2:", font=('Bold', 14), bg="#ffffff")
	label_vector2.grid(row=2, column=0, padx=5, pady=10)

	vector2 = tk.Entry(angle_frame, font=14)
	vector2.grid(row=2, column=1, padx=5, pady=10)

	def result():
		v1 = vector1.get().split(',')
		v2 = vector2.get().split(',')

		canvas = tk.Canvas(angle_frame, width=1100, height=500, bg="white", highlightthickness=0)
		canvas.grid(row=4, columnspan=2, padx=10, pady=10)

		img_label = tk.Label(angle_frame)
		img_label.grid(row=4, columnspan=2, padx=10, pady=10)

		def set_image():

			img = tk.PhotoImage(file = rf.formula("angle", v1, v2))

			img_label.config(image=img, bd=0)
			img_label.image=img

		

		set_image()

	show_button = tk.Button(angle_frame, text='Calculate', command=lambda: result())
	show_button.grid(row=3,columnspan=2,  pady = (20, 0))




def hide_indicate():
	dot_button.config(bg="#888888")
	length_button.config(bg="#888888")
	angle_button.config(bg="#888888")

def destroy_page():
	for frame in main_frame.winfo_children():
		frame.destroy()

def indicating(btn, page):
	hide_indicate()
	destroy_page()

	page()
	btn.config(bg='#ffffff')



dot_button = tk.Button(options_frame, width=10, anchor='w', text='Dot', font=('Bold', 14), fg='#158aff',bd=0, bg="#888888", command=lambda: indicating(dot_button, dot_page))
dot_button.place(x=10, y=50)


length_button = tk.Button(options_frame, width=10, anchor='w', text='Length', font=('Bold', 14), fg='#158aff',bd=0, bg="#888888", command=lambda: indicating(length_button, length_page))
length_button.place(x=10, y=100)

angle_button = tk.Button(options_frame, width=10, anchor='w', text='Angle', font=('Bold', 14), fg='#158aff',bd=0, bg="#888888", command=lambda: indicating(angle_button, angle_page))
angle_button.place(x=10, y=150)

options_frame.pack(side=tk.LEFT)
options_frame.pack_propagate(False)
options_frame.configure(width=100, height=768)

main_frame = tk.Frame(root, bg='#ffffff')

main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(False)
main_frame.configure(height=768, width=1366)

welcome_label = tk.Label(main_frame, text="Kelompok 6", font=('Bold', 16), bg='#ffffff')
welcome_label.pack(pady=(50, 0))

count = 0

for key, value in anggota.items():
	member_label = tk.Label(main_frame, text='{} {}'.format(key, value), font=11, bg='#ffffff', anchor='w')
	member_label.place(x = 40, y = 120+count)
	count += 30


root.mainloop()