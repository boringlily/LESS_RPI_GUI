# Import the required libraries
from tkinter import *
from PIL import ImageTk, Image

# env variable definitions
window_width = 1024
window_height = 550
# Create an instance of tkinter frame
win = Tk()
# win.attributes('-fullscreen', True)
win.configure(background='white')
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
    footer = Frame(win, background="#c4c4c4", width='1024', height=100).place(x=0, y=500)
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
               command=main_page).place(x=893, y=507)


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

    global main_button_img
    main_button_img = ImageTk.PhotoImage(Image.open('./UI/Large_Button.jpg'))
    Button(win, image=main_button_img, text='Sequential Toggle', font=('nunito', 30, 'bold'),
           compound='center', foreground='white', command=preset_page).place(x=324, y=175)

    Button(win, image=main_button_img, text='Sequential Toggle', font=('nunito', 30, 'bold'),
           compound='center', foreground='white', command=preset_page).place(x=324, y=175)


def preset_page():
    clear_body_frame()
    draw_header()
    draw_footer('Presets', 'main')
    _x, _y = 45, 200
    y_spacing = 50 +75
    x_spacing = 73+180
    global fault_img
    fault_img = ImageTk.PhotoImage(Image.open('./UI/Fault_Blue.jpg'))
    Button(win, image=fault_img, text='1', font=('nunito', 30, 'bold'),
           compound='center', foreground='white', command=fault1_page).place(x=_x, y=_y)
    Button(win, image=fault_img, text='2', font=('nunito', 30, 'bold'),
           compound='center', foreground='white', command=fault2_page).place(x=_x+x_spacing, y=_y)
    Button(win, image=fault_img, text='3', font=('nunito', 30, 'bold'),
           compound='center', foreground='white', command=fault3_page).place(x=_x + x_spacing*2, y=_y)
    Button(win, image=fault_img, text='4', font=('nunito', 30, 'bold'),
           compound='center', foreground='white', command=fault4_page).place(x=_x + x_spacing*3, y=_y)
    Button(win, image=fault_img, text='5', font=('nunito', 30, 'bold'),
           compound='center', foreground='white', command=fault5_page).place(x=_x, y=_y+y_spacing)
    Button(win, image=fault_img, text='6', font=('nunito', 30, 'bold'),
           compound='center', foreground='white', command=fault6_page).place(x=_x+x_spacing, y=_y+y_spacing)
    Button(win, image=fault_img, text='7', font=('nunito', 30, 'bold'),
           compound='center', foreground='white', command=fault7_page).place(x=_x + x_spacing*2, y=_y+y_spacing)
    Button(win, image=fault_img, text='8', font=('nunito', 30, 'bold'),
           compound='center', foreground='white', command=fault8_page).place(x=_x + x_spacing*3, y=_y+y_spacing)


def fault1_page():
    clear_body_frame()
    draw_header()
    draw_footer('Fault #1', 'preset')

    global fault_blue
    fault_blue = ImageTk.PhotoImage(Image.open('./UI/Fault_Blue.jpg'))
    global fault_grey
    fault_grey = ImageTk.PhotoImage(Image.open('./UI/Fault_Grey.jpg'))
    step_display = Label(win, image=fault_grey, text='Step:#', font=('nunito', 30, 'bold'),
                         compound='center', foreground='#206CB9').place(x=422, y=250)
    fault1_counter = [0]
    fault1_counter[0]=0

    def fault1_counter_add():
        fault1_counter[0] +=1
        Label(win, image=fault_grey, text=f'Step: {fault1_counter[0]}', font=('nunito', 30, 'bold'),
              compound='center', foreground='#206CB9').place(x=422, y=250)

    def fault1_counter_sub():
        fault1_counter[0] -=1
        Label(win, image=fault_grey, text=f'Step: {fault1_counter[0]}', font=('nunito', 30, 'bold'),
              compound='center', foreground='#206CB9').place(x=422, y=250)


    Button(win, image=fault_blue, text='Back', font=('nunito', 30, 'bold'),
           compound='center', foreground='white', command=fault1_counter_sub).place(x=202, y=250)
    Button(win, image=fault_blue, text='Next', font=('nunito', 30, 'bold'),
           compound='center', foreground='white', command=fault1_counter_add).place(x=642, y=250)


