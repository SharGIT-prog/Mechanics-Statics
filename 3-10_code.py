import tkinter as tk
from tkinter import ttk
import math
from tkinter import messagebox

'''
Textbook : Engineering Mechanics Statics [JL Meriam, LG Kraige, JN Bolton]
Problem : 3-10
What horizontal force P must a worker exert on the rope to position the 50-kg crate directly over the trailer? 
'''

def total_moment():
    def retrieve_inputs():
        x_val = x.get()
        y_val = y.get()
        m_val = m.get()
        d = {'x': x_val, 'y': y_val, 'm': m_val}
        l = list(d.values())
        inf = 0
        if '' in l:
            messagebox.showinfo("Empty", "No value entered")
        else:
            for i in l:
                try:
                    if abs(float(i)) == float('inf'):
                        messagebox.showinfo("Infinity", "Value exceeds limits")
                        inf += 1
                        break
                except ValueError:
                    continue
            if inf == 0:
                s = 0
                for i in l:
                    for j in i:
                        if j not in '0-.123456789':
                            s += 1
                            break
                if s != 0:
                    def convert_to_symbolic(value):
                        try:
                            return float(value)
                        except ValueError:
                            return value
                    x_val = convert_to_symbolic(x_val)
                    y_val = convert_to_symbolic(y_val)
                    m_val = convert_to_symbolic(m_val)
                    symbolic_terms = []
                    numeric_result = 0           
                    if isinstance(y_val, str) or isinstance(x_val, str) or isinstance(m_val, str):
                        symbolic_terms.append(f"(9.81*{m_val}*{y_val})/(({x_val}**2 - {y_val}**2)**0.5)")
                    else:
                        numeric_result += (9.81 * float(m_val) * float(y_val)) / ((float(x_val)**2 - float(y_val)**2) ** 0.5)
                    final_result = "P = "
                    if symbolic_terms:
                        final_result += " + ".join(symbolic_terms)
                        if numeric_result != 0:
                            final_result += f" + {numeric_result}"
                    else:
                        final_result += str(numeric_result)
                    messagebox.showinfo("Answer", f"The answer is, {final_result} N")
                else:
                    try:
                        x_val = float(x_val)
                        y_val = float(y_val)
                        m_val = float(m_val)                
                        if x_val < 0 or y_val < 0:
                            x_val = math.fabs(x_val)
                            y_val = math.fabs(y_val)
                            messagebox.showinfo("Length", "Negative LENGTH entered. Modulus considered.")
                        if m_val < 0:
                            m_val = math.fabs(m_val)
                            messagebox.showinfo("Mass", "Negative MASS entered. Modulus considered as mass cannot be negative.")
                        if (x_val<y_val):
                            messagebox.showerror("Error", "Value of hypotenuse is lesser than side! Try again.")
                        else:
                            try:
                                P = (9.81 * m_val * y_val) / ((x_val ** 2 - y_val ** 2) ** 0.5)
                                messagebox.showinfo("Answer", f"The answer is, {P} N")
                            except ZeroDivisionError:
                                messagebox.showinfo("Answer", f"The answer is, 0 N")
                    except ValueError:
                        messagebox.showinfo("Error", "Invalid input detected.")
            else:
                pass
    root = tk.Tk()
    root.title("Q. 3/10")
    root.geometry('900x900')
    canvas = tk.Canvas(root, width=900, height=500, bg="white")
    canvas.grid(row=0, column=0, columnspan=4)
    canvas.create_line(400, 300, 430, 200, arrow=tk.LAST, fill="red", width=3)
    canvas.create_line(430, 200, 460, 100, fill="black", dash=(5, 5), width=3)
    canvas.create_line(460, 100, 460, 300, fill="black", dash=(5, 5), width=3)
    canvas.create_line(400, 300, 460, 300, fill="black", dash=(5, 5), width=3)
    canvas.create_line(400, 300, 320, 300, arrow=tk.LAST, fill="red", width=3)
    canvas.create_line(400, 300, 400, 400, arrow=tk.LAST, fill="red", width=3)
    canvas.create_text(453, 150, text="θ", fill="blue", font=("Arial", 20, "bold"))
    canvas.create_text(425, 180, text="x", font=("Arial", 20, "bold"))
    canvas.create_text(440, 310, text="y", font=("Arial", 20, "bold"))
    canvas.create_text(415, 210, text="R", fill="red", font=("Arial", 20, "bold"))
    canvas.create_text(315, 300, text="P", fill="red", font=("Arial", 20, "bold"))
    canvas.create_text(400, 410, text="W", fill="red", font=("Arial", 20, "bold"))
    x = tk.Entry(root)
    x.grid(row=1, column=1)
    tk.Label(root, text="Enter the value of x <in m>", font=("Garamond", 20, "bold")).grid(row=1, column=0)
    y = tk.Entry(root)
    y.grid(row=2, column=1)
    tk.Label(root, text="Enter the value of y <in m>", font=("Garamond", 20, "bold")).grid(row=2, column=0)
    m = tk.Entry(root)
    m.grid(row=3, column=1)
    tk.Label(root, text="Enter the value of m <in kg>", font=("Garamond", 20, "bold")).grid(row=3, column=0)
    btn = ttk.Button(root, text="Submit", command=retrieve_inputs)
    btn.grid(row=4, column=0, columnspan=2)
    root.mainloop()
root = tk.Tk()
root.title("Q.3/10")
root.geometry("1000x1000")
title_label = tk.Label(root, text="Q. What horizontal force P must a worker exert on the rope to position the crate directly over the trailer?",
                       font=("Helvetica", 14, "bold"), fg="red", justify="center")
title_label.pack(pady=10)
image_path = "g.png"   
photo = tk.PhotoImage(file=image_path)
image_label = tk.Label(root, image=photo, bg="grey")
image_label.pack()
def option1():
    total_moment()
def create_button(text, command):
    frame = tk.Frame(root, bg="black", padx=5, pady=5, width=600, height=90)
    frame.pack(pady=10, padx=50)
    frame.pack_propagate(False)
    button = tk.Button(frame, text=text, font=("Helvetica", 12, "bold"),
                       fg="black", relief="flat", activebackground="gray",
                       wraplength=550, justify="center", command=command)
    button.pack(expand=True, fill="both")
create_button("Check Answer", option1)
root.mainloop()
