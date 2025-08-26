import tkinter as tk
from tkinter import ttk
import math


'''
Textbook : Engineering Mechanics Statics [JL Meriam, LG Kraige, JN Bolton]
Problem : 2-15
A compressive force F is transmitted via the coupler arm AB to disk OA. Develop the general expression for the n- and t- components of force F as they act on the disk.
'''
def calculate_forces(F_val, theta_val, phi_val):
    # Handle empty inputs
    if F_val == "" or theta_val == "" or phi_val == "":
        return "Error: One or more inputs are empty.", ""

    # Handle infinite values
    for val in [F_val, theta_val, phi_val]:
        try:
            if abs(float(val)) == float('inf'):
                return "Error: Value exceeds limits (Infinity).\nKindly enter a smaller value.", ""
                
        except ValueError:
            pass  # Non-numeric values will be handled later

    try:
        # Try full numeric calculation
        F = float(F_val)
        theta = float(theta_val)
        phi = float(phi_val)

        theta_rad = math.radians(theta)
        phi_rad = math.radians(phi)
        angle_sum = theta_rad + phi_rad

        F_n = -F * math.cos(angle_sum)
        F_t = F * math.sin(angle_sum)
        return F_n, F_t

    except ValueError:
        # Convert values to strings for symbolic use
        F_str = str(F_val)
        theta_str = str(theta_val)
        phi_str = str(phi_val)

        def try_float(val):
            try:
                return float(val)
            except:
                return None

        F_num = try_float(F_val)
        theta_num = try_float(theta_val)
        phi_num = try_float(phi_val)

        if F_num is None and theta_num is not None and phi_num is not None:
            angle_sum = math.radians(theta_num + phi_num)
            cos_val = math.cos(angle_sum)
            sin_val = math.sin(angle_sum)
            F_n_str = f"-{F_str} * {cos_val:.4f}"
            F_t_str = f"{F_str} * {sin_val:.4f}"
            return F_n_str, F_t_str

        if F_num is not None and theta_num is None and phi_num is None:
            F_n_str = f"-{F_num}*cos({theta_str}+{phi_str})"
            F_t_str = f"{F_num}*sin({theta_str}+{phi_str})"
            return F_n_str, F_t_str

        if F_num is not None and theta_num is not None and phi_num is None:
            F_n_str = f"-{F_num}*cos({theta_num}+{phi_str})"
            F_t_str = f"{F_num}*sin({theta_num}+{phi_str})"
            return F_n_str, F_t_str

        if F_num is not None and theta_num is None and phi_num is not None:
            F_n_str = f"-{F_num}*cos({theta_str}+{phi_num})"
            F_t_str = f"{F_num}*sin({theta_str}+{phi_num})"
            return F_n_str, F_t_str

        if F_num is None and theta_num is None and phi_num is not None:
            F_n_str = f"-{F_str}*cos({theta_str}+{phi_num})"
            F_t_str = f"{F_str}*sin({theta_str}+{phi_num})"
            return F_n_str, F_t_str

        if F_num is None and theta_num is not None and phi_num is None:
            F_n_str = f"-{F_str}*cos({theta_num}+{phi_str})"
            F_t_str = f"{F_str}*sin({theta_num}+{phi_str})"
            return F_n_str, F_t_str

        # Case: all symbolic
        F_n_str = f"-{F_str}*cos({theta_str}+{phi_str})"
        F_t_str = f"{F_str}*sin({theta_str}+{phi_str})"
        return F_n_str, F_t_str

    except Exception as e:
        return f"An unexpected error occurred: {e}", ""



