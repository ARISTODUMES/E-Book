from os import remove
from tkinter import *
from PIL import ImageTk, Image
import threading 

root = Tk()
root.title("E-Book")
root.iconbitmap("book logo.ico")
root.configure(background="blue")
root.geometry("2020x1900")


# mylabel1=Label(root,text="E-Book",background="blue",foreground="white")
# mylabel1.grid(row=0,column=0)

def signup():
    global login_frame_1st_page
    login_frame_1st_page.grid_forget()

    signup_page = LabelFrame(root, text="Signup", font='Helvetica 34', padx=100, pady=10)
    signup_page.grid(row=9, column=2)

    s_name_label = Label(signup_page, text="Enter Full Name")
    s_name_label.grid(row=0, column=0, padx=20, pady=20)
    s_name_entry = Entry(signup_page, width=30, borderwidth=2)
    s_name_entry.grid(row=0, column=1)

    s_dob_label = Label(signup_page, text="Enter D-O-B")
    s_dob_label.grid(row=1, column=0)
    s_dob_entry = Entry(signup_page, width=30, borderwidth=2)
    s_dob_entry.grid(row=1, column=1)

    s_idnumlabel = Label(signup_page, text="Enter ID/Num")
    s_idnumlabel.grid(row=2, column=0, padx=20, pady=20)
    s_idnumentry = Entry(signup_page, width=30, borderwidth=2)
    s_idnumentry.grid(row=2, column=1)

    s_passwordlabel = Label(signup_page, text="Enter Password")
    s_passwordlabel.grid(row=3, column=0)
    s_passwordentry = Entry(signup_page, width=30, borderwidth=2)
    s_passwordentry.grid(row=3, column=1)

    s_re_passwordlabel = Label(signup_page, text="Re-Enter Password")
    s_re_passwordlabel.grid(row=4, column=0, padx=20, pady=20)
    s_re_passwordentry = Entry(signup_page, width=30, borderwidth=2)
    s_re_passwordentry.grid(row=4, column=1)

    def Signupsuccessfully():
        global login_frame_1st_page
        signup_page.grid_forget()
        signup_successfully_label.grid(row=9, column=2)

        def loginagain():
            signup_successfully_label.grid_forget()
            login_again.grid_forget()
            login_frame_1st_page.grid(row=9, column=2)

        login_again = Button(root, text="Click Here To Login", font='Helvetica 14', background="blue",
                             foreground="white", padx=200, pady=10, command=loginagain)
        login_again.grid(row=10, column=1, columnspan=3)

    signup_button = Button(signup_page, text="NEXT", borderwidth=5, command=Signupsuccessfully)
    signup_button.grid(row=5, column=1, columnspan=2)


def forgetpassword():
    global login_frame_1st_page
    login_frame_1st_page.grid_forget()

    forget_password_page = LabelFrame(root, text="Forget Password", font='Helvetica 34', padx=100, pady=10)
    forget_password_page.grid(row=9, column=2)

    f_idnumlabel = Label(forget_password_page, text="Enter ID/Num")
    f_idnumlabel.grid(row=0, column=0, padx=20, pady=20)
    f_idnumentry = Entry(forget_password_page, width=30, borderwidth=2)
    f_idnumentry.grid(row=0, column=1)

    f_passwordlabel = Label(forget_password_page, text="Enter Password")
    f_passwordlabel.grid(row=1, column=0)
    f_passwordentry = Entry(forget_password_page, width=30, borderwidth=2)
    f_passwordentry.grid(row=1, column=1)

    f_reenter_passwordlabel = Label(forget_password_page, text="Re-Enter Password")
    f_reenter_passwordlabel.grid(row=2, column=0, padx=20, pady=20)
    f_reenter_passwordentry = Entry(forget_password_page, width=30, borderwidth=2)
    f_reenter_passwordentry.grid(row=2, column=1)

    def passwordchanged():
        global login_frame_1st_page
        forget_password_page.grid_forget()
        changed_successfully_label.grid(row=9, column=2)

        def loginagain():
            changed_successfully_label.grid_forget()
            login_again.grid_forget()
            login_frame_1st_page.grid(row=9, column=2)

        login_again = Button(root, text="Click Here To Login", font='Helvetica 14', background="blue",foreground="white", padx=200, pady=10, command=loginagain)
        login_again.grid(row=10, column=1, columnspan=3)

    forget_password_button = Button(forget_password_page, text="NEXT", borderwidth=5, command=passwordchanged)
    forget_password_button.grid(row=3, column=1, columnspan=2)


