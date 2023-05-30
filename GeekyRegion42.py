import json
import tkinter as tk
from tkinter import messagebox, filedialog

def variationinator():
    try:
        # Reading the seed, feather ratio, seed increment, and prompts
        prompt1 = prompt_entry1.get()
        prompt2 = prompt_entry2.get()
        seed = int(seed_entry.get())import json
import tkinter as tk
from tkinter import messagebox, filedialog

def variationinator():
    try:
        # Reading the seed, feather ratio, seed increment, and prompts
        prompt1 = prompt_entry1.get()
        prompt2 = prompt_entry2.get()
        seed = int(seed_entry.get())
        feather = float(feather_entry.get())
        seed_inc = int(seed_inc_entry.get())

        # Template
        template = {
            "bbox_controls": [
                {"enable": True, "x": 0, "y": 0, "w": 0.15, "h": 1, "prompt": "", "neg_prompt": "", "blend_mode": "Foreground", "feather_ratio": feather, "seed": seed},
                {"enable": True, "x": 0.15, "y": 0, "w": 0.1, "h": 1, "prompt": "", "neg_prompt": "", "blend_mode": "Foreground", "feather_ratio": feather, "seed": seed},
                {"enable": True, "x": 0.25, "y": 0, "w": 0.15, "h": 1, "prompt": "", "neg_prompt": "", "blend_mode": "Foreground", "feather_ratio": feather, "seed": seed},
                {"enable": True, "x": 0.4, "y": 0, "w": 0.1, "h": 1, "prompt": "", "neg_prompt": "", "blend_mode": "Foreground", "feather_ratio": feather, "seed": seed},
                {"enable": True, "x": 0.5, "y": 0, "w": 0.15, "h": 1, "prompt": "", "neg_prompt": "", "blend_mode": "Foreground", "feather_ratio": feather, "seed": seed},
                {"enable": True, "x": 0.65, "y": 0, "w": 0.1, "h": 1, "prompt": "", "neg_prompt": "", "blend_mode": "Foreground", "feather_ratio": feather, "seed": seed},
                {"enable": True, "x": 0.75, "y": 0, "w": 0.15, "h": 1, "prompt": "", "neg_prompt": "", "blend_mode": "Foreground", "feather_ratio": feather, "seed": seed},
                {"enable": True, "x": 0.9, "y": 0, "w": 0.1, "h": 1, "prompt": "", "neg_prompt": "", "blend_mode": "Foreground", "feather_ratio": feather, "seed": seed},
            ]
        }

        # Update prompt and seed
        for idx, control in enumerate(template['bbox_controls']):
            control['prompt'] = prompt1 if idx % 2 == 0 else (prompt2 if prompt2 else prompt1)
            control['seed'] = seed + idx * seed_inc

        # Get the filename from the user
        filename = filedialog.asksaveasfilename(defaultextension='.json', filetypes=[('JSON files', '*.json')])

        if filename:
            # Save to file
            with open(filename, 'w') as f:
                json.dump(template, f, indent=4)
            messagebox.showinfo("Success", "JSON file has been created")

    except Exception as e:
        messagebox.showerror("Error", str(e))


# Create the main window
root = tk.Tk()
root.title("Variationinator")
root.geometry("500x300")

# Create input fields
prompt_label1 = tk.Label(root, text="Prompt 1:")
prompt_label1.pack()

prompt_entry1 = tk.Entry(root)
prompt_entry1.pack()

prompt_label2 = tk.Label(root, text="Prompt 2 (optional):")
prompt_label2.pack()

prompt_entry2 = tk.Entry(root)
prompt_entry2.pack()

seed_label = tk.Label(root, text="Seed:")
seed_label.pack()

seed_entry = tk.Entry(root)
seed_entry.pack()

feather_label = tk.Label(root, text="Feather Ratio (0 to 1 in increments of 0.05):")
feather_label.pack()

feather_entry = tk.Entry(root)
feather_entry.pack()

