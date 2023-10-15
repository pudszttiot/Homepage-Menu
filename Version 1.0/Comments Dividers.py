# ============================== IMPORTS =====================================
from tkinter import *
import pyqrcode
import png
from pyqrcode import QRCode

# ============================== TKINTER SETUP ==============================
root = Tk()
root.title("QR Code Generator App")

# Window dimensions and position
width = 400
height = 280
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)

# ============================== VARIABLES ===================================
qrname = StringVar()

# ============================== FUNCTIONS ===================================
# Function to generate QR code
def generate(event=None):
    s = qrname.get()
    url = pyqrcode.create(s)
    r = s[0:-4]
    url.svg("{}.svg".format(r), scale=8)

# ============================== FRAMES ======================================
# Frame for the top part of the window
Top = Frame(root, bd=2, relief=RIDGE)
Top.pack(side=TOP, fill=X)

# Frame for the form and input elements
Form = Frame(root, height=200)
Form.pack(side=TOP, pady=20)

# ============================== LABELS =====================================
lbl_title = Label(Top, text="QR Code Generator App", font=('arial', 15))
lbl_title.pack(fill=X)

lbl_qrurl = Label(Form, text="Enter URL:", font=('arial', 14), bd=15)
lbl_qrurl.grid(row=0, sticky="e")

# ============================== ENTRY WIDGETS =============================
qrurl = Entry(Form, textvariable=qrname, font=(14))
qrurl.grid(row=0, column=1)

# ============================== BUTTON WIDGETS =============================
btn_generate = Button(Form, text="Generate", width=45, command=generate)
btn_generate.grid(pady=25, row=2, columnspan=2)
btn_generate.bind('<Return>', generate)

# ============================== MAIN LOOP ===================================
if __name__ == '__main__':
    root.mainloop()
