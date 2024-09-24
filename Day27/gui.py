import tkinter

window = tkinter.Tk()
window.title("My first Gui")
window.minsize(500, 300)

# label
my_label = tkinter.Label(text="I am Mahadev", font=("Arial", 24, "bold"))
# To display the text at center
my_label.pack()

window.mainloop()
