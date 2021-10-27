from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.geometry("1024x600")

frame = Frame(root)
frame.pack(side="top", expand=True, fill="both")

def clear_frame():
   for widgets in root.winfo_children():
      widgets.destroy()

def tab(): #Main Page
    clear_frame()
    global my_img
    
    canv1 = Canvas(root, bg='white', width=1600, height=1000) #1024X600 for everything
    canv1.place(x=1, y=1)


    my_img = ImageTk.PhotoImage(Image.open("LE_Logo.png"))  # LE Logo Resize

    my_label = Label(image=my_img)
    my_label.grid(column=1, row=0)
    #resized=my_img.resize((200, 200))

    STTS = Canvas(root, bg='blue', width = 600, height = 200) #Blue Box in every page 'Substation Technical Training Simulator'
    STTS.place(x=1000, y=1)
    STTS.create_text(300, 50, text="Substation Technical", font="Calibri 45", fill="white")
    STTS.create_text(300, 120, text="Training Simulator", font="Calibri 45", fill= "white")

    greyborder = Canvas(root, bg='grey', width=1600, height=100) #Grey border at bottom of each page with button navigation
    greyborder.place(x=1, y=725)

    simmode = Canvas(root, bg='white', width=400, height=50, highlightbackground = "white")#Simulation mode text
    simmode.place(x=600, y=250)
    simmode.create_text(200, 25, text="Simulation Modes", font="Arial 25 bold", fill="black")

    settings = Button(root, text='Settings', font=('Calibri', 20),bg='grey',border = 0, command= tab1) #Settings Button
    settings.place(x=1400, y=740)
    mainpg = Button(root, text='Main Page', font=('Calibri', 20), bg='grey', border=0)#main page button (doesn't do anything on 1st pg)
    mainpg.place(x=700, y=740)
    back = Button(root, text='Back', font=('Calibri', 20),bg='grey',border = 0)#back button (doesn't do anything on first page)
    back.place(x=140, y=740)
    preset = Button(root, text='Preset Modes', font=('Calibri',20), bg='blue', fg='white', command = tab2)#Presets menu button
    preset.place(x=700, y=400)
    manual = Button(root, text='Manual Control', font=('Calibri',20), bg='blue', fg='white', command = tab11) #Manual control menu button
    manual.place(x=700, y=500)      

def tab1(): #Settings Page
    clear_frame()
    global my_img

    canv1 = Canvas(root, bg='white', width=1600, height=1000)
    canv1.place(x=1, y=1)

    my_img = ImageTk.PhotoImage(Image.open("LE_Logo.png")) #LE Logo
    my_label = Label(image=my_img)
    my_label.grid(column=1, row=0)

    operator_mode= Label(root, text='Operator Mode', bg='white', fg='black', font=('Arial Black', 20)) #Operator mode label
    operator_mode.place(x=200, y=250)
    LEDtest= Label(root, text='LED Tests', bg='white', fg='black', font=('Arial Black', 20)) #LED Test label
    LEDtest.place(x=1200, y=250)

    STTS = Canvas(root, bg='blue', width = 600, height = 200) #Blue Box in every page 'Substation Technical Training Simulator'
    STTS.place(x=1000, y=1)
    STTS.create_text(300, 50, text="Substation Technical", font="Calibri 45", fill="white")
    STTS.create_text(300, 120, text="Training Simulator", font="Calibri 45", fill= "white")

    greyborder = Canvas(root, bg='grey', width=1600, height=100) #Grey border at bottom of each page with button navigation
    greyborder.place(x=1, y=725)

    back = Button(root, text='Back', font=('Calibri', 20),bg='grey',border = 0, command = tab) #back button
    back.place(x=140, y=740)
    mainpg = Button(root, text='Go to Main', font=('Calibri', 20), bg='grey', border = 0, command = tab) #main page button
    mainpg.place(x=1300, y=740)
    sett = Canvas(root, bg='grey', width=400, height=50, highlightbackground = "grey") #settings page label
    sett.place(x=600, y=740)
    sett.create_text(200, 25, text="Settings", font="Calibri 20", fill="black")

    tog = Button(root, text='Sequential Toggle', font=('Calibri',20), bg='blue', fg='white') #add command later #Sequential toggle button
    tog.place(x=1180, y=300)
    AG = Button(root, text='All Green', font=('Calibri',20), bg='blue', fg='white',) #add command later #All Green button
    AG.place(x=1175, y=375)
    AR = Button(root, text='All Red', font=('Calibri',20), bg='blue', fg='white') #add command later #All REd button
    AR.place(x=1325, y=375)
    LH = Button(root, text='Left Handed', font = ('Calibri', 20), bg='grey', fg='white') #Left Handed mode button
    LH.place(x=185, y=325)
    RH = Button(root, text='Right Handed', font = ('Calibri', 20), bg='blue', fg='white') #Right Handed mode button
    RH.place(x=375, y=325)


