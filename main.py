from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.geometry("1024x600")

frame = Frame(root)
frame.pack(side="top", expand=True, fill="both")


def clear_frame():
    for widgets in root.winfo_children():
        widgets.destroy()


def main_page():  # Main Page
    clear_frame()

    my_img = ImageTk.PhotoImage(Image.open("LE_Logo.png"))  # LE Logo Resize
    my_label = Label(image=my_img)
    my_label.grid(column=1, row=0)

    canv2 = Canvas(root, bg='blue', width=600, height=200)  # Blue Box in every page
    canv2.place(x=1000, y=1)
    canv2.create_text(300, 50, text="Substation Technical", font="Calibri 45", fill="white")
    canv2.create_text(300, 120, text="Training Simulator", font="Calibri 45", fill="white")
    strip1 = Canvas(root, bg='grey', width=1575, height=100)
    strip1.place(x=1, y=725)
    c2 = Canvas(root, bg='blue', width=600, height=200)
    c2.place(x=1000, y=1)
    c2.create_text(300, 50, text="Substation Technical", font="Calibri 45", fill="white")
    c2.create_text(300, 120, text="Training Simulator", font="Calibri 45", fill="white")
    c3 = Canvas(root, bg='white', width=400, height=50, highlightbackground="white")
    c3.place(x=600, y=250)
    c3.create_text(200, 25, text="Simulation Modes", font="Arial 25 bold", fill="black")
    t1_b = Button(root, text='Settings', font=('Calibri', 20), bg='grey', border=0, command=settings_page)
    t1_b.place(x=1400, y=740)
    t2_b = Button(root, text='Main Page', font=('Calibri', 20), bg='grey', border=0)  # Add command tab2
    t2_b.place(x=700, y=740)
    t3_b = Button(root, text='Back', font=('Calibri', 20), bg='grey', border=0)  # add command tab3
    t3_b.place(x=140, y=740)
    t5_b = Button(root, text='Preset Modes', font=('Calibri', 20), bg='blue', fg='white', command=faults_selection_page)
    t5_b.place(x=700, y=400)
    t6_b = Button(root, text='Manual Control', font=('Calibri', 20), bg='blue', fg='white', command=manual_control_page)
    t6_b.place(x=700, y=500)


def settings_page():  # Settings Page
    clear_frame()
    global my_img
    canv1 = Canvas(root, bg='white', width=1600, height=1000)
    canv1.place(x=1, y=1)
    label1 = Label(root, text='Operator Mode', bg='white', fg='black', font=('Arial Black', 20))
    label1.place(x=200, y=250)
    label2 = Label(root, text='LED Tests', bg='white', fg='black', font=('Arial Black', 20))
    label2.place(x=1200, y=250)

    my_img = ImageTk.PhotoImage(Image.open("LE_Logo.png"))  # LE Logo
    my_label = Label(image=my_img)
    my_label.grid(column=1, row=0)

    canv2 = Canvas(root, bg='blue', width=600, height=200)  # Blue Box in every page
    canv2.place(x=1000, y=1)
    canv2.create_text(300, 50, text="Substation Technical", font="Calibri 45", fill="white")
    canv2.create_text(300, 120, text="Training Simulator", font="Calibri 45", fill="white")

    strip1 = Canvas(root, bg='grey', width=1575, height=100)  # Grey border at bottom with buttons
    strip1.place(x=1, y=725)
    tab3_b = Button(root, text='Back', font=('Calibri', 20), bg='grey', border=0, command=main_page)
    tab3_b.place(x=140, y=740)
    tab4_b = Button(root, text='Go to Main', font=('Calibri', 20), bg='grey', border=0, command=main_page)
    tab4_b.place(x=1300, y=740)
    c3 = Canvas(root, bg='grey', width=400, height=50, highlightbackground="grey")
    c3.place(x=600, y=740)
    c3.create_text(200, 25, text="Settings", font="Calibri 20", fill="black")

    tab5_b = Button(root, text='Sequential Toggle', font=('Calibri', 20), bg='blue', fg='white')  # add command later
    tab5_b.place(x=1180, y=300)
    tab6_b = Button(root, text='All Green', font=('Calibri', 20), bg='blue', fg='white', )  # add command later
    tab6_b.place(x=1175, y=375)
    tab7_b = Button(root, text='All Red', font=('Calibri', 20), bg='blue', fg='white')  # add command later
    tab7_b.place(x=1325, y=375)
    tab8_b = Button(root, text='Left Handed', font=('Calibri', 20), bg='grey', fg='white')
    tab8_b.place(x=185, y=325)
    tab9_b = Button(root, text='Right Handed', font=('Calibri', 20), bg='blue', fg='white')
    tab9_b.place(x=375, y=325)


