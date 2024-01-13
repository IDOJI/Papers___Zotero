import tkinter as tk

def on_button_click():
    print("버튼이 클릭되었습니다!")

# 메인 윈도우 생성
root = tk.Tk()
root.title("간단한 GUI 프로그램")

# 버튼 위젯 생성 및 배치
button = tk.Button(root, text="클릭하세요", command=on_button_click)
button.pack()

# 이벤트 루프 시작
root.mainloop()
