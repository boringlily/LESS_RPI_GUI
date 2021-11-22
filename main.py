# Import the required libraries
from tkinter import *
from PIL import ImageTk, Image
from dataclasses import dataclass, field
from rpi_ws281x import *
import argparse

# RGB strip object definition

LED_COUNT      = 58      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).  
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 20    # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

#if __name__ == '__main__':
# Process arguments
parser = argparse.ArgumentParser()
parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
args = parser.parse_args()

# Create NeoPixel object with appropriate configuration.
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
# Intialize the library (must be called once before other functions).
strip.begin()


@dataclass()
class Faults:
    # faults object class
    totalSteps: int
    num: int
    steps = tuple()
    timing = tuple()
    

    def __init__(self, steps, timing, num):
        self.steps = steps
        self.timing = timing
        self.num = num
        self.totalSteps = len(self.steps)
    
    def clear(self):
        for i in range(LED_COUNT):
            strip.setPixelColor(i,Color(0,0,0))
        strip.show()
        
    def step(self, i):
        print(self.steps[i-1])
        strip.setPixelColor(i-1,Color(255,0,0))
        strip.show()
    


# env variable definitions
window_width = 1024
window_height = 550
# Create an instance of tkinter frame
win = Tk()
# win.attributes('-fullscreen', True) # uncomment to force window fullscreen
win.configure(background='white')
win.title("Substation Technical Training Simulator")
win.geometry(f"{window_width}x{window_height}")


def draw_header():
    global logo_img
    logo_img = ImageTk.PhotoImage(Image.open('./UI/logo.jpg'))  # Lakeland Electric Logo

    global UI_image
    UI_image = ImageTk.PhotoImage(Image.open('./UI/HeaderTextBox.png'))  # Rounded corner label template

    Label(win, image=logo_img, highlightthickness = 0, bd = 0).place(x=0, y=14)
    Label(win, image=UI_image, text="Substation Technical \n Training Simulator", font=('graphik', 30, 'bold'),
            compound="center", foreground="white", highlightthickness = 0, bd = 0, bg = "white").place(x=512, y=14)


def draw_footer(page_name, back_to):  # back_to can be: quit, main, preset
    footer = Frame(win, background="#c4c4c4", width='1024', height=100).place(x=0, y=500)
    Label(footer, text=f'{page_name}', font=('nunito', 22), foreground="black", bg="#c4c4c4", justify='center').\
        place(x=450, y=507)

    if back_to == 'quit':
        Button(footer, text='Quit', font=('nunito', 22), fg="black", bg="#c4c4c4", justify='center',
               command=close_app).place(x=39, y=507)
    elif back_to == 'preset':
        Button(footer, text='Back', font=('nunito', 22), fg="black", bg="#c4c4c4", justify='center',
               command=preset_page).place(x=39, y=507)


# a function that clears everything of the page, make sure to only define one window and frame
def clear_body_frame():
    for widgets in win.winfo_children():
        widgets.destroy()


def close_app():
    quit()


def preset_page():
    # fault object initializations
    fault1 = Faults([1, 2, 3, 4], [50, 10, 50, 20], 1)

    clear_body_frame()
    draw_header()
    draw_footer('Presets', 'quit')
    _x, _y = 45, 200
    y_spacing = 50 + 75
    x_spacing = 73+180
    global fault_img
    fault_img = ImageTk.PhotoImage(Image.open('./UI/Fault_Blue.jpg'))
    Button(win, image=fault_img, text='1', font=('nunito', 30, 'bold'),
           compound='center', foreground="white", highlightthickness = 0, bd = 0, bg = "white", command=lambda: fault_page(fault1)).place(x=_x, y=_y)
    Button(win, image=fault_img, text='2', font=('nunito', 30, 'bold'),
           compound='center', foreground="white", highlightthickness = 0, bd = 0, bg = "white").place(x=_x + x_spacing, y=_y)
    Button(win, image=fault_img, text='3', font=('nunito', 30, 'bold'),
           compound='center', foreground="white", highlightthickness = 0, bd = 0, bg = "white").place(x=_x + x_spacing * 2, y=_y)
    Button(win, image=fault_img, text='4', font=('nunito', 30, 'bold'),
           compound='center', foreground="white", highlightthickness = 0, bd = 0, bg = "white").place(x=_x + x_spacing * 3, y=_y)
    Button(win, image=fault_img, text='5', font=('nunito', 30, 'bold'),
           compound='center', foreground="white", highlightthickness = 0, bd = 0, bg = "white").place(x=_x, y=_y + y_spacing)
    Button(win, image=fault_img, text='6', font=('nunito', 30, 'bold'),
           compound='center', foreground="white", highlightthickness = 0, bd = 0, bg = "white").place(x=_x + x_spacing, y=_y + y_spacing)
    Button(win, image=fault_img, text='7', font=('nunito', 30, 'bold'),
           compound='center', foreground="white", highlightthickness = 0, bd = 0, bg = "white").place(x=_x + x_spacing * 2, y=_y + y_spacing)
    Button(win, image=fault_img, text='8', font=('nunito', 30, 'bold'),
           compound='center', foreground="white", highlightthickness = 0, bd = 0, bg = "white").place(x=_x + x_spacing * 3, y=_y + y_spacing)


def fault_page(fault:Faults):
    clear_body_frame()
    draw_header()
    draw_footer(f'Fault #{fault.num}', 'preset')
    

    global fault_blue
    fault_blue = ImageTk.PhotoImage(Image.open('./UI/Fault_Blue.jpg'))
    global fault_grey
    fault_grey = ImageTk.PhotoImage(Image.open('./UI/Fault_Grey.jpg'))
    step_label = Label(win, image=fault_grey, text='Step:#', font=('nunito', 30, 'bold'),
                       compound='center', foreground="#206CB9", highlightthickness = 0, bd = 0, bg = "white")
    step_label.place(x=425, y=200)
    fault1_counter = [0]
    fault1_counter[0] = 0

    def fault1_counter_add():
        fault1_counter[0] += 1
        step_label.configure(text=f' {fault1_counter[0]} / {fault.totalSteps}')
        fault.clear()
        fault.step(fault1_counter[0])
     #  print(f'{all_children(win)}\n')

    def fault1_counter_sub():
        fault1_counter[0] -= 1
        step_label.configure(text=f' {fault1_counter[0]} / {fault.totalSteps}')
        fault.clear()
        fault.step(fault1_counter[0])
        
     #  print(f'{all_children(win)}\n')

    Button(win, image=fault_blue, text='Back', font=('nunito', 30, 'bold'),
           compound='center', foreground="white", highlightthickness = 0, bd = 0, bg = "white", command=fault1_counter_sub).place(x=202, y=200)
    Button(win, image=fault_blue, text='Next', font=('nunito', 30, 'bold'),
           compound='center', foreground="white", highlightthickness = 0, bd = 0, bg = "white", command=fault1_counter_add).place(x=642, y=200)


# test and validation
def all_children(wid):
    # returns the number of widgets currently drawn on the screen.
    num = 0
    for item in wid.winfo_children():
        num += 1
    return num





preset_page()

win.mainloop()