def faults_selection_page():  # Faults Page
    clear_frame()
    global my_img
    canv1 = Canvas(root, bg='white', width=1600, height=1000)
    canv1.place(x=1, y=1)
    label1 = Label(root, text='Preset Faults', bg='white', fg='black', font=('Arial Black', 20))
    label1.place(x=200, y=250)

    my_img = ImageTk.PhotoImage(Image.open("LE_Logo.png"))  # LE Logo
    my_label = Label(image=my_img)
    my_label.grid(column=1, row=0)

    canv2 = Canvas(root, bg='blue', width=600, height=200)  # Blue Box in every page
    canv2.place(x=1000, y=1)
    canv2.create_text(300, 50, text="Substation Technical", font="Calibri 45", fill="white")
    canv2.create_text(300, 120, text="Training Simulator", font="Calibri 45", fill="white")

    strip1 = Canvas(root, bg='grey', width=1575, height=100)  # Grey border at bottom with buttons
    strip1.place(x=1, y=725)
    tab3_b = Button(root, text='Back', font=('Calibri', 20), bg='grey', border=0, command=main_page)
    tab3_b.place(x=140, y=740)
    tab4_b = Button(root, text='Go to Main', font=('Calibri', 20), bg='grey', border=0, command=main_page)
    tab4_b.place(x=1300, y=740)
    c3 = Canvas(root, bg='grey', width=400, height=50, highlightbackground="grey")
    c3.place(x=600, y=740)
    c3.create_text(200, 25, text="Preset Selection", font="Calibri 20", fill="black")

    tab5_b = Button(root, text='      1      ', font=('Calibri', 20), bg='blue', fg='white', command=fault1_page)
    tab5_b.place(x=150, y=350)
    tab6_b = Button(root, text='      2      ', font=('Calibri', 20), bg='blue', fg='white', command=fault2_page)
    tab6_b.place(x=550, y=350)
    tab7_b = Button(root, text='      3      ', font=('Calibri', 20), bg='blue', fg='white', command=fault3_page)
    tab7_b.place(x=950, y=350)
    tab8_b = Button(root, text='      4      ', font=('Calibri', 20), bg='blue', fg='white', command=fault4_page)
    tab8_b.place(x=1350, y=350)
    tab9_b = Button(root, text='      5      ', font=('Calibri', 20), bg='blue', fg='white', command=fault5_page)
    tab9_b.place(x=150, y=550)
    tab10_b = Button(root, text='      6      ', font=('Calibri', 20), bg='blue', fg='white', command=fault6_page)
    tab10_b.place(x=550, y=550)
    tab11_b = Button(root, text='      7      ', font=('Calibri', 20), bg='blue', fg='white', command=fault7_page)
    tab11_b.place(x=950, y=550)
    tab12_b = Button(root, text='      8      ', font=('Calibri', 20), bg='blue', fg='white', command=fault8_page)
    tab12_b.place(x=1350, y=550)


