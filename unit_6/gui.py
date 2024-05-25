import tkinter as tk
from PIL import ImageTk, Image
import os

def onButtonClick(root):
    img_path = "/home/goodman/school/next.py/unit_6/rosh-tzipor-park.jpg"
    img = ImageTk.PhotoImage(Image.open(img_path))
    panel = tk.Label(root, image=img)
    panel.image = img

    panel.pack(side="bottom", fill="both", expand="yes")


def main():
    root = tk.Tk()
    root.title("tk")

    label = tk.Label(root, text="Hello, World?")
    label.pack()

    button = tk.Button(root, text="Click me!", command=lambda: onButtonClick(root))
    button.pack()

    root.mainloop()


if __name__ == '__main__':
    main()