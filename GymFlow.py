import tkinter as tk

window = tk.Tk()

window.title("GymFlow")
window.geometry("650x500")
window.configure(bg="#171717")

title_label = tk.Label(
    window,
    text="GYMFLOW",
    font=("Arial", 26, "bold"),
    bg="#171717",
    fg="#C8FF00"
)

title_label.pack(pady=25)

window.mainloop()
