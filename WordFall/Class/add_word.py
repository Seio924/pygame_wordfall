import os
import tkinter as tk
from pathlib import Path

def data_path(sel):
    data_path = os.path.abspath(__file__).replace("\\", "/").replace("Class/add_word.py", "")    
    if sel == 0:
        word = data_path
    elif sel == 1:
        word = data_path + "data/TOEIC.txt"
    elif sel == 2:
        word = data_path + "data/USER.txt"
    elif sel == 3:
        word = data_path + "ADD.txt"
    return word

def load_word(word):
    arr = []
    print("loading..." + word)
    with open(word) as f:
        lines = f.readlines()
    print(lines)
    for i in lines:
        if i == "\n":
            continue
        tmp = list(i.split(" "))
        arr.append([tmp[0], tmp[1].replace("\n", "")])
    return arr

def append(User, Add):
    User_word = load_word(User)
    Add_word = load_word(Add)
    f = open(User, "at")
    for i in Add_word:
        if i not in User_word:
            f.writelines(["\n"+i[0]+" ", i[1]+"\n"])
    f.close

def Input_word(path):
    root = tk.Tk()
    root.geometry("400x240")
    root.title("단어 입력기")

    def getTextInput():
        result=textExample.get("1.0", "end")
        arr = list(result.split())
        tmp = []
        for i in range(len(arr)//2):
            tmp.append([arr[i*2], arr[i*2+1]])
        f = open(path, "at")
        for i in tmp:
            f.writelines([i[0]+" ", i[1]+"\n"])
        f.close
        root.destroy()
        return
    
    def getLoad():
        root.destroy()
        return

    textExample=tk.Text(root, height=10)
    textExample.pack()
    btnRead=tk.Button(root, height=1, width=10, text="입력", command=getTextInput)
    btnLoad=tk.Button(root, height=1, width=10, text="불러오기", command=getLoad)
    btnRead.pack(side = "left")
    btnLoad.pack(side = "right")
    root.mainloop()