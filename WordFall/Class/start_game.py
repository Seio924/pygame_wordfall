from tkinter import *
import tkinter.font

root = Tk()
root.title("Word")
root.geometry("471x80+300+100") #가로 * 세로 + x좌표 + y좌표
root.resizable(False, False) #창크기 변경불가
font = tkinter.font.Font(size=50, weight="bold")
txt = Text(root, width=471, height=80, font=font)
txt.pack()
def re(n):
    enter_word = txt.get("1.0", END)
    txt.delete("1.0", "end")
root.bind("<Return>", re)
root.mainloop()