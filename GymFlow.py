import tkinter as tk

window = tk.Tk()

window.title("GymFlow")
window.geometry("650x500")
window.configure(bg="#171717")

machines = {
    "Leg Press": "Occupied",
    "Treadmill": "Available",
    "Pec Deck": "Maintenance"
}








title_label = tk.Label(
    window,
    text="GYMFLOW",
    font=("Arial", 26, "bold"),
    bg="#171717",
    fg="#C8FF00"
)

title_label.pack(pady=25)

machine_list = tk.Listbox(
    window,
    width=35,
    height=5
)

for machine in machines:
    machine_list.insert(tk.END, machine)

machine_list.pack(pady=20)

status_label = tk.Label(
    window,
    text="Select a machine to check its status",
    font=("Arial", 12),
    bg="#171717",
    fg="white"
)

status_label.pack(pady=10)

def check_status():
    selected_machine = machine_list.get(tk.ACTIVE)
    status = machines[selected_machine]
    status_label.config(
    text=f"{selected_machine}: {status}"
)


check_button = tk.Button(
    window,
    text="Check Status",
    command=check_status
)

check_button.pack()

window.mainloop()
