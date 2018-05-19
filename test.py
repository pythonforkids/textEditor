from tkinter import *

def NewWindow():
	fq = Toplevel(root)
	fq.title('Новое окно')

	label1 = Label(fq, text = 'Новое окно\n\
*Здесь куча полезного текста.\n\
* Ошибки никогда не должны замалчиваться.\n\
* Явное лучше неявного.\n\n')
	label1.pack()

root = Tk()

leftFrame = Frame(root, bg = 'blue', bd = 5)
rightFrame = Frame(root, bg = 'red', bd = 5)
botFrame = Frame(root, bd = 5)

leftFrame.place(x = 300, y = 0, height = '500', width = '300')
rightFrame.place(x = 600, y =0, height = '500', width = '300')
botFrame.place(x = 0, y = 0, height = '500', width = '300')

Button1p = Button(botFrame, text = '1p')
Button2p = Button(botFrame, text = '2p', command = NewWindow)
Button3p = Button(botFrame, text = '3p')
Button4p = Button(botFrame, text = '4p')
Button5p = Button(botFrame, text = '5p')

Button1 = Button(leftFrame, text = '1')
Button2 = Button(leftFrame, text = '2')
Button3 = Button(leftFrame, text = '3')
Button4 = Button(leftFrame, text = '4')
Button5 = Button(leftFrame, text = '5')

Button1g = Button(rightFrame, text = '1g')
Button2g = Button(rightFrame, text = '2g')
Button3g = Button(rightFrame, text = '3g')
Button4g = Button(rightFrame, text = '4g')
Button5g = Button(rightFrame, text = '5g')

Button1p.place(x = 100, y = 100)
Button2p.place(x = 20, y = 30)
Button3p.place(x = 30, y = 70)
Button4p.place(x = 40, y = 90)
Button5p.place(x = 50, y = 110)

Button1.pack(side = 'left')
Button2.pack(side = 'left')
Button3.pack(side = 'top')
Button4.pack(side = 'right')
Button5.pack(side = 'bottom')

Button1g.grid(row = 0, column = 0, columnspan = 3)
Button2g.grid(row = 1, column = 1)
Button3g.grid(row = 1, column = 2)
Button4g.grid(row = 2, column = 2, rowspan = 2)
Button5g.grid(row = 4, rowspan = 2, columnspan = 3)

root.mainloop()