seed_inc_label = tk.Label(root, text="Seed Increment:")
seed_inc_label.pack()

seed_inc_entry = tk.Entry(root)
seed_inc_entry.pack()

# Create button
var_button = tk.Button(root, text="Variationinator!", command=variationinator)
var_button.pack()

# Run the GUI
root.mainloop()

        feather = float(feather_entry.get())
        seed_inc = int(seed_inc_entry.get())

        # Template
        template = {
            "bbox_controls": [
                {"enable": True, "x": 0, "y": 0, "w": 0.127, "h": 1, "prompt": "", "neg_prompt": "", "blend_mode": "Foreground", "feather_ratio": feather, "seed": seed},
                {"enable": True, "x": 0.1243, "y": 0, "w": 0.119, "h": 1, "prompt": "", "neg_prompt": "", "blend_mode": "Foreground", "feather_ratio": feather, "seed": seed},
                {"enable": True, "x": 0.2434, "y": 0, "w": 0.1217, "h": 1, "prompt": "", "neg_prompt": "", "blend_mode": "Foreground", "feather_ratio": feather, "seed": seed},
                {"enable": True, "x": 0.3651, "y": 0, "w": 0.1164, "h": 1, "prompt": "", "neg_prompt": "", "blend_mode": "Foreground", "feather_ratio": feather, "seed": seed},
                {"enable": True, "x": 0.4815, "y": 0, "w": 0.1111, "h": 1, "prompt": "", "neg_prompt": "", "blend_mode": "Foreground", "feather_ratio": feather, "seed": seed},
                {"enable": True, "x": 0.5833, "y": 0, "w": 0.1405, "h": 1, "prompt": "", "neg_prompt": "", "blend_mode": "Foreground", "feather_ratio": feather, "seed": seed},
                {"enable": True, "x": 0.718, "y": 0, "w": 0.1353, "h": 1, "prompt": "", "neg_prompt": "", "blend_mode": "Foreground", "feather_ratio": feather, "seed": seed},
                {"enable": True, "x": 0.8474, "y": 0, "w": 0.1534, "h": 1, "prompt": "", "neg_prompt": "", "blend_mode": "Foreground", "feather_ratio": feather, "seed": seed},
            ]
        }

        # Update prompt and seed
        for idx, control in enumerate(template['bbox_controls']):
            control['prompt'] = prompt1 if idx % 2 == 0 else (prompt2 if prompt2 else prompt1)
            control['seed'] = seed + idx * seed_inc

        # Get the filename from the user
        filename = filedialog.asksaveasfilename(defaultextension='.json', filetypes=[('JSON files', '*.json')])

        if filename:
            # Save to file
            with open(filename, 'w') as f:
                json.dump(template, f, indent=4)
            messagebox.showinfo("Success", "JSON file has been created")

    except Exception as e:
        messagebox.showerror("Error", str(e))


# Create the main window
root = tk.Tk()
root.title("Variationinator")
root.geometry("500x300")

# Create input fields
prompt_label1 = tk.Label(root, text="Prompt 1:")
prompt_label1.pack()

prompt_entry1 = tk.Entry(root)
prompt_entry1.pack()

prompt_label2 = tk.Label(root, text="Prompt 2 (optional):")
prompt_label2.pack()

prompt_entry2 = tk.Entry(root)
prompt_entry2.pack()

seed_label = tk.Label(root, text="Seed:")
seed_label.pack()

seed_entry = tk.Entry(root)
seed_entry.pack()

feather_label = tk.Label(root, text="Feather Ratio (0 to 1 in increments of 0.05):")
feather_label.pack()

feather_entry = tk.Entry(root)
feather_entry.pack()

seed_inc_label = tk.Label(root, text="Seed Increment:")
seed_inc_label.pack()

seed_inc_entry = tk.Entry(root)
seed_inc_entry.pack()

# Create button
var_button = tk.Button(root, text="Variationinator!", command=variationinator)
var_button.pack()

# Run the GUI
root.mainloop()
