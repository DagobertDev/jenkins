from tkinter import *
from tkinter.font import Font

from PIL import ImageTk, Image
import jenkins

root = Tk()

canvas = Canvas(root, height=500, width=500)
canvas.pack()


root.title("Jenkins - V1")
root.iconbitmap("../images/Jenkins_Icon.ico")


sentence_label = Label(root, text="Task", borderwidth=2, relief="solid", bg="#858585")
sentence_label.config(height=5, width=70)
sentence_label.pack()
sentence_label.place(x=5, y=165)

term_label = Label(root, text="Term", borderwidth=2, relief="solid", bg="#858585")
term_label.config(height=5, width=30)
term_label.pack()
term_label.place(x=5, y=280)


output_label = Label(root, text="Result", borderwidth=2, relief="solid", bg="#858585")
output_label.config(height=5, width=30)
output_label.pack()
output_label.place(x=282, y=280)


def update_labels():
    result = jenkins.recognize_input()
    sentence_label.config(text=result["sentence"])
    term_label.config(text=result["term"])
    output_label.config(text=result["result"])


boldButton = Font(size=10, weight="bold")


start_button = Button(root, text="Click on me,\n" "to tell me something!", font=boldButton,
                      borderwidth=2, relief="solid", bg="#6CA6CD", command=lambda: update_labels())
start_button.config(height=7, width=60)
start_button.place(x=5, y=20)

speaker = ImageTk.PhotoImage(Image.open("../images/Lautsprecher2.png"))
speaker_label = Label(root, image=speaker)
speaker_label.place(x=380, y=50)


end_button = Button(root, text="Exit!", font=boldButton,
                    borderwidth=2, relief="solid", bg="#6CA6CD", command=root.destroy)
end_button.config(height=7, width=60)
end_button.place(x=5, y=378)

exitImage = ImageTk.PhotoImage(Image.open("../images/exit4.png"))
exitImage_label = Label(root, image=exitImage)
exitImage_label.place(x=380, y=415)

root.mainloop()