def fault2_page():
    clear_body_frame()
    draw_header()
    draw_footer('Fault #2', 'preset')

    global fault_blue
    fault_blue = ImageTk.PhotoImage(Image.open('./UI/Fault_Blue.jpg'))
    global fault_grey
    fault_grey = ImageTk.PhotoImage(Image.open('./UI/Fault_Grey.jpg'))
    step_display = Label(win, image=fault_grey, text='Step:#', font=('nunito', 30, 'bold'),
                         compound='center', foreground='#206CB9').place(x=422, y=250)
    fault2_counter = [0]
    fault2_counter[0]=0

    def fault2_counter_add():
        fault2_counter[0] +=1
        Label(win, image=fault_grey, text=f'Step: {fault2_counter[0]}', font=('nunito', 30, 'bold'),
              compound='center', foreground='#206CB9').place(x=422, y=250)

    def fault2_counter_sub():
        fault2_counter[0] -=1
        Label(win, image=fault_grey, text=f'Step: {fault2_counter[0]}', font=('nunito', 30, 'bold'),
              compound='center', foreground='#206CB9').place(x=422, y=250)

    Button(win, image=fault_blue, text='Back', font=('nunito', 30, 'bold'),
           compound='center', foreground='white', command=fault2_counter_sub).place(x=202, y=250)
    Button(win, image=fault_blue, text='Next', font=('nunito', 30, 'bold'),
           compound='center', foreground='white', command=fault2_counter_add).place(x=642, y=250)


def fault3_page():
    clear_body_frame()
    draw_header()
    draw_footer('Fault #3', 'preset')

    global fault_blue
    fault_blue = ImageTk.PhotoImage(Image.open('./UI/Fault_Blue.jpg'))
    global fault_grey
    fault_grey = ImageTk.PhotoImage(Image.open('./UI/Fault_Grey.jpg'))
    step_display = Label(win, image=fault_grey, text='Step:#', font=('nunito', 30, 'bold'),
                         compound='center', foreground='#206CB9').place(x=422, y=250)
    fault3_counter = [0]
    fault3_counter[0] = 0

    def fault3_counter_add():
        fault3_counter[0] += 1
        Label(win, image=fault_grey, text=f'Step: {fault3_counter[0]}', font=('nunito', 30, 'bold'),
              compound='center', foreground='#206CB9').place(x=422, y=250)

    def fault3_counter_sub():
        fault3_counter[0] -=1
        Label(win, image=fault_grey, text=f'Step: {fault3_counter[0]}', font=('nunito', 30, 'bold'),
              compound='center', foreground='#206CB9').place(x=422, y=250)

    Button(win, image=fault_blue, text='Back', font=('nunito', 30, 'bold'),
           compound='center', foreground='white', command=fault3_counter_sub).place(x=202, y=250)
    Button(win, image=fault_blue, text='Next', font=('nunito', 30, 'bold'),
           compound='center', foreground='white', command=fault3_counter_add).place(x=642, y=250)


def fault4_page():
    clear_body_frame()
    draw_header()
    draw_footer('Fault #4', 'preset')

    global fault_blue
    fault_blue = ImageTk.PhotoImage(Image.open('./UI/Fault_Blue.jpg'))
    global fault_grey
    fault_grey = ImageTk.PhotoImage(Image.open('./UI/Fault_Grey.jpg'))
    step_display = Label(win, image=fault_grey, text='Step:#', font=('nunito', 30, 'bold'),
                         compound='center', foreground='#206CB9').place(x=422, y=250)
    fault4_counter = [0]
    fault4_counter[0]=0

    def fault4_counter_add():
        fault4_counter[0] +=1
        Label(win, image=fault_grey, text=f'Step: {fault4_counter[0]}', font=('nunito', 30, 'bold'),
              compound='center', foreground='#206CB9').place(x=422, y=250)

    def fault4_counter_sub():
        fault4_counter[0] -=1
        Label(win, image=fault_grey, text=f'Step: {fault4_counter[0]}', font=('nunito', 30, 'bold'),
              compound='center', foreground='#206CB9').place(x=422, y=250)


    Button(win, image=fault_blue, text='Back', font=('nunito', 30, 'bold'),
           compound='center', foreground='white', command=fault4_counter_sub).place(x=202, y=250)
    Button(win, image=fault_blue, text='Next', font=('nunito', 30, 'bold'),
           compound='center', foreground='white', command=fault4_counter_add).place(x=642, y=250)


def fault5_page():
    clear_body_frame()
    draw_header()
    draw_footer('Fault #5', 'preset')

    global fault_blue
    fault_blue = ImageTk.PhotoImage(Image.open('./UI/Fault_Blue.jpg'))
    global fault_grey
    fault_grey = ImageTk.PhotoImage(Image.open('./UI/Fault_Grey.jpg'))
    step_display = Label(win, image=fault_grey, text='Step:#', font=('nunito', 30, 'bold'),
                         compound='center', foreground='#206CB9').place(x=422, y=250)
    fault5_counter = [0]
    fault5_counter[0]=0

    def fault5_counter_add():
        fault5_counter[0] +=1
        Label(win, image=fault_grey, text=f'Step: {fault5_counter[0]}', font=('nunito', 30, 'bold'),
              compound='center', foreground='#206CB9').place(x=422, y=250)

    def fault5_counter_sub():
        fault5_counter[0] -=1
        Label(win, image=fault_grey, text=f'Step: {fault5_counter[0]}', font=('nunito', 30, 'bold'),
              compound='center', foreground='#206CB9').place(x=422, y=250)


    Button(win, image=fault_blue, text='Back', font=('nunito', 30, 'bold'),
           compound='center', foreground='white', command=fault5_counter_sub).place(x=202, y=250)
    Button(win, image=fault_blue, text='Next', font=('nunito', 30, 'bold'),
           compound='center', foreground='white', command=fault5_counter_add).place(x=642, y=250)


