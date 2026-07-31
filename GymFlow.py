import tkinter as tk

ventana = tk.Tk()

ventana.title("GymFlow")
ventana.geometry("650x500")
ventana.configure(bg="#171717")

titulo = tk.Label(
    ventana,
    text="GYMFLOW",
    font=("Arial", 26, "bold"),
    bg="#171717",
    fg="#C8FF00"
)

titulo.pack(pady=25)

ventana.mainloop()