def fault1_page():  # Fault 1
    clear_frame()
    global my_img
    canv1 = Canvas(root, bg='white', width=1600, height=1000)
    canv1.place(x=1, y=1)
    label1 = Label(root, text='    Step 1    ', bg='grey', fg='blue', font=('Arial Black', 20))
    label1.place(x=200, y=325)

    my_img = ImageTk.PhotoImage(Image.open("LE_Logo.png"))  # LE Logo
    my_label = Label(image=my_img)
    my_label.grid(column=1, row=0)

    canv2 = Canvas(root, bg='blue', width=600, height=200)  # Blue Box in every page
    canv2.place(x=1000, y=1)
    canv2.create_text(300, 50, text="Substation Technical", font="Calibri 45", fill="white")
    canv2.create_text(300, 120, text="Training Simulator", font="Calibri 45", fill="white")

    strip1 = Canvas(root, bg='grey', width=1575, height=100)  # Grey border at bottom with buttons
    strip1.place(x=1, y=725)
    tab3_b = Button(root, text='Back', font=('Calibri', 20), bg='grey', border=0, command=faults_selection_page)
    tab3_b.place(x=140, y=740)
    tab4_b = Button(root, text='Go to Main', font=('Calibri', 20), bg='grey', border=0, command=main_page)
    tab4_b.place(x=1300, y=740)
    c3 = Canvas(root, bg='grey', width=400, height=50, highlightbackground="grey")
    c3.place(x=600, y=740)
    c3.create_text(200, 25, text="Fault 1 Simulation", font="Calibri 20", fill="black")

    tab5_b = Button(root, text='   Next   ', font=('Calibri', 20), bg='blue', fg='white',
                    command=fault2_page)  # Add a command for going to next fault
    tab5_b.place(x=1200, y=400)
    tab6_b = Button(root, text='   Back   ', font=('Calibri', 20), bg='blue', fg='white')
    tab6_b.place(x=1200, y=500)


def fault2_page():  # Fault 2
    clear_frame()
    global my_img
    canv1 = Canvas(root, bg='white', width=1600, height=1000)
    canv1.place(x=1, y=1)
    label1 = Label(root, text='    Step 2    ', bg='grey', fg='blue', font=('Arial Black', 20))
    label1.place(x=200, y=325)

    my_img = ImageTk.PhotoImage(Image.open("LE_Logo.png"))  # LE Logo
    my_label = Label(image=my_img)
    my_label.grid(column=1, row=0)

    canv2 = Canvas(root, bg='blue', width=600, height=200)  # Blue Box in every page
    canv2.place(x=1000, y=1)
    canv2.create_text(300, 50, text="Substation Technical", font="Calibri 45", fill="white")
    canv2.create_text(300, 120, text="Training Simulator", font="Calibri 45", fill="white")

    strip1 = Canvas(root, bg='grey', width=1575, height=100)  # Grey border at bottom with buttons
    strip1.place(x=1, y=725)
    tab3_b = Button(root, text='Back', font=('Calibri', 20), bg='grey', border=0, command=faults_selection_page)
    tab3_b.place(x=140, y=740)
    tab4_b = Button(root, text='Go to Main', font=('Calibri', 20), bg='grey', border=0, command=main_page)
    tab4_b.place(x=1300, y=740)
    c3 = Canvas(root, bg='grey', width=400, height=50, highlightbackground="grey")
    c3.place(x=600, y=740)
    c3.create_text(200, 25, text="Fault 2 Simulation", font="Calibri 20", fill="black")

    tab5_b = Button(root, text='   Next   ', font=('Calibri', 20), bg='blue', fg='white',
                    command=fault3_page)  # Add a command for going to next fault
    tab5_b.place(x=1200, y=400)
    tab6_b = Button(root, text='   Back   ', font=('Calibri', 20), bg='blue', fg='white', command=fault1_page)
    tab6_b.place(x=1200, y=500)


