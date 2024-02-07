'''Ομάδα 26 Εργασία πρώτου εξαμήνου(Εισαγωγή στους Η/Υ)/My Expenses Tracker'''
#απαραίτητες βιβλιοθήκες
from tkinter import *  #υπάρχει στην Python 3
from tkcalendar import * #pip install   
from PIL import ImageTk, Image
import sqlite3 #υπάρχει στην Python 3
from matplotlib import pyplot as plt #pip install   
import datetime #υπάρχει στην Python 3
#δημιουργία database , database table, 
conn= sqlite3.connect('expenses.db')
c= conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS expenses(money REAL, year INT,month INT, day INT, category TEXT)')
#δημιουργία παραθύρου GUI (tkinter)
window=Tk()
window.title('My Expenses Tracker')
window.iconbitmap("Pictures/code1.ico") #εικονίδο εφαρμογής
window.geometry('800x800')
#window.resizable(False, False)
#δημιουργία των Frame του προγράμματος 
file_new_frame= Frame(window, width= 1483, height=669)
file_new_frame2= Frame(window, width= 1483, height=669)
#Συνάρτηση δημιουργίας widget για το GUI
def widgets():
    #Εισαγωγή εικόνων
    global image1, image2, image3, image4, image5, cal_img, my_img, my_img1, my_img2, my_img3, my_img4, my_img5, cal_img, my_lbl, what_year_lbl, what_year, what_month_lbl, what_month, btn1, btn2, btn3, btn4, btn5, btn6, contact_lbl, text_lbl
    image1 = Image.open("Pictures/plot2.png") 
    image1 = image1.resize((60,60))
    image2 = Image.open("Pictures/bar2.png")
    image2 = image2.resize((55,55))
    image3 = Image.open("Pictures/pie2.png")
    image3 = image3.resize((60,60))
    image4 = Image.open("Pictures/plots.png")
    image4 = image4.resize((60,60))
    image5 = Image.open("Pictures/expense.jpg")
    image5 = image5.resize((60,50))
    cal_img = Image.open('Pictures/calendar.jpg')
    cal_img = cal_img.resize((30,30))
    my_img = ImageTk.PhotoImage(Image.open("Pictures/2.png"))
    my_img1 = ImageTk.PhotoImage(image1)
    my_img2 = ImageTk.PhotoImage(image2)
    my_img3 = ImageTk.PhotoImage(image3)
    my_img4 = ImageTk.PhotoImage(image4)
    my_img5 = ImageTk.PhotoImage(image5)
    cal_img = ImageTk.PhotoImage(cal_img)
    my_lbl=Label(image=my_img)
    my_lbl.grid(column=0, row=45)
    what_year_lbl=Label(file_new_frame2,text="Για ποια χρονιά θα θέλατε διάγραμμα;",font= "arial 12")
    what_year_lbl.grid(column = 0, padx = 0)
    what_year=Entry(file_new_frame2,width=10)
    what_year.insert(END,"2020")
    what_year.grid(column = 0, pady = 40)
    what_month_lbl=Label(file_new_frame2,text="Για ποιο μήνα θα θέλατε επιπλέον διάγραμμα;",font= "arial 12")
    what_month_lbl.grid(column = 1, row = 0, padx = 0)
    what_month = Entry(file_new_frame2, width = 10)
    what_month.insert(END,"1")
    what_month.grid(column = 1, row = 1)
    btn1= Button(file_new_frame2, text="Πίτα έτους  ", anchor=NW, font= "arial 20", command= show_plot3,image=my_img3, compound= RIGHT, bg="lightyellow", height=60)
    btn2= Button(file_new_frame2, text="Διάγραμμα έτους  ", anchor=NW, font= "arial 20", command= show_plot2, image=my_img2, compound= RIGHT, bg="lightyellow", height=60)
    btn3= Button(file_new_frame2, text="Σύγκριση τελευταίων ετών", anchor=NW, font= "arial 20", command= show_plot1, image=my_img1, compound= RIGHT, bg="lightyellow", height=60)
    btn4=Button(file_new_frame2,text="Πίτα μήνα  ",anchor=NW, font= "arial 20", command= show_plot4, image=my_img3, compound= RIGHT, bg="lightyellow", height=60)
    btn5=Button(window, text="Νέο Έξοδο", anchor=NW, font= "arial 20", command=new_expenses, image=my_img5, compound= RIGHT, bg="lightyellow")
    btn5.grid(sticky= "W", pady=30, padx=310)
    btn6=Button(window,text="Διαγράμματα", anchor=NW, font= "arial 20", command=show_diagrams, image=my_img4, compound= RIGHT, bg="lightyellow")
    btn6.grid(sticky="W", padx=295)
    contact_lbl=Label(text= "Γιώργος Στεργιόπουλος: up1083861@upnet.gr\n\n Παναγιώτης Χούσος: up1083869@upnet.gr\n\n Μαριλένα Καραΐτση: up1084043@upnet.gr\n\n Ορέστης Παπαθανασόπουλος: up1083867@upnet.gr\n\n Βίκυ Κασουρίδου: up1083790@upnet.gr\n\n Γιάννης Αναστασόπουλος: up1089185@upnet.gr", font="Arial 12")
    text_lbl=Label(text='''Άν θέλετε να δουλέψετε με κενή Database διαγράψτε το αρχείο expenses.db απο τον φάκελο του \nπρογράμματος, και το πρόγραμμα θα δημιουργήσει οταν τρέξει μια νέα, κενή database\n**H γεμάτη database δίνεται ως Sample, για την εξοικίωση σας με το πρόγραμμα και την \nανακάλυψη των δυνατοτήτων του.\nΕγκαταστήστε το DB Browser for SQL (https://sqlitebrowser.org/dl/) και ορίστε το \nως προεπιλεγμένο πρόγραμμα για άνοιγμα αρχείων τύπου .db \nετσι ώστε να μπορείτε να περιηγηθείτε στην Database σας''', font='arial 12')
