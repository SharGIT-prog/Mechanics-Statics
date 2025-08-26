import tkinter as tk
from tkinter import ttk
import math
from tkinter import messagebox

'''
Textbook : Engineering Mechanics Statics [JL Meriam, LG Kraige, JN Bolton]
Problem : 2-50
Elements of the lower arm are shown in the figure. The mass of the forearm is 2.3 kg with center of mass at G. Determine the combined moment about the elbow pivot O of the weights of the forearm and the sphere. What must the biceps tension force be so that the overall moment about O is zero?
'''


def total_moment():
    def retrieve_inputs():            
        length_1 = length_input_1.get()
        length_2 = length_input_2.get()
        length_3 = length_input_3.get()
        angle = angle_input.get()        
        Tension = Tension_input.get()
        Force_at_G = Force_input_G.get()
        Force_at_A = Force_input_A.get()        
        d = {'l1':length_1, 'l2':length_2, 'l3':length_3, 'a':angle, 'T':Tension, 'Fg': Force_at_G, 'Fa': Force_at_A}
        l = list(d.values())        
        inf =0
        if '' in l:
            messagebox.showinfo("Empty","No value entered")
        else:
            for i in l:
                try:
                    if abs(float(i))==(float('inf')):
                        messagebox.showinfo("Infinity","Value exceeds limits")
                        inf +=1
                        break                        
                except ValueError:
                    continue  
            if inf==0:
                s = 0
                for i in l:
                    for j in i:
                        if j not in '0-.123456789' :
                            s+=1
                            break                
                if s!=0:
                    def convert_to_symbolic(value):
                        try:
                            return float(value)
                        except ValueError:
                            return value
                    length_1 = convert_to_symbolic(length_1)
                    length_2 = convert_to_symbolic(length_2)
                    length_3 = convert_to_symbolic(length_3)
                    angle = convert_to_symbolic(angle)
                    Tension = convert_to_symbolic(Tension)
                    Force_at_G = convert_to_symbolic(Force_at_G)
                    Force_at_A = convert_to_symbolic(Force_at_A)                    
                    if isinstance(angle, (int, float)):
                        angle_rad = math.radians(angle)
                        sin_angle = math.sin(angle_rad)
                    else:
                        sin_angle = f"sin({angle})"                    
                    numeric_result = 0
                    symbolic_terms = []                    
                    if isinstance(Tension, str) or isinstance(length_1, str):
                        symbolic_terms.append(f"{Tension}*{length_1}")
                    else:
                        numeric_result += Tension * length_1                    
                    if isinstance(Force_at_G, str) or isinstance(length_2, str) or isinstance(sin_angle, str):
                        symbolic_terms.append(f"{Force_at_G}*-9.81*{sin_angle}*{length_2}")
                    else:
                        numeric_result += -9.81 * Force_at_G * sin_angle * length_2                    
                    if isinstance(Force_at_A, str) or isinstance(length_3, str):
                        symbolic_terms.append(f"-9.81*{Force_at_A}*{length_3}")
                    else:
                        numeric_result += -9.81 * Force_at_A * length_3                    
                    final_result = "M_o = "
                    if symbolic_terms:
                        final_result += " + ".join(symbolic_terms)
                        if numeric_result != 0:
                            final_result += f" + {numeric_result}"
                    else:
                        final_result += str(numeric_result)                    
                    messagebox.showinfo("Answer", f'The answer is, {final_result} Nm')
                else:                       
                    length_1 = float(length_1)
                    length_2 = float(length_2)
                    length_3 = float(length_3)
                    angle = float(angle)                
                    Tension = float(Tension)
                    Force_at_G = float(Force_at_G)
                    Force_at_A = float(Force_at_A)

                    if length_1<0 or length_2<0 or length_3<0 :
                        length_1 = math.fabs(length_1)
                        length_2 = math.fabs(length_2)
                        length_3 = math.fabs(length_3)
                        messagebox.showinfo("Length", "Negative LENGTH entered, not physically possible. Modulus considered.")                        
                    if angle<0 :
                        messagebox.showinfo("Angle","Negative ANGLE entered. Coterminal angle considered. ")                        
                    if Tension<0 :
                        Tension = math.fabs(Tension)
                        messagebox.showinfo("Force","Negative FORCE entered. Modulus considered as the direction cannot vary.")
                    if Force_at_G<0 or Force_at_A<0 :
                        Force_at_G = math.fabs(Force_at_G)
                        Force_at_A = math.fabs(Force_at_A)
                        messagebox.showinfo("Mass","Negative MASS entered. Modulus considered as mass cannot be negative.")
                    M_o = ((float(Tension) * float(length_1))
                    + (float(Force_at_G) * -9.81 * math.sin(math.radians(float(angle)))*float(length_2))
                    +(-1 * float(Force_at_A) * 9.81 * float(length_3))
                    )
                    messagebox.showinfo("Answer", f"The answer is, {M_o} Nm")        
                
            else:
                pass
    root = tk.Tk()
    root.title("Q. 2/50")
    root.geometry('900x900')
    canvas = tk.Canvas(root, width=900, height=500, bg="white")
    canvas.grid(row=0, column=0, columnspan=4)
    canvas.create_line(200,100,450,250 ,fill="black", width=2)
    canvas.create_line(450,250,750,260 ,fill="black", width=2)
    canvas.create_line(200,380,200,100 ,fill="green", width=2)
    canvas.create_line(750,350,750,380 ,fill="green", width=2)
    canvas.create_line(200,130, 235, 120 ,fill="blue", width=2)
    canvas.create_line(200,100,320,100, fill="red", dash=(5,5))
    canvas.create_line(198,106,448,256, fill="red", dash=(5,5))
    canvas.create_line(200,380,750,380, fill="red", dash=(5,5))
    canvas.create_line(320,100, 320, 170, arrow=tk.FIRST, fill="brown", width=2)
    canvas.create_line(450,250, 450,350, arrow=tk.LAST, fill="brown", width=2)
    canvas.create_line(750,260, 750,350, arrow=tk.LAST, fill="brown", width=2) 
    canvas.create_text(190, 100, text="O", font=("Arial", 20, "bold"))
    canvas.create_text(320,185, text="F", font=("Arial", 20, "bold"))
    canvas.create_text(450, 240, text="G", font=("Arial", 20, "bold"))
    canvas.create_text(750, 250, text="A", font=("Arial", 20, "bold"))
    canvas.create_text(600, 50, text="Sign Convention:", font=("Garamond", 20, "bold","underline"))
    canvas.create_text(610, 70, text="+ve : Anti Clockwise", font=("Garamond", 20))
    canvas.create_text(600, 90, text="-ve : Clockwise", font=("Garamond", 20))    
    canvas.create_text(260,90, text="Length 1", fill="red", font=("Arial", 20, "italic"))
    canvas.create_text(370, 230, text="Length 2", fill="red", font=("Arial", 20, "italic"))
    canvas.create_text(600, 370, text="Length 3", fill="red", font=("Arial", 20, "italic"))
    canvas.create_text(180,130, text="Angle", fill="blue", font=("Arial", 20, "italic")) 
    length_input_1 = tk.Entry(root)
    length_input_1.grid(row=1, column=1)
    tk.Label(root, text="Length 1<in m>",font=("Arial", 15, "bold")).grid(row=1, column=0)
    length_input_2 = tk.Entry(root)
    length_input_2.grid(row=2, column=1)
    tk.Label(root, text="Length 2<in m>",font=("Arial", 15, "bold")).grid(row=2, column=0)
    length_input_3 = tk.Entry(root)
    length_input_3.grid(row=3, column=1)
    tk.Label(root, text="Length 3<in m>",font=("Arial", 15, "bold")).grid(row=3, column=0)
    angle_input = tk.Entry(root)
    angle_input.grid(row=4, column=1)
    tk.Label(root, text="Angle <in degrees> ",font=("Arial", 15, "bold")).grid(row=4, column=0)
    Tension_input = tk.Entry(root)
    Tension_input.grid(row=5, column=1)
    tk.Label(root, text="Tension<in N>",font=("Arial", 15, "bold")).grid(row=5, column=0)
    Force_input_G = tk.Entry(root)
    Force_input_G.grid(row=6, column=1)
    tk.Label(root, text="Mass at G<in kg>",font=("Arial", 15, "bold")).grid(row=6, column=0)
    Force_input_A = tk.Entry(root)
    Force_input_A.grid(row=7, column=1)
    tk.Label(root, text="Mass at A<in kg>",font=("Arial", 15, "bold")).grid(row=7, column=0) 
    btn = ttk.Button(root, text="Submit", command=retrieve_inputs)
    btn.grid(row=10, column=0, columnspan=2)
    root.mainloop()
