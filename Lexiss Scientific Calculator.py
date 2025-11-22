from tkinter import *
from tkinter import simpledialog
import math
import cmath

equation_text = ""
equation_label = None
entry = None
is_dark_mode = False

def button_press(num):
    global equation_text
    equation_text += str(num)
    equation_label.set(equation_text)

def equals():
    global equation_text
    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total
    except SyntaxError:
        equation_label.set("Syntax error")
        equation_text = ""
    except ZeroDivisionError:
        equation_label.set("Arithmetic error")
        equation_text = ""

def clear():
    global equation_text
    equation_text = ""
    equation_label.set("")

def backspace():
    global equation_text
    equation_text = equation_text[:-1]
    equation_label.set(equation_text)

def toggle_dark_mode():
    global is_dark_mode
    is_dark_mode = not is_dark_mode

    if is_dark_mode:
        bg_color = "#2b2b2b"
        fg_color = "white"
        btn_bg = "#3c3f41"
        btn_fg = "white"
        border_color = "white"
    else:
        bg_color = "SystemButtonFace"
        fg_color = "black"
        btn_bg = "SystemButtonFace"
        btn_fg = "black"
        border_color = "black"

    window.configure(bg=bg_color)
    entry.configure(
        readonlybackground=bg_color,
        fg=fg_color,
        highlightbackground=border_color,
        highlightcolor=border_color
    )
    frame.configure(bg=bg_color)
    geo_frame.configure(bg=bg_color, fg=fg_color)
    center_wrapper.configure(bg=bg_color)

    for container in [window, frame, geo_frame, center_wrapper]:
        for widget in container.winfo_children():
            if isinstance(widget, Button):
                widget.configure(bg=btn_bg, fg=btn_fg)
            elif isinstance(widget, Frame) or isinstance(widget, LabelFrame):
                widget.configure(bg=bg_color)

def area_square():
    a = simpledialog.askfloat("Area of Square", "Enter side (cm):", parent=window)
    if a:
        equation_label.set(f"Area: {a ** 2:.2f} cm²")

def area_rectangle():
    l = simpledialog.askfloat("Length", "Enter length (cm):", parent=window)
    b = simpledialog.askfloat("Breadth", "Enter breadth (cm):", parent=window)
    if l and b:
        equation_label.set(f"Area: {l * b:.2f} cm²")

def area_triangle_heron():
    a = simpledialog.askfloat("Side a", "Enter a (cm):", parent=window)
    b = simpledialog.askfloat("Side b", "Enter b (cm):", parent=window)
    c = simpledialog.askfloat("Side c", "Enter c (cm):", parent=window)
    if a and b and c:
        s = (a + b + c) / 2
        try:
            area = math.sqrt(s * (s - a) * (s - b) * (s - c))
            equation_label.set(f"Area: {area:.2f} cm²")
        except ValueError:
            equation_label.set("Invalid triangle")

def area_triangle_base_height():
    base = simpledialog.askfloat("Base", "Enter base (cm):", parent=window)
    height = simpledialog.askfloat("Height", "Enter height (cm):", parent=window)
    if base and height:
        equation_label.set(f"Area: {0.5 * base * height:.2f} cm²")

def area_cube():
    a = simpledialog.askfloat("Cube Side", "Enter side (cm):", parent=window)
    if a:
        equation_label.set(f"Surface Area: {6 * a**2:.2f} cm²")

def volume_cube():
    a = simpledialog.askfloat("Cube Side", "Enter side (cm):", parent=window)
    if a:
        equation_label.set(f"Volume: {a**3:.2f} cm³")

def volume_cylinder():
    h = simpledialog.askfloat("Height", "Enter height (cm):", parent=window)
    r = simpledialog.askfloat("Radius", "Enter radius (cm):", parent=window)
    if h and r:
        volume = math.pi * r**2 * h
        equation_label.set(f"Volume: {volume:.2f} cm³")

def volume_cone():
    r = simpledialog.askfloat("Radius", "Enter radius (cm):", parent=window)
    h = simpledialog.askfloat("Height", "Enter height (cm):", parent=window)
    if r and h:
        volume = (1/3) * math.pi * r**2 * h
        equation_label.set(f"Volume: {volume:.2f} cm³")

def area_sphere():
    r = simpledialog.askfloat("Radius", "Enter radius (cm):", parent=window)
    if r:
        area = 4 * math.pi * r**2
        equation_label.set(f"Surface Area: {area:.2f} cm²")

