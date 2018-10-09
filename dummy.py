import GUI
import pickle
import random
from time import sleep
from tkinter import *
team_name =["Team_1", "Team_2"]

decision_tree_pkl_filename = 'decision_tree_classifier_IPL.pkl'
decision_tree_model_pkl = open(decision_tree_pkl_filename, 'rb')
decision_tree_model = pickle.load(decision_tree_model_pkl)

index_data_pkl = open('dismissal_kind_index_data.pkl','rb')
dismissal_kind_index_data = pickle.load(index_data_pkl)


index_data_pkl = open('batsman_index_data.pkl','rb')
batsman_index_data = pickle.load(index_data_pkl)


index_data_pkl = open('non_striker_index_data.pkl','rb')
non_striker_index_data = pickle.load(index_data_pkl)


index_data_pkl = open('bowler_index_data.pkl','rb')
bowler_index_data = pickle.load(index_data_pkl)

##Setting up Batsman Information
batsman_mapping = batsman_index_data.copy()
batsman_mapping = sorted(batsman_mapping)
players = [[],[]]
players_team_1 = []
players_team_2 = []


def set_name():
    def get_names():
        GUI.team_name[0] = team_name[0] = y.Entry1.get()
        GUI.team_name[1] = team_name[1] = y.Entry1_1.get()
        x.destroy()
        #main_window.Button1_2.place(relx=0.1, rely=0.67, height=73, width=476)

    x = Toplevel()
    y = GUI.Name_Window(x)
    y.Button1.configure(command = get_names)

#for i in range(0,20):
    # top1.Listbox1.insert(i,2*i)
# n = [0]
# def add_to_team():
    # print(top1.Listbox1.get(top1.Listbox1.curselection()))
    # top1.Listbox2.insert(n[0],top1.Listbox1.get(top1.Listbox1.curselection()))
    # n[0] = n[0] + 1

def form_teams():
    form_window = Toplevel()
    form_window_obj = GUI.Team_Form_Window(form_window)
    ##Setting up team form window
    n = 0
    for bat in batsman_mapping:
        form_window_obj.Listbox1.insert(n,bat)
        n = n + 1


    ##Functions to add Players
    num_players = [0,0]
    form_window_obj.Button1_4.place_forget()
    form_window_obj.Button1_5.place_forget()
    def add_to_team1():
        if num_players[0]==11:
            return
        form_window_obj.Listbox2.insert(num_players[0], form_window_obj.Listbox1.get(form_window_obj.Listbox1.curselection()))
        form_window_obj.Listbox1.delete(form_window_obj.Listbox1.curselection())
        num_players[0] = num_players[0] + 1
        form_window_obj.Button1.place_forget()
        form_window_obj.Button1_4.place(relx=0.72, rely=0.83, height=43, width=250)

    def add_to_team2():
        if num_players[1]==10:
            form_window_obj.Button1_5.place(relx=0.88, rely=0.93, height=43, width=106)
        if num_players[1]==11:
            return
        form_window_obj.Listbox2_3.insert(num_players[1], form_window_obj.Listbox1.get(form_window_obj.Listbox1.curselection()))
        form_window_obj.Listbox1.delete(form_window_obj.Listbox1.curselection())
        num_players[1] = num_players[1] + 1
        form_window_obj.Button1_4.place_forget()
        form_window_obj.Button1.place(relx=0.09, rely=0.83, height=43, width=250)

    def done_selection():
        for i in range(0,11):
            players[0].append(form_window_obj.Listbox2.get(i))
            players[1].append(form_window_obj.Listbox2_3.get(i))

        form_window.destroy()
        main_window.Button1_2.place(relx=0.1, rely=0.67, height=73, width=476)


    ##Key Bindings
    form_window_obj.Button1.configure(command=add_to_team1)
    form_window_obj.Button1_4.configure(command=add_to_team2)
    form_window_obj.Button1_5.configure(command=done_selection)


def start_match():
    toss_result = random.randint(0,1)
    def toss_win_bat():
        start_first_innings(toss_root, toss_result)

    def toss_win_bowl():
        start_first_innings(toss_root, abs(toss_result-1))

    main_root.destroy()
    toss_root = Tk()
    toss_window_obj = GUI.Toss_Window(toss_root)
    toss_window_obj.Label1.configure(text = team_name[toss_result] + " won the toss and they opt for...")
    toss_window_obj.Button1.configure(command=toss_win_bat)
    toss_window_obj.Button1_1.configure(command=toss_win_bowl)
    toss_root.mainloop()

