import pandas as pd
#import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("data/survey_results_public.csv", low_memory=False)
#Ceci c'est pour lire les 5 premières lignes des données récupérées précédemment
df.head()
#La ligne suivante permet de sélectionner uniquement les colonnes qui nous intéressent pour le traitement
df = df [["Country", "EdLevel", "YearsCodePro", "Employment", "ConvertedComp"]]

#Pour renommer Converted en Salary, axis=1 pour dire que c'est une colonne; axis=0 c'est pour une ligne (on dit aussi index)
df = df.rename({"ConvertedComp":"Salary"}, axis=1)
df.head()
#On retire les lignes qui ont des valeurs nulles pour Salary
df = df[df["Salary"].notnull()]
df.head()
#Pour avoir les détails sur le DataFrame, les types de données, etc
df.info()
#Ceci pour supprimer directment les lignes qui ont une ou plusieurs valeurs nulles
df = df.dropna()
#Pour s'assurer qu'il n'y a plus de lignes avec de valeurs nulles
df.isnull().sum()
#Pour choisir seulement els lignes où employment est à full-time
df = df[df["Employment"] == "Employed full-time"]
#Pour supprimer la colonne Emplyment puisque maintenant elle contient la même chose, full-time
df = df.drop("Employment", axis=1)
df.info()
#Pour compter le nombre de personnes par pays
df['Country'].value_counts()


def shorten_categories(categories, cutoff):
    categorical_map = {}
    for i in range(len(categories)):
        if categories.values[i] >= cutoff:
            categorical_map[categories.index[i]] = categories.index[i]
        else:
            categorical_map[categories.index[i]] = 'Other'
    return categorical_map


country_map = shorten_categories(df.Country.value_counts(), 400)
df['Country'] = df['Country'].map(country_map)
df.Country.value_counts()
#C'est pour créer la figure et l'axe, on peut le faire séparémment comme ceci:  fig = plt.figure(figsize=(12, 7))  et ax = fig.add_subplot(111)
fig, ax = plt.subplots(1, 1, figsize=(12, 7))
#Salary sur y et Country sur x
df.boxplot('Salary', 'Country', ax=ax)
plt.suptitle('Salary (US$) v Country')
plt.title('')
plt.ylabel('Salary')
plt.xticks(rotation=90)
plt.show()
#Les lignes suivantes pour supprimer des lignes et conserver seulement celles qui respectent les conditions
df = df[df["Salary"] <= 250000 ]
df = df[df["Salary"] >= 10000 ]
df = df[df['Country'] != 'Other' ]
fig, ax = plt.subplots(1, 1, figsize=(12, 7))
df.boxplot('Salary', 'Country', ax=ax)
plt.suptitle('Salary (US$) v Country')
plt.title('')
plt.ylabel('Salary')
plt.xticks(rotation=90)
plt.show()
#Pour voir les différentes valeurs de YearsCodePro
df["YearsCodePro"].unique()
def clean_experience(x):
    if x == 'More than 50 years':
        return 50
    if x == 'Less than 1 year':
        return 0.5
    return float(x)

df['YearsCodePro'] = df['YearsCodePro'].apply(clean_experience)
#Pour voir les différentes valeurs de EdLevel
df["EdLevel"].unique()


def clean_education(x):
    if 'Bachelor’s degree' in x:
        return 'Bachelor’s degree'
    if 'Master’s degree' in x:
        return 'Master’s degree'
    if 'Professional degree' in x or 'Other doctoral' in x:
        return 'Post grad'
    return 'Less than a Bachelors'

df['EdLevel'] = df['EdLevel'].apply(clean_education)
#Pour voir les différentes valeurs de EdLevel
df["EdLevel"].unique()
#Les modèles ne comprennent que les nombres donc on utilise LabelEncoder pour transformer les catégories en nombres


from sklearn.preprocessing import LabelEncoder
le_education = LabelEncoder()
df['EdLevel'] = le_education.fit_transform(df['EdLevel'])
df["EdLevel"].unique()
le_country = LabelEncoder()
df['Country'] = le_country.fit_transform(df['Country'])
df["Country"].unique()
#La première ligne crée une copie de df sans la colonne Salary
X = df.drop("Salary", axis=1)
y = df["Salary"]
"""
On importe l'algorithme de Régression Linéaire. C'est un modèle qui cherche à tracer une ligne droite 
(ou un "plan" en plusieurs dimensions) qui passe le plus près possible de tous les points de données pour 
prédire une valeur numérique (le salaire).


linear_reg.fit(X, y.values)
C'est l'étape cruciale de l'entraînement (le Learning dans Machine Learning).
X : Ce sont vos variables prédictives (ex: Pays, Niveau d'étude, Expérience). On l'appelle souvent 
la matrice de caractéristiques (features).
y.values : C'est votre cible (le Salaire), ce que le modèle doit apprendre à deviner.
.fit() : Cette méthode dit au modèle : "Regarde les données dans X et essaie de trouver la formule mathématique 
qui permet d'arriver au résultat y".


Maintenant que le modèle est "entraîné", vous pouvez lui demander de prédire un salaire pour quelqu'un qu'il n'a jamais vu :
python

y_pred = linear_reg.predict(X)

"""
from sklearn.linear_model import LinearRegression
linear_reg = LinearRegression()
linear_reg.fit(X, y.values)
y_pred = linear_reg.predict(X)


