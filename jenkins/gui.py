from tkinter import *
from tkinter.font import Font

from PIL import ImageTk, Image
import speech_to_text
import jenkins

root = Tk()

canvas = Canvas(root, height=500, width=500)
canvas.pack()


root.title("Jenkins - V1")
root.iconbitmap("../images/Jenkins_Icon.ico")


def create_label(task: str):
    output = Label(root, text=task, borderwidth=2, relief="solid", bg="#858585")
    output.config(height=10, width=70)
    output.pack()
    output.place(x=5, y=180)


boldButton = Font(size=10, weight="bold")


start_button = Button(root, text="Click on me,\n" "to tell me something!", font=boldButton,
                      borderwidth=2, relief="solid", bg="#6CA6CD", command=lambda:
[jenkins.main, create_label(task=speech_to_text.get_input())])
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
