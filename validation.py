# Preprocessing
from sklearn.preprocessing import Normalizer
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.feature_selection import SelectKBest
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import Pipeline
from nltk.corpus import stopwords
import pandas as pd

# Transformers 
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer, TfidfTransformer 
from sklearn.decomposition import TruncatedSVD

# Models 
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC 
import xgboost as xgb
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import MultinomialNB

# Module to write final params 
import csv
import datetime
import pickle 

# Get a list of stopwords
stopwords = stopwords.words("english")

# Transformers 
c_vect = CountVectorizer(lowercase=True, encoding="utf-8", decode_error="ignore", strip_accents='unicode',stop_words=stopwords, analyzer = "word")
tfidf_vect = TfidfVectorizer(lowercase=True, encoding = "utf-8",  decode_error = 'ignore', strip_accents='unicode', stop_words=stopwords, analyzer = "word")  
tfidf_trans = TfidfTransformer()
svd = TruncatedSVD()
nml = Normalizer()

# Estimators 
log_reg = LogisticRegression()
svc = SVC(C = 1.0, kernel = 'rbf') # class weight , experiement values 
xgb = xgb.XGBClassifier(objective='multi:softmax')
decision_tree_clf = DecisionTreeClassifier()
rff = RandomForestClassifier()
multi_NB = MultinomialNB()

# Building pipeline 
# pipeline_cvect = Pipeline([('cvect', c_vect), ('clf', multi_NB)], verbose=True)
# pipeline_cvect_svd = Pipeline([('cvect', c_vect),('svd', svd), ("nml", nml), ('clf', multi_NB)], verbose=True)
pipeline_tfidf = Pipeline([('tfidf', tfidf_vect), ('clf', multi_NB)], verbose=True)
# pipeline_tfidf_svd = Pipeline([('tfidf', tfidf_vect), ('svd', svd), ("nml", nml), ('clf', multi_NB)], verbose=True)
# pipeline_cvect_tfidf = Pipeline([('cvect', c_vect),('tfidf', tfidf_trans), ('kbest', SelectKBest()), ('clf', multi_NB)], verbose=True)

# Read DataFrame
stemmed_df = pd.read_csv("preprocessed_reddit_train_SnowballStemmer.csv")
lemmatized_df = pd.read_csv("preprocessed_reddit_train_WordNetLemmatizer.csv")

# Separate X and Y 
X_stem = stemmed_df["cleaned"] 
y_stem = stemmed_df["label"]    
X_lemma = lemmatized_df["cleaned"]
y_lemma = lemmatized_df["label"]

""" 
Results
Model: Multinomial NB
Stemmed
10 folds: 0.5609857142857144
100 Folds: 0.5643571428571428
1000 Folds: 0.5639875000000001

Lemmatized
3 folds: 0.5482855547765574
5 folds: 0.5561857142857143
10 folds: 0.5603857142857143
100 Folds: 0.5641714285714287

Model: XGBoost 
Stemmed
Lemmatized
5 folds: 


Model: SVC 
Model: Logistic Regression:

"""

print("Mean cross validation score: ", cross_val_score(pipeline_tfidf, X_stem, y_stem, cv=100).mean()) 