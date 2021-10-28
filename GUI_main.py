# Import the required libraries
from tkinter import *
from PIL import ImageTk, Image

# global image variable definitions

# Create an instance of tkinter frame
win = Tk()
win.title("Substation Technical Training Simulator")
win.geometry("1024x600")


def draw_header():
    global logo_img
    logo_img = ImageTk.PhotoImage(Image.open('./UI/logo.jpg'))  # Lakeland Electric Logo

    global UI_image
    UI_image = ImageTk.PhotoImage(Image.open('./UI/HeaderTextBox.png'))  # Rounded corner label template

    Label(win, image=logo_img).place(x=0, y=14)
    Label(win, image=UI_image, text="Substation Technical \n Training Simulator", font=('graphik', 30, 'bold'),
          foreground="white", compound="center").place(x=512, y=14)


# a function that clears everything of the page, make sure to only define one window and frame
def clear_body_frame():
    for widgets in win.winfo_children():
        widgets.destroy()


def main_page():
    clear_body_frame()
    draw_header()
    global main_button_img
    main_button_img = ImageTk.PhotoImage(Image.open('./UI/Large_Button.jpg'))

    Button(win, image=main_button_img, text='Preset Faults', font=('nunito', 30, 'bold'), compound='center', foreground='white').place(x=324, y=248)
    Button(win, image=main_button_img, text='Manual Control', font=('nunito', 30, 'bold'), compound='center', foreground='white').place(x=324, y=342)



def settings_page():
    clear_body_frame()
    draw_header()
    settings_name = Label(win, text='settings page', font=('nunito', 28), background='grey', foreground='black').pack()
    to_main_page = Button(win, text='main menu', command=main_page).pack(pady=20)


main_page()

win.mainloop()
