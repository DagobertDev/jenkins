from tkinter import *
from PIL import ImageTk, Image
import speech_to_text
import jenkins

root = Tk()

canvas = Canvas(root, height=500, width=500)
canvas.pack()


root.title("Jenkins - V1")
root.iconbitmap("C:\\Users\\Vinci\\Jenkins_Icon.ico")


def execute_application(task: str):
    if task.lower() == "jenkins stop":
        root.destroy


def create_label(task: str):
    output = Label(root, text=task, borderwidth=2, relief="solid", bg="#858585")
    output.config(height=10, width=70)
    output.pack()
    output.place(x=5, y=180)


start_button = Button(root, text="Click on me, to tell me something!",
                      borderwidth=2, relief="solid", bg="#6CA6CD", command=lambda:
[jenkins.main, create_label(task=speech_to_text.get_input()), execute_application(task=speech_to_text.get_input())])
start_button.config(height=7, width=69)
start_button.place(x=5, y=20)

speaker = ImageTk.PhotoImage(Image.open("C:\\Users\\Vinci\\Lausprecher2.png"))
speaker_label = Label(root, image=speaker)
speaker_label.place(x=380, y=50)


end_button = Button(root, text="Jenkins schließen!",
                    borderwidth=2, relief="solid", bg="#6CA6CD", command=root.destroy)
end_button.config(height=7, width=69)
end_button.place(x=5, y=380)

exitImage = ImageTk.PhotoImage(Image.open("C:\\Users\\Vinci\\exit4.png"))
exitImage_label = Label(root, image=exitImage)
exitImage_label.place(x=380, y=415)

root.mainloop()