def fault3_page():  # Fault 3
    clear_frame()
    global my_img
    canv1 = Canvas(root, bg='white', width=1600, height=1000)
    canv1.place(x=1, y=1)
    label1 = Label(root, text='    Step 3    ', bg='grey', fg='blue', font=('Arial Black', 20))
    label1.place(x=200, y=325)

    my_img = ImageTk.PhotoImage(Image.open("LE_Logo.png"))  # LE Logo
    my_label = Label(image=my_img)
    my_label.grid(column=1, row=0)

    canv2 = Canvas(root, bg='blue', width=600, height=200)  # Blue Box in every page
    canv2.place(x=1000, y=1)
    canv2.create_text(300, 50, text="Substation Technical", font="Calibri 45", fill="white")
    canv2.create_text(300, 120, text="Training Simulator", font="Calibri 45", fill="white")

    strip1 = Canvas(root, bg='grey', width=1575, height=100)  # Grey border at bottom with buttons
    strip1.place(x=1, y=725)
    tab3_b = Button(root, text='Back', font=('Calibri', 20), bg='grey', border=0, command=faults_selection_page)
    tab3_b.place(x=140, y=740)
    tab4_b = Button(root, text='Go to Main', font=('Calibri', 20), bg='grey', border=0, command=main_page)
    tab4_b.place(x=1300, y=740)
    c3 = Canvas(root, bg='grey', width=400, height=50, highlightbackground="grey")
    c3.place(x=600, y=740)
    c3.create_text(200, 25, text="Fault 3 Simulation", font="Calibri 20", fill="black")

    tab5_b = Button(root, text='   Next   ', font=('Calibri', 20), bg='blue', fg='white',
                    command=fault4_page)  # Add a command for going to next fault
    tab5_b.place(x=1200, y=400)
    tab6_b = Button(root, text='   Back   ', font=('Calibri', 20), bg='blue', fg='white', command=fault2_page)
    tab6_b.place(x=1200, y=500)


def fault4_page():  # Fault 4
    clear_frame()
    global my_img
    canv1 = Canvas(root, bg='white', width=1600, height=1000)
    canv1.place(x=1, y=1)
    label1 = Label(root, text='    Step 4    ', bg='grey', fg='blue', font=('Arial Black', 20))
    label1.place(x=200, y=325)

    my_img = ImageTk.PhotoImage(Image.open("LE_Logo.png"))  # LE Logo
    my_label = Label(image=my_img)
    my_label.grid(column=1, row=0)

    canv2 = Canvas(root, bg='blue', width=600, height=200)  # Blue Box in every page
    canv2.place(x=1000, y=1)
    canv2.create_text(300, 50, text="Substation Technical", font="Calibri 45", fill="white")
    canv2.create_text(300, 120, text="Training Simulator", font="Calibri 45", fill="white")

    strip1 = Canvas(root, bg='grey', width=1575, height=100)  # Grey border at bottom with buttons
    strip1.place(x=1, y=725)
    tab3_b = Button(root, text='Back', font=('Calibri', 20), bg='grey', border=0, command=faults_selection_page)
    tab3_b.place(x=140, y=740)
    tab4_b = Button(root, text='Go to Main', font=('Calibri', 20), bg='grey', border=0, command=main_page)
    tab4_b.place(x=1300, y=740)
    c3 = Canvas(root, bg='grey', width=400, height=50, highlightbackground="grey")
    c3.place(x=600, y=740)
    c3.create_text(200, 25, text="Fault 4 Simulation", font="Calibri 20", fill="black")

    tab5_b = Button(root, text='   Next   ', font=('Calibri', 20), bg='blue', fg='white',
                    command=fault5_page)  # Add a command for going to next fault
    tab5_b.place(x=1200, y=400)
    tab6_b = Button(root, text='   Back   ', font=('Calibri', 20), bg='blue', fg='white', command=fault3_page)
    tab6_b.place(x=1200, y=500)


