# Importing headers
import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk

class Calculator:
    def __init__(self):
        ctk.set_appearance_mode("dark")  # Dark Mode

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
        self.btn_sin = ctk.CTkButton(self.buttonframe, text="sin", font=font_style, fg_color=button_color, text_color=text_color)
        self.btn_cos = ctk.CTkButton(self.buttonframe, text="cos", font=font_style, fg_color=button_color, text_color=text_color)
        self.btn_tan = ctk.CTkButton(self.buttonframe, text="tan", font=font_style, fg_color=button_color, text_color=text_color)
        self.btn_mod = ctk.CTkButton(self.buttonframe, text="|x|", font=font_style, fg_color=button_color, text_color=text_color)
        self.btn_c = ctk.CTkButton(self.buttonframe, text="⌫", font=font_style, fg_color=button_color, text_color=text_color)

        # Row 2
        self.btn_csc = ctk.CTkButton(self.buttonframe, text="csc", font=font_style, fg_color=button_color, text_color=text_color)
        self.btn_sec = ctk.CTkButton(self.buttonframe, text="sec", font=font_style, fg_color=button_color, text_color=text_color)
        self.btn_cot = ctk.CTkButton(self.buttonframe, text="cot", font=font_style, fg_color=button_color, text_color=text_color)
        self.btn_exp = ctk.CTkButton(self.buttonframe, text="exp", font=font_style, fg_color=button_color, text_color=text_color)
        self.btn_ac = ctk.CTkButton(self.buttonframe, text="AC", font=font_style, fg_color=button_color, text_color=text_color)

        # Row 3
        self.btn_sqrt = ctk.CTkButton(self.buttonframe, text="√x", font=font_style, fg_color=button_color, text_color=text_color)
        self.btn_open = ctk.CTkButton(self.buttonframe, text="(", font=font_style, fg_color=button_color, text_color=text_color)
        self.btn_close = ctk.CTkButton(self.buttonframe, text=")", font=font_style, fg_color=button_color, text_color=text_color)
        self.btn_fact = ctk.CTkButton(self.buttonframe, text="n!", font=font_style, fg_color=button_color, text_color=text_color)
        self.btn_div = ctk.CTkButton(self.buttonframe, text="/", font=font_style, fg_color=button_color, text_color=text_color)

        # Row 4
        self.btn_xy = ctk.CTkButton(self.buttonframe, text="xʸ", font=font_style, fg_color=button_color, text_color=text_color)
        self.btn_7 = ctk.CTkButton(self.buttonframe, text="7", font=font_style, fg_color="#454545", text_color=text_color)
        self.btn_8 = ctk.CTkButton(self.buttonframe, text="8", font=font_style, fg_color="#454545", text_color=text_color)
        self.btn_9 = ctk.CTkButton(self.buttonframe, text="9", font=font_style, fg_color="#454545", text_color=text_color)
        self.btn_mul = ctk.CTkButton(self.buttonframe, text="×", font=font_style, fg_color=button_color, text_color=text_color)

        # Row 5
        self.btn_pie = ctk.CTkButton(self.buttonframe, text="π", font=font_style, fg_color=button_color, text_color=text_color)
        self.btn_4 = ctk.CTkButton(self.buttonframe, text="4", font=font_style, fg_color="#454545", text_color=text_color)
        self.btn_5 = ctk.CTkButton(self.buttonframe, text="5", font=font_style, fg_color="#454545", text_color=text_color)
        self.btn_6 = ctk.CTkButton(self.buttonframe, text="6", font=font_style, fg_color="#454545", text_color=text_color)
        self.btn_sub = ctk.CTkButton(self.buttonframe, text="-", font=font_style, fg_color=button_color, text_color=text_color)

        # Row 6
        self.btn_log = ctk.CTkButton(self.buttonframe, text="log", font=font_style, fg_color=button_color, text_color=text_color)
        self.btn_1 = ctk.CTkButton(self.buttonframe, text="1", font=font_style, fg_color="#454545", text_color=text_color)
        self.btn_2 = ctk.CTkButton(self.buttonframe, text="2", font=font_style, fg_color="#454545", text_color=text_color)
        self.btn_3 = ctk.CTkButton(self.buttonframe, text="3", font=font_style, fg_color="#454545", text_color=text_color)
        self.btn_add = ctk.CTkButton(self.buttonframe, text="+", font=font_style, fg_color=button_color, text_color=text_color)

        # Row 7
        self.btn_ln = ctk.CTkButton(self.buttonframe, text="ln", font=font_style, fg_color=button_color, text_color=text_color)
        self.btn_pm = ctk.CTkButton(self.buttonframe, text="+/-", font=font_style, fg_color="#454545", text_color=text_color)
        self.btn_0 = ctk.CTkButton(self.buttonframe, text="0", font=font_style, fg_color="#454545", text_color=text_color)
        self.btn_dot = ctk.CTkButton(self.buttonframe, text=".", font=font_style, fg_color="#454545", text_color=text_color)
        self.btn_equal = ctk.CTkButton(self.buttonframe, text="=", font=font_style, fg_color="#6B6B6B", text_color=text_color)

        # Placing buttons in grid
        buttons = [
            [self.btn_sin, self.btn_cos, self.btn_tan, self.btn_mod, self.btn_c],
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
    
    def clear_default_text(self, event):
        if self.textbox.get() == "0":
            self.textbox.delete(0, "end")

    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):
            self.cal.destroy()

Calculator()