def tension_for_zero_moment():
    def retrieve_inputs():            
        length_1 = length_input_1.get()
        length_2 = length_input_2.get()
        length_3 = length_input_3.get()
        angle = angle_input.get()         
        Force_at_G = Force_input_G.get()
        Force_at_A = Force_input_A.get()        
        d = {'l1':length_1, 'l2':length_2, 'l3':length_3, 'a':angle, 'Fg': Force_at_G, 'Fa': Force_at_A}
        l = list(d.values())       
        err =0
        if '' in l:
            err+=1
            messagebox.showinfo("Empty","No value entered")        
        for i in l:
            if [c for c in i if c not in "0123456789."]:   
                messagebox.showinfo("Invalid input","Invalid Input. You must only enter positive numerical values.")
                err += 1
                break       
        for i in l:
            try:
                if abs(float(i))==(float('inf')):
                    messagebox.showinfo("Infinity","Value exceeds limits")
                    err+=1
                    break
            except ValueError:
                pass
        if err==0:            
            length_1 = float(length_1)
            length_2 = float(length_2)
            length_3 = float(length_3)
            angle = float(angle)       
            Force_at_G = float(Force_at_G)
            Force_at_A = float(Force_at_A)            
            if length_1<0 or length_2<0 or length_3<0 :
                length_1 = math.fabs(length_1)
                length_2 = math.fabs(length_2)
                length_3 = math.fabs(length_3)
                messagebox.showinfo("Length", "Negative LENGTH entered, which is not physically possible. Modulus considered.")                
            if angle<0 :
                messagebox.showinfo("Angle","Negative ANGLE entered. Coterminal angle considered. ")                
            if Force_at_G<0 or Force_at_A<0 :
                Force_at_G = math.fabs(Force_at_G)
                Force_at_A = math.fabs(Force_at_A)
                messagebox.showinfo("Mass","Negative MASS entered. Modulus considered as the mass cannot be negative.")
            try:
                T = ((9.81*length_2*Force_at_G*math.sin(math.radians(angle)))+(9.81*Force_at_A*length_3))/(length_1)
                messagebox.showinfo("Answer",f"The answer is, {T} N")
            except ZeroDivisionError:
                messagebox.showinfo("Answer",f"The answer is, 0 N")
        else:
            pass
    root = tk.Tk()
    root.title("Q. 2/50")
    root.geometry('900x900')
    canvas = tk.Canvas(root, width=900, height=500, bg="white")
    canvas.grid(row=0, column=0, columnspan=4)
    canvas.create_line(200,100,450,250 ,fill="black", width=2)
    canvas.create_line(450,250,750,260 ,fill="black", width=2)
    canvas.create_line(200,380,200,100 ,fill="green", width=2)
    canvas.create_line(750,350,750,380 ,fill="green", width=2)
    canvas.create_line(200,130, 235, 120 ,fill="blue", width=2)
    canvas.create_line(200,100,320,100, fill="red", dash=(5,5))
    canvas.create_line(198,106,448,256, fill="red", dash=(5,5))
    canvas.create_line(200,380,750,380, fill="red", dash=(5,5))
    canvas.create_line(320,100, 320, 170, arrow=tk.FIRST, fill="brown", width=2)
    canvas.create_line(450,250, 450,350, arrow=tk.LAST, fill="brown", width=2)
    canvas.create_line(750,260, 750,350, arrow=tk.LAST, fill="brown", width=2)     
    canvas.create_text(190, 100, text="O", font=("Arial", 20, "bold"))
    canvas.create_text(320,185, text="F", font=("Arial", 20, "bold"))
    canvas.create_text(450, 240, text="G", font=("Arial", 20, "bold"))
    canvas.create_text(750, 250, text="A", font=("Arial", 20, "bold"))
    canvas.create_text(600, 50, text="Sign Convention:", font=("Garamond", 20, "bold","underline"))
    canvas.create_text(610, 70, text="+ve : Anti Clockwise", font=("Garamond", 20))
    canvas.create_text(600, 90, text="-ve : Clockwise", font=("Garamond", 20))    
    canvas.create_text(260,90, text="Length 1", fill="red", font=("Arial", 20, "italic"))
    canvas.create_text(370, 230, text="Length 2", fill="red", font=("Arial", 20, "italic"))
    canvas.create_text(600, 370, text="Length 3", fill="red", font=("Arial", 20, "italic"))
    canvas.create_text(180,130, text="Angle", fill="blue", font=("Arial", 20, "italic"))    
    length_input_1 = tk.Entry(root)
    length_input_1.grid(row=1, column=1)
    tk.Label(root, text="Length 1<in m>",font=("Arial", 15, "bold")).grid(row=1, column=0)
    length_input_2 = tk.Entry(root)
    length_input_2.grid(row=2, column=1)
    tk.Label(root, text="Length 2<in m>",font=("Arial", 15, "bold")).grid(row=2, column=0)
    length_input_3 = tk.Entry(root)
    length_input_3.grid(row=3, column=1)
    tk.Label(root, text="Length 3<in m>",font=("Arial", 15, "bold")).grid(row=3, column=0)
    angle_input = tk.Entry(root)
    angle_input.grid(row=4, column=1)
    tk.Label(root, text="Angle <in degrees> ",font=("Arial", 15, "bold")).grid(row=4, column=0)
    Force_input_G = tk.Entry(root)
    Force_input_G.grid(row=5, column=1)
    tk.Label(root, text="Mass at G<in kg>",font=("Arial", 15, "bold")).grid(row=5, column=0)
    Force_input_A = tk.Entry(root)
    Force_input_A.grid(row=6, column=1)
    tk.Label(root, text="Mass at A<in kg>",font=("Arial", 15, "bold")).grid(row=6, column=0) 
    btn = ttk.Button(root, text="Submit", command=retrieve_inputs)
    btn.grid(row=10, column=0, columnspan=2)
    root.mainloop()
