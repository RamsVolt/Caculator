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
        text_result.insert(1.0,calculation)
    except:
        clear()
        text_result.insert(1.0, "Error")
        pass

def clear():
    global calculation
    calculation = ""
    text_result.delete(1.0,"end")



root = tk.Tk()
root.geometry("300x250")

text_result = tk.Text(root, height=2, width=16, font=("Arial", 25))
text_result.grid(columnspan=5)

root.title("Kakulator")

root.mainloop()
