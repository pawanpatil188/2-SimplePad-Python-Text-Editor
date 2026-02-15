# import tkinter for creating GUI apps 
import tkinter as tk 
from tkinter import filedialog, messagebox 

# Main window code 
root = tk.Tk()
root.title("Modern Text Editor")
root.geometry("900x600")

# ----------- TOOLBAR -----------
toolbar = tk.Frame(root, bg="#dddddd")
toolbar.pack(fill=tk.X)

# ----------- TEXT AREA FRAME -----------
text_frame = tk.Frame(root)
text_frame.pack(fill=tk.BOTH, expand=True)

# Scrollbar
scroll = tk.Scrollbar(text_frame)
scroll.pack(side=tk.RIGHT, fill=tk.Y)

# Text Widget
text = tk.Text(
    text_frame,
    wrap=tk.WORD,
    font=("Segoe UI", 16),
    undo=True,
    yscrollcommand=scroll.set,
    padx=10,
    pady=10
)

text.pack(fill=tk.BOTH, expand=True)
scroll.config(command=text.yview)

# ----------- STATUS BAR -----------
status_bar = tk.Label(root, text="Words: 0", anchor="e")
status_bar.pack(fill=tk.X)


# ===========================
# FILE FUNCTIONS
# ===========================

def new_file():
    text.delete(1.0, tk.END)


def open_file():
    file_path = filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )

    if file_path:
        with open(file_path, "r") as file:
            text.delete(1.0, tk.END)
            text.insert(tk.END, file.read())


def save_file():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )

    if file_path:
        with open(file_path, "w") as file:
            file.write(text.get(1.0, tk.END))
        messagebox.showinfo("Info", "File saved successfully")


# ===========================
# FORMATTING FUNCTIONS
# ===========================

def make_bold():
    try:
        current_tags = text.tag_names("sel.first")
        if "bold" in current_tags:
            text.tag_remove("bold", "sel.first", "sel.last")
        else:
            text.tag_add("bold", "sel.first", "sel.last")
            text.tag_config("bold", font=("Segoe UI", 16, "bold"))
    except:
        pass


def make_italic():
    try:
        current_tags = text.tag_names("sel.first")
        if "italic" in current_tags:
            text.tag_remove("italic", "sel.first", "sel.last")
        else:
            text.tag_add("italic", "sel.first", "sel.last")
            text.tag_config("italic", font=("Segoe UI", 16, "italic"))
    except:
        pass


# ===========================
# WORD COUNT
# ===========================

def update_word_count(event=None):
    content = text.get(1.0, tk.END)
    words = len(content.split())
    status_bar.config(text=f"Words: {words}")

text.bind("<KeyRelease>", update_word_count)


def word_count():
    content = text.get(1.0, tk.END)
    words = len(content.split())
    messagebox.showinfo("Word Count", f"Total Words: {words}")


# ===========================
# DARK MODE
# ===========================

dark_mode_on = False

def toggle_dark_mode():
    global dark_mode_on

    if dark_mode_on:
        text.config(bg="white", fg="black", insertbackground="black")
        toolbar.config(bg="#dddddd")
        dark_mode_on = False
    else:
        text.config(bg="#1e1e1e", fg="#f5f5f5", insertbackground="white")
        toolbar.config(bg="#2c2c2c")
        dark_mode_on = True


# ===========================
# MENU BAR
# ===========================

menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

edit_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Edit", menu=edit_menu)

edit_menu.add_command(label="Bold", command=make_bold)
edit_menu.add_command(label="Italic", command=make_italic)
edit_menu.add_separator()
edit_menu.add_command(label="Word Count", command=word_count)

view_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="View", menu=view_menu)

view_menu.add_command(label="Toggle Dark Mode", command=toggle_dark_mode)


# ===========================
# TOOLBAR BUTTONS
# ===========================

bold_btn = tk.Button(toolbar, text="Bold", command=make_bold)
bold_btn.pack(side=tk.LEFT, padx=5, pady=5)

italic_btn = tk.Button(toolbar, text="Italic", command=make_italic)
italic_btn.pack(side=tk.LEFT, padx=5, pady=5)

count_btn = tk.Button(toolbar, text="Word Count", command=word_count)
count_btn.pack(side=tk.LEFT, padx=5, pady=5)

dark_btn = tk.Button(toolbar, text="Dark Mode", command=toggle_dark_mode)
dark_btn.pack(side=tk.LEFT, padx=5, pady=5)


# Start application
root.mainloop()



