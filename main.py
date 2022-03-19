#Developed by Levko Nikitin as part of the Research Assitant Position at
#Florida Polytechnic University under the mentorship of Dr. Mohammad Reza Khalghani.

# Import the required libraries
from tkinter import *
from PIL import ImageTk, Image
from dataclasses import dataclass, field
from rpi_ws281x import *
import time
import argparse


# RGB strip object definition
LED_COUNT = 47  # Number of LED pixels.
LED_PIN = 18  # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10  # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 20  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False  # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0  # set to '1' for GPIOs 13, 19, 41, 45 or 53

# Process arguments
parser = argparse.ArgumentParser()
parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
args = parser.parse_args()

# Create NeoPixel object with appropriate configuration and initialize.
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()  # Initialize the library (must be called once before other functions).

# predefined led states
led_closed = Color(255, 0, 0)  # led state 0
led_open = Color(0, 255, 0)  # led state 1
led_energized = Color(255, 255, 255)  # led state 2
led_fault = Color(253, 181, 6)  # led state 3
led_off = Color(0, 0, 0)  # led state 4
led_blink = Color(0, 0, 255) # led state 9
led_error = Color(100, 100, 100)  # led state if no other state is applied (signifies assignment error)


@dataclass()

class Faults:  # faults object class


    totalSteps: int
    name: str
    step_name = list()
    steps = list()
    timing = list()

    def __init__(self, name, step_name, timing, steps):
        self.name = name
        self.step_name = step_name
        self.steps = steps
        self.timing = timing
        self.totalSteps = len(self.steps)

    @staticmethod
    def clear():
        for i in range(LED_COUNT):
            strip.setPixelColor(i, led_off)
            
        strip.show()

    def step(self, index):
        global blink_list
        global blink_count
        global blink_index
        global blink
        blink = True
        blink_list = []
        blink_count = 0
        blink_index = 0
        
        for i in range(LED_COUNT):
            state = self.steps[index][i]
            
            if state == 0:
                strip.setPixelColor(i, led_closed)
            elif state == 1:
                strip.setPixelColor(i, led_open)
            elif state == 2:
                strip.setPixelColor(i, led_energized)
            elif state == 3:
                strip.setPixelColor(i, led_fault)
            elif state == 4:
                strip.setPixelColor(i, led_off)
            elif state == 9:
                strip.setPixelColor(i, led_blink)
            else:
                strip.setPixelColor(i, led_error)
        strip.show()
                    
# Widget positioning variable
window_width = 1024
window_height = 550

footer_top = 540

dark_blue = "#206CB9"
light_blue = "#5B92CC"
dark_grey = "#C4C4C4"
light_grey = "#E5E5E5"

# Create an instance of tkinter frame
root = Tk()
root.attributes('-fullscreen', True) # uncomment to force window fullscreen
root.configure(background='white')
root.title("Substation Technical Training Simulator")
root.geometry(f"{window_width}x{window_height}")


def draw_header():
    global logo_img
    logo_img = ImageTk.PhotoImage(Image.open('./UI/logo.jpg'))  # Lakeland Electric Logo

    global UI_image
    UI_image = ImageTk.PhotoImage(Image.open('./UI/HeaderTextBox.png'))  # Rounded corner label template

    Label(root, image=logo_img, highlightthickness=0, bd=0).place(x=0, y=14)
    Label(root, image=UI_image, text="Substation Technical \n Training Simulator", font=('graphik', 30, 'bold'),
          compound="center", foreground="white", highlightthickness=0, bd=0, bg="white").place(x=512, y=14)



def draw_footer(page_name, back_to):  # back_to can be: quit or preset
    footer = Frame(root, background=dark_grey, width='1024', height=100).place(x=0, y=footer_top-20)
    pageName = Label(footer, text=f'{page_name}', font=('nunito', 22), foreground="black", bg=dark_grey, justify='center').place(x=250, y=footer_top)

    if back_to == 'quit':
        Button(footer, text='Quit', font=('nunito', 22), fg="black", bg=dark_grey, justify='center',
               command=close_app).place(x=39, y=footer_top)
    elif back_to == 'preset':
        Button(footer, text='Back', font=('nunito', 22), fg="black", bg=dark_grey, justify='center',
               command=preset_page).place(x=39, y=footer_top)


# a function that delets all graphical objects from the page main page, make sure to only define one window and frame
def clear_body_frame():
    for widgets in root.winfo_children():
        widgets.destroy()
    Faults.clear()


def close_app():
    quit()


