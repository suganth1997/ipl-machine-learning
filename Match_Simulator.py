import GUI
import pickle
from tkinter import *
team_name =["Team_1", "Team_2"]
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
            players_team_1.append(form_window_obj.Listbox2.get(i))
            players_team_2.append(form_window_obj.Listbox2_3.get(i))

        form_window.destroy()
        main_window.Button1_2.place(relx=0.1, rely=0.67, height=73, width=476)


    ##Key Bindings
    form_window_obj.Button1.configure(command=add_to_team1)
    form_window_obj.Button1_4.configure(command=add_to_team2)
    form_window_obj.Button1_5.configure(command=done_selection)



main_root = Tk()
main_window = GUI.Main_Window(main_root)
main_window.Button1.configure(command=set_name)
main_window.Button1_1.configure(command=form_teams)
main_root.mainloop()
print(players_team_1)
print(players_team_2)