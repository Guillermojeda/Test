import tkinter as tk
from tkinter import ttk, Tk, W, S, E, N

def completar():
    entry_1.delete(0,"end")
    entry_1.insert(0, "Luciano")
    
    entry_2.delete(0,"end")
    entry_2.insert(0, "Øjeda")
    
    entry_3.delete(0,"end")
    entry_3.insert(0, "34")

raiz = Tk()
raiz.title("App_Test")
try:
    raiz.iconbitmap("Ball.ico")
except Exception as e: print(f"Error al cargar el file .ico: {e}")

main_frame = tk.Frame(raiz, bg="black")
main_frame.pack(fill="both", expand="true")

label_1 = tk.Label(main_frame, text="Nombre:", background="black", fg="white")
label_1.grid(row=1, column=1, padx=5, pady=5, sticky=W)

entry_1 = ttk.Entry(main_frame, width=15, font=("Calibri", 11,"bold"))
entry_1.grid(row=1, column=2, padx=5, pady=5, sticky=W)

label_2 = tk.Label(main_frame, text="Apellido:", background="black", fg="white")
label_2.grid(row=2, column=1, padx=5, pady=5, sticky=W)

entry_2 = ttk.Entry(main_frame, width=15, font=("Calibri", 11,"bold"))
entry_2.grid(row=2, column=2, padx=5, pady=5, sticky=W)

label_3 = ttk.Label(main_frame, text="Edad:")
label_3.grid(row=3, column=1, padx=5, pady=5, sticky=W)

entry_3 = ttk.Entry(main_frame, width=15, font=("Calibri", 11,"bold"))
entry_3.grid(row=3, column=2, padx=5, pady=5, sticky=W)

boton = ttk.Button(main_frame, width=15, text="AutoCompletar", command=completar)
boton.grid(row=4, column=2, padx=5, pady=5, sticky=W)

raiz.mainloop()