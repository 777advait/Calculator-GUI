from tkinter import *

root = Tk()
root.title("Calculator by Advait Jadhav")

buttons = [
'7',  '8',  '9',  '*',  'C',
'4',  '5',  '6',  '÷',  'π',
'1',  '2',  '3',  '-',  'x^2',
'0',  '.',  '+',  '=',  '√x' ]

# set up GUI
row = 1
col = 0
for i in buttons:
    button_style = 'raised'
    action = lambda x = i: click_event(x)
    Button(root, text = i, width = 5, height = 5, bg = "#4F4F4F", fg = "#D6DFE0", bd = 3, relief = button_style, command = action) \
		.grid(row = row, column = col, sticky = 'nesw', )
    col += 1
    if col > 4:
        col = 0
        row += 1

display = Entry(root, width = 22, font = "Courier_Regular 18", fg = "#627E8B", bg = "#D6DFE0")
display.grid(row = 0, column = 0, pady = 15, columnspan = 5)

def click_event(key):

	# = -> calculate results
    if key == '=':
        # safeguard against integer division
        if '/' in display.get() and '.' not in display.get():
            display.insert(END, ".0")
			
        # attempt to evaluate results
        try:
            result = eval(display.get())
            display.insert(END, " = " + str(result))
        except:
            display.insert(END, "   Error, use only valid chars")
			
	# C -> clear display		
    elif key == 'C':
        display.delete(0, END)
		
    elif key == 'x^2':
        result = eval(display.get())
        display.delete(0, END)
        display.insert(END, result**2)

    elif key == '√x':
        result = eval(display.get())
        display.delete(0, END)
        display.insert(END, result**0.5)		

    elif key == 'π':
        display.insert(END, "3.14")

	# clear display and start new input		
    else:
        if '=' in display.get():
            display.delete(0, END)
        display.insert(END, key)

# RUNTIME
root.mainloop()