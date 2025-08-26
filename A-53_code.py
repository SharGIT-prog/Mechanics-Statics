import tkinter as tk
from tkinter import ttk
import math
from tkinter import messagebox

'''
Textbook : Engineering Mechanics Statics [JL Meriam, LG Kraige, JN Bolton]
Problem : A-53
Develop a formula for the moment of inertia of the regular hexagonal area of side b about its central x-axis.
'''
def total_moment():
    def retrieve_inputs():
        x_val = x.get()
        
        inf = 0
        if x_val=='':
            messagebox.showinfo("Empty", "No value entered")
        else:            
            try:
                if abs(float(x_val)) == float('inf'):
                    messagebox.showinfo("Infinity", "Value exceeds limits")
                    inf += 1
                    
            except ValueError:
                pass
            
            if inf == 0:
                s = 0                
                for j in x_val:
                    if j not in '0-.123456789':
                        s += 1
                        break
                if s != 0:                         
                    if isinstance(x_val, str):
                        messagebox.showinfo("Answer", f"The answer is, (5√3/16)*({x_val}^4)) mm^4")
                else:
                    try:
                        x_val = float(x_val)
                        
                        if x_val < 0:                        
                            x_val = math.fabs(x_val)                           
                            messagebox.showinfo("Length", "Negative LENGTH entered. Modulus considered.")
                            
                        
                                                    
                        P = (0.54126587*(x_val**4))
                        messagebox.showinfo("Answer", f"The answer is, {P} mm^4")
                        
                    except ValueError:
                        messagebox.showinfo("Error", "Invalid input detected.")
            else:
                pass
    root = tk.Tk()
    root.title("Q. A-53")
    root.geometry('500x200')
    
    x = tk.Entry(root)
    x.grid(row=1, column=1)
    tk.Label(root, text="Enter the value of b <in mm>", font=("Garamond", 20, "bold")).grid(row=1, column=0)
    btn = ttk.Button(root, text="Submit", command=retrieve_inputs)
    btn.grid(row=4, column=0, columnspan=2)
    root.mainloop()
    
root = tk.Tk()
root.title("Q.A-53")
root.geometry("1000x1000")

image_path = "f.png"   
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