#Συνάρτηση καταχώρησεις εξόδων(βασικός πυλώνας του προγράμματος)
'''Η συνάρτηση main αποτέλει τον πυρήνα του προγράμματος και μπορεί με κατάλληλες τροποποιήσεις να λειτουργήσει σαν αυτόνομο πρόγραμμα καταχώρησης εξόδων και αποθήκευσης σε SQL Database
    ξεχωριστά δηλαδή απο την ανάλυση εξόδων που γίνεται στα πλαίσια της Ομαδικής Εργασίας'''
def main():
    #Αρχικό μήνυμα
    def message():
        global lbl
        lbl = Label(file_new_frame, text='Εισάγετε νέο έξοδο:', font='arial 11')
        lbl.grid(column=2, row=0)
        return message
    # Εισαγωγή ποσού
    def expense():
        value = Label(file_new_frame, text='Πόσα χρήματα ξοδέψατε;', font='arial 11')
        value.grid(column=2,row=1)
        txt=Entry(file_new_frame,width=10)
        txt.grid(column=2,row=2, pady=15)
        expense=Label(file_new_frame,text='Το νέο σας έξοδο:', font='arial 11')
        expense.grid(column=7,row=15) 
        #συνάρτηση-αντίδραση στο κουμπί "Καταχώρηση εξόδου"
        def clicked1():
            lbl.configure(text="Επιτυχής καταχώρηση εξόδου", fg='green', font='arial 11')
            lbl.grid(column=3,row=2, padx=0)
            global value1
            if txt.get()=="":
                value1=0
                lbl.configure(text="Λανθασμένη είσοδος", fg="red", font='arial 11')
            elif not txt.get().replace(".","",1).isdigit():
                value1=0
                lbl.configure(text="Λανθασμένη είσοδος", fg="red", font='arial 11')  
            else:
                value1=txt.get()
            global output1
            output1=Label(file_new_frame,text=value1)
            output1.grid(column=8, row=15)
            return clicked1
        btn = Button(file_new_frame, text="Καταχώρηση ποσού", command=clicked1, font='arial 11')
        btn.grid(column=2, row=3)
        return expense
    # Εισαγώγη ημερομηνίας
    def date_final():
        #έξοδος του ημερολογίου και συνάρτηση αντίδραση στο κουμπί "Καταχώρηση"
        def print_sel():
            global value2
            value2=str(cal.selection_get())
            global day 
            day=value2[8:]
            global month
            month=value2[5:7]
            global yeard
            yeard=value2[0:4]
            global output2
            output2=Label(file_new_frame,text=value2)
            output2.grid(column=8,row=16)
            global lbl2
            lbl2=Label(file_new_frame,text="Επιτυχής καταχώρηση ημερομηνίας", fg='green', font='arial 11')
            lbl2.grid(column=3,row=8)
            top.destroy()
            return print_sel
        #δημιουργία αναδυώμενου παραθύρου-ημερολογίου
        top=Toplevel(file_new_frame)
        top.geometry('300x300+600+50')
        cal = Calendar(top,
                   font="Arial 14", selectmode='day',
                   cursor="hand1", year=2021, month=1, day=15)
        cal.pack(fill="both", expand=True)
        dateButton= Button(top, text="Καταχώρηση", command=print_sel, font='arial 11').pack()   
    # Κουμπί προς εμφάνιση ημερολογίου   
    def selectDate():
        dateButton=Button(file_new_frame, text="Εισαγωγή ημερομηνίας εξόδου ", image=cal_img, compound=RIGHT, command=date_final, font='arial 11')
        dateButton.grid(column=2, row=8, pady=15)
        return selectDate
    #Επιλογή κατηγορίας εξόδου
    def category():
        #δημιουργία Listbox με scrollbar
        category=Label(file_new_frame,text='Κατηγορία Εξόδου', font='arial 11')
        category.grid(column=2,row=10)
        my_listbox = Listbox(file_new_frame)
        my_scrollbar=Scrollbar(file_new_frame, orient=VERTICAL, command=my_listbox.yview)
        my_listbox.config(yscrollcommand=my_scrollbar.set, width=25)
        my_scrollbar.config(command=my_listbox.yview)
        my_scrollbar.grid(column=3,row=14, sticky=NS)
        my_listbox.grid(column=2,row=14, padx=0)
        #Κατηγορίες (Βασισμένες σε κατηγορίες εξόδων ελληνικών τραπεζών)
        my_listbox.insert(END,'Super Market')
        my_listbox.insert(END,'Ψυχαγωγία')
        my_listbox.insert(END,'Οικιακά')
        my_listbox.insert(END,'Επικοινωνίες')
        my_listbox.insert(END,'Συνδρομητικές Υπηρεσίες')
        my_listbox.insert(END,'Στέγαση')
        my_listbox.insert(END,'Μεταφόρα/Καύσιμα')
        my_listbox.insert(END,'Επενδύσεις')
        my_listbox.insert(END,'Έξοδα παιδιών')
        my_listbox.insert(END,'Ιατρικά')
        my_listbox.insert(END,'Άλλο')
        global my_label
        my_label=Label(file_new_frame,text='')
        #συνάρτηση-αντίδραση στο κουμπί "Καταχώρηση κατηγορίας εξόδου"
        def clicked3():
            my_label.config(text=my_listbox.get(ANCHOR))
            my_label.grid(column=8,row=17)
            global lbl3
            lbl3=Label(file_new_frame,text="Επιτυχής καταχώρηση κατηγορίας εξόδου", fg='green', font='arial 11')
            lbl3.grid(column=3,row=10)
            global value3
            value3=my_label.cget("text")
            return clicked3
        btn3 = Button(file_new_frame, text="Καταχώρηση κατηγορίας εξόδου ", command=clicked3, font='arial 11')
        btn3.grid(column=2, row=15, pady=10)
        return category
    #Κουμπί καταχώρησης εξόδου και επαναφοράς ωστέ να ξανακαταχωρήσει ο χρήστης άλλο εξοδο
    def resumbit():   
        #Συνάρτηση-αντίδραση στο κουμπί "Καταχώρηση"
        def clicked5():
            #κλήση της συνάρτησης οπου αποθηκεύει στην database
            output()
            #κλήση της main για να επανακατάθεση εξόδου
            main()
            return clicked5
        
        
        btn5= Button(file_new_frame, text="Καταχώρηση", command=clicked5, font='arial 11')
        btn5.grid(column=8, row=19)
        return resumbit
    #Συνάρτηση αποθήκευσης του εξόδου στην SQL Database
    def output():
        global error_lbl
        error_lbl=Label(text="")
        error_lbl.grid()
        #αποφυγή error του προγράμματος σε περίπτωση κενών εισόδων
        try:
            error_lbl.configure(text="")
            L=[value1, yeard, month, day, value3]
            lbl.configure(text="")
            lbl2.configure(text="")
            lbl3.configure(text="")
            output1.configure(text="")
            output2.configure(text="")
            my_label.configure(text="")
        except NameError:
            #Σε περίπτωση κενόυ εξόδου εισάγωνται στην Database μηδενικά και αργότερα έχει προγραμματίστει να σβήνονται
            L=[0,0,0,0,0]
        dynamic_data_entry(L)
        return output
    #Συνάρητηση "γεμίσματος" του πίνακα expenses της SQL Database
    def dynamic_data_entry(L):
            money=float(L[0])
            year=int(L[1])
            month=int(L[2])
            day=int(L[3])
            category= str(L[-1])
            c.execute('Insert into expenses(money, year, month , day , category)VALUES (?,?,?,?,?)',
            (money, year, month, day, category))
            #H διαγραφή των μηδενικών καταχωρήσεων που προαναφέρθηκε
            c.execute("DELETE from expenses where money=0")
            conn.commit()   
    #κλήση των απαραίτητων συναρτήσεων της main, για την καταχώρηση εξόδων 
    message()
    expense()
    selectDate()
    category()
    resumbit()
    return main