def tab2(): #Faults Page
    clear_frame()
    global my_img
    canv1 = Canvas(root, bg='white', width=1600, height=1000)
    canv1.place(x=1, y=1)
    label1= Label(root, text='Preset Faults', bg='white', fg='black', font=('Arial Black', 20))
    label1.place(x=200, y=250)

    my_img = ImageTk.PhotoImage(Image.open("LE_Logo.png")) #LE Logo
    my_label = Label(image=my_img)
    my_label.grid(column=1, row=0)

    STTS = Canvas(root, bg='blue', width = 600, height = 200) #Blue Box in every page 'Substation Technical Training Simulator'
    STTS.place(x=1000, y=1)
    STTS.create_text(300, 50, text="Substation Technical", font="Calibri 45", fill="white")
    STTS.create_text(300, 120, text="Training Simulator", font="Calibri 45", fill= "white")

    greyborder = Canvas(root, bg='grey', width=1600, height=100) #Grey border at bottom of each page with button navigation
    greyborder.place(x=1, y=725)

    back = Button(root, text='Back', font=('Calibri', 20),bg='grey',border = 0, command = tab) #back button to Faults Page
    back.place(x=140, y=740)
    mainpg = Button(root, text='Go to Main', font=('Calibri', 20), bg='grey', border = 0, command = tab) #main page button
    mainpg.place(x=1300, y=740)
    preset = Canvas(root, bg='grey', width=400, height=50, highlightbackground = "grey") #Preset Selection page label
    preset.place(x=600, y=740)
    preset.create_text(200, 25, text="Preset Selection", font="Calibri 20", fill="black")

    flt1 = Button(root, text='      1      ', font=('Calibri',20), bg='blue', fg='white', command = tab3) #fault 1
    flt1.place(x=150, y=350)
    flt2 = Button(root, text='      2      ', font=('Calibri',20), bg='blue', fg='white', command = tab4) #fault 2
    flt2.place(x=550, y=350)
    flt3 = Button(root, text='      3      ', font=('Calibri',20), bg='blue', fg='white', command = tab5) #fault 3
    flt3.place(x=950, y=350)
    flt4 = Button(root, text='      4      ', font=('Calibri',20), bg='blue', fg='white', command = tab6) #fault 4
    flt4.place(x=1350, y=350)
    flt5 = Button(root, text='      5      ', font=('Calibri',20), bg='blue', fg='white', command = tab7) #fault 5
    flt5.place(x=150, y=550)
    flt6 = Button(root, text='      6      ', font=('Calibri',20), bg='blue', fg='white', command = tab8) #fault 6
    flt6.place(x=550, y=550)
    flt7 = Button(root, text='      7      ', font=('Calibri',20), bg='blue', fg='white', command = tab9) #fault 7
    flt7.place(x=950, y=550)
    flt8 = Button(root, text='      8      ', font=('Calibri',20), bg='blue', fg='white', command = tab10) #fault 8
    flt8.place(x=1350, y=550)


