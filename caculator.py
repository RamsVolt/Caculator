import tkinter as tk

calculation = ""

def add(x):
    global calculation
    calculation += str(x)
    text_result.delete(1.0,"end")
    text_result.insert(1.0,calculation)

def evaluate():
    global calculation
    try:
        result=str(eval(calculation))
        calculation = ""
        text_result.delete(1.0,"end")
        text_result.insert(1.0,result)
    except:
        clear()
        text_result.insert(1.0, "Error")
        pass

def clear():
    global calculation
    calculation = ""
    text_result.delete(1.0,"end")

def percent():
    global calculation
    result=eval(calculation) / 100
    calculation = str(result)
    text_result.delete(1.0,"end")
    text_result.insert(1.0,calculation)
    
       



root = tk.Tk()
root.geometry("300x250")

text_result = tk.Text(root, height=2, width=16, font=("Arial", 25))
text_result.grid(columnspan=5)

root.title("Kakulator")

btn_1 = tk.Button(root, text=1, command=lambda:add(1), width=5,font=("Arial", 12))
btn_1.grid(row=2,column=1)
btn_2 = tk.Button(root, text=2, command=lambda:add(2), width=5,font=("Arial", 12))
btn_2.grid(row=2,column=2)
btn_3 = tk.Button(root, text=3, command=lambda:add(3), width=5,font=("Arial", 12))
btn_3.grid(row=2,column=3)
btn_4 = tk.Button(root, text=4, command=lambda:add(4), width=5,font=("Arial", 12))
btn_4.grid(row=3,column=1)
btn_5 = tk.Button(root, text=5, command=lambda:add(5), width=5,font=("Arial", 12))
btn_5.grid(row=3,column=2)
btn_6 = tk.Button(root, text=6, command=lambda:add(6), width=5,font=("Arial", 12))
btn_6.grid(row=3,column=3)
btn_7 = tk.Button(root, text=7, command=lambda:add(7), width=5,font=("Arial", 12))
btn_7.grid(row=4,column=1)
btn_8 = tk.Button(root, text=8, command=lambda:add(8), width=5,font=("Arial", 12))
btn_8.grid(row=4,column=2)
btn_9 = tk.Button(root, text=9, command=lambda:add(9), width=5,font=("Arial", 12))
btn_9.grid(row=4,column=3)
btn_0 = tk.Button(root, text=0, command=lambda:add(0), width=5,font=("Arial", 12))
btn_0.grid(row=5,column=1)
plus = tk.Button(root, text="+", command=lambda:add("+"), width=5,font=("Arial", 12))
plus.grid(row=2,column=4)
minus = tk.Button(root, text="-", command=lambda:add("-"), width=5,font=("Arial", 12))
minus.grid(row=3,column=4)
kali = tk.Button(root, text="*", command=lambda:add("*"), width=5,font=("Arial", 12))
kali.grid(row=4,column=4)
bagi = tk.Button(root, text="/", command=lambda:add("/"), width=5,font=("Arial", 12))
bagi.grid(row=5,column=4)
open = tk.Button(root, text="(", command=lambda:add("("), width=5,font=("Arial", 12))
open.grid(row=5,column=2)
close = tk.Button(root, text=")", command=lambda:add(")"), width=5,font=("Arial", 12))
close.grid(row=5,column=3)
equal = tk.Button(root, text="=", command=evaluate, width=5,font=("Arial", 12))
equal.grid(row=6,column=1, columnspan=3)
btn_clear = tk.Button(root, text="C", command=clear, width=5,font=("Arial", 12))
btn_clear.grid(row=6,column=1)
btn_percent = tk.Button(root, text="%", command=percent, width=5,font=("Arial", 12))
btn_percent.grid(row=6,column=3)

root.mainloop()