#Συνάρτηση "καθαρίσμου" του παραθύρου για εναλλαγή μεταξύ των Frame
def hide_all_frames():
    file_new_frame.grid_forget()
    file_new_frame2.grid_forget()
#Συνάρτηση-αντίδραση στην επιλογή του Menu "Νέο έξοδο"
def new_expenses():
    hide_all_frames()
    hide_buttons()
    file_new_frame.grid()
    #κλήση της main για καταχώρηση εξόδου 
    main()
#Δημιουργία του Μενού περιήγηση 
def my_menu():
    my_menu=Menu(window)
    #Μέσω της Database, το πρόγραμμα εντοπίζει και αναγράφει το συνολικό ποσό που έχει ξοδέψει ο χρήστης απο την εγκατάσταση του προγράμματος
    c.execute("SELECT SUM(money) FROM expenses")
    data=c.fetchall()
    #Μέσω της Database, το πρόγραμμα εντοπίζει και αναγράφει την τελευταία εισαγωγή εξόδου του χρήστη
    c.execute("SELECT MAX(year) from expenses ")
    y=c.fetchall()
    c.execute("SELECT MAX(month) FROM expenses WHERE year=2021")
    m=c.fetchall()
    c.execute("SELECT MAX(day) FROM expenses WHERE year=2021")
    d=c.fetchall()
    labelwindow=Label(window, text="Καλώς ήρθατε στο My Expenses Tracker! Eπιλέξτε πάνω αριστερά τι θα θέλατε να κάνετε. \n Τα εξοδά σας απο την μέρα που εγκαταστείσατε την εφαρμογή μας είναι {} ευρώ \n \n Η τελευταία εισαγωγή εξόδου ήταν {}-{}-{} ".format(data[0][0],y[0][0],m[0][0],d[0][0]), font='arial 11')
    labelwindow.grid(column=0, row=0)
    #Αναγραφή της ώρας εισόδου μέσω της βιβλιοθήκης datetime
    clock=Label(window, text="Τελευταία σας είσοδος:  " + str(datetime.datetime.now())[0:19], font='arial 11')
    clock.grid(column=0,row=1)
    window.config(menu=my_menu)
    file_menu=Menu(my_menu)
    #Δημιουργία κουμπιού Μενού
    my_menu.add_cascade(label= "Μενού", menu= file_menu)
    #Επιλογή Μενού για εμφάνιση της αρχικής σελίδας
    file_menu.add_command(label="Αρχική", command=home)
    #Επιλογή Μενού για εμφάνιση του Frame των νέων εξόδων
    file_menu.add_command(label="Νέο Έξοδο", command=new_expenses)
    #Επιλογή Μενού για εμφάνιση του Frame των διαγραμμάτων
    file_menu.add_command(label="Διαγράμματα", command=show_diagrams)
    #Διαχωριστική γραμμή
    file_menu.add_separator()
    #Επιλογή Μενού για έξοδο απο το πρόγραμμα
    file_menu.add_command(label="Έξοδος", command= window.destroy)
    #Δημιουργία κουμπιού για εμφάνιση βοήθειας
    my_menu.add_cascade(label="Βοήθεια", command=help)
    #Δημιουργία κουμπιού για επικοινωνία
    my_menu.add_cascade(label="Επικοινωνία", command=Contact)
