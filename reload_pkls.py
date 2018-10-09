import pandas as pd
import pickle
import random
from time import sleep


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
target = [0]


def bowl_the_ball( over, balls, batsman_index, non_striker_index, bowler_index ):
#    ball = pd.DataFrame([])
#    ball.at[0,'over'] = over
#    ball.at[0,'ball'] = balls
#    ball.at[0,'batsman_index'] = batsman_index
#    ball.at[0,'non_striker_index'] = non_striker_index
#    ball.at[0,'bowler_index'] = bowler_index
    
    return [decision_tree_model.predict([[over, balls, batsman_index, non_striker_index, bowler_index]])[0][0],decision_tree_model.predict([[over, balls, batsman_index, non_striker_index, bowler_index]])[0][1]]


def form_team(team):
    while len(team) < 11:
            print("Enter a search term to find the player\n")
            key = input()
            for play in batsman_index_data:
                    if key.lower() in play.lower():
                            print("Enter " + str(batsman_index_data.index(play)) + " to select " + play + " into your team!\n") 
            print("Enter the appropriate key for the player to add to your team\nEnter -1 to search again\n")
            key = int(input())
            if key == -1:
                    continue
            else:
                    team.append(key)
    
    print("Players of your team are \n")
    for play in team:
            print(batsman_index_data[play] + "\n")
    print("\n THANK YOU FOR CHOOSING YOUR TEAM")
    



def start_innings( batting_team, bowling_team , batting_team_name, bowling_team_name):
    print("Who do you want to be the Opening striker?\n")
    for i in range(1,12):
            print("Enter " + str(i) + " for " + batsman_index_data[batting_team[i-1]] + "\n")
    
    striker_team_index = int(input())
    done_batsman = []
    print("Who do you want to be the Opening non striker?\n")
    for i in list(set(range(1,12)) - set(done_batsman)):
            print("Enter " + str(i) + " for " + batsman_index_data[batting_team[i-1]] + "\n")
    
    non_striker_team_index = int(input())
    done_batsman.append(non_striker_team_index)
    done_batsman.append(striker_team_index)
    score = 0
    set_allout = 0
    wickets = 0
    striker = batting_team[striker_team_index - 1]
    non_striker = batting_team[non_striker_team_index - 1]
    for i in range(1,21):
            print("Whom do you want to bowl this over?\n")
            for l in range(1,12):
                    if batsman_index_data[bowling_team[l-1]] in bowler_index_data:
                            print("Enter " + str(l) + " for " + batsman_index_data[bowling_team[l-1]] + "\n")
            bowler = int(input())
            bowler = bowling_team[bowler - 1]
            for j in range(1,7):
                    res = bowl_the_ball(i,j,striker,non_striker_index_data.index(batsman_index_data[non_striker]),bowler_index_data.index(batsman_index_data[bowler]))
                    #If its a Wicket
                    if res[1] != 0:
                            done_batsman.append(striker_team_index)
                            wickets += 1
                            if wickets == 10:
                                    set_allout = 1
                                    break
                            print("Its a WICKET\n")
                            if res[0] == 0:
                                    print(batsman_index_data[striker] + " goes out by " + dismissal_kind_index_data[int(res[1])] + "\n")
                            elif res[0] != 0:
                                    print("A run out and " + batsman_index_data[striker] + " departs\n")
                                    score += res[0]
                            print("Whom do you want to be the next batsman?\n")		
                            for k in list(set(range(1,12)) - set(done_batsman)):
                                    print("Enter " + str(k) + " for " + batsman_index_data[batting_team[k-1]] + "\n")
                            striker_team_index = int(input())
                            striker = batting_team[striker_team_index - 1]
                    #If its a dot ball
                    if res[0] == 0:
                            print("A dot ball \n")
                    #If its a single
                    if res[0] == 1:
                            score += 1
                            print("A single by " + batsman_index_data[striker] + "\n")
                            striker_team_index, non_striker_team_index = non_striker_team_index, striker_team_index
                            striker, non_striker = non_striker, striker
                    
                    #If its a double
                    if res[0] == 2:
                            score += 2
                            print("A double by " + batsman_index_data[striker] + "\n")
                            
                    #If its a triple
                    if res[0] == 3:
                            score += 3
                            striker_team_index, non_striker_team_index = non_striker_team_index, striker_team_index
                            striker, non_striker = non_striker, striker
                            print("A triple by " + batsman_index_data[striker] + "\n")
                            
                    #If its a boundary
                    if res[0] == 4:
                            score+= 4
                            print(batsman_index_data[striker] + " scores a boundary!!!! Fours runs\n")
                            
                    #If its a five
                    if res[0] == 5:
                            score += 5
                            print("Very poor bowling or strategy gone wrong by " + bowler_index_data[bowler] + "\n")
                            
                    #If its a six
                    if res[0] == 6:
                            score += 6
                            print("A MAXIMUM!!!!\n" + batsman_index_data[striker] + " is on fire... SIX RUNS!!\n")
                    
            if set_allout == 1:
                    break
            striker_team_index, non_striker_team_index = non_striker_team_index, striker_team_index
            striker, non_striker = non_striker, striker
            print(str(score) + " - " + str(wickets) + " at the end of over " + str(i) + "\n")
    
    if set_allout==1:
            print("At the end of " + str(i) + "." + str(j) + " overs," + batting_team_name + " scored " + str(score) + " with all wickets fallen\n")
    else:
            print("At the end of 20 overs " + batting_team_name + " scored " + str(score) + " with a loss of " + str(wickets) + " wickets!\n")

    target[0] = score + 1