def start_first_innings(toss_root, batting_team_index):
    toss_root.destroy()
    match_root = Tk()
    match_window_obj = GUI.Match_Window(match_root)
    match_window_obj.Label4.configure(text="Batting: " + team_name[batting_team_index])
    match_window_obj.Label4_1.configure(text="Bowling: " + team_name[abs(batting_team_index-1)])
    comment_index = [0]
    score = [0]
    wickets = [0]
    over = [1]
    ball = [1]
    current_play = []
    for i in range(0,len(players[0])):
        match_window_obj.Listbox2.insert(i,players[batting_team_index][i])
        if players[abs(batting_team_index-1)][i] in bowler_index_data:
            match_window_obj.Listbox2_2.insert(i,players[abs(batting_team_index-1)][i])

    def choose_batsman():
        current_play.append(match_window_obj.Listbox2.get(match_window_obj.Listbox2.curselection()))
        match_window_obj.Listbox2.delete(match_window_obj.Listbox2.curselection())
        if len(current_play)==1:
            insert_commentary("Choose the opening non striker")
        if len(current_play)==2:
            match_window_obj.Button1.place_forget()
            match_window_obj.Button1_3.place(relx=0.79, rely=0.69, height=53, width=126)
            insert_commentary("Choose the bowler for first over")

    def choose_bowler():
        current_play.append(match_window_obj.Listbox2_2.get(match_window_obj.Listbox2_2.curselection()))
        match_window_obj.Button1_3.place_forget()

    def insert_commentary(comment):
        match_window_obj.Listbox1.insert(comment_index[0],comment)
        match_window_obj.Listbox1.see(comment_index[0])
        comment_index[0] += 1

    def hide_for_selection():
        match_window_obj.Button2.place_forget()
        #match_window_obj.Button2_4.place_forget()

    def show_after_selection():
        match_window_obj.Button2.place(relx=0.59, rely=0.69, height=43, width=116)
        match_window_obj.Button2_4.place(relx=0.59, rely=0.76, height=43, width=116)

    def select_new_batsman():
        hide_for_selection()
        def selection():
            current_play[0] = match_window_obj.Listbox2.get(match_window_obj.Listbox2.curselection())
            match_window_obj.Listbox2.delete(match_window_obj.Listbox2.curselection())
            match_window_obj.Button1.place_forget()
            show_after_selection()

        insert_commentary("Select the next batsman")
        match_window_obj.Button1.place(relx=0.09, rely=0.69, height=53, width=126)
        match_window_obj.Button1.configure(command=selection)

    def select_new_bowler():
        hide_for_selection()
        def selection():
            current_play[2] = match_window_obj.Listbox2_2.get(match_window_obj.Listbox2_2.curselection())
            match_window_obj.Button1_3.place_forget()
            show_after_selection()

        insert_commentary("Select the next bowler")
        match_window_obj.Button1_3.place(relx=0.79, rely=0.69, height=53, width=126)
        match_window_obj.Button1_3.configure(command=selection)

    def end_innings():

        def selection():
            #del match_window_obj
            start_chasing(match_root, abs(batting_team_index - 1), score[0])

        insert_commentary("At the end of " + str(over[0]-1) + "." + str(ball[0]-1) + " overs ")
        insert_commentary(team_name[batting_team_index] + " scored " + str(score[0]) + " for " + str(wickets[0]) + " wickets")
        insert_commentary(team_name[abs(batting_team_index-1)] + " needs " + str(score[0]+1) + " to win")
        insert_commentary("Click the start chasing button when you are ready")
        match_window_obj.Button2_4.place(relx=0.59, rely=0.76, height=43, width=116)
        match_window_obj.Button2_4.configure(text="Start Chasing",command=selection)

    def bowl_the_ball():
        res = decision_tree_model.predict([[over[0],ball[0],batsman_index_data.index(current_play[0]),non_striker_index_data.index(current_play[1]),bowler_index_data.index(current_play[2])]])

        if res[0][1] != 0:
            insert_commentary("Its a WICKET!!")
            wickets[0] += 1
            if res[0][0] == 0:
                insert_commentary(current_play[0] + " goes out by " + dismissal_kind_index_data[int(res[0][1])])
            elif res[0][0] != 0:
                insert_commentary("Its a run out and " + current_play[0] + " departs")
                score[0] += res[0][0]
            if wickets[0]==10:
                end_innings()
            select_new_batsman()
            if ball[0]==6:
                hide_for_selection()

        elif res[0][0] == 0:
            insert_commentary("A dot ball")

        elif res[0][0] == 1:
            insert_commentary("A single by " + current_play[0])
            score[0] += 1
            current_play[0], current_play[1] = current_play[1], current_play[0]

        elif res[0][0] == 2:
            insert_commentary("A double by " + current_play[0])
            score[0] += 2

        elif res[0][0] == 3:
            insert_commentary("A triple by " + current_play[0])
            insert_commentary("Boy, he is a run machine")
            score[0] += 3
            current_play[0], current_play[1] = current_play[1], current_play[0]

        elif res[0][0] == 4:
            insert_commentary(current_play[0] + " scores a boundary, FOUR RUNS!!")
            score[0] += 4

        elif res[0][0] == 5:
            insert_commentary("Very poor bowling by " + current_play[2])
            insert_commentary("A wide and a boundary")
            score[0] += 5

        elif res[0][0] == 6:
            insert_commentary(current_play[0] + " is on fire!!")
            insert_commentary("SIX RUNS!!")
            score[0] += 6

        ball[0] += 1
        if ball[0]==7:
            ball[0] = 1
            over[0] += 1
            select_new_bowler()

        if over[0]==21:
            end_innings()

        match_window_obj.Message2.configure(text=str(score[0]) + " - " + str(wickets[0]))
        match_window_obj.Message1.configure(text="Overs - " + str(over[0]-1) + "." + str(ball[0]-1))


    match_window_obj.Button1_3.place_forget()
    match_window_obj.Button1.configure(command=choose_batsman)
    match_window_obj.Button1_3.configure(command=choose_bowler)
    match_window_obj.Button2.configure(command=bowl_the_ball)
    match_window_obj.Button2_4.place_forget()
    match_window_obj.Button2_5.place_forget()

    insert_commentary("Its a hot day here in your computer ")
    insert_commentary("coz its running the whole day, duh!")
    sleep(3)
    insert_commentary("Choose the opening striker")


    match_root.mainloop()


