# Import the required libraries
from tkinter import *
from PIL import ImageTk, Image
from dataclasses import dataclass, field
from rpi_ws281x import *
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
led_error = Color(0, 0, 255)  # led state if no other state is applied (signifies assignment error)


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
    def clear(self):
        for i in range(LED_COUNT):
            strip.setPixelColor(i, Color(0, 0, 0))
        strip.show()

    def step(self, index):
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
            else:
                strip.setPixelColor(i, led_error)

        strip.show()


# env variable definitions
window_width = 1024
window_height = 550

dark_blue = "#206CB9"
light_blue = "#5B92CC"
dark_grey = "#C4C4C4"
light_grey = "#E5E5E5"

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

    Label(win, image=logo_img, highlightthickness=0, bd=0).place(x=0, y=14)
    Label(win, image=UI_image, text="Substation Technical \n Training Simulator", font=('graphik', 30, 'bold'),
          compound="center", foreground="white", highlightthickness=0, bd=0, bg="white").place(x=512, y=14)


def draw_footer(page_name, back_to):  # back_to can be: quit, main, preset
    footer = Frame(win, background=dark_grey, width='1024', height=100).place(x=0, y=500)
    Label(footer, text=f'{page_name}', font=('nunito', 22), foreground="black", bg=dark_grey, justify='center'). \
        place(x=450, y=507)

    if back_to == 'quit':
        Button(footer, text='Quit', font=('nunito', 22), fg="black", bg=dark_grey, justify='center',
               command=close_app).place(x=39, y=507)
    elif back_to == 'preset':
        Button(footer, text='Back', font=('nunito', 22), fg="black", bg=dark_grey, justify='center',
               command=preset_page).place(x=39, y=507)


# a function that clears everything of the page, make sure to only define one window and frame
def clear_body_frame():
    for widgets in win.winfo_children():
        widgets.destroy()


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
    Button(win, image=fault_img, text='1', font=('nunito', 30, 'bold'),
           compound='center', foreground="white", highlightthickness=0, bd=0, bg="white",
           command=lambda: fault_page(fault1)).place(x=_x, y=_y)
    Button(win, image=fault_img, text='2', font=('nunito', 30, 'bold'),
           compound='center', foreground="white", highlightthickness=0, bd=0, bg="white",
           command=lambda: fault_page(fault2)).place(x=_x + x_spacing, y=_y)
    Button(win, image=fault_img, text='3', font=('nunito', 30, 'bold'),
           compound='center', foreground="white", highlightthickness=0, bd=0, bg="white",
           command=lambda: fault_page(fault3)).place(x=_x + x_spacing * 2,
                                                            y=_y)
    Button(win, image=fault_img, text='4', font=('nunito', 30, 'bold'),
           compound='center', foreground="white", highlightthickness=0, bd=0, bg="white",
           command=lambda: fault_page(fault4)).place(x=_x + x_spacing * 3,
                                                            y=_y)
    Button(win, image=fault_img, text='5', font=('nunito', 30, 'bold'),
           compound='center', foreground="white", highlightthickness=0, bd=0, bg="white",
           command=lambda: fault_page(fault5)).place(x=_x, y=_y + y_spacing)
    Button(win, image=fault_img, text='6', font=('nunito', 30, 'bold'),
           compound='center', foreground="white", highlightthickness=0, bd=0, bg="white",
           command=lambda: fault_page(fault6)).place(x=_x + x_spacing,
                                                            y=_y + y_spacing)
    Button(win, image=fault_img, text='7', font=('nunito', 30, 'bold'),
           compound='center', foreground="white", highlightthickness=0, bd=0, bg="white",
           command=lambda: fault_page(fault7)).place(x=_x + x_spacing * 2,
                                                            y=_y + y_spacing)
    Button(win, image=fault_img, text='8', font=('nunito', 30, 'bold'),
           compound='center', foreground="white", highlightthickness=0, bd=0, bg="white",
           command=lambda: fault_page(fault8)).place(x=_x + x_spacing * 3,
                                                            y=_y + y_spacing)


def fault_page(fault: Faults):
    clear_body_frame()
    draw_header()
    draw_footer(f'Fault {fault.name}', 'preset')

    global fault_blue
    fault_blue = ImageTk.PhotoImage(Image.open('./UI/Fault_Blue.jpg'))
    global fault_grey
    fault_grey = ImageTk.PhotoImage(Image.open('./UI/Fault_Grey.jpg'))
    step_label = Label(win, image=fault_grey, text='Step:#', font=('nunito', 30, 'bold'),
                       compound='center', foreground=dark_blue, highlightthickness=0, bd=0, bg="white")
    step_label.place(x=425, y=200)
    counter = [0]
    counter[0] = 0

    def fault1_counter_add():
        if counter[0] <= fault.totalSteps:
            counter[0] += 1
            step_label.configure(text=f' {counter[0]} / {fault.totalSteps}')
            fault.clear()
            fault.step(counter[0])

        # print(f'{all_children(win)}\n')

    def fault1_counter_sub():
        if counter[0] <= fault.totalSteps:
            counter[0] -= 1
            step_label.configure(text=f' {counter[0]} / {fault.totalSteps}')
            fault.clear()
            fault.step(counter[0])

        # print(f'{all_children(win)}\n')

    Button(win, image=fault_blue, text='Back', font=('nunito', 30, 'bold'),
           compound='center', foreground="white", highlightthickness=0, bd=0, bg="white",
           command=fault1_counter_sub).place(x=202, y=200)
    Button(win, image=fault_blue, text='Next', font=('nunito', 30, 'bold'),
           compound='center', foreground="white", highlightthickness=0, bd=0, bg="white",
           command=fault1_counter_add).place(x=642, y=200)


# test and validation
def all_children(wid):
    # returns the number of widgets currently drawn on the screen.
    num = 0
    for item in wid.winfo_children():
        num += 1
    return num


preset_page()

win.mainloop()
