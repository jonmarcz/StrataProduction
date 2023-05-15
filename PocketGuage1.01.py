import tkinter as tk
from PIL import Image, ImageTk

def calculate_oil(output, strap1_feet_entry, strap1_inches_entry, strap2_feet_entry, strap2_inches_entry, tank_height_entry):
    strap1_feet = int(strap1_feet_entry.get())
    strap1_inches = int(strap1_inches_entry.get())
    strap2_feet = int(strap2_feet_entry.get())
    strap2_inches = int(strap2_inches_entry.get())

    tank_height = int(tank_height_entry.get())

    if tank_height == 16:
        strap1_barrels = ((strap1_feet * 12) + strap1_inches) * 2.80
        strap2_barrels = ((strap2_feet * 12) + strap2_inches) * 2.80
        oil_produced = strap2_barrels - strap1_barrels
        output.config(text=f"Oil produced: {oil_produced:.2f} barrels")
    elif tank_height == 25:
        strap1_barrels = ((strap1_feet * 12) + strap1_inches) * 1.67
        strap2_barrels = ((strap2_feet * 12) + strap2_inches) * 1.67
        oil_produced = strap2_barrels - strap1_barrels
        output.config(text=f"Oil produced: {oil_produced:.2f} barrels")
    else:
        output.config(text="Please enter a valid tank height in feet.")

def calculate_tank(i, frame):
    label1 = tk.Label(frame, text=f'Tank {i+1}')
    label1.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

    label2 = tk.Label(frame, text='Strap 1 (feet):')
    label2.grid(row=1, column=0, padx=5, pady=5)

    strap1_feet_entry = tk.Entry(frame)
    strap1_feet_entry.grid(row=1, column=1, padx=5, pady=5)

    label3 = tk.Label(frame, text='Strap 1 (inches):')
    label3.grid(row=1, column=2, padx=5, pady=5)

    strap1_inches_entry = tk.Entry(frame)
    strap1_inches_entry.grid(row=1, column=3, padx=5, pady=5)

    label4 = tk.Label(frame, text='Strap 2 (feet):')
    label4.grid(row=2, column=0, padx=5, pady=5)

    strap2_feet_entry = tk.Entry(frame)
    strap2_feet_entry.grid(row=2, column=1, padx=5, pady=5)

    label5 = tk.Label(frame, text='Strap 2 (inches):')
    label5.grid(row=2, column=2, padx=5, pady=5)

    strap2_inches_entry = tk.Entry(frame)
    strap2_inches_entry.grid(row=2, column=3, padx=5, pady=5)

    label6 = tk.Label(frame, text='Tank height (feet):')
    label6.grid(row=3, column=0, padx=5, pady=5)

    tank_height_entry = tk.Entry(frame)
    tank_height_entry.grid(row=3, column=1, columnspan=3, padx=5, pady=5)
    
    output_label = tk.Label(frame, text='Oil Produced:')
    output_label.grid(row=4,column=1, columnspan=3, padx=5)
    
    calculate_button = tk.Button(frame, text='Calculate', command=lambda: calculate_oil(output_label, strap1_feet_entry, strap1_inches_entry, strap2_feet_entry, strap2_inches_entry, tank_height_entry))
    calculate_button.grid(row=4, column=0, columnspan=1, padx=5, pady=5)

# create the main window
root = tk.Tk()
root.title("VAS Energy Production Calculator")

# Add logo image
logo_image = Image.open(r"C:\Users\jonat\Strataprod\VASWHITEONBLUE.png")
logo_image = logo_image.resize((150, 50))
logo_photo = ImageTk.PhotoImage(logo_image)
logo_label = tk.Label(root, image=logo_photo)
logo_label.grid(row=3, column=3, sticky="nw")

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

# Create frames for each tank
for i in range(10):
    frame = tk.Frame(root, bd=2, relief=tk.RIDGE)
    frame.grid(row=i//5, column=i%5, padx=0, pady=5)
    calculate_tank(i, frame)
    
    for j in range(4):
        frame.grid_columnconfigure(j, weight=1)
    frame.grid_rowconfigure(4, weight=1)

# run the GUI
root.mainloop()