#Δημιουργία πρώτου διαγράμματος (Σύγκριση του έτους επιλογής του χρήστη-με το προηγούμενο)
def show_plot1():
    global values
    #Συνάρτηση συλλογής δεδομένων απο την Database και μορφοποιήσης τους σε μορφή λίστα για το διάγραμμα
    def values(m1):
        c.execute("SELECT SUM(money) from expenses WHERE year={} and month=1".format(m1))
        jan=c.fetchall()
        ##
        c.execute("SELECT SUM(money) from expenses WHERE year={} and month=2".format(m1))
        feb=c.fetchall()
        ##
        c.execute("SELECT SUM(money) from expenses WHERE year={} and month=3".format(m1))
        mar=c.fetchall()
        ##
        c.execute("SELECT SUM(money) from expenses WHERE year={} and month=4".format(m1))
        apr=c.fetchall()
        ##
        c.execute("SELECT SUM(money) from expenses WHERE year={} and month=5".format(m1))
        may=c.fetchall()
        ##
        c.execute("SELECT SUM(money) from expenses WHERE year={} and month=6".format(m1))
        jun=c.fetchall()
        ##
        c.execute("SELECT SUM(money) from expenses WHERE year={} and month=7".format(m1))
        jul=c.fetchall()
        ##
        c.execute("SELECT SUM(money) from expenses WHERE year={} and month=8".format(m1))
        aug=c.fetchall()
        ##
        c.execute("SELECT SUM(money) from expenses WHERE year={} and month=9".format(m1))
        sep=c.fetchall()
        ##
        c.execute("SELECT SUM(money) from expenses WHERE year={} and month=10".format(m1))
        oct=c.fetchall()
        ##
        c.execute("SELECT SUM(money) from expenses WHERE year={} and month=11".format(m1))
        nov=c.fetchall()
        ##
        c.execute("SELECT SUM(money) from expenses WHERE year={} and month=12".format(m1))
        dec=c.fetchall()
        l=[jan,feb,mar,apr,may,jun,jul,aug,sep,oct,nov,dec]
        #Η λίστα για το δίαγραμμα
        ml=[]
        for i in l:
            ml.append(i[0][0])
        #Δημιουργία παραθύρου "Warning" σε περίπτωση που δεν υπάρχουν τα απαραίτητα δεδομένα για δημιουργία γραφήματος, στο έτος που επέλεξε ο χρήστης
        if ml[0] is None and ml[1] is None and ml[2] is None and ml[3] is None and ml[4] is None and ml[5] is None and ml[6] is None and ml[7] is None and ml[8] is None and ml[9] is None and ml[10] is None and ml[11] is None:
            warn = Tk()
            warn.title('Warning')
            warn.geometry('325x100')
            warn.resizable(False, False)
            window.iconbitmap("Pictures/code1.ico")
            warn_frame = Frame(warn)
            warn_lbl = Label(warn_frame, text="Δεν υπάρχουν στοιχεία για το έτος που ζητάτε", font= "arial 10", fg='red')
            warn_lbl.grid(padx=25, pady=10)
            warn_btn = Button(warn_frame, text='Close', command=warn.destroy)
            warn_btn.grid()
            warn_frame.grid()
            warn.mainloop()
        else:    
            return ml
    
    plt.style.use("seaborn")
    mon_x= ["Jan", "Feb","Mar","Apr","May","Jun","Jul","Aug","Sept","Oct","Nov","Dec"]
    #Αποφυγή error σε περίπτωση κενής εισόδου
    try:
        m=int(what_year.get())
    except ValueError:
        m=2020

    exp1_y= values(m)
    plt.plot(mon_x,exp1_y,color="c",linewidth=3, label=m)
    exp2_y=values(m-1)
    try:
        plt.plot(mon_x,exp2_y, linestyle="--", color= "black", label=m-1)
    except ValueError:
        pass

    plt.xlabel("Months")
    plt.ylabel("Expenses")
    plt.title("Annual expenses")
    plt.legend()
    plt.tight_layout()
    plt.show()
