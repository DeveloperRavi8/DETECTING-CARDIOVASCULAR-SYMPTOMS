from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Heart Dignostic Report")
root.geometry("600x600")
root.configure(bg="pink")

def get_report():
    score = 0
    
    print(question1_radiobutton.get())
    if(question1_radiobutton.get() == "Yes"):
        score = score + 10
    if(question2_radiobutton.get() == "Yes"):
        score = score + 10
    if(question3_radiobutton.get() == "Yes"):
        score = score + 10
    if(question4_radiobutton.get() == "Yes"):
        score = score + 10
    if(question5_radiobutton.get() == "Yes"):
        score = score + 10
            
    if(score <= 10):
        messagebox.showinfo(title="Report", message="You don't need to visit a doctor")
    elif(score > 10 and score <= 30):
        messagebox.showinfo(title="Report", message="You might perhaps have to visit a doctor")
    else:
        messagebox.showinfo(title="Report", message="I strongly advise you to visit doctor")

question1_label = Label(root, background="pink", text="Do you experience shortness of breath during routine activities?")
question1_label.pack()

question1_radiobutton = StringVar(value="0")
question1_r1 = Radiobutton(root, background="pink", text='Yes', variable=question1_radiobutton, value="Yes")
question1_r1.pack()
question1_r2 = Radiobutton(root, background="pink", text="No", variable=question1_radiobutton, value="No")
question1_r2.pack()

question2_label = Label(root, background="pink", text="Do you have swlling in the feet/ankles/legs (shoes feel tighter) or abdomen?")
question2_label.pack()

question2_radiobutton = StringVar(value="0")
question2_r1 = Radiobutton(root, background="pink", text='Yes', variable=question2_radiobutton, value="Yes")
question2_r1.pack()
question2_r2 = Radiobutton(root, background="pink", text="No", variable=question2_radiobutton, value="No")
question2_r2.pack()

question3_label = Label(root, background="pink", text="Do you experience shortness of breath while at rest/lying down?")
question3_label.pack()

question3_radiobutton = StringVar(value="0")
question3_r1 = Radiobutton(root, background="pink", text='Yes', variable=question3_radiobutton, value="Yes")
question3_r1.pack()
question3_r2 = Radiobutton(root, background="pink", text="No", variable=question3_radiobutton, value="No")
question3_r2.pack()

question4_label = Label(root, background="pink", text="Do you experience shortness of breath while at rest/lying down?")
question4_label.pack()

question4_radiobutton = StringVar(value="0")
question4_r1 = Radiobutton(root, background="pink", text='Yes', variable=question4_radiobutton, value="Yes")
question4_r1.pack()
question4_r2 = Radiobutton(root, background="pink", text="No", variable=question4_radiobutton, value="No")
question4_r2.pack()

question5_label = Label(root, background="pink", text="Do you experience persistent wheezing/coughing that produces white or pink blood tinged musus?")
question5_label.pack()

question5_radiobutton = StringVar(value="0")
question5_r1 = Radiobutton(root, background="pink", text='Yes', variable=question5_radiobutton, value="Yes")
question5_r1.pack()
question5_r2 = Radiobutton(root, background="pink", text="No", variable=question5_radiobutton, value="No")
question5_r2.pack()



button = Button(root, text="Get Report", command=get_report)
button.pack()

root.mainloop()