def fault5_page():  # Fault 5
    clear_frame()
    global my_img
    canv1 = Canvas(root, bg='white', width=1600, height=1000)
    canv1.place(x=1, y=1)
    label1 = Label(root, text='    Step 5    ', bg='grey', fg='blue', font=('Arial Black', 20))
    label1.place(x=200, y=325)

    my_img = ImageTk.PhotoImage(Image.open("LE_Logo.png"))  # LE Logo
    my_label = Label(image=my_img)
    my_label.grid(column=1, row=0)

    canv2 = Canvas(root, bg='blue', width=600, height=200)  # Blue Box in every page
    canv2.place(x=1000, y=1)
    canv2.create_text(300, 50, text="Substation Technical", font="Calibri 45", fill="white")
    canv2.create_text(300, 120, text="Training Simulator", font="Calibri 45", fill="white")

    strip1 = Canvas(root, bg='grey', width=1575, height=100)  # Grey border at bottom with buttons
    strip1.place(x=1, y=725)
    tab3_b = Button(root, text='Back', font=('Calibri', 20), bg='grey', border=0, command=faults_selection_page)
    tab3_b.place(x=140, y=740)
    tab4_b = Button(root, text='Go to Main', font=('Calibri', 20), bg='grey', border=0, command=main_page)
    tab4_b.place(x=1300, y=740)
    c3 = Canvas(root, bg='grey', width=400, height=50, highlightbackground="grey")
    c3.place(x=600, y=740)
    c3.create_text(200, 25, text="Fault 5 Simulation", font="Calibri 20", fill="black")

    tab5_b = Button(root, text='   Next   ', font=('Calibri', 20), bg='blue', fg='white',
                    command=fault6_page)  # Add a command for going to next fault
    tab5_b.place(x=1200, y=400)
    tab6_b = Button(root, text='   Back   ', font=('Calibri', 20), bg='blue', fg='white', command=fault4_page)
    tab6_b.place(x=1200, y=500)


def fault6_page():  # Fault 6
    clear_frame()
    global my_img
    canv1 = Canvas(root, bg='white', width=1600, height=1000)
    canv1.place(x=1, y=1)
    label1 = Label(root, text='    Step 6    ', bg='grey', fg='blue', font=('Arial Black', 20))
    label1.place(x=200, y=325)

    my_img = ImageTk.PhotoImage(Image.open("LE_Logo.png"))  # LE Logo
    my_label = Label(image=my_img)
    my_label.grid(column=1, row=0)

    canv2 = Canvas(root, bg='blue', width=600, height=200)  # Blue Box in every page
    canv2.place(x=1000, y=1)
    canv2.create_text(300, 50, text="Substation Technical", font="Calibri 45", fill="white")
    canv2.create_text(300, 120, text="Training Simulator", font="Calibri 45", fill="white")

    strip1 = Canvas(root, bg='grey', width=1575, height=100)  # Grey border at bottom with buttons
    strip1.place(x=1, y=725)
    tab3_b = Button(root, text='Back', font=('Calibri', 20), bg='grey', border=0, command=faults_selection_page)
    tab3_b.place(x=140, y=740)
    tab4_b = Button(root, text='Go to Main', font=('Calibri', 20), bg='grey', border=0, command=main_page)
    tab4_b.place(x=1300, y=740)
    c3 = Canvas(root, bg='grey', width=400, height=50, highlightbackground="grey")
    c3.place(x=600, y=740)
    c3.create_text(200, 25, text="Fault 6 Simulation", font="Calibri 20", fill="black")

    tab5_b = Button(root, text='   Next   ', font=('Calibri', 20), bg='blue', fg='white',
                    command=fault7_page)  # Add a command for going to next fault
    tab5_b.place(x=1200, y=400)
    tab6_b = Button(root, text='   Back   ', font=('Calibri', 20), bg='blue', fg='white', command=fault5_page)
    tab6_b.place(x=1200, y=500)


