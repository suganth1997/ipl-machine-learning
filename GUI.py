from tkinter import *
team_name = ["Team_1", "Team_2"]
class Main_Window:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85'
        font9 = "-family {Courier New} -size 20 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"

        top.geometry("600x450+650+150")
        top.title("IPL Match Simulator")
        top.configure(background="#d9d9d9")



        self.Label1 = Label(top)
        self.Label1.place(relx=0.05, rely=0.07, height=46, width=542)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''IPL Team Strategy Tester''')
        self.Label1.configure(width=542)

        self.Button1 = Button(top)
        self.Button1.place(relx=0.1, rely=0.22, height=73, width=476)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(font=font9)
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Set Team Names''')
        self.Button1.configure(width=476)

        self.Button1_1 = Button(top)
        self.Button1_1.place(relx=0.1, rely=0.44, height=73, width=476)
        self.Button1_1.configure(activebackground="#d9d9d9")
        self.Button1_1.configure(activeforeground="#000000")
        self.Button1_1.configure(background="#d9d9d9")
        self.Button1_1.configure(font=font9)
        self.Button1_1.configure(disabledforeground="#a3a3a3")
        self.Button1_1.configure(foreground="#000000")
        self.Button1_1.configure(highlightbackground="#d9d9d9")
        self.Button1_1.configure(highlightcolor="black")
        self.Button1_1.configure(pady="0")
        self.Button1_1.configure(text='''Form Teams''')

        self.Button1_2 = Button(top)
        self.Button1_2.place(relx=0.1, rely=0.67, height=73, width=476)
        self.Button1_2.configure(activebackground="#d9d9d9")
        self.Button1_2.configure(activeforeground="#000000")
        self.Button1_2.configure(background="#d9d9d9")
        self.Button1_2.configure(font=font9)
        self.Button1_2.configure(disabledforeground="#a3a3a3")
        self.Button1_2.configure(foreground="#000000")
        self.Button1_2.configure(highlightbackground="#d9d9d9")
        self.Button1_2.configure(highlightcolor="black")
        self.Button1_2.configure(pady="0")
        self.Button1_2.configure(text='''Start Match''')
        self.Button1_2.place_forget()



