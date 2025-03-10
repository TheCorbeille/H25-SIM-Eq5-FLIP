import tkinter as tk
from tkinter import ttk, messagebox

def control_motor(vitesse, angle):
    print(f"\nControlleur de moteur activé:")
    print(f"  - Vitesse: {vitesse}%")
    print(f"  - Angle: {angle}°")
    print("En marche...\n")

def apply_settings():
    try:
        vitesse = float(entree_vitesse.get())
        angle = float(entree_angle.get())

        # Validate inputs
        if 0 <= vitesse <= 300 and 0 <= angle <= 45:
            control_motor(vitesse, angle)
        else:
            messagebox.showerror("Invalide", "Vitesse doit etre entre 0rpm et 300rpm et angle entre 0° et 45°.")
            entree_vitesse.delete(0, tk.END)
            entree_angle.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Invalide", "Entrées invalides.")
        entree_vitesse.delete(0, tk.END)
        entree_angle.delete(0, tk.END)

root = tk.Tk()
root.title("Interface Controlleur de Moteur")

root.geometry("500x300")

frame = ttk.Frame(root, padding="10")
frame.pack(fill=tk.BOTH, expand=True)

vitesse_label = ttk.Label(frame, text="Vitesse (0-300rpm):")
vitesse_label.grid(row=0, column=0, sticky=tk.W)

entree_vitesse = ttk.Entry(frame, justify=tk.CENTER)
entree_vitesse.grid(row=0, column=1, sticky=tk.EW)

angle_label = ttk.Label(frame, text="Angle (0-45°):")
angle_label.grid(row=1, column=0, sticky=tk.W)

entree_angle = ttk.Entry(frame, justify=tk.CENTER)
entree_angle.grid(row=1, column=1, sticky=tk.EW)

button_utiliser = ttk.Button(frame, text="Appliquer", command=apply_settings)
button_utiliser.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()