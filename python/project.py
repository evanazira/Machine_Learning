from os.path import exists
###########################################################################################
def keyboardInput (datatype, caption, errorMessage, defaultValue = None):
    value = None
    isInvalid = True
    while (isInvalid):
        try:
            if defaultValue==None:
                value = datatype(input(caption))
            else:
                value = (input(caption))
                if value.strip()=="":
                    value = defaultValue
                else:
                    value = datatype(value)
        except:
            print(errorMessage)

        else:
            isInvalid = False

    return value
#-----------------------------------------------------------------------------#

def doMenu(filename):
    choice = -1

    while (choice != 0):
        print("\n\n")
        print("================================")
        print("| 0 - Exit                     |")
        print("| 1 - Create Car Insurance     |")
        print("| 2 - Create Drivers Insurance |")
        print("| 3 - Insurance Claim          |")
        print("| 4 - Print Receipt            |")
        print("================================")
        choice = keyboardInput(int, "Choice [0, 1, 2, 3, 4]: ", "Choice must be integer")
        print("\n\n")

        if choice== 0:
            print("Thank you for using our system")
        elif(choice==1):
            carInsurance(filename)
        elif(choice==2):
            driversInsurance(filename)
        elif(choice==3):
            insuranceClaim(filename)
        elif(choice==3):
             printReceipt(filename)

#----------------------------------------------------------------------------#

def open_txt_files(filename):
    try:
        with open(filename,'r') as file:
            content = file.read()
            print(f"Contents of {filename}:")
            print(content)
    except FileNotFoundError:
        print(f"File{filename} is not found")
    except Exception as e:
        print(f"ErrorL {e}")