class Team_Form_Window:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#d9d9d9'  # X11 color: 'gray85'
        font10 = "-family {Javanese Text} -size 9 -weight normal " \
                 "-slant roman -underline 0 -overstrike 0"
        font9 = "-family {@Microsoft YaHei UI} -size 15 -weight normal" \
                " -slant roman -underline 0 -overstrike 0"
        self.top = top

        top.geometry("1280x720+633+138")
        top.title("Form Teams")
        top.configure(background="#d9d9d9")

        self.Label1 = Label(top)
        self.Label1.place(relx=0.06, rely=0.04, height=46, width=350)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text=team_name[0])
        self.Label1.configure(width=302)

        self.Label1_1 = Label(top)
        self.Label1_1.place(relx=0.38, rely=0.04, height=46, width=322)
        self.Label1_1.configure(activebackground="#f9f9f9")
        self.Label1_1.configure(activeforeground="black")
        self.Label1_1.configure(background="#d9d9d9")
        self.Label1_1.configure(disabledforeground="#a3a3a3")
        self.Label1_1.configure(font=font9)
        self.Label1_1.configure(foreground="#000000")
        self.Label1_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1.configure(highlightcolor="black")
        self.Label1_1.configure(text='''ALL AVAILABLE PLAYERS''')
        self.Label1_1.configure(width=322)

        self.Label1_2 = Label(top)
        self.Label1_2.place(relx=0.7, rely=0.04, height=46, width=350)
        self.Label1_2.configure(activebackground="#f9f9f9")
        self.Label1_2.configure(activeforeground="black")
        self.Label1_2.configure(background="#d9d9d9")
        self.Label1_2.configure(disabledforeground="#a3a3a3")
        self.Label1_2.configure(font=font9)
        self.Label1_2.configure(foreground="#000000")
        self.Label1_2.configure(highlightbackground="#d9d9d9")
        self.Label1_2.configure(highlightcolor="black")
        self.Label1_2.configure(text=team_name[1])

        self.Listbox1 = Listbox(top)
        self.Listbox1.place(relx=0.37, rely=0.11, relheight=0.83, relwidth=0.27)
        self.Listbox1.configure(background="white")
        self.Listbox1.configure(disabledforeground="#a3a3a3")
        self.Listbox1.configure(font="TkFixedFont")
        self.Listbox1.configure(foreground="#000000")
        self.Listbox1.configure(width=344)

        self.Listbox2 = Listbox(top)
        self.Listbox2.place(relx=0.07, rely=0.11, relheight=0.68, relwidth=0.22)
        self.Listbox2.configure(background="white")
        self.Listbox2.configure(disabledforeground="#a3a3a3")
        self.Listbox2.configure(font="TkFixedFont")
        self.Listbox2.configure(foreground="#000000")
        self.Listbox2.configure(width=284)

        self.Listbox2_3 = Listbox(top)
        self.Listbox2_3.place(relx=0.71, rely=0.11, relheight=0.68
                              , relwidth=0.22)
        self.Listbox2_3.configure(background="white")
        self.Listbox2_3.configure(disabledforeground="#a3a3a3")
        self.Listbox2_3.configure(font="TkFixedFont")
        self.Listbox2_3.configure(foreground="#000000")
        self.Listbox2_3.configure(highlightbackground="#d9d9d9")
        self.Listbox2_3.configure(highlightcolor="black")
        self.Listbox2_3.configure(selectbackground="#c4c4c4")
        self.Listbox2_3.configure(selectforeground="black")
        self.Listbox2_3.configure(width=284)

        self.Button1 = Button(top)
        self.Button1.place(relx=0.09, rely=0.83, height=43, width=250)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(anchor=S)
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font=font10)
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text=("Add to " + team_name[0]))
        self.Button1.configure(width=106)

        self.Button1_4 = Button(top)
        self.Button1_4.place(relx=0.72, rely=0.83, height=43, width=250)
        self.Button1_4.configure(activebackground="#d9d9d9")
        self.Button1_4.configure(activeforeground="#000000")
        self.Button1_4.configure(anchor=S)
        self.Button1_4.configure(background="#d9d9d9")
        self.Button1_4.configure(disabledforeground="#a3a3a3")
        self.Button1_4.configure(font=font10)
        self.Button1_4.configure(foreground="#000000")
        self.Button1_4.configure(highlightbackground="#d9d9d9")
        self.Button1_4.configure(highlightcolor="black")
        self.Button1_4.configure(pady="0")
        self.Button1_4.configure(text="Add to " + team_name[1])

        self.Button1_5 = Button(top)
        self.Button1_5.place(relx=0.88, rely=0.93, height=43, width=106)
        self.Button1_5.configure(activebackground="#d9d9d9")
        self.Button1_5.configure(activeforeground="#000000")
        self.Button1_5.configure(anchor=S)
        self.Button1_5.configure(background="#d9d9d9")
        self.Button1_5.configure(disabledforeground="#a3a3a3")
        self.Button1_5.configure(font=font10)
        self.Button1_5.configure(foreground="#000000")
        self.Button1_5.configure(highlightbackground="#d9d9d9")
        self.Button1_5.configure(highlightcolor="black")
        self.Button1_5.configure(pady="0")
        self.Button1_5.configure(text='''Done Selection''')



class Toss_Window:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85'
        font11 = "-family {Hobo Std} -size 15 -weight normal -slant "  \
            "italic -underline 0 -overstrike 0"
        font12 = "-family {Hobo Std} -size 14 -weight normal -slant "  \
            "italic -underline 0 -overstrike 0"

        top.geometry("640x360+707+176")
        top.title("Toss")
        top.configure(background="#d9d9d9")



        self.Label1 = Label(top)
        self.Label1.place(relx=0.08, rely=0.06, height=66, width=522)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font12)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Toss result''')
        self.Label1.configure(width=522)

        self.Button1 = Button(top)
        self.Button1.place(relx=0.06, rely=0.36, height=173, width=246)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font=font11)
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Batting''')
        self.Button1.configure(width=246)

        self.Button1_1 = Button(top)
        self.Button1_1.place(relx=0.55, rely=0.36, height=173, width=246)
        self.Button1_1.configure(activebackground="#d9d9d9")
        self.Button1_1.configure(activeforeground="#000000")
        self.Button1_1.configure(background="#d9d9d9")
        self.Button1_1.configure(disabledforeground="#a3a3a3")
        self.Button1_1.configure(font=font11)
        self.Button1_1.configure(foreground="#000000")
        self.Button1_1.configure(highlightbackground="#d9d9d9")
        self.Button1_1.configure(highlightcolor="black")
        self.Button1_1.configure(pady="0")
        self.Button1_1.configure(text='''Bowling''')