def login():
    
    global p1
    global p2
    global p3
    global p4
    global login_frame_1st_page
    global root    
    global clicked
    clicked=StringVar()
    login_frame_1st_page.grid_forget()
    def contact():
        global Connection_label
        global Review_Request_button
        Connection_label=Label(top,text="Connection Stablisesd with "+clicked.get(),font = 'Helvetica 15')
        Connection_label.grid(row=3,column=2)
        Review_Request_button=Button(top,text="Send Review Request",font = 'Helvetica 15',command=sending)
        Review_Request_button.grid(row=4,column=2)
    def sending():
        delay=2
        def sent():
            de=2
            sending_label.grid_forget()
            sent_label=Label(top,text="Sent",font = 'Helvetica 15')
            sent_label.grid(row=5,column=2)
            def rmv():
                sent_label.grid_forget()
                Connection_label.grid_forget()
                Review_Request_button.grid_forget()
            starting_time = threading.Timer(de,rmv)
            starting_time.start()

            
        start_time = threading.Timer(delay,sent)
        start_time.start()
        sending_label=Label(top,text="Sending...",font = 'Helvetica 15')
        sending_label.grid(row=5,column=2)
         
        #Connection_label.grid_forget()
        #Review_Request_button.grid_forget()
    def B1review():
        global top
        top=Toplevel()
        top.geometry("2020x1900")
        global pa
        top.title("Living in the Light")
        pa= PhotoImage(file = r"B1.png")
        Button(top, image = pa,command=B1).grid(row=0, column=0)
        clicked.set("7 Reader's")
        Label(top,text="About The Book\nI would like to acknowledge Laurel King for her help with the\noriginal edition of this book. I appreciate Lora O’Connor for her\nmany valuable suggestions and overall support in creating this\nrevised edition. I’m very grateful to Becky Benenate, my editor for\nthe revised edition, for all her help and especially her willingness\nto work with my schedule and pull off a miracle of timing! Thanks\nto Katherine Dieter for her input, and to Marc Allen for his ongoing\nsupport. Kathy Altman, as always, has contributed her ideas\nand energy to the project. Jim Burns, thank you for your love and\nencouragement. Most of all I thank my readers, whose love and\nappreciation has been my inspiration and my reward.",font = 'Helvetica 20').grid(row=0,column=1)
        OptionMenu(top,clicked,"Uttam","Prince","Rahul","Kuldeep","Nakul","Nalin","Aayush").grid(row=1, column=2)  
        Button(top,text="Click here to Contact",font = 'Helvetica 15',command=contact).grid(row=2,column=2)
    def B1():
        import webbrowser
        path = "https://www.pdfdrive.com/living-in-the-light-a-guide-to-personal-transformation-e10172273.html"
        webbrowser.open_new(path)
    p1= PhotoImage(file = r"B1.png")
    Button(root, image = p1,command=B1review).grid(row=2, column=1)
    Label(root,text="This book is dedicated to\nthe wisdom within us \n all...",font = 'Helvetica 18',background="blue",foreground="white").grid(row=3,column=1,columnspan=1)
    Button(root, text="Read more",background="blue",foreground="white",font = 'Helvetica 18',command=B1review).grid(row=4, column=1)
    def B2():
        import webbrowser
        path = "https://www.pdfdrive.com/give-and-take-why-helping-others-drives-our-success-e58864799.html"
        webbrowser.open_new(path)
    p2= PhotoImage(file = r"B2.png")
    Button(root, image = p2,command=B2).grid(row=2, column=2)
    Label(root,text="Why helping other drives \n our success...",font = 'Helvetica 18',background="blue",foreground="white").grid(row=3,column=2)
    Button(root, text="Read more",background="blue",foreground="white",font = 'Helvetica 18').grid(row=4, column=2)
    
    Label(root,text="             ",background="blue").grid(row=2,column=3)
    def B3():
        import webbrowser
        path = "https://www.pdfdrive.com/13-things-mentally-strong-people-dont-do-take-back-your-power-embrace-change-face-your-fears-and-train-your-brain-for-happiness-and-success-e163207934.html"
        webbrowser.open_new(path)
    p3= PhotoImage(file = r"B3.png")
    Button(root, image = p3,command=B3).grid(row=2, column=4)
    Label(root,text="Take yack your power,\nEmbrace change,\nFace your fears...",font = 'Helvetica 18',background="blue",foreground="white").grid(row=3,column=4)
    Button(root, text="Read more",background="blue",foreground="white",font = 'Helvetica 18').grid(row=4, column=4)
    
    Label(root,text="             ",background="blue").grid(row=2,column=5)
    def B4():
        import webbrowser
        path = "https://www.pdfdrive.com/you-are-not-your-brain-the-4-step-solution-for-changing-bad-habits-ending-unhealthy-thinking-and-taking-control-of-your-life-e180653124.html"
        webbrowser.open_new(path)
    p4= PhotoImage(file = r"B4.png")
    Button(root, image = p4,command=B4).grid(row=2, column=6)
    Label(root,text="The 4-step solution for cha\n-nging bad habits, ending \n unhealthy thinking, and...",font = 'Helvetica 18',background="blue",foreground="white").grid(row=3,column=6)
    Button(root, text="Read more",background="blue",foreground="white",font = 'Helvetica 18').grid(row=4, column=6)
    
    def B5():
        import webbrowser
        path = "B5.pdf"
        webbrowser.open_new(path)

