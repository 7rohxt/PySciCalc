# Importing headers
import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
import math

class Calculator:
    def __init__(self):
        ctk.set_appearance_mode("dark")  # Dark Mode
        self.calculation = "" 

        self.cal = tk.Tk()
        self.cal.geometry("415x506")
        self.cal.title("PySci Calculator")
        self.cal.configure(bg="#202020")
        
    # I excluded th menubar to maintain cleaner look.

        # self.menubar = tk.Menu(self.cal)

        # self.filemenu = tk.Menu(self.menubar, tearoff = 0)
        # self.filemenu.add_command(label="Close", command=self.on_closing)
        # self.filemenu.add_separator()
        # self.filemenu.add_command(label="Close Forcefully", command=exit)
        

        # self.menubar.add_cascade(menu=self.filemenu, label="File")

        # self.cal.config(menu=self.menubar)


        self.textbox = ctk.CTkEntry(self.cal, 
                            height=70,  
                            font=('Calibri', 35), 
                            bg_color="#202020",
                            fg_color="#202020",  
                            text_color="white",
                            border_width=2,  
                            corner_radius=10,
                            justify="right") 
        self.textbox.pack(padx=0, pady=30, fill="x")
        self.textbox.insert(0, "0")
        self.textbox.bind("<FocusIn>", self.clear_default_text)

        # Button frame
        self.buttonframe = tk.Frame(self.cal, bg="#202020")  
        self.buttonframe.pack(side="bottom", fill="x")  # Fill the window
       
        # Configure columns to expand
        for i in range(5):
            self.buttonframe.columnconfigure(i, weight=1)

        font_style = ('Calibri', 14)
        button_color = "#323232"
        text_color = "white"

        # Creating buttons separately

        # Row 1
        self.btn_sin = ctk.CTkButton(self.buttonframe, text="sin", font=font_style, fg_color=button_color, text_color=text_color, command=lambda: self.trig_calc("sin"))
        self.btn_cos = ctk.CTkButton(self.buttonframe, text="cos", font=font_style, fg_color=button_color, text_color=text_color, command=lambda: self.trig_calc("cos"))
        self.btn_tan = ctk.CTkButton(self.buttonframe, text="tan", font=font_style, fg_color=button_color, text_color=text_color, command=lambda: self.trig_calc("tan"))
        self.btn_abs = ctk.CTkButton(self.buttonframe, text="|x|", font=font_style, fg_color=button_color, text_color=text_color,command=self.abs_calc)
        self.btn_c = ctk.CTkButton(self.buttonframe, text="⌫", font=font_style, fg_color=button_color, text_color=text_color, command=self.backspace)

        # Row 2
        self.btn_csc = ctk.CTkButton(self.buttonframe, text="csc", font=font_style, fg_color=button_color, text_color=text_color, command=lambda: self.trig_calc("csc"))
        self.btn_sec = ctk.CTkButton(self.buttonframe, text="sec", font=font_style, fg_color=button_color, text_color=text_color, command=lambda: self.trig_calc("sec"))
        self.btn_cot = ctk.CTkButton(self.buttonframe, text="cot", font=font_style, fg_color=button_color, text_color=text_color, command=lambda: self.trig_calc("cot"))
        self.btn_exp = ctk.CTkButton(self.buttonframe, text="exp", font=font_style, fg_color=button_color, text_color=text_color, command=self.exp_calc)
        self.btn_ac = ctk.CTkButton(self.buttonframe, text="AC", font=font_style, fg_color=button_color, text_color=text_color, command=self.clear_field)

        # Row 3
        self.btn_sqrt = ctk.CTkButton(self.buttonframe, text="√x", font=font_style, fg_color=button_color, text_color=text_color, command=self.sqrt_calc)
        self.btn_open = ctk.CTkButton(self.buttonframe, text="(", font=font_style, fg_color=button_color, text_color=text_color, command=lambda: self.add_to_calc("("))
        self.btn_close = ctk.CTkButton(self.buttonframe, text=")", font=font_style, fg_color=button_color, text_color=text_color, command=lambda: self.add_to_calc(")"))
        self.btn_fact = ctk.CTkButton(self.buttonframe, text="n!", font=font_style, fg_color=button_color, text_color=text_color, command=self.fact_calc)
        self.btn_div = ctk.CTkButton(self.buttonframe, text="÷", font=font_style, fg_color=button_color, text_color=text_color, command=lambda: self.add_to_calc("/"))

        # Row 4
        self.btn_xy = ctk.CTkButton(self.buttonframe, text="xʸ", font=font_style, fg_color=button_color, text_color=text_color, command=self.add_power_symbol)
        self.btn_7 = ctk.CTkButton(self.buttonframe, text="7", font=font_style, fg_color="#454545", text_color=text_color, command=lambda: self.add_to_calc(7))
        self.btn_8 = ctk.CTkButton(self.buttonframe, text="8", font=font_style, fg_color="#454545", text_color=text_color, command=lambda: self.add_to_calc(8))
        self.btn_9 = ctk.CTkButton(self.buttonframe, text="9", font=font_style, fg_color="#454545", text_color=text_color, command=lambda: self.add_to_calc(9))
        self.btn_mul = ctk.CTkButton(self.buttonframe, text="×", font=font_style, fg_color=button_color, text_color=text_color, command=lambda: self.add_to_calc("*"))

        # Row 5
        self.btn_pie = ctk.CTkButton(self.buttonframe, text="π", font=font_style, fg_color=button_color, text_color=text_color, command=self.insert_pi)
        self.btn_4 = ctk.CTkButton(self.buttonframe, text="4", font=font_style, fg_color="#454545", text_color=text_color, command=lambda: self.add_to_calc(4))
        self.btn_5 = ctk.CTkButton(self.buttonframe, text="5", font=font_style, fg_color="#454545", text_color=text_color, command=lambda: self.add_to_calc(5))
        self.btn_6 = ctk.CTkButton(self.buttonframe, text="6", font=font_style, fg_color="#454545", text_color=text_color, command=lambda: self.add_to_calc(6))
        self.btn_sub = ctk.CTkButton(self.buttonframe, text="-", font=font_style, fg_color=button_color, text_color=text_color, command=lambda: self.add_to_calc("-"))

        # Row 6
        self.btn_log = ctk.CTkButton(self.buttonframe, text="log", font=font_style, fg_color=button_color, text_color=text_color,command=self.log_calc)
        self.btn_1 = ctk.CTkButton(self.buttonframe, text="1", font=font_style, fg_color="#454545", text_color=text_color, command=lambda: self.add_to_calc(1))
        self.btn_2 = ctk.CTkButton(self.buttonframe, text="2", font=font_style, fg_color="#454545", text_color=text_color, command=lambda: self.add_to_calc(2))
        self.btn_3 = ctk.CTkButton(self.buttonframe, text="3", font=font_style, fg_color="#454545", text_color=text_color, command=lambda: self.add_to_calc(3))
        self.btn_add = ctk.CTkButton(self.buttonframe, text="+", font=font_style, fg_color=button_color, text_color=text_color, command=lambda: self.add_to_calc("+"))

        # Row 7
        self.btn_ln = ctk.CTkButton(self.buttonframe, text="ln", font=font_style, fg_color=button_color, text_color=text_color, command=self.ln_calc)
        self.btn_pm = ctk.CTkButton(self.buttonframe, text="+/-", font=font_style, fg_color="#454545", text_color=text_color, command=self.plus_minus)
        self.btn_0 = ctk.CTkButton(self.buttonframe, text="0", font=font_style, fg_color="#454545", text_color=text_color, command=lambda: self.add_to_calc(0))
        self.btn_dot = ctk.CTkButton(self.buttonframe, text=".", font=font_style, fg_color="#454545", text_color=text_color, command=lambda: self.add_to_calc("."))
        self.btn_equal = ctk.CTkButton(self.buttonframe, text="=", font=font_style, fg_color="#6B6B6B", text_color=text_color, command= self.eval_calc)

        # Placing buttons in grid
        buttons = [
            [self.btn_sin, self.btn_cos, self.btn_tan, self.btn_abs, self.btn_c],
            [self.btn_csc, self.btn_sec, self.btn_cot, self.btn_exp, self.btn_ac],
            [self.btn_sqrt, self.btn_open, self.btn_close, self.btn_fact, self.btn_div],
            [self.btn_xy, self.btn_7, self.btn_8, self.btn_9, self.btn_mul],
            [self.btn_pie, self.btn_4, self.btn_5, self.btn_6, self.btn_sub],
            [self.btn_log, self.btn_1, self.btn_2, self.btn_3, self.btn_add],
            [self.btn_ln, self.btn_pm, self.btn_0, self.btn_dot, self.btn_equal],
        ]

        for i, row in enumerate(buttons):
            for j, btn in enumerate(row):
                btn.grid(row=i, column=j, sticky=tk.W+tk.E, ipady=6, padx=1, pady=1)

        self.cal.protocol("WM_DELETE_WINDOW", self.on_closing)
    
        self.cal.mainloop()

    def add_to_calc(self, symbol):
  
        self.calculation += str(symbol)
        self.textbox.delete(0, "end")
        self.textbox.insert(0, self.calculation)

    def eval_calc(self):
    
        try:
            self.calculation= str(eval(self.calculation))
            self.textbox.delete(0, "end")
            self.textbox.insert(0, self.calculation)
        except:
            self.clear_field()
            self.textbox.delete(0, "end")
            self.textbox.insert(0, "Error")
    
    def clear_field(self):

        self.calculation  = ""
        self.textbox.delete(0, "end")
        self.textbox.insert(0, "0")

    def backspace(self):

        if self.textbox.get() == "0":
            pass
        else:
            self.calculation = self.calculation[:-1]
            self.textbox.delete(0,"end")
            self.textbox.insert(0, self.calculation)
    
    def trig_calc(self, operation):
        
        self.value = float(self.textbox.get())
        self.value = math.radians(self.value)

        if operation == "csc":
            result = getattr(math, "sin")(self.value)
            result = 1/result
        
        elif operation == "sec":
            result = getattr(math, "cos")(self.value)
            result = 1/result
        
        elif operation == "cot":
            result = getattr(math, operation)(self.value)
            result = 1/result
        
        else:
            result = getattr(math, operation)(self.value)

        self.calculation = result
        self.textbox.delete(0,"end")
        self.textbox.insert(0, self.calculation)

    def abs_calc(self):
            
        value = float(self.textbox.get()) 
        result = abs(value) 

        self.calculation = str(result)
        self.textbox.delete(0, "end")
        self.textbox.insert(0, self.calculation)

        self.safe_eval(self, abs, float(self.textbox.get()))
    
    def exp_calc(self):
            
        value = float(self.textbox.get())
        result = math.exp(value)

        self.calculation = str(result)
        self.textbox.delete(0, "end")
        self.textbox.insert(0, self.calculation)
    
    def add_power_symbol(self):

        self.calculation += "**"  
        self.textbox.delete(0, "end")
        self.textbox.insert(0, self.calculation)

    def sqrt_calc(self):
            
        value = float(self.textbox.get())
        if value < 0:
            self.textbox.delete(0, "end")
            self.textbox.insert(0, "No negatives Please!") 
        else:
            result = math.sqrt(value)  
            self.calculation = str(result)
            self.textbox.delete(0, "end")
            self.textbox.insert(0, self.calculation)
    
    def fact_calc(self):
        
        value = int(float(self.textbox.get())) 
        if value < 0:
            self.textbox.delete(0, "end")
            self.textbox.insert(0, "No negatives please!") 
        else:
            result = math.factorial(value) 
            self.calculation = str(result)
            self.textbox.delete(0, "end")
            self.textbox.insert(0, self.calculation)
    
    def insert_pi(self):

        self.textbox.delete(0, "end")  
        self.textbox.insert(0, str(math.pi))

    def log_calc(self):

        value = float(self.textbox.get())
        if value < 0:
            self.textbox.delete(0, "end")
            self.textbox.insert(0, "No Negatives please!")

        else:
            result = math.log10(value)
            self.textbox.delete(0, "end")
            self.textbox.insert(0, str(result))

    def ln_calc(self):

        value = float(self.textbox.get())
        if value < 0:
            self.textbox.delete(0, "end")
            self.textbox.insert(0, "No Negatives please!")
        else:
            result = math.log(value) 
            self.textbox.delete(0, "end")
            self.textbox.insert(0, str(result))
    def plus_minus(self):

        value = float(self.textbox.get())  
        result = -value 
        self.textbox.delete(0, "end")
        self.textbox.insert(0, str(result))

    def safe_eval(self, func, *args):
        try:
            result = func(*args) 
            self.calculation = str(result)
            self.textbox.delete(0, "end")
            self.textbox.insert(0, self.calculation)
        except Exception:
            self.textbox.delete(0, "end")
            self.textbox.insert(0, "Error")

    def clear_default_text(self, event):

        if self.textbox.get() == "0":
            self.textbox.delete(0, "end")

    def on_closing(self):

        if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):
            self.cal.destroy()

Calculator() 