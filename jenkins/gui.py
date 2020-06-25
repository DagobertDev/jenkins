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


input_label = Label(root, text="Task", borderwidth=2, relief="solid", bg="#858585")
input_label.config(height=10, width=30)
input_label.pack()
input_label.place(x=5, y=180)


output_label = Label(root, text="Result", borderwidth=2, relief="solid", bg="#858585")
output_label.config(height=10, width=30)
output_label.pack()
output_label.place(x=282, y=180)


def update_labels():
    result = jenkins.recognize_input()
    input_label.config(text=result["term"])
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
