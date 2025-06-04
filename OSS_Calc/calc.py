import tkinter as tk
import random

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x400")

        self.expression = ""

        # 입력창
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        self.button_widgets = []

        # 버튼 생성
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['Theme', '=']
        ]

        for row in buttons:
            frame = tk.Frame(root)
            frame.pack(expand=True, fill="both")
            for char in row:
                btn = tk.Button(
                    frame,
                    text=char,
                    font=("Arial", 18),
                    command=lambda ch=char: self.on_click(ch)
                )
                btn.pack(side="left", expand=True, fill="both")

    def on_click(self, char):
        if char == 'C':
            self.expression = ""
        elif char == '=':
            try:
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "에러"
        elif char == 'Theme':  # Theme 버튼 처리 추가
            self.change_theme()
        else:
            self.expression += str(char)

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)

    # 테마 변경 함수 추가
    def change_theme(self):
        bg_color = self.random_color()
        btn_color = self.random_color()

        self.root.configure(bg=bg_color)
        self.entry.configure(bg=bg_color, fg='black')

        for btn in self.button_widgets:
            btn.configure(bg=btn_color, fg='black')

    # 랜덤 색상 생성 함수 추가
    def random_color(self):
        r = lambda: random.randint(100, 255)
        return f'#{r():02x}{r():02x}{r():02x}'