def start_chasing(first_innings_root, batting_team_index, target):
    first_innings_root.destroy()
    chasing_root = Tk()
    match_window_obj = GUI.Match_Window(chasing_root)
    match_window_obj.Label4.configure(text="Batting: " + team_name[batting_team_index])
    match_window_obj.Label4_1.configure(text="Bowling: " + team_name[abs(batting_team_index-1)])
    comment_index = [0]
    score = [0]
    wickets = [0]
    over = [1]
    ball = [1]
    current_play = []
    for i in range(0,len(players[0])):
        match_window_obj.Listbox2.insert(i,players[batting_team_index][i])
        if players[abs(batting_team_index-1)][i] in bowler_index_data:
            match_window_obj.Listbox2_2.insert(i,players[abs(batting_team_index-1)][i])

    def choose_batsman():
        current_play.append(match_window_obj.Listbox2.get(match_window_obj.Listbox2.curselection()))
        match_window_obj.Listbox2.delete(match_window_obj.Listbox2.curselection())
        if len(current_play)==1:
            insert_commentary("Choose the opening non striker")
        if len(current_play)==2:
            match_window_obj.Button1.place_forget()
            match_window_obj.Button1_3.place(relx=0.79, rely=0.69, height=53, width=126)
            insert_commentary("Choose the bowler for first over")

    def choose_bowler():
        current_play.append(match_window_obj.Listbox2_2.get(match_window_obj.Listbox2_2.curselection()))
        match_window_obj.Listbox2_2.delete(match_window_obj.Listbox2_2.curselection())
        match_window_obj.Button1_3.place_forget()

    def insert_commentary(comment):
        match_window_obj.Listbox1.insert(comment_index[0],comment)
        match_window_obj.Listbox1.see(comment_index[0])
        comment_index[0] += 1

    def hide_for_selection():
        match_window_obj.Button2.place_forget()
        match_window_obj.Button2_4.place_forget()

    def show_after_selection():
        match_window_obj.Button2.place(relx=0.59, rely=0.69, height=43, width=116)
        match_window_obj.Button2_4.place(relx=0.59, rely=0.76, height=43, width=116)

    def select_new_batsman():
        hide_for_selection()
        def selection():
            current_play[0] = match_window_obj.Listbox2.get(match_window_obj.Listbox2.curselection())
            match_window_obj.Listbox2.delete(match_window_obj.Listbox2.curselection())
            match_window_obj.Button1.place_forget()
            show_after_selection()

        insert_commentary("Select the next batsman")
        match_window_obj.Button1.place(relx=0.09, rely=0.69, height=53, width=126)
        match_window_obj.Button1.configure(command=selection)

    def select_new_bowler():
        hide_for_selection()
        def selection():
            current_play[2] = match_window_obj.Listbox2_2.get(match_window_obj.Listbox2_2.curselection())
            match_window_obj.Button1_3.place_forget()
            show_after_selection()

        insert_commentary("Select the next bowler")
        match_window_obj.Button1_3.place(relx=0.79, rely=0.69, height=53, width=126)
        match_window_obj.Button1_3.configure(command=selection)

    def end_innings():
        if score[0]>target:
            insert_commentary(team_name[batting_team_index] + " defeated " + team_name[abs(batting_team_index-1)] + " by " + str(11-wickets[0]) + " wickets")
            match_window_obj.Message2.configure(text=(team_name[batting_team_index] + " defeated " + team_name[abs(batting_team_index-1)] + " by " + str(11-wickets[0]) + " wickets"))

        elif score[0]==target:
            insert_commentary("The teams are perfect competitors as the match end in a draw!")
            match_window_obj.Message2.configure(text="The teams are perfect competitors as the match end in a draw!")

        else:
            insert_commentary(team_name[abs(batting_team_index-1)] + " defeated " + team_name[batting_team_index] + " by " + str(target-score[0]) + " runs")
            match_window_obj.Message2.configure(text=team_name[abs(batting_team_index-1)] + " defeated " + team_name[batting_team_index] + " by " + str(target-score[0]) + " runs")

        insert_commentary("Thank you for playing!")

    def bowl_the_ball():
        res = decision_tree_model.predict([[over[0],ball[0],batsman_index_data.index(current_play[0]),non_striker_index_data.index(current_play[1]),bowler_index_data.index(current_play[2])]])

        if res[0][1] != 0:
            insert_commentary("Its a WICKET!!")
            wickets[0] += 1
            if res[0][0] == 0:
                insert_commentary(current_play[0] + " goes out by " + dismissal_kind_index_data[int(res[0][1])])
            elif res[0][0] != 0:
                insert_commentary("Its a run out and " + current_play[0] + " departs")
                score[0] += res[0][0]
            if wickets[0]==10:
                end_innings()
            select_new_batsman()
            if ball[0]==6:
                hide_for_selection()

        elif res[0][0] == 0:
            insert_commentary("A dot ball")

        elif res[0][0] == 1:
            insert_commentary("A single by " + current_play[0])
            score[0] += 1
            current_play[0], current_play[1] = current_play[1], current_play[0]

        elif res[0][0] == 2:
            insert_commentary("A double by " + current_play[0])
            score[0] += 2

        elif res[0][0] == 3:
            insert_commentary("A triple by " + current_play[0])
            insert_commentary("Boy, he is a run machine")
            score[0] += 3
            current_play[0], current_play[1] = current_play[1], current_play[0]

        elif res[0][0] == 4:
            insert_commentary(current_play[0] + " scores a boundary, FOUR RUNS!!")
            score[0] += 4

        elif res[0][0] == 5:
            insert_commentary("Very poor bowling by " + current_play[2])
            insert_commentary("A wide and a boundary")
            score[0] += 5

        elif res[0][0] == 6:
            insert_commentary(current_play[0] + " is on fire!!")
            insert_commentary("SIX RUNS!!")
            score[0] += 6

        ball[0] += 1
        if ball[0]==7:
            ball[0] = 1
            over[0] += 1
            select_new_bowler()

        if over[0]==21:
            end_innings()

        if score[0]>target:
            end_innings()

        match_window_obj.Message1.configure(text=str(score[0]) + " - " + str(wickets[0]))
        match_window_obj.Message2.configure(text=str(target-score[0]+1) + " needed from " + str(121-((over[0]-1)*6 + ball[0])) + " balls")


    match_window_obj.Button1_3.place_forget()
    match_window_obj.Button1.configure(command=choose_batsman)
    match_window_obj.Button1_3.configure(command=choose_bowler)
    match_window_obj.Button2.configure(command=bowl_the_ball)
    match_window_obj.Button2_4.place_forget()
    match_window_obj.Button2_5.place_forget()

    insert_commentary("The chase is on ")
    insert_commentary("Multi Layer Perceptron and Support Vector Machine ")
    insert_commentary("has joined with me, Here from Commentary Box")
    sleep(3)
    insert_commentary("Choose the opening striker")


    match_root.mainloop()




main_root = Tk()
main_window = GUI.Main_Window(main_root)
main_window.Button1.configure(command=set_name)
main_window.Button1_1.configure(command=form_teams)
main_window.Button1_2.configure(command=start_match)
main_root.mainloop()