def preset_page():
    # fault object initializations

    fault1 = Faults("Transmission Fault (644)", ["Normal State", "Fault", "Isolation", "Return to Normal"],
                    [1000, 1000, 1000, 1000],
                    [
                        [2, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 2, 2, 0, 0, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2,
                         2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2],
                        [3, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 2, 2, 0, 0, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2,
                         2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2],
                        [4, 2, 1, 0, 0, 2, 0, 2, 0, 0, 0, 2, 2, 0, 0, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2,
                         2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2],
                        [2, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 2, 2, 0, 0, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2,
                         2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2]
                    ]
                    )

    fault2 = Faults("Transmission Fault & Breaker Failure",
                    ["Normal State", "Fault", "Breaker Failure", "Isolation/SA", "Return to Normal"],
                    [2000, 2000, 2000, 2000, 2000],
                    [
                        [2, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 2, 2, 0, 0, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2,
                         2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2],
                        [3, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 2, 2, 0, 0, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2,
                         2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2],
                        [3, 2, 9, 0, 0, 2, 0, 2, 0, 0, 0, 2, 2, 0, 0, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2,
                         2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2],
                        [4, 2, 9, 0, 1, 4, 1, 2, 0, 1, 0, 4, 2, 1, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2,
                         2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2],
                        [2, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 2, 2, 0, 0, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2,
                         2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2]
                    ]
                    )

    fault3 = Faults("69 kV Bus #1 Fault", ['Normal State', 'Fault', 'Isolation/SA', 'Return to Normal'],
                    [2000, 2000, 2000, 2000, 2000],
                    [
                        [2, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 2, 2, 0, 0, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2,
                         2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2],
                        [2, 2, 0, 0, 0, 3, 0, 2, 0, 0, 0, 2, 2, 0, 0, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2,
                         2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2],
                        [4, 2, 1, 0, 1, 4, 1, 2, 0, 1, 0, 2, 2, 1, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2,
                         2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2],
                        [2, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 2, 2, 0, 0, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2,
                         2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2]
                    ]
                    )

    fault4 = Faults('Transformer #1 Fault', ['Normal state', 'Fault', 'Isolation', 'Return to normal'],
                    [2000, 2000, 2000, 2000],
                    [
                        [2, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 2, 2, 0, 0, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2,
                         2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2],
                        [2, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 3, 2, 0, 0, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2,
                         2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2],
                        [2, 2, 0, 0, 0, 2, 0, 2, 0, 1, 0, 4, 2, 1, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2,
                         2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2],
                        [2, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 2, 2, 0, 0, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2,
                         2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2]
                    ]
                    )

    fault5 = Faults('12kV Bus #1 Fault', ['Normal State', 'Fault', 'Isolation', 'Return to Normal'],
                    [2000, 2000, 2000, 2000],
                    [
                        [2, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 2, 2, 0, 0, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2,
                         2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2],
                        [2, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 2, 2, 0, 0, 3, 1, 2, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2,
                         2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2],
                        [2, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 2, 2, 1, 0, 4, 1, 2, 1, 1, 1, 0, 0, 0, 4, 4, 4, 2, 2, 2, 4, 4,
                         4, 4, 4, 4, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2],
                        [2, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 2, 2, 0, 0, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2,
                         2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2]
                    ]
                    )

    fault6 = Faults('12kV Feeder Fault (334)',
                    ['Normal State', 'Fault', 'Trip 1', 'Reclose 1', 'Trip 2', 'Reclose 2', 'Trip 3', 'Reclose 3',
                     'Trip 4/ LO'],
                    [2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000],
                    [
                        [2, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 2, 2, 0, 0, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2,
                         2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2],
                        [2, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 2, 2, 0, 0, 2, 1, 2, 0, 0, 0, 0, 0, 0, 3, 2, 2, 2, 2, 2, 2, 2,
                         2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2],
                        [2, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 2, 2, 0, 0, 2, 1, 2, 1, 0, 0, 0, 0, 0, 4, 2, 2, 2, 2, 2, 4, 4,
                         4, 4, 4, 4, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2],
                        [2, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 2, 2, 0, 0, 2, 1, 2, 0, 0, 0, 0, 0, 0, 3, 2, 2, 2, 2, 2, 2, 2,
                         2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2],
                        [2, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 2, 2, 0, 0, 2, 1, 2, 1, 0, 0, 0, 0, 0, 4, 2, 2, 2, 2, 2, 4, 4,
                         4, 4, 4, 4, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2],
                        [2, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 2, 2, 0, 0, 2, 1, 2, 0, 0, 0, 0, 0, 0, 3, 2, 2, 2, 2, 2, 2, 2,
                         2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2],
                        [2, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 2, 2, 0, 0, 2, 1, 2, 1, 0, 0, 0, 0, 0, 4, 2, 2, 2, 2, 2, 4, 4,
                         4, 4, 4, 4, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2],
                        [2, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 2, 2, 0, 0, 2, 1, 2, 0, 0, 0, 0, 0, 0, 3, 2, 2, 2, 2, 2, 2, 2,
                         2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2],
                        [2, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 2, 2, 0, 0, 2, 1, 2, 1, 0, 0, 0, 0, 0, 4, 2, 2, 2, 2, 2, 4, 4,
                         4, 4, 4, 4, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2]
                    ]
                    )

    fault7 = Faults('Feeder W/ Recloser Fault',
                    ['Normal State', 'Fault', 'Trip 1', 'Reclose 1', 'Trip 2', 'Reclose 2', 'Trip 3', 'Reclose 3',
                     'Trip 4/ LO'],
                    [2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000],
                    [
                        [2, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 2, 2, 0, 0, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2,
                         2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2],
                        [2, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 2, 2, 0, 0, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2,
                         2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 3],
                        [2, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 2, 2, 0, 0, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2,
                         2, 2, 2, 2, 2, 2, 2, 4, 4, 4, 4, 2, 1, 4, 4],
                        [2, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 2, 2, 0, 0, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2,
                         2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 3],
                        [2, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 2, 2, 0, 0, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2,
                         2, 2, 2, 2, 2, 2, 2, 4, 4, 4, 4, 2, 1, 4, 4],
                        [2, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 2, 2, 0, 0, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2,
                         2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 3],
                        [2, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 2, 2, 0, 0, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2,
                         2, 2, 2, 2, 2, 2, 2, 4, 4, 4, 4, 2, 1, 4, 4],
                        [2, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 2, 2, 0, 0, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2,
                         2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 3],
                        [2, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 2, 2, 0, 0, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2,
                         2, 2, 2, 2, 2, 2, 2, 4, 4, 4, 4, 2, 1, 4, 4]
                    ]
                    )

    fault8 = Faults('Feeder W/ Recloser Fault 2',
                    ['Normal State', 'Fault', 'Trip 1', 'Reclose 1', 'Trip 2', 'Reclose 2', 'Trip 3', 'Reclose 3',
                     'Trip 4/ LO'],
                    [2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000],
                    [
                        [2, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 2, 2, 0, 0, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2,
                         2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2],
                        [2, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 2, 2, 0, 0, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2,
                         2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 3, 2],
                        [2, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 2, 2, 0, 0, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2,
                         2, 2, 2, 2, 2, 2, 2, 4, 2, 2, 2, 2, 1, 4, 2],
                        [2, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 2, 2, 0, 0, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2,
                         2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 3, 2],
                        [2, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 2, 2, 0, 0, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2,
                         2, 2, 2, 2, 2, 2, 2, 4, 2, 2, 2, 2, 1, 4, 2],
                        [2, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 2, 2, 0, 0, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2,
                         2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 3, 2],
                        [2, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 2, 2, 0, 0, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2,
                         2, 2, 2, 2, 2, 2, 2, 4, 2, 2, 2, 2, 1, 4, 2],
                        [2, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 2, 2, 0, 0, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2,
                         2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 3, 2],
                        [2, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 2, 2, 0, 0, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2,
                         2, 2, 2, 2, 2, 2, 2, 4, 2, 2, 2, 2, 1, 4, 2]
                    ]
                    )

    clear_body_frame()
    draw_header()
    draw_footer('Presets', 'quit')
    _x, _y = 45, 200
    y_spacing = 50 + 75
    x_spacing = 73 + 180
    global fault_img
    fault_img = ImageTk.PhotoImage(Image.open('./UI/Fault_Blue.jpg'))

    # fault menu buttons 1-8
    Button(root, image=fault_img, text='1', font=('nunito', 30, 'bold'),
           compound='center', foreground="white", highlightthickness=0, bd=0, bg="white",
           command=lambda: fault_page(fault1)).place(x=_x, y=_y)
    Button(root, image=fault_img, text='2', font=('nunito', 30, 'bold'),
           compound='center', foreground="white", highlightthickness=0, bd=0, bg="white",
           command=lambda: fault_page(fault2)).place(x=_x + x_spacing, y=_y)
    Button(root, image=fault_img, text='3', font=('nunito', 30, 'bold'),
           compound='center', foreground="white", highlightthickness=0, bd=0, bg="white",
           command=lambda: fault_page(fault3)).place(x=_x + x_spacing * 2,
                                                            y=_y)
    Button(root, image=fault_img, text='4', font=('nunito', 30, 'bold'),
           compound='center', foreground="white", highlightthickness=0, bd=0, bg="white",
           command=lambda: fault_page(fault4)).place(x=_x + x_spacing * 3,
                                                            y=_y)
    Button(root, image=fault_img, text='5', font=('nunito', 30, 'bold'),
           compound='center', foreground="white", highlightthickness=0, bd=0, bg="white",
           command=lambda: fault_page(fault5)).place(x=_x, y=_y + y_spacing)
    Button(root, image=fault_img, text='6', font=('nunito', 30, 'bold'),
           compound='center', foreground="white", highlightthickness=0, bd=0, bg="white",
           command=lambda: fault_page(fault6)).place(x=_x + x_spacing,
                                                            y=_y + y_spacing)
    Button(root, image=fault_img, text='7', font=('nunito', 30, 'bold'),
           compound='center', foreground="white", highlightthickness=0, bd=0, bg="white",
           command=lambda: fault_page(fault7)).place(x=_x + x_spacing * 2,
                                                            y=_y + y_spacing)
    Button(root, image=fault_img, text='8', font=('nunito', 30, 'bold'),
           compound='center', foreground="white", highlightthickness=0, bd=0, bg="white",
           command=lambda: fault_page(fault8)).place(x=_x + x_spacing * 3,
                                                            y=_y + y_spacing)


