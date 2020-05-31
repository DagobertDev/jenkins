from tkinter import *
import speech_to_text
import tkinter.simpledialog
import tkinter.messagebox

root = Tk()


def main() -> None:
    print("Hello, I'm Jenkins. Give me a task:")

    while True:
        task = speech_to_text.get_input()
        print("I heard '", task, "'.")

        should_stop = not execute(task)

        if should_stop:
            print("Stopping now, see you soon.")
            return

        print("Please ask your next question:")


def execute(task: str) -> bool:
    """Resolves the provided task, returns whether Jenkins should continue working or not."""

    if task.lower() == "jenkins stop":
        return False

    print("I'm sorry, but i can't understand the task '", task, "'.")
    # TODO: Understand and execute task
    return True


canvas = Canvas(root, height=500, width=500)
canvas.pack()


def execute_application(task: str):
    if task.lower() == "jenkins stop":
        root.destroy


def create_label(task: str):
    output = Label(root, text=task, bg="yellow")
    output.config(height=10, width=69)
    output.place(x=5, y=180)


start_button = Button(root, text="Click on me, to tell me something!", bg="green", command=lambda: [main, create_label
(task=speech_to_text.get_input()), execute_application(task=speech_to_text.get_input())])
start_button.config(height=7, width=69)
start_button.place(x=5, y=20)

end_button = Button(root, text="end", bg="red", command=root.destroy)
end_button.config(height=7, width=69)
end_button.place(x=5, y=380)

root.mainloop()
