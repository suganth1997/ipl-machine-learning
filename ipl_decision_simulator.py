import pandas as pd
import pickle
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier

data = pd.read_csv('deliveries.csv')
data['batsman_index'] = 0
data['non_striker_index'] = 0
data['bowler_index'] = 0
data['dismissal_kind_index'] = 0
data = data[['over', 'ball', 'batsman', 'non_striker', 'bowler', 'batsman_runs', 'dismissal_kind', 'batsman_index', 'non_striker_index', 'bowler_index', 'dismissal_kind_index']].copy()

dismissal_kind_index_data = list(data.dismissal_kind.unique())
batsman_index_data = list(data.batsman.unique())
non_striker_index_data = list(data.non_striker.unique())
bowler_index_data = list(data.bowler.unique())

for i in range(0,150460):
	data.at[i,'dismissal_kind_index'] = dismissal_kind_index_data.index(data.iloc[i]['dismissal_kind'])
	data.at[i,'batsman_index'] = batsman_index_data.index(data.iloc[i]['batsman'])
	data.at[i,'non_striker_index'] = non_striker_index_data.index(data.iloc[i]['non_striker'])
	data.at[i,'bowler_index'] = bowler_index_data.index(data.iloc[i]['bowler'])

X = data[['over', 'ball', 'batsman_index', 'non_striker_index', 'bowler_index']].copy()
y = data[['batsman_runs', 'dismissal_kind_index']].copy()

##batsman_runs_classifier = DecisionTreeClassifier()
##batsman_runs_classifier.fit(X, y)


#decision_tree_pkl_filename = 'decision_tree_classifier_IPL.pkl'
#decision_tree_model_pkl = open(decision_tree_pkl_filename, 'wb')
#pickle.dump(batsman_runs_classifier, decision_tree_model_pkl)
#decision_tree_model_pkl.close()


##index_data_pkl = open('dismissal_kind_index_data.pkl','wb')
##pickle.dump(dismissal_kind_index_data, index_data_pkl)
##index_data_pkl.close()
##
##index_data_pkl = open('batsman_index_data.pkl','wb')
##pickle.dump(batsman_index_data, index_data_pkl)
##index_data_pkl.close()
##
##index_data_pkl = open('non_striker_index_data.pkl','wb')
##pickle.dump(non_striker_index_data, index_data_pkl)
##index_data_pkl.close()
##
##index_data_pkl = open('bowler_index_data.pkl','wb')
##pickle.dump(bowler_index_data, index_data_pkl)
##index_data_pkl.close()