def fault7_page():  # Fault 7
    clear_frame()
    global my_img
    canv1 = Canvas(root, bg='white', width=1600, height=1000)
    canv1.place(x=1, y=1)
    label1 = Label(root, text='    Step 7    ', bg='grey', fg='blue', font=('Arial Black', 20))
    label1.place(x=200, y=325)

    my_img = ImageTk.PhotoImage(Image.open("LE_Logo.png"))  # LE Logo
    my_label = Label(image=my_img)
    my_label.grid(column=1, row=0)

    canv2 = Canvas(root, bg='blue', width=600, height=200)  # Blue Box in every page
    canv2.place(x=1000, y=1)
    canv2.create_text(300, 50, text="Substation Technical", font="Calibri 45", fill="white")
    canv2.create_text(300, 120, text="Training Simulator", font="Calibri 45", fill="white")

    strip1 = Canvas(root, bg='grey', width=1575, height=100)  # Grey border at bottom with buttons
    strip1.place(x=1, y=725)
    tab3_b = Button(root, text='Back', font=('Calibri', 20), bg='grey', border=0, command=faults_selection_page)
    tab3_b.place(x=140, y=740)
    tab4_b = Button(root, text='Go to Main', font=('Calibri', 20), bg='grey', border=0, command=main_page)
    tab4_b.place(x=1300, y=740)
    c3 = Canvas(root, bg='grey', width=400, height=50, highlightbackground="grey")
    c3.place(x=600, y=740)
    c3.create_text(200, 25, text="Fault 7 Simulation", font="Calibri 20", fill="black")

    tab5_b = Button(root, text='   Next   ', font=('Calibri', 20), bg='blue', fg='white',
                    command=fault8_page)  # Add a command for going to next fault
    tab5_b.place(x=1200, y=400)
    tab6_b = Button(root, text='   Back   ', font=('Calibri', 20), bg='blue', fg='white', command=fault6_page)
    tab6_b.place(x=1200, y=500)


def fault8_page():  # Fault 8
    clear_frame()
    global my_img
    canv1 = Canvas(root, bg='white', width=1600, height=1000)
    canv1.place(x=1, y=1)
    label1 = Label(root, text='    Step 8    ', bg='grey', fg='blue', font=('Arial Black', 20))
    label1.place(x=200, y=325)

    my_img = ImageTk.PhotoImage(Image.open("LE_Logo.png"))  # LE Logo
    my_label = Label(image=my_img)
    my_label.grid(column=1, row=0)

    canv2 = Canvas(root, bg='blue', width=600, height=200)  # Blue Box in every page
    canv2.place(x=1000, y=1)
    canv2.create_text(300, 50, text="Substation Technical", font="Calibri 45", fill="white")
    canv2.create_text(300, 120, text="Training Simulator", font="Calibri 45", fill="white")

    strip1 = Canvas(root, bg='grey', width=1575, height=100)  # Grey border at bottom with buttons
    strip1.place(x=1, y=725)
    tab3_b = Button(root, text='Back', font=('Calibri', 20), bg='grey', border=0, command=faults_selection_page)
    tab3_b.place(x=140, y=740)
    tab4_b = Button(root, text='Go to Main', font=('Calibri', 20), bg='grey', border=0, command=main_page)
    tab4_b.place(x=1300, y=740)
    c3 = Canvas(root, bg='grey', width=400, height=50, highlightbackground="grey")
    c3.place(x=600, y=740)
    c3.create_text(200, 25, text="Fault 8 Simulation", font="Calibri 20", fill="black")

    tab5_b = Button(root, text='   Next   ', font=('Calibri', 20), bg='blue',
                    fg='white')  # Add a command for going to next fault
    tab5_b.place(x=1200, y=400)
    tab6_b = Button(root, text='   Back   ', font=('Calibri', 20), bg='blue', fg='white', command=fault7_page)
    tab6_b.place(x=1200, y=500)


