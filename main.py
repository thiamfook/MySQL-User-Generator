from tkinter import *
import tkinter.messagebox as box

def validateInputs():
    if len(txtDB.get()) == 0:
        box.showerror("Error", "Please fill in Datavase Name")
        txtDB.focus()
        return False
    if len(txtUser.get()) == 0:
        box.showerror("Error", "Please fill in User Name")
        txtUser.focus()
        return False
    if len(txtPassword.get()) < 6:
        box.showerror("Error", "Please fill in a valid Password")
        txtPassword.focus()
        return False
    return True

def generateScript(Event):
    if validateInputs():
        print("Generating...")
        print("CREATE USER '" + txtUser.get() + "'@'" + txtHost.get()+ "' IDENTIFIED BY '" + txtPassword.get() + "';")
        permissionList = list()
        for key in privilegeDic:
            if privilegeVal[key].get():
                permissionList.append(key)
        if len(permissionList) > 0:
            print("GRANT " + ', '.join(permissionList) + " ON '" + txtDB.get() + "'.* TO '" + txtUser.get() + "'@'" + txtHost.get()+ "';")

def terminateProg(Event):
    exit()
    
# Permissions available
privilegeDic = {
    'SELECT': 1,
    'INSERT': 0,
    'UPDATE': 0,
    'DELETE': 0,
    'EXECUTE': 0
}

# Defines the layout
root = Tk()
topFrame = Frame(root)
topFrame.pack()
privilegeFrame = Frame(root)
privilegeFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

# Get user info
lblDB = Label(topFrame, text="Database:")
lblDB.grid(row=0, sticky=E)
txtDB = Entry(topFrame, width=15)
txtDB.grid(row=0, column=1, columnspan=3, sticky=W)
lblUser = Label(topFrame, text="User name:")
txtUser = Entry(topFrame, width=10)
lblUser.grid(row=1, sticky=E)
txtUser.grid(row=1, column=1, sticky=W)
lblAt = Label(topFrame, text="@")
lblAt.grid(row=1,column=2, sticky=W)
txtHost = Entry(topFrame, width=15)
txtHost.grid(row=1, column=3, sticky=W)

lblPassword = Label(topFrame, text="Password:")
txtPassword = Entry(topFrame, width=20)
lblPassword.grid(row=2, sticky=E)
txtPassword.grid(row=2, column=1, columnspan=3, sticky=W)

# Get user privileges
lblPrivileges = Label(privilegeFrame, text="Privileges:")
lblPrivileges.grid(row=0,columnspan=4, sticky=W)

# Draw check boxes of privileges
colCount = 0
privilegeVal = dict()
for key in privilegeDic:
    #print(key, '==', privilegeDic[key])
    privilegeVal[key] = IntVar()
    chkPermission = Checkbutton(privilegeFrame, text=key, variable=privilegeVal[key])
    chkPermission.grid(row=1, column=colCount, sticky=W)
    colCount += 1

# action buttons
btnGenerate = Button(bottomFrame, text="Generate", fg="blue")
btnGenerate.bind("<Button-1>", generateScript)
btnCancel = Button(bottomFrame, text="Cancel", fg="red")
btnCancel.bind("<Button-1>", terminateProg)

btnGenerate.pack(side=LEFT)
btnCancel.pack(side=RIGHT)

# Initialization 
txtDB.focus()
root.mainloop()