#Δημιουργία δεύτερου διαγράμματος (Μπάρες εξόδων ανα μήνα, για το έτος επιλογής του χρήστη)
def show_plot2():
    #Συνάρτηση συλλογής δεδομένων απο την Database και μορφοποιήσης τους σε μορφή λίστα για το διάγραμμα
    def values(m1):
        c.execute("SELECT SUM(money) from expenses WHERE year={} and month=1".format(m1))
        jan=c.fetchall()
        ##
        c.execute("SELECT SUM(money) from expenses WHERE year={} and month=2".format(m1))
        feb=c.fetchall()
        ##
        c.execute("SELECT SUM(money) from expenses WHERE year={} and month=3".format(m1))
        mar=c.fetchall()
        ##
        c.execute("SELECT SUM(money) from expenses WHERE year={} and month=4".format(m1))
        apr=c.fetchall()
        ##
        c.execute("SELECT SUM(money) from expenses WHERE year={} and month=5".format(m1))
        may=c.fetchall()
        ##
        c.execute("SELECT SUM(money) from expenses WHERE year={} and month=6".format(m1))
        jun=c.fetchall()
        ##
        c.execute("SELECT SUM(money) from expenses WHERE year={} and month=7".format(m1))
        jul=c.fetchall()
        ##
        c.execute("SELECT SUM(money) from expenses WHERE year={} and month=8".format(m1))
        aug=c.fetchall()
        ##
        c.execute("SELECT SUM(money) from expenses WHERE year={} and month=9".format(m1))
        sep=c.fetchall()
        ##
        c.execute("SELECT SUM(money) from expenses WHERE year={} and month=10".format(m1))
        oct=c.fetchall()
        ##
        c.execute("SELECT SUM(money) from expenses WHERE year={} and month=11".format(m1))
        nov=c.fetchall()
        ##
        c.execute("SELECT SUM(money) from expenses WHERE year={} and month=12".format(m1))
        dec=c.fetchall()
        ##
        l=[jan,feb,mar,apr,may,jun,jul,aug,sep,oct,nov,dec]
        ml=[]
        for i in l:
            ml.append(i[0][0])

        #Αποφυγή error σε περίπτωση μη πλήρους απο data έτους
        if ml[0] is None:
            ml[0]=int(0)
        if ml[1] is None:
            ml[1]=int(0)
        if ml[2] is None:
            ml[2]=int(0)
        if ml[3] is None:
            ml[3]=int(0)
        if ml[4] is None:
            ml[4]=int(0)
        if ml[5] is None:
            ml[5]=int(0)
        if ml[6] is None:
            ml[6]=int(0)
        if ml[7] is None:
            ml[7]=int(0)
        if ml[8] is None:
            ml[8]=int(0)
        if ml[9] is None:
            ml[9]=int(0)
        if ml[10] is None:
            ml[10]=int(0)
        if ml[11] is None:
            ml[11]=int(0)
        
        #Δημιουργία παραθύρου "Warning" σε περίπτωση που δεν υπάρχουν τα απαραίτητα δεδομένα για δημιουργία γραφήματος, στο έτος που επέλεξε ο χρήστης
        if ml[0]==0 and ml[1]==0 and ml[2]==0 and ml[3]==0 and ml[4]==0 and ml[5]==0 and ml[6]==0 and ml[7]==0 and ml[8]==0 and ml[9]==0 and ml[10]==0 and ml[11]==0:
            warn = Tk()
            warn.title('Warning')
            warn.geometry('325x100')
            warn.resizable(False, False)
            window.iconbitmap("Pictures/code1.ico")
            warn_frame = Frame(warn)
            warn_lbl = Label(warn_frame, text="Δεν υπάρχουν στοιχεία για το έτος που ζητάτε", font= "arial 10", fg='red')
            warn_lbl.grid(padx=25, pady=10)
            warn_btn = Button(warn_frame, text='Close', command=warn.destroy)
            warn_btn.grid()
            warn_frame.grid()
            warn.mainloop()
        else:    
            return ml
    
    try:
        m=int(what_year.get())
    except ValueError:
        m=2020

    plt.style.use("seaborn")
    days_x= ["Jan", "Feb","Mar","Apr","May","Jun","Jul","Aug","Sept","Oct","Nov","Dec"]
    exp1_y= values(m)
    plt.bar(days_x,exp1_y,color="y",linewidth=23, label=m)
    try:
        for index, value in enumerate(exp1_y):
            plt.text(index - .33, value/exp1_y[index]+100, round(exp1_y[index]), fontsize=10)
    except ZeroDivisionError:
        pass

    plt.xlabel("Months")
    plt.ylabel("Expenses")
    plt.title("Annual expenses")
    plt.legend()
    plt.tight_layout()
    plt.show()