def tab3(): #Fault 1
    clear_frame()
    global my_img

    canv1 = Canvas(root, bg='white', width=1600, height=1000)
    canv1.place(x=1, y=1)
    stp1= Label(root, text='    Step 1    ', bg='grey', fg='blue', font=('Arial Black', 20), width=10, height=2) #Step 1 Page label
    stp1.place(x=710, y=400)

    my_img = ImageTk.PhotoImage(Image.open("LE_Logo.png")) #LE Logo
    my_label = Label(image=my_img)
    my_label.grid(column=1, row=0)
    
    STTS = Canvas(root, bg='blue', width = 600, height = 200) #Blue Box in every page 'Substation Technical Training Simulator'
    STTS.place(x=1000, y=1)
    STTS.create_text(300, 50, text="Substation Technical", font="Calibri 45", fill="white")
    STTS.create_text(300, 120, text="Training Simulator", font="Calibri 45", fill= "white")

    greyborder = Canvas(root, bg='grey', width=1600, height=100) #Grey border at bottom of each page with button navigation
    greyborder.place(x=1, y=725)

    back1 = Button(root, text='Back', font=('Calibri', 20),bg='grey',border = 0, command = tab2) #back button to Faults Page
    back1.place(x=140, y=740)
    mainpg = Button(root, text='Go to Main', font=('Calibri', 20), bg='grey', border = 0, command = tab) #Main page button
    mainpg.place(x=1300, y=740)
    fltsim1 = Canvas(root, bg='grey', width=400, height=50, highlightbackground = "grey") #Fault simulation 1 label
    fltsim1.place(x=600, y=740)
    fltsim1.create_text(200, 25, text="Fault 1 Simulation", font="Calibri 20", fill="black")

    nxt = Button(root, text='         Next         ', font=('Calibri',20), bg='blue', fg='white', height = 2, command = tab4) #next fault button 
    nxt.place(x=1015, y=400)
    back2 = Button(root, text='         Back         ', font=('Calibri',20), bg='blue', fg='white', height = 2) #back button to previous fault. doesn't do anything on 1.
    back2.place(x=400, y=400)

def tab4(): #Fault 2
    clear_frame()
    global my_img

    canv1 = Canvas(root, bg='white', width=1600, height=1000)
    canv1.place(x=1, y=1)
    stp2= Label(root, text='    Step 2    ', bg='grey', fg='blue', font=('Arial Black', 20), width=10, height=2) #Step 2 Page label
    stp2.place(x=710, y=400)

    my_img = ImageTk.PhotoImage(Image.open("LE_Logo.png")) #LE Logo
    my_label = Label(image=my_img)
    my_label.grid(column=1, row=0)
    
    STTS = Canvas(root, bg='blue', width = 600, height = 200) #Blue Box in every page 'Substation Technical Training Simulator'
    STTS.place(x=1000, y=1)
    STTS.create_text(300, 50, text="Substation Technical", font="Calibri 45", fill="white")
    STTS.create_text(300, 120, text="Training Simulator", font="Calibri 45", fill= "white")

    greyborder = Canvas(root, bg='grey', width=1600, height=100) #Grey border at bottom of each page with button navigation
    greyborder.place(x=1, y=725)

    back1 = Button(root, text='Back', font=('Calibri', 20),bg='grey',border = 0, command = tab2) #back button to Faults Page
    back1.place(x=140, y=740)
    mainpg = Button(root, text='Go to Main', font=('Calibri', 20), bg='grey', border = 0, command = tab) #main page button
    mainpg.place(x=1300, y=740)
    fltsim2 = Canvas(root, bg='grey', width=400, height=50, highlightbackground = "grey") #Fault simulation 2 label
    fltsim2.place(x=600, y=740)
    fltsim2.create_text(200, 25, text="Fault 2 Simulation", font="Calibri 20", fill="black")

    nxt = Button(root, text='         Next         ', font=('Calibri',20), bg='blue', fg='white', height = 2, command = tab5) #next fault button 
    nxt.place(x=1015, y=400)
    back2 = Button(root, text='         Back         ', font=('Calibri',20), bg='blue', fg='white', height = 2, command = tab3) #back to fault 1.
    back2.place(x=400, y=400)

def tab5(): #Fault 3
    clear_frame()
    global my_img

    canv1 = Canvas(root, bg='white', width=1600, height=1000)
    canv1.place(x=1, y=1)
    stp3= Label(root, text='    Step 3    ', bg='grey', fg='blue', font=('Arial Black', 20), width=10, height=2) #Step 3 Page label
    stp3.place(x=710, y=400)

    my_img = ImageTk.PhotoImage(Image.open("LE_Logo.png")) #LE Logo
    my_label = Label(image=my_img)
    my_label.grid(column=1, row=0)
    
    STTS = Canvas(root, bg='blue', width = 600, height = 200) #Blue Box in every page 'Substation Technical Training Simulator'
    STTS.place(x=1000, y=1)
    STTS.create_text(300, 50, text="Substation Technical", font="Calibri 45", fill="white")
    STTS.create_text(300, 120, text="Training Simulator", font="Calibri 45", fill= "white")

    greyborder = Canvas(root, bg='grey', width=1600, height=100) #Grey border at bottom of each page with button navigation
    greyborder.place(x=1, y=725)

    back1 = Button(root, text='Back', font=('Calibri', 20),bg='grey',border = 0, command = tab2) #Back button to Faults page
    back1.place(x=140, y=740)
    mainpg = Button(root, text='Go to Main', font=('Calibri', 20), bg='grey', border = 0, command = tab) #Main page button
    mainpg.place(x=1300, y=740)
    fltsim3 = Canvas(root, bg='grey', width=400, height=50, highlightbackground = "grey") #Fault simulation 3 label
    fltsim3.place(x=600, y=740)
    fltsim3.create_text(200, 25, text="Fault 3 Simulation", font="Calibri 20", fill="black")

    nxt = Button(root, text='         Next         ', font=('Calibri',20), bg='blue', fg='white', height = 2, command = tab6) #next fault button 
    nxt.place(x=1015, y=400)
    back2 = Button(root, text='         Back         ', font=('Calibri',20), bg='blue', fg='white', height = 2, command = tab4) #back to fault 2
    back2.place(x=400, y=400)

