import tkinter as tk

if __name__ == "__main__":
    """
    """
    
    #
    # Input Window
    # #############################################################################################################

    tkFrame = tk.Tk()
    tkFrame.configure(background='grey80') 
    tkFrame.title("Name")

    # First and Lastname
    tk.Label(tkFrame, text="First Name",font=("Arial", 16),background='grey80').grid(row=0, column=0)
    tk.Label(tkFrame, text="Last Name",font=("Arial", 16),background='grey80').grid(row=1, column=0)
    tkFirstField=tk.Entry(tkFrame,font=("Arial", 24),background='grey90')
    tkFirstField.grid(row=0,column=1)
    tkLastField=tk.Entry(tkFrame,font=("Arial", 24),background='grey90')
    tkLastField.grid(row=1,column=1)

    # Enter Button
    tkEnterButtonVar = tk.IntVar()
    tkEnterButton    = tk.Button(tkFrame, text="Submit",
                                 font=("Arial", 16),
                                 bg='gray90',
                                 command=lambda:tkEnterButtonVar.set(1))
    tkEnterButton.grid(row=2, columnspan=2, pady=5)
    # tkEnterButton.place(relx=0.5, rely=0.5, anchor="c")

    #
    # Main Loop
    # #############################################################################################################
    stopped = False
    while (not stopped):
        # ask for user name
        tkFirstField.delete(0, tk.END)
        tkLastField.delete(0, tk.END)
        tkFrame.tkraise()
        tkFrame.wait_variable(tkEnterButtonVar)
        firstName = tkFirstField.get()
        lastName  = tkLastField.get()
        print("{}, {}".format(firstName,lastName))                        

# Clean up and Release handle to window
#######################################