def fault_page(fault: Faults):
    # widget constructors
    clear_body_frame()
    draw_header()
    draw_footer(f'{fault.name}', 'preset')

    # ***** VARIABLES *****
    global running
    global counter
    
    running = False  # use a boolean variable to help control state of time (running or not running)
    counter = -1  # time variables initially set to -1 so that when counted up the index passed to the list starts at 0

    def counter_add():
        global counter
        if counter < fault.totalSteps - 1:
            counter += 1
            step_label.config(text=f'{fault.step_name[counter]}')
            fault.step(counter)

    def counter_sub():
        global counter
        if counter > 0:
            counter -= 1
            step_label.config(text=f'{fault.step_name[counter]}')
            fault.step(counter)

    def start():
        global running
        if not running:
            update()
            running = True

    # pause function
    def pause():
        global running
        if running:
            # cancel updating loop using after_cancel()
            step_label.after_cancel(update_time)
            running = False

    # reset function
    def reset():
        # clear strip
        Faults.clear()
        
        global update_time
        global running
        
        # check loop state
        if running:

            step_label.after_cancel(update_time)
            running = False
        # reset variables
        global counter
        counter = -1
        # reset label
        step_label.config(text='Step Name')

    # update function
    def update():
        # update counter
        global counter
        counter += 1
        
        step_label.config(text=f'{fault.step_name[counter]}')
        
        fault.step(counter)
        
        if counter < fault.totalSteps - 1:
            global update_time
            update_time = step_label.after(fault.timing[counter], update)

    global fault_blue
    fault_blue = ImageTk.PhotoImage(Image.open('./UI/Fault_Blue.jpg').resize((150, 80), Image.ANTIALIAS))
    global fault_grey
    fault_grey = ImageTk.PhotoImage(Image.open('./UI/Fault_Grey.jpg').resize((800, 80), Image.ANTIALIAS))

    step_label = Label(root, image=fault_grey, text='Step Name', font=('nunito', 30, 'bold'),
                       compound='center', foreground=dark_blue, highlightthickness=0, bd=0, bg="white")
    step_label.place(x=112, y=200)
    

    back_button = Button(root, image=fault_blue, text='Back', font=('nunito', 30, 'bold'), compound='center', foreground="white", highlightthickness=0, bd=0, bg="white",command=counter_sub)

    start_button = Button(root, image=fault_blue, text='Play', font=('nunito', 30, 'bold'), compound='center', foreground="white", highlightthickness=0, bd=0, bg="white", command=start)
    

    reset_button = Button(root, image=fault_blue, text='Reset', font=('nunito', 30, 'bold'), compound='center', foreground="white", highlightthickness=0, bd=0, bg="white", command=reset)
    

    pause_button = Button(root, image=fault_blue, text='Pause', font=('nunito', 30, 'bold'), compound='center', foreground="white", highlightthickness=0, bd=0, bg="white", command=pause)
    

    next_button = Button(root, image=fault_blue, text='Next', font=('nunito', 30, 'bold'), compound='center', foreground="white", highlightthickness=0, bd=0, bg="white", command=counter_add)
    
    back_button.place(x=27, y=300)
    start_button.place(x=232, y=300)
    reset_button.place(x=437, y=300)
    pause_button.place(x=641, y=300)
    next_button.place(x=846, y=300)


preset_page()

root.mainloop()
