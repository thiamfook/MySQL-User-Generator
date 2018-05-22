from tkinter import *
import tkinter.messagebox as box

def generateScript(Event):
    if validateInputs():
        print("Generating...")
        print("CREATE USER '" + txtUser.get() + "'@'" + txtHost.get()+ "' IDENTIFIED BY '" + txtPassword.get() + "';")

def terminateProg(Event):
    exit()
    
def validateInputs():
    if len(txtUser.get()) == 0:
        box.showerror("Error", "Please fill in User Name")
        txtUser.focus()
        return False
    if len(txtPassword.get()) < 6:
        box.showerror("Error", "Please fill in a valid Password")
        txtPassword.focus()
        return False
    return True

# Defines the layout
root = Tk()
topFrame = Frame(root)
topFrame.pack()
permissionFrame = Frame(root)
permissionFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

# Get user info
lblUser = Label(topFrame, text="User name:")
txtUser = Entry(topFrame, width=10)
lblUser.grid(row=0, sticky=E)
txtUser.grid(row=0, column=1, sticky=W)
lblAt = Label(topFrame, text="@")
lblAt.grid(row=0,column=2, sticky=W)
txtHost = Entry(topFrame, width=15)
txtHost.grid(row=0, column=3, sticky=W)

lblPassword = Label(topFrame, text="Password:")
txtPassword = Entry(topFrame, width=20)
lblPassword.grid(row=1, sticky=E)
txtPassword.grid(row=1, column=1, columnspan=3, sticky=W)

# Get user permissions
lblPermissions = Label(permissionFrame, text="Permissions:")
lblPermissions.grid(row=0,columnspan=4, sticky=W)
chkSelect = Checkbutton(permissionFrame, text="SELECT")
chkSelect.grid(row=1, column=0)
chkInsert = Checkbutton(permissionFrame, text="INSERT")
chkInsert.grid(row=1, column=1)
chkUpdate = Checkbutton(permissionFrame, text="UPDATE")
chkUpdate.grid(row=1, column=2)
chkDelete = Checkbutton(permissionFrame, text="DELETE")
chkDelete.grid(row=1, column=3)
chkExecute = Checkbutton(permissionFrame, text="EXECUTE")
chkExecute.grid(row=1, column=3)

# action buttons
btnGenerate = Button(bottomFrame, text="Generate", fg="blue")
btnGenerate.bind("<Button-1>", generateScript)
btnCancel = Button(bottomFrame, text="Cancel", fg="red")
btnCancel.bind("<Button-1>", terminateProg)

btnGenerate.pack(side=LEFT)
btnCancel.pack(side=RIGHT)

# Initialization 
txtUser.focus()
root.title = "MySQL Create User Script Generator"
root.mainloop()