from sklearn.metrics import mean_squared_error, mean_absolute_error
import numpy as np
error = np.sqrt(mean_squared_error(y, y_pred))
error
"""
On importe l'algorithme d'Arbre de Décision pour la Régression. Contrairement à la ligne droite
de la régression linéaire, ce modèle cherche à créer une structure de choix (comme un organigramme). 
Il découpe vos données en groupes de plus en plus précis pour prédire le salaire.

"""
from sklearn.tree import DecisionTreeRegressor
dec_tree_reg = DecisionTreeRegressor(random_state=0)
dec_tree_reg.fit(X, y.values)
y_pred = dec_tree_reg.predict(X)
error = np.sqrt(mean_squared_error(y, y_pred))
print("${:,.02f}".format(error))
"""
Le concept : Par défaut, il va créer 100 (par défaut mais on peut changer avec n_estimators=50) arbres de décision différents.
L'aspect "Aléatoire" : Chaque arbre ne voit pas tout à fait les mêmes données. Certains vont se spécialiser sur 
l'expérience, d'autres sur le pays. Cela évite qu'un seul arbre ne fasse une erreur monumentale.
random_state=0 : Comme pour l'arbre simple, cela permet de stabiliser le hasard pour que tes 100 arbres soient 
les mêmes à chaque exécution du code.

"""
from sklearn.ensemble import RandomForestRegressor
random_forest_reg = RandomForestRegressor(random_state=0)
random_forest_reg.fit(X, y.values)
y_pred = random_forest_reg.predict(X)
error = np.sqrt(mean_squared_error(y, y_pred))
print("${:,.02f}".format(error))
"""
Ce bloc utilise la technique de Grid Search pour trouver la configuration optimale de l'arbre de décision avec le type de
modèle qu'on a choisi, ici DecisionTreeRegressor.
max_depth : Liste des profondeurs maximales à tester pour l'arbre.
None : L'arbre s'étend jusqu'à ce que toutes les feuilles soient pures (risque d'overfitting).
2 à 12 : Valeurs fixes pour contraindre l'arbre à rester simple et à mieux généraliser.
parameters : Dictionnaire associant le nom du paramètre de l'algorithme ("max_depth") aux valeurs à tester.

scoring='neg_mean_squared_error' : La métrique de performance. On cherche à minimiser l'erreur quadratique 
moyenne (MSE). En Scikit-Learn, elle est exprimée en "négatif" car l'outil cherche toujours à maximiser un score 
(maximiser un nombre négatif revient à minimiser l'erreur).
"""
from sklearn.model_selection import GridSearchCV

max_depth = [None, 2,4,6,8,10,12]
parameters = {"max_depth": max_depth}

regressor = DecisionTreeRegressor(random_state=0)
gs = GridSearchCV(regressor, parameters, scoring='neg_mean_squared_error')
gs.fit(X, y.values)
#Ici on choisit le meilleur modèle trouvé par GridSearchCV


regressor = gs.best_estimator_

regressor.fit(X, y.values)
y_pred = regressor.predict(X)
error = np.sqrt(mean_squared_error(y, y_pred))
print("${:,.02f}".format(error))
X
X = np.array([["United States", 'Master’s degree', 15 ]])
#df = pd.DataFrame(X, columns=["Country", "EdLevel", "YearsCodePro"])
#df
X

#Applique mon encodeur sur toutes les lignes de la première colonne pour les tranformer en nombres
X[:, 0] = le_country.transform(X[:, 0])
#Applique mon encodeur sur toutes les lignes de la deuxième colonne pour les tranformer en nombres
X[:, 1] = le_education.transform(X[:, 1])
#Forcer toutes les valeurs de X à devenir des floats
X = X.astype(float)
X
y_pred = regressor.predict(X)
y_pred
import pickle
#Ce bloc pour exporter le modèle et les encodeurs pour pouvoir les réutiliser ailleurs 
data = {"model": regressor, "le_country": le_country, "le_education": le_education}
with open('saved_steps.pkl', 'wb') as file:
    pickle.dump(data, file)
#Ce bloc pour charger le modèles et les encodeurs qu'on avait exporté plutôt
with open('saved_steps.pkl', 'rb') as file:
    data = pickle.load(file)

regressor_loaded = data["model"]
le_country = data["le_country"]
le_education = data["le_education"]
y_pred = regressor_loaded.predict(X)
y_pred

