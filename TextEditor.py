from tkinter import filedialog
from tkinter import *

def Quit(eval):
	global root
	root.destroy()
	
def SaveFile(eval):
	fn = filedialog.asksaveasfilename(initialdir = "/", title = "Select file", filetypes = (("text files", "*.txt"), ("all files", "*.*")))
    
def LoadFile(eval): 
    fn = filedialog.Open(root, filetypes = [('*.txt files', '.txt')]).show()

root = Tk()

panelFrame = Frame(root, height = 40, bg = 'Gray')
textFrame = Frame(root, height = 340, width = 600)

panelFrame.pack(side = 'top', fill = 'x')
textFrame.pack(side = 'bottom', fill = 'both')

textbox = Text(textFrame, font = 'Arial 14', wrap = 'word')
scrollbar = Scrollbar(textFrame)

textbox.pack(side = 'left', fill = 'both', expand = 1)
scrollbar.pack(side = 'right', fill = 'y')

loadButton = Button(panelFrame, text = 'Load file')
saveButton = Button(panelFrame, text = 'Save file')
quitButton = Button(panelFrame, text = 'Quit')

loadButton.place(x = 10, width = 60, height = 40)
saveButton.place(x = 80, width = 60, height = 40)
quitButton.place(x = 150, width = 60, height = 40)

loadButton.bind('<Button-1>', LoadFile)
saveButton.bind('<Button-1>', SaveFile)
quitButton.bind('<Button-1>', Quit)

root.mainloop()