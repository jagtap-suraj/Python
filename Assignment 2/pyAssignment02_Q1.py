#Python Assignment No. 02 (Q1)

"""Write a python program to display the following drawing"""

import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

canvas.create_rectangle(100, 160, 400, 460, fill="yellow", outline="red", width=5)
canvas.create_rectangle(175, 235, 325, 385, fill="blue", outline="#FFD700", width=5)
canvas.create_polygon(100, 160, 250, 60, 400, 160, fill="yellow", outline="red", width=5)

root.mainloop()
