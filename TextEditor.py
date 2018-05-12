from tkinter import filedialog
from tkinter import *

def Quit():
	global root
	root.destroy()
	
def SaveFile():
	fn = filedialog.asksaveasfilename(initialdir = "/", title = "Select file", filetypes = (("text files", "*.txt"), ("all files", "*.*")))
    
def LoadFile(): 
    fn = filedialog.Open(root, filetypes = [('*.txt files', '.txt')]).show()

def FAQ():
	fq = Toplevel(root)
	fq.title('Справка')

	label1 = Label(fq, text = 'Дзэн Питона\n\
* Если реализацию сложно объяснить — это плохая идея.\n\
* Ошибки никогда не должны замалчиваться.\n\
* Явное лучше неявного.\n\n')
	label1.pack()

#Основное окно программы
root = Tk()
root.title('TextRedactor')

textFrame = Frame(root, height = 340, width = 600)

textFrame.pack(side = 'bottom', fill = 'both')

textbox = Text(textFrame, font = 'Arial 14', wrap = 'word')
scrollbar = Scrollbar(textFrame)

textbox.pack(side = 'left', fill = 'both', expand = 1)
scrollbar.pack(side = 'right', fill = 'y')

#Меню программы
menubar = Menu(root, bd = 1)
root.config(menu=menubar)

fileMenu = Menu(menubar)
FAQMenu = Menu(menubar)

fileMenu.add_command(label = 'Save File', command = SaveFile)
fileMenu.add_command(label = 'Load File', command = LoadFile)
fileMenu.add_separator()
fileMenu.add_command(label = "Exit", command = Quit)

FAQMenu.add_command(label = 'Documentation', command = FAQ)

menubar.add_cascade(label="File", menu = fileMenu)
menubar.add_cascade(label="Help", menu = FAQMenu)

#Панель инструментов
toolbar = Frame(root, bd = 1, relief = 'raised')
toolbar.pack(side = 'top', fill = 'x')

#eimg = PhotoImage(open('exit.png'))
path = 'images\exit.png'
exitIM = PhotoImage(path)
exitButton = Button(toolbar, relief = 'flat', command = Quit, image = exitIM)
exitButton.pack(side = 'left', padx = '2', pady = '2')

path2 = 'images\exit.png'
exitIM = PhotoImage(path2)
boldButton = Button(toolbar, relief = 'flat', image = boldIM)
boldButton.pack(side = 'left', padx = '2', pady = '2')

path3 = 'images\exit.png'
exitIM = PhotoImage(path3)
italButton = Button(toolbar, relief = 'flat', image = italIM)
italButton.pack(side = 'left', padx = '2', pady = '2')

root.mainloop()