def tab6(): #Fault 4 
    clear_frame()
    global my_img
    canv1 = Canvas(root, bg='white', width=1600, height=1000)
    canv1.place(x=1, y=1)
    stp4= Label(root, text='    Step 4    ', bg='grey', fg='blue', font=('Arial Black', 20), width=10, height=2) #Step 4 Page label
    stp4.place(x=710, y=400)

    my_img = ImageTk.PhotoImage(Image.open("LE_Logo.png")) #LE Logo
    my_label = Label(image=my_img)
    my_label.grid(column=1, row=0)
    
    STTS = Canvas(root, bg='blue', width = 600, height = 200) #Blue Box in every page 'Substation Technical Training Simulator'
    STTS.place(x=1000, y=1)
    STTS.create_text(300, 50, text="Substation Technical", font="Calibri 45", fill="white")
    STTS.create_text(300, 120, text="Training Simulator", font="Calibri 45", fill= "white")

    greyborder = Canvas(root, bg='grey', width=1600, height=100) #Grey border at bottom of each page with button navigation
    greyborder.place(x=1, y=725)

    back1 = Button(root, text='Back', font=('Calibri', 20),bg='grey',border = 0, command = tab2) #back button to Faults page
    back1.place(x=140, y=740)
    mainpg = Button(root, text='Go to Main', font=('Calibri', 20), bg='grey', border = 0, command = tab) #Main page button
    mainpg.place(x=1300, y=740)
    fltsim4 = Canvas(root, bg='grey', width=400, height=50, highlightbackground = "grey") #fault simulation 4 label
    fltsim4.place(x=600, y=740)
    fltsim4.create_text(200, 25, text="Fault 4 Simulation", font="Calibri 20", fill="black")

    nxt = Button(root, text='   Next   ', font=('Calibri',20), bg='blue', fg='white', command = tab7) #Next fault button 
    nxt.place(x=1015, y=400)
    nxt = Button(root, text='         Next         ', font=('Calibri',20), bg='blue', fg='white', height = 2, command = tab7) #next fault button 
    nxt.place(x=1015, y=400)
    back2 = Button(root, text='         Back         ', font=('Calibri',20), bg='blue', fg='white', height = 2, command = tab5) #back to fault 3
    back2.place(x=400, y=400)

def tab7(): #Fault 5
    clear_frame()
    global my_img
    canv1 = Canvas(root, bg='white', width=1600, height=1000)
    canv1.place(x=1, y=1)
    stp5= Label(root, text='    Step 5    ', bg='grey', fg='blue', font=('Arial Black', 20), width=10, height=2) #Step 5 Page label
    stp5.place(x=710, y=400)

    my_img = ImageTk.PhotoImage(Image.open("LE_Logo.png")) #LE LogoSTTS
    my_label = Label(image=my_img)
    my_label.grid(column=1, row=0)
    
    STTS = Canvas(root, bg='blue', width = 600, height = 200) #Blue Box in every page 'Substation Technical Training Simulator'
    STTS.place(x=1000, y=1)
    STTS.create_text(300, 50, text="Substation Technical", font="Calibri 45", fill="white")
    STTS.create_text(300, 120, text="Training Simulator", font="Calibri 45", fill= "white")

    greyborder = Canvas(root, bg='grey', width=1600, height=100) #Grey border at bottom of each page with button navigation
    greyborder.place(x=1, y=725)

    back1 = Button(root, text='Back', font=('Calibri', 20),bg='grey',border = 0, command = tab2) #back button to faults page
    back1.place(x=140, y=740)
    mainpg = Button(root, text='Go to Main', font=('Calibri', 20), bg='grey', border = 0, command = tab) #Main page button
    mainpg.place(x=1300, y=740)
    fltsim5 = Canvas(root, bg='grey', width=400, height=50, highlightbackground = "grey") #fault simulation 5 label
    fltsim5.place(x=600, y=740)
    fltsim5.create_text(200, 25, text="Fault 5 Simulation", font="Calibri 20", fill="black")

    nxt = Button(root, text='   Next   ', font=('Calibri',20), bg='blue', fg='white', command = tab8) #Next fault button 
    nxt.place(x=1015, y=400)
    nxt = Button(root, text='         Next         ', font=('Calibri',20), bg='blue', fg='white', height = 2, command = tab8) #next fault button 
    nxt.place(x=1015, y=400)
    back2 = Button(root, text='         Back         ', font=('Calibri',20), bg='blue', fg='white', height = 2, command = tab6) #back to fault 4
    back2.place(x=400, y=400)

