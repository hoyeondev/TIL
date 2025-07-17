import tkinter as tk
import time
import random


'''
이진 검색 gui 시뮬레이터
#사용 방법#
1. 프로그램 실행
2. 검색을 원하는 숫자 input창에 입력
3. 검색 버튼 클릭
'''

class BinarySearchVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("이진 검색 시뮬레이터")

        self.label = tk.Label(root, text="검색하기 위한 숫자를 입력하세요:")
        self.label.pack(pady=10)
        self.label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.search_button = tk.Button(root, text="검색", command=self.start_search)
        self.search_button.pack(pady=10)
        self.search_button.pack()

        self.canvas = tk.Canvas(root, width=620, height=100)
        self.canvas.pack(pady=20)

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

        #self.array = list(range(1, 21)) 
        self.array = sorted(random.sample(range(1, 101), 20))
        self.rects = []
        self.texts = []

        self.draw_array()

    def draw_array(self):
        self.canvas.delete("all")
        self.rects.clear()
        self.texts.clear()

        for i, val in enumerate(self.array):
            x0 = 30 * i + 10
            y0 = 20
            x1 = x0 + 25
            y1 = 70
            rect = self.canvas.create_rectangle(x0, y0, x1, y1, fill="white")
            text = self.canvas.create_text((x0+x1)//2, (y0+y1)//2, text=str(val))
            self.rects.append(rect)
            self.texts.append(text)

    def highlight(self, index, color):
        self.canvas.itemconfig(self.rects[index], fill=color)
        self.root.update()
        time.sleep(0.5)

    def start_search(self):
        try:
            target = int(self.entry.get())
        except ValueError:
            self.result_label.config(text="Please enter a valid integer.")
            return

        low = 0
        high = len(self.array) - 1

        self.draw_array()
        self.result_label.config(text="")
        o_num = [1, 3, 6, 7, 8, 0]
        n_num = [2, 4, 5, 9]
        last_digit = target % 10

        while low <= high:
            mid = (low + high) // 2

            self.highlight(mid, "yellow")

            if self.array[mid] == target:
                self.highlight(mid, "lightgreen")
                #self.result_label.config(text=f"Found {target} at index {mid}.")

                if last_digit in o_num:
                    self.result_label.config(text=f"{target}은 {mid+1}번째에 있습니다.")
                elif last_digit in n_num:
                    self.result_label.config(text=f"{target}는 {mid+1}번째에 있습니다.")
                return
            elif self.array[mid] < target:
                for i in range(low, mid+1):
                    self.highlight(i, "lightgray")
                low = mid + 1
            else:
                for i in range(mid, high+1):
                    self.highlight(i, "lightgray")
                high = mid - 1
                
        if last_digit in o_num:
            self.result_label.config(text=f"{target}을 찾을 수 없습니다.")
        elif last_digit in n_num:
            self.result_label.config(text=f"{target}를 찾을 수 없습니다.")

if __name__ == "__main__":
    root = tk.Tk()
    app = BinarySearchVisualizer(root)
    root.mainloop()

