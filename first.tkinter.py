'''# .set just means that you're giving it a value-

        self.varFName.set('Bob')
        self.varLName.set('Smith')
'''
# .get retrieves the info you've set.. 
'''
        print(self.varFName.get())
        print(self.varLName.get())'''

# creating a textbox using 'txt'.. Entry() is built in to tkinter.
'''self.txtFName = Entry(self.master,text=self.varFName, font=('Helvetica', 16), fg='black', bg='lightblue')
        self.txtFName.pack()
        
        self.txtLName = Entry(self.master,text=self.varLName, font=('Helvetica', 16), fg='black', bg='lightblue')
        self.txtLName.pack()
# above, 'pack' asks to just pack the graphics in. 'grid is a more specific way to design the 'wigdets'.'''




import tkinter
from tkinter import *

#this creates a window and calls it 'self.master'

class ParentWindow(Frame):
    def __init__(self,master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width=True, height=True)
        self.master.geometry('{}x{}'.format(700,400))
        self.master.title('Learning Tkinter!')
        self.master.config(bg='#ff7f50')


# instantiating is calling the variable by mentioning it with parethesis like StringVar()
# for all the variables, you name them then invoke the name you give it. like this-

        self.varFName = StringVar()
        self.varLName = StringVar()
        

        self.lblFName = Label(self.master,text='First Name', font=("Helvetica", 16), fg='black', bg='#ff7f50' )
        self.lblFName.grid(row=0, column=0,padx=(10,0),pady=(10,0))
        
        self.lblLName = Label(self.master,text='Last Name', font=("Helvetica", 16), fg='black', bg='#ff7f50' )
        self.lblLName.grid(row=1, column=0)


        self.txtFName = Entry(self.master,text=self.varFName, font=('Helvetica', 16), fg='black', bg='white')
        self.txtFName.grid(row=0, column=1)
        
        self.txtLName = Entry(self.master,text=self.varLName, font=('Helvetica', 16), fg='black', bg='white')
        self.txtLName.grid(row=1, column=1)

        self.btnSubmit = Button(self.master, text="Submit")
        self.btnSubmit.grid(row=2, column=1, sticky=NE, pady=10)

# colspan=1 means that the column is 1 column thick.. tk also includes 'sticky' but with cardinal directions!


if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