#Δημιουργία τρίτου διαγράμματος (Πίτα έξοδων ανα κατηγορία για το έτος επιλογής του χρήστη)
def show_plot3():
    try:
        m=int(what_year.get())
    except ValueError:
        m=2020

    labels = 'Super Market','Ψυχαγωγία','Οικιακά','Συνδρομητικές Υπηρεσίες','Στέγαση','Μεταφόρα/Καύσιμα','Επενδύσεις','Έξοδα παιδιών','Ιατρικά','Άλλο','Επικοινωνίες'
    #Συνάρτηση συλλογής δεδομένων απο την Database με βάση την κατηγορία και το έτος επιλογής του χρήστη
    def cat(x):
        c.execute("select sum(money) from expenses where category='Super Market' and year={}".format(x))
        cat1=c.fetchall()
        ##
        c.execute("select sum(money) from expenses where category='Ψυχαγωγία' and year={}".format(x))
        cat2=c.fetchall()
        ##
        c.execute("select sum(money) from expenses where category='Οικιακά' and year={}".format(x))
        cat3=c.fetchall()
        ##
        c.execute("select sum(money) from expenses where category='Συνδρομητικές Υπηρεσίες' and year={}".format(x))
        cat4=c.fetchall()
        ##
        c.execute("select sum(money) from expenses where category='Στέγαση' and year={}".format(x))
        cat5=c.fetchall()
        ##
        c.execute("select sum(money) from expenses where category='Μεταφόρα/Καύσιμα' and year={}".format(x))
        cat6=c.fetchall()
        ##
        c.execute("select sum(money) from expenses where category='Επενδύσεις' and year={}".format(x))
        cat7=c.fetchall()
        ##
        c.execute("select sum(money) from expenses where category='Έξοδα παιδιών' and year={}".format(x))
        cat8=c.fetchall()
        ##
        c.execute("select sum(money) from expenses where category='Ιατρικά' and year={}".format(x))
        cat9=c.fetchall()
        ##
        c.execute("select sum(money) from expenses where category='Άλλο' and year={}".format(x))
        cat10=c.fetchall()
        ##
        c.execute("select sum(money) from expenses where category='Επικοινωνίες' and year={}".format(x))
        cat11=c.fetchall()
        ##
        l2=[cat1,cat2,cat3,cat4,cat5,cat6,cat7,cat8,cat9,cat10,cat11]
        ml2=[]
        for i in l2:
            ml2.append(i[0][0])
        
        #Αποφυγή error λόγο μη πλήρους απο δεδόμενα έτους
        if ml2[0] is None:
            ml2[0]=int(0)
        if ml2[1] is None:
            ml2[1]=int(0)
        if ml2[2] is None:
            
            ml2[2]=int(0)
        if ml2[3] is None:
            ml2[3]=int(0)
        if ml2[4] is None:
            ml2[4]=int(0)
        if ml2[5] is None:
            ml2[5]=int(0)
        if ml2[6] is None:
            ml2[6]=int(0)
        if ml2[7] is None:
            ml2[7]=int(0)
        if ml2[8] is None:
            ml2[8]=int(0)
        if ml2[9] is None:
            ml2[9]=int(0)
        if ml2[10] is None:
            ml2[10]=int(0) 

        #Δημιουργία παραθύρου "Warning" σε περίπτωση που δεν υπάρχουν τα απαραίτητα δεδομένα για δημιουργία γραφήματος, στο έτος που επέλεξε ο χρήστης
        if ml2[0]==0 and ml2[1]==0 and ml2[2]==0 and ml2[3]==0 and ml2[4]==0 and ml2[5]==0 and ml2[6]==0 and ml2[7]==0 and ml2[8]==0 and ml2[9]==0 and ml2[10]==0:
            warn = Tk()
            warn.title('Warning')
            warn.geometry('325x100')
            warn.resizable(False, False)
            window.iconbitmap("Pictures/code1.ico")
            warn_frame = Frame(warn)
            warn_lbl = Label(warn_frame, text="Δεν υπάρχουν στοιχεία για το έτος που ζητάτε", font= "arial 10", fg='red')
            warn_lbl.grid(padx=25, pady=10)
            warn_btn = Button(warn_frame, text='Close', command=warn.destroy)
            warn_btn.grid()
            warn_frame.grid()
            warn.mainloop()
        else:    
            return ml2
        
        ###
    sizes = cat(m)
    explode = (0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01)  
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes,explode=explode, labels=labels, autopct='%1.1f%%',
       shadow=True, startangle=90)
    ax1.axis('equal')  
    plt.show()