book_name = ImageTk.PhotoImage(Image.open("book name.png"))
book_name_label = Label(image=book_name, background="blue")
book_name_label.grid(row=0, column=0)

changed_successfully = ImageTk.PhotoImage(Image.open("changed successfully logo.png"))
changed_successfully_label = Label(root, image=changed_successfully, background="blue")

signup_successfully = ImageTk.PhotoImage(Image.open("signup  successfully logo.png"))
signup_successfully_label = Label(root, image=signup_successfully, background="blue")

book_logo = ImageTk.PhotoImage(Image.open("book logo.png"))
book_logo_label = Label(image=book_logo, background="blue")
book_logo_label.grid(row=1, column=0)

blank_label1 = Label(root,text="                                                                                                                   ",background="blue")
blank_label1.grid(row=1, column=1)
blank_label2 = Label(root, text=" ", background="blue")
blank_label2.grid(row=2, column=1)
blank_label3 = Label(root, text=" ", background="blue")
blank_label3.grid(row=3, column=1)
blank_label4 = Label(root, text=" ", background="blue")
blank_label4.grid(row=4, column=1)
blank_label5 = Label(root, text=" ", background="blue")
blank_label5.grid(row=5, column=1)
blank_label6 = Label(root, text=" ", background="blue")
blank_label6.grid(row=6, column=1)
blank_label7 = Label(root, text=" ", background="blue")
blank_label7.grid(row=7, column=1)
blank_label8 = Label(root, text=" ", background="blue")
blank_label8.grid(row=8, column=1)
blank_label9 = Label(root, text=" ", background="blue")
blank_label9.grid(row=9, column=3)

login_frame_1st_page = LabelFrame(root, text="Login", font='Helvetica 34', padx=100, pady=10)
login_frame_1st_page.grid(row=9, column=2)

idnumlabel = Label(login_frame_1st_page, text="Enter ID/Num")
idnumlabel.grid(row=0, column=0, padx=20, pady=20)
idnumentry = Entry(login_frame_1st_page, width=30, borderwidth=2)
idnumentry.grid(row=0, column=1)

passwordlabel = Label(login_frame_1st_page, text="Enter Password")
passwordlabel.grid(row=1, column=0)
passwordentry = Entry(login_frame_1st_page, width=30, borderwidth=2)
passwordentry.grid(row=1, column=1)

signup_button = Button(login_frame_1st_page, text="Sign Up", width=10, borderwidth=5, command=signup)
signup_button.grid(row=2, column=0, columnspan=1, padx=20, pady=20)
forget_password_button = Button(login_frame_1st_page, text="Forget Password", width=25, borderwidth=5,command=forgetpassword)
forget_password_button.grid(row=2, column=1, columnspan=2, pady=20)
login_button = Button(login_frame_1st_page, text="Login", borderwidth=5, command=login)
login_button.grid(row=3, column=1, columnspan=2)

root.mainloop()