def start_chasing( batting_team, bowling_team , batting_team_name, bowling_team_name):
    print("Who do you want to be the Opening striker?\n")
    for i in range(1,12):
            print("Enter " + str(i) + " for " + batsman_index_data[batting_team[i-1]] + "\n")
    
    striker_team_index = int(input())
    done_batsman = []
    print("Who do you want to be the Opening non striker?\n")
    for i in list(set(range(1,12)) - set(done_batsman)):
            print("Enter " + str(i) + " for " + batsman_index_data[batting_team[i-1]] + "\n")
    
    non_striker_team_index = int(input())
    done_batsman.append(non_striker_team_index)
    done_batsman.append(striker_team_index)
    score = 0
    
    #Flags
    already_update = 0
    batting_win = 0
    set_allout = 0
    
    wickets = 0
    striker = batting_team[striker_team_index - 1]
    non_striker = batting_team[non_striker_team_index - 1]
    for i in range(0,20):
            print("Whom do you want to bowl this over?\n")
            for l in range(1,12):
                    if batsman_index_data[bowling_team[l-1]] in bowler_index_data:
                            print("Enter " + str(l) + " for " + batsman_index_data[bowling_team[l-1]] + "\n")
            bowler = int(input())
            bowler = bowling_team[bowler - 1]
            for j in range(1,7):
                    res = bowl_the_ball(i,j,striker,non_striker_index_data.index(batsman_index_data[non_striker]),bowler_index_data.index(batsman_index_data[bowler]))
                    #If its a Wicket
                    if res[1] != 0:
                            done_batsman.append(striker_team_index)
                            wickets += 1
                            if wickets == 10:
                                    set_allout = 1
                                    break
                            print("Its a WICKET\n")
                            if res[0] == 0:
                                    print(batsman_index_data[striker] + " goes out by " + dismissal_kind_index_data[int(res[1])] + "\n")
                            elif res[0] != 0:
                                    print("A run out and " + batsman_index_data[striker] + " departs\n")
                                    score += res[0]
                            print("Whom do you want to be the next batsman?\n")		
                            for k in list(set(range(1,12)) - set(done_batsman)):
                                    print("Enter " + str(k) + " for " + batsman_index_data[batting_team[k-1]] + "\n")
                            striker_team_index = int(input())
                            done_batsman.append(striker_team_index)
                            striker = batting_team[striker_team_index - 1]
                    #If its a dot ball
                    if res[0] == 0:
                            print("A dot ball \n")
                    #If its a single
                    if res[0] == 1:
                            score += 1
                            print("A single by " + batsman_index_data[striker] + "\n")
                            striker_team_index, non_striker_team_index = non_striker_team_index, striker_team_index
                            striker, non_striker = non_striker, striker
                    
                    #If its a double
                    if res[0] == 2:
                            score += 2
                            print("A double by " + batsman_index_data[striker] + "\n")
                            
                    #If its a triple
                    if res[0] == 3:
                            score += 3
                            striker_team_index, non_striker_team_index = non_striker_team_index, striker_team_index
                            striker, non_striker = non_striker, striker
                            print("A triple by " + batsman_index_data[striker] + "\n")
                            
                    #If its a boundary
                    if res[0] == 4:
                            score+= 4
                            print(batsman_index_data[striker] + " scores a boundary!!!! Fours runs\n")
                            
                    #If its a five
                    if res[0] == 5:
                            score += 5
                            print("Very poor bowling or strategy gone wrong by " + bowler_index_data[bowler] + "\n")
                            
                    #If its a six
                    if res[0] == 6:
                            score += 6
                            print("A MAXIMUM!!!!\n" + batsman_index_data[striker] + " is on fire... SIX RUNS!!\n")

                    if (i==18) | (abs(score-target[0])<20):
                            already_updated = 1
                            print("Next ball here we go\n")
                            update_status(score,i,j,batting_team_name,bowling_team_name)
                            sleep(5)
                    
                    if score>=target[0]:
                            batting_win = 1
                            break
            if set_allout == 1:
                    break
            if batting_win == 1:
                    break
            striker_team_index, non_striker_team_index = non_striker_team_index, striker_team_index
            striker, non_striker = non_striker, striker
            print(str(score) + " - " + str(wickets) + " at the end of over " + str(i+1) + "\n")
            if already_update == 0:
                    update_status(score,i+1,0,batting_team_name,bowling_team_name)
    if batting_win == 1:
            print(batting_team_name + " defeated " + bowling_team_name + " by " + str(10 - wickets) + " wickets\n")
    else:
            print(bowling_team_name + " defeated " + batting_team_name + " by " + str(target[0] - score) + " runs\n")
    
    if set_allout==1:
            print("At the end of " + str(i) + "." + str(j) + " overs," + batting_team_name + " scored " + str(score) + " with all wickets fallen\n")
    else:
            print("At the end of 20 overs " + batting_team_name + " scored " + str(score) + " with a loss of " + str(wickets) + " wickets!\n")


