#Import the required libraries
from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image

#Create an instance of tkinter frame
win = Tk()
hello = "hello"
#Set the geometry of frame
win.geometry("1200x600")

#Create a frame
frame = Frame(win)
frame.pack(side="top", expand=True, fill="both")


def draw_header():
    my_img = ImageTk.PhotoImage(Image.open("LE_Logo.png"))  # LE Logo Resize
    le_logo = Label(frame, width="500px", aght="100px", image="LE_Logo.png", position="0,0").pack()
    app_label = Label(frame, width="500px", height="100px", position="0,600").pack()



#a function that clears everything of the page, make sure to only define one window and frame
def clear_frame():
    for widgets in frame.winfo_children():
        widgets.destroy()


def main_page():
    clear_frame()
    draw_header()
    main_name = Label(frame, text='main page', font=('nunito', 28), background='grey', foreground='black').pack(pady=20)
    to_settings_page = Button(frame, text='settings', command=settings_page).pack(pady=20)


def settings_page():
    clear_frame()
    settings_name = Label(frame, text='settings page', font=('nunito', 28), background='grey', foreground='black').\
        pack(pady=20)
    to_main_page = Button(frame, text='main menu', command=main_page).pack(pady=20)


main_page()


win.mainloop()