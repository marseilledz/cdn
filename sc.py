import tkinter as tk

# Créer la fenêtre principale
root = tk.Tk()
root.title("Exemple Tkinter")
root.geometry("640x480")

# Ajouter un label
label = tk.Label(root, text="Bonjour, Tkinter!", font=("Arial", 24))
label.pack(pady=20)

# Lancer la boucle principale
root.mainloop()
