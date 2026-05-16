import re
import tkinter as tk
from tkinter import filedialog

# Token patterns
keywords = {"int","float","if","else","while","return","for","char","double","break","continue","void"}

token_patterns = [
    ('COMMENT', r'//.*'),
    ('STRING', r'"[^"]*"'),
    ('NUMBER', r'\d+'),
    ('ID', r'[A-Za-z_]\w*'),
    ('OPERATOR', r'[+\-*/=%]'),
    ('SYMBOL', r'[;{}(),$%]'),
    ('INVALID', r'[@#$^&]'),
    ('WHITESPACE', r'\s+'),
]

pattern = '|'.join('(?P<%s>%s)' % pair for pair in token_patterns)

# Lexer Function
def analyze_code():
    output.delete(1.0, tk.END)
    code = text_input.get("1.0", tk.END)

    for match in re.finditer(pattern, code):
        kind = match.lastgroup
        value = match.group()

        if kind == 'WHITESPACE':
            continue

        if kind == 'ID' and value in keywords:
            kind = 'KEYWORD'

        # color tags
        color = {
            "KEYWORD": "blue",
            "ID": "black",
            "NUMBER": "purple",
            "OPERATOR": "red",
            "SYMBOL": "brown",
            "STRING": "green",
            "COMMENT": "gray",
            "INVALID": "orange"
        }.get(kind, "black")

        output.insert(tk.END, f"{value:15} → {kind}\n", kind)
        output.tag_config(kind, foreground=color)

# Load file
def open_file():
    file = filedialog.askopenfile(filetypes=[("Text Files","*.txt"),("C Files","*.c"),("All Files","*.*")])
    if file:
        text_input.delete(1.0, tk.END)
        text_input.insert(tk.END, file.read())

# GUI setup
root = tk.Tk()
root.title("Creative Lexical Analyzer")
root.geometry("700x500")

tk.Label(root, text="Enter Code:", font=("Arial",12,"bold")).pack()

text_input = tk.Text(root, height=12, font=("Consolas",11))
text_input.pack(fill="both", padx=10)

tk.Button(root, text="Analyze", command=analyze_code, bg="#4CAF50", fg="white").pack(pady=5)
tk.Button(root, text="Open File", command=open_file).pack()

tk.Label(root, text="Tokens:", font=("Arial",12,"bold")).pack()

output = tk.Text(root, height=12, font=("Consolas",11))
output.pack(fill="both", padx=10, pady=5)

root.mainloop()