def tab8(): #Fault 6
    clear_frame()
    global my_img
    canv1 = Canvas(root, bg='white', width=1600, height=1000)
    canv1.place(x=1, y=1)
    stp6= Label(root, text='    Step 6    ', bg='grey', fg='blue', font=('Arial Black', 20), width=10, height=2) #Step 6 Page label
    stp6.place(x=710, y=400)

    my_img = ImageTk.PhotoImage(Image.open("LE_Logo.png")) #LE Logo
    my_label = Label(image=my_img)
    my_label.grid(column=1, row=0)
    
    STTS = Canvas(root, bg='blue', width = 600, height = 200) #Blue Box in every page 'Substation Technical Training Simulator'
    STTS.place(x=1000, y=1)
    STTS.create_text(300, 50, text="Substation Technical", font="Calibri 45", fill="white")
    STTS.create_text(300, 120, text="Training Simulator", font="Calibri 45", fill= "white")

    greyborder = Canvas(root, bg='grey', width=1600, height=100) #Grey border at bottom with buttons
    greyborder.place(x=1, y=725)

    back1 = Button(root, text='Back', font=('Calibri', 20),bg='grey',border = 0, command = tab2) #back button to faults page
    back1.place(x=140, y=740)
    mainpg = Button(root, text='Go to Main', font=('Calibri', 20), bg='grey', border = 0, command = tab) #Main page button
    mainpg.place(x=1300, y=740)
    fltsim6 = Canvas(root, bg='grey', width=400, height=50, highlightbackground = "grey") #fault simulation 6 label
    fltsim6.place(x=600, y=740)
    fltsim6.create_text(200, 25, text="Fault 6 Simulation", font="Calibri 20", fill="black")

    nxt = Button(root, text='         Next         ', font=('Calibri',20), bg='blue', fg='white', height = 2, command = tab9) #next fault button 
    nxt.place(x=1015, y=400)
    back2 = Button(root, text='         Back         ', font=('Calibri',20), bg='blue', fg='white', height = 2, command = tab7) #back to fault 5
    back2.place(x=400, y=400)

def tab9(): #Fault 7
    clear_frame()
    global my_img
    canv1 = Canvas(root, bg='white', width=1600, height=1000)
    canv1.place(x=1, y=1)
    stp7= Label(root, text='    Step 7    ', bg='grey', fg='blue', font=('Arial Black', 20), width=10, height=2) #Step 7 Page label
    stp7.place(x=710, y=400)

    my_img = ImageTk.PhotoImage(Image.open("LE_Logo.png")) #LE Logo
    my_label = Label(image=my_img)
    my_label.grid(column=1, row=0)
    
    STTS = Canvas(root, bg='blue', width = 600, height = 200) #Blue Box in every page 'Substation Technical Training Simulator'
    STTS.place(x=1000, y=1)
    STTS.create_text(300, 50, text="Substation Technical", font="Calibri 45", fill="white")
    STTS.create_text(300, 120, text="Training Simulator", font="Calibri 45", fill= "white")

    greyborder = Canvas(root, bg='grey', width=1600, height=100) #Grey border at bottom with buttons
    greyborder.place(x=1, y=725)

    back1 = Button(root, text='Back', font=('Calibri', 20),bg='grey',border = 0, command = tab2) #back button to faults page
    back1.place(x=140, y=740)
    mainpg = Button(root, text='Go to Main', font=('Calibri', 20), bg='grey', border = 0, command = tab) #Main page button
    mainpg.place(x=1300, y=740)
    fltsim7 = Canvas(root, bg='grey', width=400, height=50, highlightbackground = "grey") #fault simulation 7 label
    fltsim7.place(x=600, y=740)
    fltsim7.create_text(200, 25, text="Fault 7 Simulation", font="Calibri 20", fill="black")

    nxt = Button(root, text='         Next         ', font=('Calibri',20), bg='blue', fg='white', height = 2, command = tab10) #next fault button 
    nxt.place(x=1015, y=400)
    back2 = Button(root, text='         Back         ', font=('Calibri',20), bg='blue', fg='white', height = 2, command = tab8) #back to fault 6
    back2.place(x=400, y=400)