def fault6_page():
    clear_body_frame()
    draw_header()
    draw_footer('Fault #6', 'preset')

    global fault_blue
    fault_blue = ImageTk.PhotoImage(Image.open('./UI/Fault_Blue.jpg'))
    global fault_grey
    fault_grey = ImageTk.PhotoImage(Image.open('./UI/Fault_Grey.jpg'))
    step_display = Label(win, image=fault_grey, text='Step:#', font=('nunito', 30, 'bold'),
                         compound='center', foreground='#206CB9').place(x=422, y=250)
    fault6_counter = [0]
    fault6_counter[0]=0

    def fault6_counter_add():
        fault6_counter[0] +=1
        Label(win, image=fault_grey, text=f'Step: {fault6_counter[0]}', font=('nunito', 30, 'bold'),
              compound='center', foreground='#206CB9').place(x=422, y=250)

    def fault6_counter_sub():
        fault6_counter[0] -=1
        Label(win, image=fault_grey, text=f'Step: {fault6_counter[0]}', font=('nunito', 30, 'bold'),
              compound='center', foreground='#206CB9').place(x=422, y=250)

    Button(win, image=fault_blue, text='Back', font=('nunito', 30, 'bold'),
           compound='center', foreground='white', command=fault6_counter_sub).place(x=202, y=250)
    Button(win, image=fault_blue, text='Next', font=('nunito', 30, 'bold'),
           compound='center', foreground='white', command=fault6_counter_add).place(x=642, y=250)


def fault7_page():
    clear_body_frame()
    draw_header()
    draw_footer('Fault #7', 'preset')

    global fault_blue
    fault_blue = ImageTk.PhotoImage(Image.open('./UI/Fault_Blue.jpg'))
    global fault_grey
    fault_grey = ImageTk.PhotoImage(Image.open('./UI/Fault_Grey.jpg'))
    step_display = Label(win, image=fault_grey, text='Step:#', font=('nunito', 30, 'bold'),
                         compound='center', foreground='#206CB9').place(x=422, y=250)
    fault7_counter = [0]
    fault7_counter[0]=0

    def fault7_counter_add():
        fault7_counter[0] +=1
        Label(win, image=fault_grey, text=f'Step: {fault7_counter[0]}', font=('nunito', 30, 'bold'),
              compound='center', foreground='#206CB9').place(x=422, y=250)

    def fault7_counter_sub():
        fault7_counter[0] -=1
        Label(win, image=fault_grey, text=f'Step: {fault7_counter[0]}', font=('nunito', 30, 'bold'),
              compound='center', foreground='#206CB9').place(x=422, y=250)

    Button(win, image=fault_blue, text='Back', font=('nunito', 30, 'bold'),
           compound='center', foreground='white', command=fault7_counter_sub).place(x=202, y=250)
    Button(win, image=fault_blue, text='Next', font=('nunito', 30, 'bold'),
           compound='center', foreground='white', command=fault7_counter_add).place(x=642, y=250)


def fault8_page():
    clear_body_frame()
    draw_header()
    draw_footer('Fault #8', 'preset')

    global fault_blue
    fault_blue = ImageTk.PhotoImage(Image.open('./UI/Fault_Blue.jpg'))
    global fault_grey
    fault_grey = ImageTk.PhotoImage(Image.open('./UI/Fault_Grey.jpg'))
    step_display = Label(win, image=fault_grey, text='Step:#', font=('nunito', 30, 'bold'),
                         compound='center', foreground='#206CB9').place(x=422, y=250)
    fault8_counter = [0]
    fault8_counter[0] = 0

    def fault8_counter_add():
        fault8_counter[0] += 1
        Label(win, image=fault_grey, text=f'Step: {fault8_counter[0]}', font=('nunito', 30, 'bold'),
              compound='center', foreground='#206CB9').place(x=422, y=250)

    def fault8_counter_sub():
        fault8_counter[0] -= 1
        Label(win, image=fault_grey, text=f'Step: {fault8_counter[0]}', font=('nunito', 30, 'bold'),
              compound='center', foreground='#206CB9').place(x=422, y=250)

    Button(win, image=fault_blue, text='Back', font=('nunito', 30, 'bold'),
           compound='center', foreground='white', command=fault8_counter_sub).place(x=202, y=250)
    Button(win, image=fault_blue, text='Next', font=('nunito', 30, 'bold'),
           compound='center', foreground='white', command=fault8_counter_add).place(x=642, y=250)



main_page()

win.mainloop()