def volume_sphere():
    r = simpledialog.askfloat("Radius", "Enter radius (cm):", parent=window)
    if r:
        volume = (4/3) * math.pi * r**3
        equation_label.set(f"Volume: {volume:.2f} cm³")

def quadratic_equation():
    a = simpledialog.askfloat("a", "Enter a:", parent=window)
    b = simpledialog.askfloat("b", "Enter b:", parent=window)
    c = simpledialog.askfloat("c", "Enter c:", parent=window)
    if a and b and c:
        d = b**2 - 4*a*c
        root1 = (-b - cmath.sqrt(d)) / (2*a)
        root2 = (-b + cmath.sqrt(d)) / (2*a)
        equation_label.set(f"Roots: {root1:.2f}, {root2:.2f}")

def simultaneous_equations():
    choice = simpledialog.askstring("Equations", "Solve 2 or 3 variables?", parent=window)
    if choice == '2':
        a1 = simpledialog.askfloat("a1", "Eq1 x coefficient:", parent=window)
        b1 = simpledialog.askfloat("b1", "Eq1 y coefficient:", parent=window)
        c1 = simpledialog.askfloat("c1", "Eq1 constant:", parent=window)
        a2 = simpledialog.askfloat("a2", "Eq2 x coefficient:", parent=window)
        b2 = simpledialog.askfloat("b2", "Eq2 y coefficient:", parent=window)
        c2 = simpledialog.askfloat("c2", "Eq2 constant:", parent=window)
        if None not in (a1, b1, c1, a2, b2, c2):
            det = a1 * b2 - a2 * b1
            if det == 0:
                equation_label.set("No unique solution.")
            else:
                x = (c1 * b2 - c2 * b1) / det
                y = (a1 * c2 - a2 * c1) / det
                equation_label.set(f"x = {x:.2f}, y = {y:.2f}")
    elif choice == '3':
        equation_label.set("3-variable solver available above.")
    else:
        equation_label.set("Invalid input.")

window = Tk()
window.title("Lexiss Scientific Calculator")
window.geometry("600x730")

equation_label = StringVar()

entry = Entry(
    window,
    textvariable=equation_label,
    font=('consolas', 18),
    bd=0,
    relief='flat',
    justify='right',
    state='readonly',
    readonlybackground='white',
    highlightthickness=2,
    highlightbackground="black",
    highlightcolor="black"
)
entry.pack(fill='x', ipady=6, padx=10, pady=(10, 5))

frame = Frame(window)
frame.pack()

buttons = [
    ('1', 0, 0), ('2', 0, 1), ('3', 0, 2), ('+', 0, 3),
    ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('-', 1, 3),
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('*', 2, 3),
    ('0', 3, 0), ('.', 3, 1), ('=', 3, 2), ('/', 3, 3)
]

for (text, r, c) in buttons:
    action = lambda x=text: button_press(x) if x != '=' else equals()
    Button(frame, text=text, height=2, width=9, font=35, command=action).grid(row=r, column=c)

center_wrapper = Frame(window)
center_wrapper.pack(fill='both', expand=True)

geo_frame = LabelFrame(center_wrapper, text="Geometry Operations", font=("consolas", 12), padx=10, pady=10, relief="flat", labelanchor='n')
geo_frame.pack(pady=10)

geometry_ops = [
    ("Area of Square", area_square),
    ("Area of Rectangle", area_rectangle),
    ("Area of Triangle (Heron)", area_triangle_heron),
    ("Area Triangle (b×h)", area_triangle_base_height),
    ("Area of Cube", area_cube),
    ("Volume of Cube", volume_cube),
    ("Volume of Cylinder", volume_cylinder),
    ("Volume of Cone", volume_cone),
    ("Quadratic Equation", quadratic_equation),
    ("Simultaneous Equations", simultaneous_equations),
    ("Area of Sphere", area_sphere),
    ("Volume of Sphere", volume_sphere)
]

for i, (label_text, func) in enumerate(geometry_ops):
    Button(geo_frame, text=label_text, height=2, width=25, command=func).grid(row=i // 2, column=i % 2, padx=5, pady=3)

clear_btn = Button(center_wrapper, text='Clear', height=2, width=36, font=("consolas", 12), command=clear)
clear_btn.pack(pady=(5, 0))

Button(window, text='Dark Mode', height=2, width=18, font=35, command=toggle_dark_mode).pack(pady=(5, 10))

def key_handler(event):
    if event.char in '0123456789+-*/().':
        button_press(event.char)
    elif event.keysym == 'Return':
        equals()
    elif event.keysym == 'BackSpace':
        backspace()

window.bind("<Key>", key_handler)

window.mainloop()