def tab10(): #Fault 8
    clear_frame()
    global my_img
    canv1 = Canvas(root, bg='white', width=1600, height=1000)
    canv1.place(x=1, y=1)
    stp8= Label(root, text='    Step 8    ', bg='grey', fg='blue', font=('Arial Black', 20), width=10, height=2) #Step 8 Page label
    stp8.place(x=710, y=400)

    my_img = ImageTk.PhotoImage(Image.open("LE_Logo.png")) #LE Logo
    my_label = Label(image=my_img)
    my_label.grid(column=1, row=0)
    
    STTS = Canvas(root, bg='blue', width = 600, height = 200) #Blue Box in every page 'Substation Technical Training Simulator'
    STTS.place(x=1000, y=1)
    STTS.create_text(300, 50, text="Substation Technical", font="Calibri 45", fill="white")
    STTS.create_text(300, 120, text="Training Simulator", font="Calibri 45", fill= "white")

    greyborder = Canvas(root, bg='grey', width=1600, height=100) #Grey border at bottom with buttons
    greyborder.place(x=1, y=725)

    back1 = Button(root, text='Back', font=('Calibri', 20),bg='grey',border = 0, command = tab2) #back button to faults page
    back1.place(x=140, y=740)
    mainpg = Button(root, text='Go to Main', font=('Calibri', 20), bg='grey', border = 0, command = tab) #Main page button
    mainpg.place(x=1300, y=740)
    fltsim8 = Canvas(root, bg='grey', width=400, height=50, highlightbackground = "grey") #fault simulation 8 label
    fltsim8.place(x=600, y=740)
    fltsim8.create_text(200, 25, text="Fault 8 Simulation", font="Calibri 20", fill="black")

    nxt = Button(root, text='         Next         ', font=('Calibri',20), bg='blue', fg='white', height = 2) #next fault button. Doesn't do anything
    nxt.place(x=1015, y=400)
    back2 = Button(root, text='         Back         ', font=('Calibri',20), bg='blue', fg='white', height = 2, command = tab9) #back to fault 7
    back2.place(x=400, y=400)

def tab11(): #Manual Mode

    clear_frame()
    global my_img

    canv1 = Canvas(root, bg='white', width=1600, height=1000)
    canv1.place(x=1, y=1)
    manual_mode1= Label(root, text='Manual Mode', bg='white', fg='black', font=('Arial Black', 20)) #Manual mode page label
    manual_mode1.place(x=700, y=225)

    my_img = ImageTk.PhotoImage(Image.open("LE_Logo.png")) #LE Logo
    my_label = Label(image=my_img)
    my_label.grid(column=1, row=0)
    
    STTS = Canvas(root, bg='blue', width = 600, height = 200) #Blue Box in every page 'Substation Technical Training Simulator'
    STTS.place(x=1000, y=1)
    STTS.create_text(300, 50, text="Substation Technical", font="Calibri 45", fill="white")
    STTS.create_text(300, 120, text="Training Simulator", font="Calibri 45", fill= "white")

    greyborder = Canvas(root, bg='grey', width=1600, height=100) #Grey border at bottom with buttons
    greyborder.place(x=1, y=725)

    back1 = Button(root, text='Back', font=('Calibri', 20),bg='grey',border = 0, command = tab2) #back button to faults page
    back1.place(x=140, y=740)
    mainpg = Button(root, text='Go to Main', font=('Calibri', 20), bg='grey', border = 0, command = tab) #Main page button
    mainpg.place(x=1300, y=740)
    manual_mode2 = Canvas(root, bg='grey', width=400, height=50, highlightbackground = "grey") #Manual mode page label
    manual_mode2.place(x=600, y=740)
    manual_mode2.create_text(200, 25, text="Manual Mode", font="Calibri 20", fill="black")

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

tab()

root.mainloop()