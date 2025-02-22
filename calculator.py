import tkinter as tk

LARGE_FONT_STYLE = ("Arial", 40, "bold")
SMALL_FONT_STYLE = ("Arial", 16)
DIGITS_FONT_STYLE = ("Arial", 24, "bold")
DEFAULT_FONT_STYLE = ("Arial", 20)

OFF_WHITE = "#F8FAFF"
WHITE = "#FFFFFF"
LIGHT_BLUE = "#CCEDFF"
LIGHT_GRAY = "#F5F5F5"
LABEL_COLOR = "#25265E"

class Calculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("375x667")
        self.root.resizable(0, 0)
        self.root.title("Calculator")
        self.total_expression = '0'
        self.current_expression = '0'
        self.is_scientific = True

        self.digits = {
            7: (3, 1), 8: (3, 2), 9: (3, 3),
            4: (4, 1), 5: (4, 2), 6: (4, 3),
            1: (5, 1), 2: (5, 2), 3: (5, 3),
            0: (6, 2), '.': (6, 3)
        }
        self.operator = {
            '/' : ('/', 2, 4),
            '*' : ('*', 3, 4),
            '-' : ('-', 4, 4),
            '+' : ('+', 5, 4)
        }

        self.display_frame = self.create_display_frame()
        self.buttons_frame = self.create_buttons_frame()

        self.total_level, self.current_level = self.create_display_levels()

        self.create_display_buttons()

    def create_buttons_frame(self):
        buttons = tk.Frame(self.root)
        buttons.pack(expand=True, fill='both')
        return buttons

    def create_display_frame(self):
        frame = tk.Frame(self.root, height=220, bg=LIGHT_GRAY)
        frame.pack(expand=True, fill='both')
        return frame
    
    def create_display_levels(self):
        total_level = tk.Label(self.display_frame, text=self.total_expression, bg=LIGHT_GRAY, anchor=tk.E, font=SMALL_FONT_STYLE, padx=25, fg=LABEL_COLOR)
        total_level.pack(expand=True, fill='both')

        cur_level = tk.Label(self.display_frame, text=self.current_expression, bg=LIGHT_GRAY, anchor=tk.E, font=LARGE_FONT_STYLE, padx=24, fg=LABEL_COLOR)
        cur_level.pack(expand=True, fill='both')

        return total_level, cur_level

    def toggle(self):
        self.is_scientific = not self.is_scientific
        self.create_display_buttons()
    
    def create_display_buttons(self):
        self.clear_buttons()
        self.buttons_frame = self.create_buttons_frame()
        if self.is_scientific:
            self.create_2nd_button()
            self.create_deg_button()
            self.create_sin_button()
            self.create_cos_button()
            self.create_tan_button()
            self.create_power_button()
            self.create_log_button()
            self.create_ln_button()
            self.create_open_parenthesis_button()
            self.create_close_parenthesis_button()

            self.create_scientific_buttons()
            self.create_operator_buttons()
            self.create_equals_button()
            self.create_clear_button()
            self.create_backspace_button()
            self.create_percentage_button()

            self.create_sqrt_button()
            self.create_factorial_button()
            self.create_inverse_button()
            self.create_pie_button()
            self.create_e_button()
            self.create_toggle_button(6, 0)

            for r in range(7):
                self.buttons_frame.rowconfigure(r, weight=1)

            for c in range(5):
                self.buttons_frame.columnconfigure(c, weight=1)

        else:
            self.create_basic_buttons()
            self.create_operator_buttons()
            self.create_equals_button()
            self.create_clear_button()
            self.create_backspace_button()
            self.create_percentage_button()
            self.create_toggle_button(6, 1)

            for r in range(2, 7):
                self.buttons_frame.rowconfigure(r, weight=1)

            for c in range(1, 5):
                self.buttons_frame.columnconfigure(c, weight=1)

    def create_basic_buttons(self):
        
        for key, pos in self.digits.items():
            button = tk.Button(self.buttons_frame, bg=WHITE, fg=LABEL_COLOR, text=str(key), font=DIGITS_FONT_STYLE, borderwidth=0)
            button.grid(row=pos[0], column=pos[1], sticky=tk.NSEW)

    def create_scientific_buttons(self):
        for key, pos in self.digits.items():
            button = tk.Button(self.buttons_frame, bg=WHITE, fg=LABEL_COLOR, text=str(key), font=DIGITS_FONT_STYLE, borderwidth=0)
            button.grid(row=pos[0], column=pos[1], sticky=tk.NSEW)
    
    def create_operator_buttons(self):
        for key, pos in self.operator.items():
            button = tk.Button(self.buttons_frame, text=pos[0], bg=OFF_WHITE, font=DIGITS_FONT_STYLE, borderwidth=0)
            button.grid(row=pos[1], column=pos[2], sticky=tk.NSEW)
    
    def create_equals_button(self):
        button = tk.Button(self.buttons_frame, text='=', bg=LIGHT_BLUE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0)
        button.grid(row=6, column=4, sticky=tk.NSEW)

    def create_percentage_button(self):
        button = tk.Button(self.buttons_frame, text='%', bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0)
        button.grid(row=2, column=3, sticky=tk.NSEW)

    def create_backspace_button(self):
        button = tk.Button(self.buttons_frame, text='\u232B', bg=OFF_WHITE, fg=LABEL_COLOR, font=SMALL_FONT_STYLE, borderwidth=0)
        button.grid(row=2, column=2, sticky=tk.NSEW)

    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text='C', bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0)
        button.grid(row=2, column=1, sticky=tk.NSEW)
    
    def create_toggle_button(self, r, c):
        button = tk.Button(self.buttons_frame, text='T', bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0, command=self.toggle)
        button.grid(row=r, column=c, sticky=tk.NSEW)

    def create_2nd_button(self):
        button = tk.Button(self.buttons_frame, text='2nd', bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0)
        button.grid(row=0, column=0, sticky=tk.NSEW)
    
    def create_deg_button(self):
        button = tk.Button(self.buttons_frame, text='deg', bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0)
        button.grid(row=0, column=1, sticky=tk.NSEW)

    def create_sin_button(self):
        button = tk.Button(self.buttons_frame, text='sin', bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0)
        button.grid(row=0, column=2, sticky=tk.NSEW)
    
    def create_cos_button(self):
        button = tk.Button(self.buttons_frame, text='cos', bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0)
        button.grid(row=0, column=3, sticky=tk.NSEW)

    def create_tan_button(self):
        button = tk.Button(self.buttons_frame, text='tan', bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0)
        button.grid(row=0, column=4, sticky=tk.NSEW)
    
    def create_power_button(self):
        button = tk.Button(self.buttons_frame, text='X\u02b8', bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0)
        button.grid(row=1, column=0, sticky=tk.NSEW)

    def create_log_button(self):
        button = tk.Button(self.buttons_frame, text='lg', bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0)
        button.grid(row=1, column=1, sticky=tk.NSEW)
    
    def create_ln_button(self):
        button = tk.Button(self.buttons_frame, text='ln', bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0)
        button.grid(row=1, column=2, sticky=tk.NSEW)

    def create_open_parenthesis_button(self):
        button = tk.Button(self.buttons_frame, text='(', bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0)
        button.grid(row=1, column=3, sticky=tk.NSEW)
    
    def create_close_parenthesis_button(self):
        button = tk.Button(self.buttons_frame, text=')', bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0)
        button.grid(row=1, column=4, sticky=tk.NSEW)

    def create_sqrt_button(self):
        button = tk.Button(self.buttons_frame, text='\u221Ax', bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0)
        button.grid(row=2, column=0, sticky=tk.NSEW)
    
    def create_factorial_button(self):
        button = tk.Button(self.buttons_frame, text='x!', bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0)
        button.grid(row=3, column=0, sticky=tk.NSEW)
    
    def create_inverse_button(self):
        button = tk.Button(self.buttons_frame, text='1/x', bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0)
        button.grid(row=4, column=0, sticky=tk.NSEW)
    
    def create_pie_button(self):
        button = tk.Button(self.buttons_frame, text='\u03c0', bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0)
        button.grid(row=5, column=0, sticky=tk.NSEW)

    def create_e_button(self):
        button = tk.Button(self.buttons_frame, text='e', bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0)
        button.grid(row=6, column=1, sticky=tk.NSEW)

    def clear_buttons(self):
        self.buttons_frame.destroy()
        # for button in self.buttons_frame.winfo_children():
        #     button.destroy()

    def run(self):
        self.root.mainloop()

def main():
    calc = Calculator()
    calc.run()

if __name__ == "__main__":
    main()
        