def default():
    def retrieve_inputs():            
        length_1 = 0.05
        length_2 = 0.15
        length_3 = 0.325
        angle = 55         
        Force_at_G = 2.3
        Force_at_A = 3.6
        T = ((9.81*length_2*Force_at_G*math.sin(math.radians(angle)))+(9.81*Force_at_A*length_3))/(length_1)
        M_o = -T*length_1
        messagebox.showinfo("Answer",f"1) The tension at which moment becomes zero about O is, {T} N\n\n 2) The combined moment about O of the weight of the forearm and the sphere is, {M_o} Nm")      
    root = tk.Tk()
    root.title("Q. 2/50")
    root.geometry('900x900')
    canvas = tk.Canvas(root, width=900, height=500, bg="white")
    canvas.grid(row=0, column=0, columnspan=4)
    canvas.create_line(200,100,450,250 ,fill="black", width=2)
    canvas.create_line(450,250,750,260 ,fill="black", width=2)
    canvas.create_line(200,380,200,100 ,fill="green", width=2)
    canvas.create_line(750,350,750,380 ,fill="green", width=2)
    canvas.create_line(200,130, 235, 120 ,fill="blue", width=2)
    canvas.create_line(200,100,320,100, fill="red", dash=(5,5))
    canvas.create_line(198,106,448,256, fill="red", dash=(5,5))
    canvas.create_line(200,380,750,380, fill="red", dash=(5,5))
    canvas.create_line(320,100, 320, 170, arrow=tk.FIRST, fill="brown", width=2)
    canvas.create_line(450,250, 450,350, arrow=tk.LAST, fill="brown", width=2)
    canvas.create_line(750,260, 750,350, arrow=tk.LAST, fill="brown", width=2)     
    canvas.create_text(190, 100, text="O", font=("Arial", 20, "bold"))
    canvas.create_text(320,185, text="F", font=("Arial", 20, "bold"))
    canvas.create_text(450, 240, text="G", font=("Arial", 20, "bold"))
    canvas.create_text(750, 250, text="A", font=("Arial", 20, "bold"))
    canvas.create_text(600, 50, text="Sign Convention:", font=("Garamond", 20, "bold","underline"))
    canvas.create_text(610, 70, text="+ve : Anti Clockwise", font=("Garamond", 20))
    canvas.create_text(600, 90, text="-ve : Clockwise", font=("Garamond", 20))    
    canvas.create_text(260,90, text="Length 1", fill="red", font=("Arial", 20, "italic"))
    canvas.create_text(370, 230, text="Length 2", fill="red", font=("Arial", 20, "italic"))
    canvas.create_text(600, 370, text="Length 3", fill="red", font=("Arial", 20, "italic"))
    canvas.create_text(180,130, text="Angle", fill="blue", font=("Arial", 20, "italic"))
    tk.Label(root, text="Length 1",font=("Arial", 20, "italic")).grid(row=1, column=0)
    tk.Label(root, text="50 mm",font=("Arial", 20, "italic")).grid(row=1, column=1)    
    tk.Label(root, text="Length 2 ",font=("Arial", 20, "italic")).grid(row=2, column=0)
    tk.Label(root, text="150 mm",font=("Arial", 20, "italic")).grid(row=2, column=1)
    tk.Label(root, text="Length 3",font=("Arial", 20, "italic")).grid(row=3, column=0)
    tk.Label(root, text="325 mm",font=("Arial", 20, "italic")).grid(row=3, column=1)
    tk.Label(root, text="Angle",font=("Arial", 20, "italic")).grid(row=4, column=0)
    tk.Label(root, text="55°",font=("Arial", 20, "italic")).grid(row=4, column=1)
    tk.Label(root, text="Mass at G",font=("Arial", 20, "italic")).grid(row=5, column=0)
    tk.Label(root, text="2.3 kg",font=("Arial", 20, "italic")).grid(row=5, column=1)
    tk.Label(root, text="Mass at A",font=("Arial", 20, "italic")).grid(row=6, column=0)
    tk.Label(root, text="3.6 kg",font=("Arial", 20, "italic")).grid(row=6, column=1)
    btn = ttk.Button(root, text="Submit", command=retrieve_inputs)
    btn.grid(row=10, column=0, columnspan=2)
    root.mainloop()