def draw_free_body_diagram(canvas, F_val, theta_val, phi_val, F_n_val, F_t_val):
    try:
        canvas.delete("all")  # Clear previous drawings

        F_val = float(F_val)
        theta_val = float(theta_val)
        phi_val=float(phi_val)
        F_n_val=float(F_n_val)
        F_t_val=float(F_t_val)

        width = int(canvas['width'])
        height = int(canvas['height'])
        origin_x = width // 2
        origin_y = height // 2

        # Increase axis size by 50%
        axis_length_factor = 2.27
        axis_length = 150 * axis_length_factor
        dotted_style = (4, 2)

        # Draw X and Y axes
        canvas.create_line(origin_x - axis_length, origin_y,
                           origin_x + axis_length, origin_y,
                           fill="black", width=2, dash=dotted_style)
        canvas.create_line(origin_x, origin_y + axis_length,
                           origin_x, origin_y - axis_length,
                           fill="black", width=2, dash=dotted_style)

        canvas.create_text(origin_x + axis_length + 10, origin_y - 10, text="X", fill="black", font=('Helvetica', 12))
        canvas.create_text(origin_x - 10, origin_y - axis_length - 10, text="Y", fill="black", font=('Helvetica', 12))

        # Calculate angles
        phi_rad = math.radians(phi_val)
        t_phi_rad = phi_rad + math.pi / 2

        # Draw n-axis
        n_x1 = origin_x - axis_length * math.cos(phi_rad)
        n_y1 = origin_y + axis_length * math.sin(phi_rad)
        n_x2 = origin_x + axis_length * math.cos(phi_rad)
        n_y2 = origin_y - axis_length * math.sin(phi_rad)
        canvas.create_line(n_x1, n_y1, n_x2, n_y2,
                           fill="#99ccff", width=2, dash=dotted_style)
        canvas.create_text(n_x2 + 10, n_y2 - 10, text="N", fill="#99ccff", font=('Helvetica', 12))

        # Draw t-axis
        t_x1 = origin_x - axis_length * math.cos(t_phi_rad)
        t_y1 = origin_y + axis_length * math.sin(t_phi_rad)
        t_x2 = origin_x + axis_length * math.cos(t_phi_rad)
        t_y2 = origin_y - axis_length * math.sin(t_phi_rad)
        canvas.create_line(t_x1, t_y1, t_x2, t_y2,
                           fill="#33ff33", width=2, dash=dotted_style)
        canvas.create_text(t_x2 + 10, t_y2 - 10, text="T", fill="#33ff33", font=('Helvetica', 12))

        # Draw vector F
        arrow_length = abs(F_val) * 0.4
        F_rad = math.radians(-theta_val)
        F_x = origin_x + arrow_length * math.cos(F_rad)
        F_y = origin_y - arrow_length * math.sin(F_rad)

        if F_val > 0:
            canvas.create_line(origin_x, origin_y, F_x, F_y,
                               fill="maroon", width=3, arrow=tk.FIRST)
        else:
            canvas.create_line(F_x, F_y, origin_x, origin_y,
                               fill="maroon", width=3, arrow=tk.FIRST)

        canvas.create_text(F_x + 10, F_y - 10, text="F", fill="maroon", font=('Helvetica', 12))

        # Draw F_n along the N-axis
        F_n_length = F_n_val  # You can use the provided value for F_n
        F_n_x = origin_x + (F_n_length*0.4) * math.cos(phi_rad)
        F_n_y = origin_y - (F_n_length*0.4 )* math.sin(phi_rad)
        canvas.create_line(origin_x, origin_y, F_n_x, F_n_y,
                           fill="#003366", width=3, arrow=tk.LAST)
        canvas.create_text(F_n_x + 10, F_n_y - 10, text="F_n", fill="#003366", font=('Helvetica', 12))

        # Draw F_t along the T-axis
        F_t_length = F_t_val  # Use the provided value for F_t
        F_t_x = origin_x + (F_t_length*0.4) * math.cos(t_phi_rad)
        F_t_y = origin_y - (F_t_length*0.4) * math.sin(t_phi_rad)
        canvas.create_line(origin_x, origin_y, F_t_x, F_t_y,
                           fill="#006600", width=3, arrow=tk.LAST)
        canvas.create_text(F_t_x + 10, F_t_y - 10, text="F_t", fill="#006600", font=('Helvetica', 12))

    except:
        canvas.delete("all")







 
def main():
    window = tk.Tk()
    window.title("2/15")

    input_frame = ttk.Frame(window, padding="10")
    input_frame.grid(row=0, column=0, sticky=(tk.W, tk.E))

    ttk.Label(input_frame, text="Force (F N):", font=("TkDefaultFont", 26)).grid(row=0, column=0, sticky=tk.W)
    F_entry = ttk.Entry(input_frame, font=("TkDefaultFont", 26))
    F_entry.grid(row=0, column=1, sticky=(tk.W, tk.E))
    F_entry.insert(0, "500")  # symbolic default

    ttk.Label(input_frame, text="Theta (θ°):", font=("TkDefaultFont", 26)).grid(row=1, column=0, sticky=tk.W)
    theta_entry = ttk.Entry(input_frame, font=("TkDefaultFont", 26))
    theta_entry.grid(row=1, column=1, sticky=(tk.W, tk.E))
    theta_entry.insert(0, "60")

    ttk.Label(input_frame, text="Phi (Φ°):", font=("TkDefaultFont", 26)).grid(row=2, column=0, sticky=tk.W)
    phi_entry = ttk.Entry(input_frame, font=("TkDefaultFont", 26))
    phi_entry.grid(row=2, column=1, sticky=(tk.W, tk.E))
    phi_entry.insert(0, "20")

    calculate_button = ttk.Button(input_frame, text="Calculate",
                                  command=lambda: calculate_and_display())
    calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

    output_frame = ttk.Frame(window, padding="10")
    output_frame.grid(row=1, column=0, sticky=(tk.W, tk.E))

    ttk.Label(output_frame, text="Normal Force (Fn):", font=("TkDefaultFont", 26)).grid(row=0, column=0, sticky=tk.W)
    Fn_label = ttk.Label(output_frame, text="", font=("TkDefaultFont", 26))
    Fn_label.grid(row=0, column=1, sticky=(tk.W, tk.E))

    ttk.Label(output_frame, text="Tangential Force (Ft):", font=("TkDefaultFont", 26)).grid(row=1, column=0, sticky=tk.W)
    Ft_label = ttk.Label(output_frame, text="", font=("TkDefaultFont", 26))
    Ft_label.grid(row=1, column=1, sticky=(tk.W, tk.E))

    canvas = tk.Canvas(window, width=900, height=725, bg="white")
    canvas.grid(row=0, column=1, rowspan=2, padx=10, pady=10)

    draw_free_body_diagram(canvas, 500, 60, 20, "", "")

    def calculate_and_display():
        F_val = F_entry.get()
        theta_val = theta_entry.get()
        phi_val = phi_entry.get()

        Fn_val, Ft_val = calculate_forces(F_val, theta_val, phi_val)

        if isinstance(Fn_val, str):  # symbolic
            Fn_label.config(text=Fn_val, foreground="blue")
            Ft_label.config(text=Ft_val, foreground="blue")
            canvas.delete("all")
            draw_free_body_diagram(canvas, F_val, theta_val, phi_val, "", "")
        else:  # numeric
            Fn_label.config(text=f"{Fn_val:.2f} N", foreground="black")
            Ft_label.config(text=f"{Ft_val:.2f} N", foreground="black")
            draw_free_body_diagram(canvas, F_val, theta_val, phi_val, Fn_val, Ft_val)

    window.mainloop()


if __name__ == "__main__":
    main()








