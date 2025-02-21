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
            0: (6, 2), '.': (6, 1)
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
    
    def create_display_buttons(self):
        if self.is_scientific:
            self.create_scientific_buttons()
        else:
            self.create_basic_buttons()

    def create_basic_buttons(self):
        
        for key, pos in self.digits.items():
            button = tk.Button(self.buttons_frame, bg=WHITE, fg=LABEL_COLOR, text=str(key), font=DIGITS_FONT_STYLE, borderwidth=0)
            button.grid(row=pos[0], column=pos[1], sticky=tk.NSEW)

    def create_scientific_buttons(self):
        for key, pos in self.digits.items():
            button = tk.Button(self.buttons_frame, bg=WHITE, fg=LABEL_COLOR, text=str(key), font=DIGITS_FONT_STYLE, borderwidth=0)
            button.grid(row=pos[0], column=pos[1], sticky=tk.NSEW)

    def run(self):
        self.root.mainloop()

def main():
    calc = Calculator()
    calc.run()

if __name__ == "__main__":
    main()
        