class Match_Window:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85'
        font10 = "-family {Hobo Std} -size 14 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"

        font11 = "-family {Hobo Std} -size 12 -weight normal -slant " \
                 "roman -underline 0 -overstrike 0"

        font9 = "-family {@Adobe Heiti Std R} -size 9 -weight normal "  \
            "-slant roman -underline 0 -overstrike 0"

        top.geometry("1280x720+608+141")
        top.title("Play Innings")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")



        self.Listbox1 = Listbox(top)
        self.Listbox1.place(relx=0.31, rely=0.13, relheight=0.53, relwidth=0.36)
        self.Listbox1.configure(background="white")
        self.Listbox1.configure(disabledforeground="#a3a3a3")
        self.Listbox1.configure(font="TkFixedFont")
        self.Listbox1.configure(foreground="#000000")
        self.Listbox1.configure(highlightbackground="#d9d9d9")
        self.Listbox1.configure(highlightcolor="black")
        self.Listbox1.configure(selectbackground="#c4c4c4")
        self.Listbox1.configure(selectforeground="black")
        self.Listbox1.configure(width=464)

        self.Label1 = Label(top)
        self.Label1.place(relx=0.31, rely=0.08, height=26, width=362)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''From the Commentary Box is DecisionTreeClassifier''')

        self.Label2 = Label(top)
        self.Label2.place(relx=0.21, rely=0.01, height=26, width=722)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font10)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text=team_name[0] + " vs " + team_name[1])

        self.Message1 = Message(top)
        self.Message1.place(relx=0.32, rely=0.68, relheight=0.08, relwidth=0.25)
        self.Message1.configure(background="#d9d9d9")
        self.Message1.configure(font=font9)
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(text='''Score - Wickets''')
        self.Message1.configure(width=326)

        self.Message2 = Message(top)
        self.Message2.place(relx=0.29, rely=0.85, relheight=0.08, relwidth=0.29)
        self.Message2.configure(background="#d9d9d9")
        self.Message2.configure(font=font11)
        self.Message2.configure(foreground="#000000")
        self.Message2.configure(highlightbackground="#d9d9d9")
        self.Message2.configure(highlightcolor="black")
        self.Message2.configure(text='''To Win ___
From ___ Balls''')
        self.Message2.configure(width=366)

        self.Label3 = Label(top)
        self.Label3.place(relx=0.31, rely=0.81, height=26, width=112)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''Status Bar:''')

        self.Label4 = Label(top)
        self.Label4.place(relx=0.04, rely=0.08, height=36, width=222)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font=font9)
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(justify=LEFT)

        self.Listbox2 = Listbox(top)
        self.Listbox2.place(relx=0.05, rely=0.15, relheight=0.5, relwidth=0.21)
        self.Listbox2.configure(background="white")
        self.Listbox2.configure(disabledforeground="#a3a3a3")
        self.Listbox2.configure(font="TkFixedFont")
        self.Listbox2.configure(foreground="#000000")
        self.Listbox2.configure(highlightbackground="#d9d9d9")
        self.Listbox2.configure(highlightcolor="black")
        self.Listbox2.configure(selectbackground="#c4c4c4")
        self.Listbox2.configure(selectforeground="black")
        self.Listbox2.configure(width=264)

        self.Button1 = Button(top)
        self.Button1.place(relx=0.09, rely=0.69, height=53, width=126)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font=font9)
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Select Batsman''')

        self.Label4_1 = Label(top)
        self.Label4_1.place(relx=0.73, rely=0.08, height=36, width=222)
        self.Label4_1.configure(activebackground="#f9f9f9")
        self.Label4_1.configure(activeforeground="black")
        self.Label4_1.configure(background="#d9d9d9")
        self.Label4_1.configure(disabledforeground="#a3a3a3")
        self.Label4_1.configure(font=font9)
        self.Label4_1.configure(foreground="#000000")
        self.Label4_1.configure(highlightbackground="#d9d9d9")
        self.Label4_1.configure(highlightcolor="black")
        self.Label4_1.configure(justify=LEFT)

        self.Listbox2_2 = Listbox(top)
        self.Listbox2_2.place(relx=0.73, rely=0.15, relheight=0.5, relwidth=0.21)

        self.Listbox2_2.configure(background="white")
        self.Listbox2_2.configure(disabledforeground="#a3a3a3")
        self.Listbox2_2.configure(font="TkFixedFont")
        self.Listbox2_2.configure(foreground="#000000")
        self.Listbox2_2.configure(highlightbackground="#d9d9d9")
        self.Listbox2_2.configure(highlightcolor="black")
        self.Listbox2_2.configure(selectbackground="#c4c4c4")
        self.Listbox2_2.configure(selectforeground="black")
        self.Listbox2_2.configure(width=264)

        self.Button1_3 = Button(top)
        self.Button1_3.place(relx=0.79, rely=0.69, height=53, width=126)
        self.Button1_3.configure(activebackground="#d9d9d9")
        self.Button1_3.configure(activeforeground="#000000")
        self.Button1_3.configure(background="#d9d9d9")
        self.Button1_3.configure(disabledforeground="#a3a3a3")
        self.Button1_3.configure(font=font9)
        self.Button1_3.configure(foreground="#000000")
        self.Button1_3.configure(highlightbackground="#d9d9d9")
        self.Button1_3.configure(highlightcolor="black")
        self.Button1_3.configure(pady="0")
        self.Button1_3.configure(text='''Select Bowler''')

        self.Button2 = Button(top)
        self.Button2.place(relx=0.59, rely=0.69, height=43, width=116)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(font=font9)
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Bowl next Ball''')

        self.Button2_4 = Button(top)
        self.Button2_4.place(relx=0.59, rely=0.76, height=43, width=116)
        self.Button2_4.configure(activebackground="#d9d9d9")
        self.Button2_4.configure(activeforeground="#000000")
        self.Button2_4.configure(background="#d9d9d9")
        self.Button2_4.configure(disabledforeground="#a3a3a3")
        self.Button2_4.configure(font=font9)
        self.Button2_4.configure(foreground="#000000")
        self.Button2_4.configure(highlightbackground="#d9d9d9")
        self.Button2_4.configure(highlightcolor="black")
        self.Button2_4.configure(pady="0")
        self.Button2_4.configure(text='''Bowl 1 Over''')

        self.Button2_5 = Button(top)
        self.Button2_5.place(relx=0.59, rely=0.83, height=43, width=116)
        self.Button2_5.configure(activebackground="#d9d9d9")
        self.Button2_5.configure(activeforeground="#000000")
        self.Button2_5.configure(background="#d9d9d9")
        self.Button2_5.configure(disabledforeground="#a3a3a3")
        self.Button2_5.configure(font=font9)
        self.Button2_5.configure(foreground="#000000")
        self.Button2_5.configure(highlightbackground="#d9d9d9")
        self.Button2_5.configure(highlightcolor="black")
        self.Button2_5.configure(pady="0")
        self.Button2_5.configure(text='''Bowl 5 overs''')