root = tk.Tk()
root.title("Lower Arm Analysis")
root.geometry("700x900")
title_label = tk.Label(root, text="Elements of the lower arm are shown below in the figure.\nChoose one of the below options.",
                       font=("Helvetica", 14, "bold"), fg="red",  justify="center")
title_label.pack(pady=10)
image_path = "Untitled.png"   
photo = tk.PhotoImage(file=image_path)
image_label = tk.Label(root, image=photo, bg="grey")
image_label.pack()
def option1():
    total_moment()
def option2():
    tension_for_zero_moment()
def option3():
    default()
def create_button(text, command):
    frame = tk.Frame(root, bg="black", padx=5, pady=5, width=600, height=90)   
    frame.pack(pady=10, padx=50)
    frame.pack_propagate(False)   
    button = tk.Button(frame, text=text, font=("Helvetica", 12, "bold"),
                       fg="black", relief="flat", activebackground="gray",
                       wraplength=550, justify="center", command=command)
    button.pack(expand=True, fill="both")
create_button("1) Enter all the values to know the total moment about the elbow pivot.", option1)
create_button("2) Enter all the values except for the tension in the bicep and calculate the numeric value of tension in the bicep.", option2)
create_button("3) Use a set of pre-written values to find the moment about the pivot only by the weight of the arm and the sphere, and also find the tension causing the moment to be zero.", option3)
root.mainloop()