#Δημιουργία τέταρτου διαγράμματος (Πίτα έξοδων ανα κατηγορία για συγκεκριμένο ΜΗΝΑ επιλογής του χρήστη, στον ήδη επιλεγμένο απο τον ίδιο χρόνο)
def show_plot4():
    try:
        m=int(what_year.get())
    except ValueError:
        m=2020
        
    try:
        mon=int(what_month.get())
    except ValueError:
        mon=1
    #Συνάρτηση συλλογής δεδομένων απο την Database με βάση την κατηγορία,το έτος και το μήνα επιλογής του χρήστη
    def cat2(x,y):
        c.execute("select sum(money) from expenses where category='Super Market' and year={} and month={}".format(x,y))
        cat21=c.fetchall()
        ##
        c.execute("select sum(money) from expenses where category='Ψυχαγωγία' and year={} and month={}".format(x,y))
        cat22=c.fetchall()
        ##
        c.execute("select sum(money) from expenses where category='Οικιακά' and year={} and month={}".format(x,y))
        cat23=c.fetchall()
        ##
        c.execute("select sum(money) from expenses where category='Συνδρομητικές Υπηρεσίες' and year={} and month={}".format(x,y))
        cat24=c.fetchall()
        ##
        c.execute("select sum(money) from expenses where category='Στέγαση' and year={} and month={}".format(x,y))
        cat25=c.fetchall()
        ##
        c.execute("select sum(money) from expenses where category='Μεταφόρα/Καύσιμα' and year={} and month={}".format(x,y))
        cat26=c.fetchall()
        ##
        c.execute("select sum(money) from expenses where category='Επενδύσεις' and year={} and month={}".format(x,y))
        cat27=c.fetchall()
        ##
        c.execute("select sum(money) from expenses where category='Έξοδα παιδιών' and year={} and month={}".format(x,y))
        cat28=c.fetchall()
        ##
        c.execute("select sum(money) from expenses where category='Ιατρικά' and year={} and month={}".format(x,y))
        cat29=c.fetchall()
        ##
        c.execute("select sum(money) from expenses where category='Άλλο' and year={} and month={}".format(x,y))
        cat210=c.fetchall()
        ##
        c.execute("select sum(money) from expenses where category='Επικοινωνίες' and year={} and month={}".format(x,y))
        cat211=c.fetchall()
        l22=[cat21,cat22,cat23,cat24,cat25,cat26,cat27,cat28,cat29,cat210,cat211]
        ml22=[]
        for i in l22:
            ml22.append(i[0][0])
        #Αποφυγή Error
        if ml22[0] is None:
            ml22[0]=int(0)
        if ml22[1] is None:
            ml22[1]=int(0)
        if ml22[2] is None:
            ml22[2]=int(0)
        if ml22[3] is None:
            ml22[3]=int(0)
        if ml22[4] is None:
            ml22[4]=int(0)
        if ml22[5] is None:
            ml22[5]=int(0)
        if ml22[6] is None:
            ml22[6]=int(0)
        if ml22[7] is None:
            ml22[7]=int(0)
        if ml22[8] is None:
            ml22[8]=int(0)
        if ml22[9] is None:
            ml22[9]=int(0)
        if ml22[10] is None:
            ml22[10]=int(0)

        #Δημιουργία παραθύρου "Warning" σε περίπτωση που δεν υπάρχουν τα απαραίτητα δεδομένα για δημιουργία γραφήματος, στο έτος που επέλεξε ο χρήστης
        if ml22[0]==0 and ml22[1]==0 and ml22[2]==0 and ml22[3]==0 and ml22[4]==0 and ml22[5]==0 and ml22[6]==0 and ml22[7]==0 and ml22[8]==0 and ml22[9]==0 and ml22[10]==0:
            warn = Tk()
            warn.title('Warning')
            warn.geometry('325x100')
            warn.resizable(False, False)
            window.iconbitmap("Pictures/code1.ico")
            warn_frame = Frame(warn)
            warn_lbl = Label(warn_frame, text="Δεν υπάρχουν στοιχεία για τον μήνα που ζητάτε", font= "arial 10", fg='red')
            warn_lbl.grid(padx=25, pady=10)
            warn_btn = Button(warn_frame, text='Close', command=warn.destroy)
            warn_btn.grid()
            warn_frame.grid()
            warn.mainloop()
        else:    
            return ml22

    labels = 'Super Market','Ψυχαγωγία','Οικιακά','Συνδρομητικές Υπηρεσίες','Στέγαση','Μεταφόρα/Καύσιμα','Επενδύσεις','Έξοδα παιδιών','Ιατρικά','Άλλο','Επικοινωνίες'
    sizes=cat2(m,mon)
    explode = (0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01)
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes,explode=explode, labels=labels, autopct='%1.1f%%',
       shadow=True, startangle=90)
    ax1.axis('equal')  
    plt.show()
