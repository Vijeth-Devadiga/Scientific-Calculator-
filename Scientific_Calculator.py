import tkinter as tk
from math import *

# ---------- state ----------
expression = ""
memory = 0.0

# ---------- core functions ----------
def press(token):
    global expression
    expression += str(token)
    display_var.set(expression)

def evaluate():
    global expression
    try:
        result = str(eval(expression))
        display_var.set(result)
        expression = result
    except Exception:
        display_var.set("Error")
        expression = ""

def clear_all():
    global expression
    expression = ""
    display_var.set("")

def backspace():
    global expression
    if expression:
        expression = expression[:-1]
        display_var.set(expression)

# ---------- memory ----------
def mem_add():
    global memory
    try:
        memory += float(eval(expression))
    except Exception:
        pass

def mem_sub():
    global memory
    try:
        memory -= float(eval(expression))
    except Exception:
        pass

def mem_recall():
    global expression
    expression += str(memory)
    display_var.set(expression)

def mem_clear():
    global memory
    memory = 0.0

# ---------- window ----------
root = tk.Tk()
root.title("Large Scientific Calculator - Dark Theme")
root.configure(bg="#1e1e1e")
root.geometry("900x1000")

display_var = tk.StringVar()

# ---------- display ----------
display = tk.Entry(root, textvariable=display_var, font=("Helvetica", 28, "bold"),
                   bg="#2d2d2d", fg="#ffffff", insertbackground="white",
                   bd=4, relief="sunken", justify="right")
display.grid(row=0, column=0, columnspan=7, sticky="nsew", padx=12, pady=12, ipady=18)

for r in range(0, 12):
    root.grid_rowconfigure(r, weight=1)
for c in range(0, 7):
    root.grid_columnconfigure(c, weight=1)

# ---------- helper to create buttons ----------
def btn(text, row, col, colspan=1, cmd=None):
    b = tk.Button(root, text=text, font=("Helvetica", 18), 
                  bg="#3c3f41", fg="#ffffff", activebackground="#5a5d5f", activeforeground="white",
                  relief="raised", bd=2, command=cmd or (lambda t=text: press(t)))
    b.grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=6, pady=6)

# ---------- top memory & utility row ----------
btn("MC", 1, 0, cmd=mem_clear)
btn("MR", 1, 1, cmd=mem_recall)
btn("M+", 1, 2, cmd=mem_add)
btn("M-", 1, 3, cmd=mem_sub)
btn("⌫", 1, 4, cmd=backspace)
btn("C", 1, 5, cmd=clear_all)
btn("%", 1, 6, cmd=lambda: press("%"))

# ---------- numbers & basic ops ----------
btn("7", 2, 0); btn("8", 2, 1); btn("9", 2, 2)
btn("/", 2, 3, cmd=lambda: press("/"))
btn("sqrt(", 2, 4, cmd=lambda: press("sqrt("))
btn("**", 2, 5, cmd=lambda: press("**"))
btn("//", 2, 6, cmd=lambda: press("//"))

btn("4", 3, 0); btn("5", 3, 1); btn("6", 3, 2)
btn("*", 3, 3, cmd=lambda: press("*"))
btn("log(", 3, 4, cmd=lambda: press("log("))
btn("ln(", 3, 5, cmd=lambda: press("log("))
btn("(", 3, 6, cmd=lambda: press("("))

btn("1", 4, 0); btn("2", 4, 1); btn("3", 4, 2)
btn("-", 4, 3, cmd=lambda: press("-"))
btn(")", 4, 4, cmd=lambda: press(")"))
btn(".", 4, 5, cmd=lambda: press("."))
btn(",", 4, 6, cmd=lambda: press(","))

btn("0", 5, 0, colspan=2, cmd=lambda: press("0"))
btn("+", 5, 2, colspan=1, cmd=lambda: press("+"))
btn("pi", 5, 3, cmd=lambda: press(pi))
btn("e", 5, 4, cmd=lambda: press(e))
btn("exp(", 5, 5, cmd=lambda: press("exp("))
btn("abs(", 5, 6, cmd=lambda: press("abs("))

# ---------- scientific functions ----------
btn("sin(", 6, 0, cmd=lambda: press("sin("))
btn("cos(", 6, 1, cmd=lambda: press("cos("))
btn("tan(", 6, 2, cmd=lambda: press("tan("))
btn("asin(", 6, 3, cmd=lambda: press("asin("))
btn("acos(", 6, 4, cmd=lambda: press("acos("))
btn("atan(", 6, 5, cmd=lambda: press("atan("))
btn("factorial(", 6, 6, cmd=lambda: press("factorial("))

btn("sinh(", 7, 0, cmd=lambda: press("sinh("))
btn("cosh(", 7, 1, cmd=lambda: press("cosh("))
btn("tanh(", 7, 2, cmd=lambda: press("tanh("))
btn("asinh(", 7, 3, cmd=lambda: press("asinh("))
btn("acosh(", 7, 4, cmd=lambda: press("acosh("))
btn("atanh(", 7, 5, cmd=lambda: press("atanh("))
btn("gamma(", 7, 6, cmd=lambda: press("gamma("))

btn("deg(", 8, 0, cmd=lambda: press("degrees("))
btn("rad(", 8, 1, cmd=lambda: press("radians("))
btn("round(", 8, 2, cmd=lambda: press("round("))
btn("floor(", 8, 3, cmd=lambda: press("floor("))
btn("ceil(", 8, 4, cmd=lambda: press("ceil("))
btn("pow(", 8, 5, cmd=lambda: press("pow("))
btn("sqrt_alt", 8, 6, cmd=lambda: press("sqrt("))

btn("comb(", 9, 0, cmd=lambda: press("comb("))
btn("perm(", 9, 1, cmd=lambda: press("perm("))
btn("log10(", 9, 2, cmd=lambda: press("log10("))
btn("ln10", 9, 3, cmd=lambda: press("log(10)"))
btn("2*x", 9, 4, cmd=lambda: press("2*"))
btn("10*x", 9, 5, cmd=lambda: press("10*"))
btn("mod", 9, 6, cmd=lambda: press("%"))

btn("C", 10, 0, cmd=clear_all)
btn("=", 10, 1, colspan=6, cmd=evaluate)

# ---------- keyboard bindings ----------
def on_key(event):
    char = event.char
    keys_allowed = "0123456789+-*/().,%"
    if char in keys_allowed:
        press(char)
    elif char == "\r":  # Enter
        evaluate()
    elif char == "\x08":  # Backspace
        backspace()

root.bind("<Key>", on_key)

root.mainloop()