def manual_control_page():  # Manual Mode

    clear_frame()
    global my_img
    canv1 = Canvas(root, bg='white', width=1600, height=1000)
    canv1.place(x=1, y=1)
    label1 = Label(root, text='Manual Mode', bg='white', fg='black', font=('Arial Black', 20))
    label1.place(x=700, y=225)

    my_img = ImageTk.PhotoImage(Image.open("LE_Logo.png"))  # LE Logo
    my_label = Label(image=my_img)
    my_label.grid(column=1, row=0)

    canv2 = Canvas(root, bg='blue', width=600, height=200)  # Blue Box in every page
    canv2.place(x=1000, y=1)
    canv2.create_text(300, 50, text="Substation Technical", font="Calibri 45", fill="white")
    canv2.create_text(300, 120, text="Training Simulator", font="Calibri 45", fill="white")

    strip1 = Canvas(root, bg='grey', width=1575, height=100)  # Grey border at bottom with buttons
    strip1.place(x=1, y=725)
    tab3_b = Button(root, text='Back', font=('Calibri', 20), bg='grey', border=0, command=faults_selection_page)
    tab3_b.place(x=140, y=740)
    tab4_b = Button(root, text='Go to Main', font=('Calibri', 20), bg='grey', border=0, command=main_page)
    tab4_b.place(x=1300, y=740)
    c3 = Canvas(root, bg='grey', width=400, height=50, highlightbackground="grey")
    c3.place(x=600, y=740)
    c3.create_text(200, 25, text="Manual Mode", font="Calibri 20", fill="black")

    b1 = Button(root, text='  1  ', font=('Calibri', 20), bg='blue', fg='white')
    b1.place(x=125, y=300)
    b2 = Button(root, text='  2  ', font=('Calibri', 20), bg='blue', fg='white')
    b2.place(x=250, y=300)
    b3 = Button(root, text='  3  ', font=('Calibri', 20), bg='blue', fg='white')
    b3.place(x=375, y=300)
    b4 = Button(root, text='  4  ', font=('Calibri', 20), bg='blue', fg='white')
    b4.place(x=500, y=300)
    b5 = Button(root, text='  5  ', font=('Calibri', 20), bg='blue', fg='white')
    b5.place(x=625, y=300)
    b6 = Button(root, text='  6  ', font=('Calibri', 20), bg='blue', fg='white')
    b6.place(x=750, y=300)
    b7 = Button(root, text='  7  ', font=('Calibri', 20), bg='blue', fg='white')
    b7.place(x=875, y=300)
    b8 = Button(root, text='  8  ', font=('Calibri', 20), bg='blue', fg='white')
    b8.place(x=1000, y=300)
    b9 = Button(root, text='  9  ', font=('Calibri', 20), bg='blue', fg='white')
    b9.place(x=1125, y=300)
    b10 = Button(root, text='10', font=('Calibri', 20), bg='blue', fg='white')
    b10.place(x=1250, y=300)
    b11 = Button(root, text='11', font=('Calibri', 20), bg='blue', fg='white')
    b11.place(x=1375, y=300)

    b12 = Button(root, text=' 12 ', font=('Calibri', 20), bg='blue', fg='white')
    b12.place(x=125, y=375)
    b13 = Button(root, text=' 13 ', font=('Calibri', 20), bg='blue', fg='white')
    b13.place(x=250, y=375)
    b14 = Button(root, text=' 14 ', font=('Calibri', 20), bg='blue', fg='white')
    b14.place(x=375, y=375)
    b15 = Button(root, text=' 15 ', font=('Calibri', 20), bg='blue', fg='white')
    b15.place(x=500, y=375)
    b16 = Button(root, text=' 16 ', font=('Calibri', 20), bg='blue', fg='white')
    b16.place(x=625, y=375)
    b17 = Button(root, text=' 17 ', font=('Calibri', 20), bg='blue', fg='white')
    b17.place(x=750, y=375)
    b18 = Button(root, text=' 18 ', font=('Calibri', 20), bg='blue', fg='white')
    b18.place(x=875, y=375)
    b19 = Button(root, text=' 19 ', font=('Calibri', 20), bg='blue', fg='white')
    b19.place(x=1000, y=375)
    b20 = Button(root, text=' 20 ', font=('Calibri', 20), bg='blue', fg='white')
    b20.place(x=1125, y=375)
    b21 = Button(root, text='21', font=('Calibri', 20), bg='blue', fg='white')
    b21.place(x=1250, y=375)
    b22 = Button(root, text='22', font=('Calibri', 20), bg='blue', fg='white')
    b22.place(x=1375, y=375)

    b23 = Button(root, text=' 23 ', font=('Calibri', 20), bg='blue', fg='white')
    b23.place(x=125, y=450)
    b24 = Button(root, text=' 24 ', font=('Calibri', 20), bg='blue', fg='white')
    b24.place(x=250, y=450)
    b25 = Button(root, text=' 25 ', font=('Calibri', 20), bg='blue', fg='white')
    b25.place(x=375, y=450)
    b26 = Button(root, text=' 26 ', font=('Calibri', 20), bg='blue', fg='white')
    b26.place(x=500, y=450)
    b27 = Button(root, text=' 27 ', font=('Calibri', 20), bg='blue', fg='white')
    b27.place(x=625, y=450)
    b28 = Button(root, text=' 28 ', font=('Calibri', 20), bg='blue', fg='white')
    b28.place(x=750, y=450)
    b29 = Button(root, text=' 29 ', font=('Calibri', 20), bg='blue', fg='white')
    b29.place(x=875, y=450)
    b30 = Button(root, text=' 30 ', font=('Calibri', 20), bg='blue', fg='white')
    b30.place(x=1000, y=450)
    b31 = Button(root, text=' 31 ', font=('Calibri', 20), bg='blue', fg='white')
    b31.place(x=1125, y=450)
    b32 = Button(root, text='32', font=('Calibri', 20), bg='blue', fg='white')
    b32.place(x=1250, y=450)
    b33 = Button(root, text='33', font=('Calibri', 20), bg='blue', fg='white')
    b33.place(x=1375, y=450)

    b34 = Button(root, text=' 23 ', font=('Calibri', 20), bg='blue', fg='white')
    b34.place(x=125, y=525)
    b35 = Button(root, text=' 24 ', font=('Calibri', 20), bg='blue', fg='white')
    b35.place(x=250, y=525)
    b36 = Button(root, text=' 25 ', font=('Calibri', 20), bg='blue', fg='white')
    b36.place(x=375, y=525)
    b37 = Button(root, text=' 26 ', font=('Calibri', 20), bg='blue', fg='white')
    b37.place(x=500, y=525)
    b38 = Button(root, text=' 27 ', font=('Calibri', 20), bg='blue', fg='white')
    b38.place(x=625, y=525)
    b39 = Button(root, text=' 28 ', font=('Calibri', 20), bg='blue', fg='white')
    b39.place(x=750, y=525)
    b40 = Button(root, text=' 29 ', font=('Calibri', 20), bg='blue', fg='white')
    b40.place(x=875, y=525)
    b41 = Button(root, text=' 30 ', font=('Calibri', 20), bg='blue', fg='white')
    b41.place(x=1000, y=525)
    b42 = Button(root, text=' 31 ', font=('Calibri', 20), bg='blue', fg='white')
    b42.place(x=1125, y=525)
    b43 = Button(root, text='32', font=('Calibri', 20), bg='blue', fg='white')
    b43.place(x=1250, y=525)
    b44 = Button(root, text='33', font=('Calibri', 20), bg='blue', fg='white')
    b44.place(x=1375, y=525)

    b45 = Button(root, text=' 45 ', font=('Calibri', 20), bg='blue', fg='white')
    b45.place(x=125, y=600)
    b46 = Button(root, text=' 46 ', font=('Calibri', 20), bg='blue', fg='white')
    b46.place(x=250, y=600)
    b47 = Button(root, text=' 47 ', font=('Calibri', 20), bg='blue', fg='white')
    b47.place(x=375, y=600)
    b48 = Button(root, text=' 48 ', font=('Calibri', 20), bg='blue', fg='white')
    b48.place(x=500, y=600)
    b49 = Button(root, text=' 49 ', font=('Calibri', 20), bg='blue', fg='white')
    b49.place(x=625, y=600)
    b50 = Button(root, text=' 50 ', font=('Calibri', 20), bg='blue', fg='white')
    b50.place(x=750, y=600)
    b51 = Button(root, text=' 51 ', font=('Calibri', 20), bg='blue', fg='white')
    b51.place(x=875, y=600)


main_page()

root.mainloop()