class Name_Window:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85'

        font9 = "-family {@Adobe Heiti Std R} -size 12 -weight normal " \
                "-slant roman -underline 0 -overstrike 0"


        top.geometry("600x450+650+150")
        top.title("Set Names")
        top.configure(background="#d9d9d9")



        self.Entry1 = Entry(top)
        self.Entry1.place(relx=0.17, rely=0.16,height=104, relwidth=0.62)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font=font9)
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(width=374)

        self.Entry1_1 = Entry(top)
        self.Entry1_1.place(relx=0.17, rely=0.58,height=104, relwidth=0.62)
        self.Entry1_1.configure(background="white")
        self.Entry1_1.configure(disabledforeground="#a3a3a3")
        self.Entry1_1.configure(font=font9)
        self.Entry1_1.configure(foreground="#000000")
        self.Entry1_1.configure(highlightbackground="#d9d9d9")
        self.Entry1_1.configure(highlightcolor="black")
        self.Entry1_1.configure(insertbackground="black")
        self.Entry1_1.configure(selectbackground="#c4c4c4")
        self.Entry1_1.configure(selectforeground="black")

        self.Label1 = Label(top)
        self.Label1.place(relx=0.18, rely=0.04, height=36, width=342)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(font=font9)
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Enter Name of First Team''')
        self.Label1.configure(width=342)

        self.Label1_2 = Label(top)
        self.Label1_2.place(relx=0.18, rely=0.47, height=36, width=342)
        self.Label1_2.configure(activebackground="#f9f9f9")
        self.Label1_2.configure(activeforeground="black")
        self.Label1_2.configure(background="#d9d9d9")
        self.Label1_2.configure(font=font9)
        self.Label1_2.configure(disabledforeground="#a3a3a3")
        self.Label1_2.configure(foreground="#000000")
        self.Label1_2.configure(highlightbackground="#d9d9d9")
        self.Label1_2.configure(highlightcolor="black")
        self.Label1_2.configure(text='''Enter Name of Second Team''')

        self.Button1 = Button(top)
        self.Button1.place(relx=0.4, rely=0.85, height=53, width=126)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font=font9)
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Done''')