#Συνάρτηση "καθαρίσμού" παραθύρου για περιήγηση μεταξύ των Frame
def hide_buttons():
    btn6.grid_forget()
    btn5.grid_forget()
    btn1.grid_forget()
    btn2.grid_forget()
    btn3.grid_forget()
    btn4.grid_forget()
    contact_lbl.grid_forget()
    text_lbl.grid_forget()
#Συνάρτηση-αντίδραση στην επιλογή του Frame "Διαγράμματα" του Μενόυ
def show_diagrams():
    hide_all_frames()
    hide_buttons()
    file_new_frame2.grid()
    btn1.grid(sticky= "W", pady=5, padx=90)
    btn2.grid(sticky= "W", pady=5, padx=50)
    btn3.grid(sticky= "W", pady=5, padx=5)
    btn4.grid(sticky="W", column=1, row=3, padx=90)
#Συνάρτηση-Αντίδραση στο κουμπί Home του Menu
def home():
    hide_all_frames()
    contact_lbl.grid_forget()
    text_lbl.grid_forget()
    btn5.grid(sticky= "W", pady=30, padx=310)
    btn6.grid(sticky="W", padx=295)
#Συνάρτηση-Αντρίδραση στο "Επικοινωνία"
def Contact():
    hide_all_frames()
    hide_buttons()
    contact_lbl.grid(pady=50)
#Συνάρτηση-Αντρίδραση στο "Βοήθεια"
def help():
    hide_all_frames()
    hide_buttons()
    text_lbl.grid(padx=10)
#Κλήση των εικονιδίων
widgets()
#Κλήση του μενόυ για εκτέλεση του προγράμματος, που βασίζεται στα Frame
my_menu()
window.mainloop()
