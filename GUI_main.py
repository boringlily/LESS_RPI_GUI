# Import the required libraries
from tkinter import *
from PIL import ImageTk, Image

# env variable definitions
window_width = 1024
window_height = 550
# Create an instance of tkinter frame
win = Tk()
# win.attributes('-fullscreen', True)
win.configure(bg='white')
win.title("Substation Technical Training Simulator")
win.geometry(f"{window_width}x{window_height}")


def draw_header():
    global logo_img
    logo_img = ImageTk.PhotoImage(Image.open('./UI/logo.jpg'))  # Lakeland Electric Logo

    global UI_image
    UI_image = ImageTk.PhotoImage(Image.open('./UI/HeaderTextBox.png'))  # Rounded corner label template

    Label(win, image=logo_img).place(x=0, y=14)
    Label(win, image=UI_image, text="Substation Technical \n Training Simulator", font=('graphik', 30, 'bold'),
          foreground="white", compound="center").place(x=512, y=14)


def draw_footer(page_name, back_to): # back_to can be: quit, main, preset
    footer = Frame(win, bg="#c4c4c4", width='1024', height=100).place(x=0, y=500)
    Label(footer, text=f'{page_name}', font=('nunito', 22), foreground="black", bg="#c4c4c4", justify='center').\
        place(x=450, y=507)

    if back_to == 'quit':
        Button(footer, text='Quit', font=('nunito', 22), fg="black", bg="#c4c4c4", justify='center',
               command=close_app).place(x=39, y=507)
        Button(footer, text='Settings', font=('nunito', 22), fg="black", bg='#c4c4c4', justify='center',
               command=settings_page).place(x=893, y=507)
    elif back_to == 'main':
        Button(footer, text='Back', font=('nunito', 22), fg="black", bg="#c4c4c4", justify='center',
               command=main_page).place(x=39, y=507)
        # Button(footer, text='Settings', font=('nunito', 22), fg="black", bg='#c4c4c4', justify='center', command=settings_page).place(x=893, y=507)
    elif back_to == 'preset':
        Button(footer, text='Back', font=('nunito', 22), fg="black", bg="#c4c4c4", justify='center',
               command=preset_page).place(x=39, y=507)
        Button(footer, text='to main', font=('nunito', 22), fg="black", bg='#c4c4c4', justify='center',
               command=settings_page).place(x=893, y=507)


# a function that clears everything of the page, make sure to only define one window and frame
def clear_body_frame():
    for widgets in win.winfo_children():
        widgets.destroy()


def close_app():
    quit()


def main_page():
    clear_body_frame()
    draw_header()
    draw_footer("Main Menu", "quit")

    global main_button_img
    main_button_img = ImageTk.PhotoImage(Image.open('./UI/Large_Button.jpg'))

    Button(win, image=main_button_img, text='Preset Faults', font=('nunito', 30, 'bold'),
           compound='center', foreground='white', command=preset_page).place(x=324, y=175)
    Button(win, image=main_button_img, text='Manual Control', font=('nunito', 30, 'bold'),
           compound='center', foreground='white').place(x=324, y=275)


def settings_page():
    clear_body_frame()
    draw_header()
    draw_footer('Settings', 'main')


def preset_page():
    clear_body_frame()
    draw_header()
    draw_footer('Presets', 'main')
    _x, _y = 45, 200
    y_spacing = 50
    x_spacing = 73
    global fault_img
    fault_img = ImageTk.PhotoImage(Image.open('./UI/Fault_Blue.jpg'))
    Button(win, image=fault_img, text='1', font=('nunito', 30, 'bold'),
           compound='center', foreground='white', command=fault1_page).place(x=_x, y=_y)


def fault1_page():
    clear_body_frame()
    draw_header()
    draw_footer('Fault #1', 'preset')




main_page()

win.mainloop()