def update_status(score_up,over_up,ball_up,name_of_batting_team,name_of_bowling_team):
    print(name_of_batting_team + " needs " + str(target[0]-score_up) + " to win from " + str(((20-over_up)*6) - (ball_up)) + " balls\n")


def countdown_delay(delay_time):
    for i in range(1,delay_time+1):
        sleep(1)
        print(str(i) + ", ")
    print("\n")


def start_match(first_bat,first_bowl):
    start_innings(team_squad_all[first_bat],team_squad_all[first_bowl],team_name_all[first_bat],team_name_all[first_bowl])
    print("Innings break for half a minute\n")
    print(team_name_all[first_bowl] + " needs " + str(target[0]) + " to win in 120 balls\n")
    countdown_delay(30)
    print("Starting second innings")
    sleep(5)
    start_chasing(team_squad_all[first_bowl],team_squad_all[first_bat],team_name_all[first_bowl],team_name_all[first_bat])
    print("THANK YOU FOR PLAYING, SEE YA NEXT TIME\n")


print("Welcome to IPL Match Simulator with scikit-learn in python\n\nPlease enter the name of your team (team 1)\n")
team_name_1 = input()
print("\nPlease follow the interface to add players to " + team_name_1 + "\n")
team1 = []
form_team(team1)
print("Please enter the name of the next team (team 2)\n")
team_name_2 = input()
print("\nPlease follow the interface to add players to " + team_name_2 + "\n")
team2 = []
form_team(team2)
print("Lets start the match\nToss starting in\n")
countdown_delay(5)
team_squad_all = [team1,team2]
team_name_all = [team_name_1,team_name_2]
toss_int = random.randint(0,1)
print(team_name_all[toss_int] + " tossing the coin!\nSo " + team_name_all[abs(toss_int-1)] + " should call it in the air.\n")
sleep(1)
print(team_name_all[toss_int] + " tosses the coin now\n")
sleep(1.5)
print(team_name_all[abs(toss_int-1)] + " calls now\nEnter 1 for heads\nEnter 2 for tails\n")
toss_call = int(input())
if random.randint(1,2)==toss_call:
    print(team_name_all[abs(toss_int-1)] + " won the toss\nEnter 1 for batting\nEnter 2 for bowling\n")
    toss_choice = int(input())
    if toss_choice == 1:
            start_match(abs(toss_int-1),toss_int)
    else:
            start_match(toss_int,abs(toss_int-1))
else:
    print(team_name_all[toss_int] + " won the toss\nEnter 1 for batting\nEnter 2 for bowling\n")
    toss_choice = int(input())
    if toss_choice == 1:
            start_match(toss_int,abs(toss_int-1))
    else:
            start_match(abs(toss_int-1),toss_int)

            
