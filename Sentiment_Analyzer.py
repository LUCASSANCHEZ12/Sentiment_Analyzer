import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
import seaborn as sn
from Stopwords import filter_review
import dill as pickle

# Reading the dataset for training
df_training = pd.read_csv('dataset_training.csv')

reviews = df_training['review'].astype(str)
filtered_reviews = reviews.apply(filter_review)
#print(filtered_reviews)

df_filtered = pd.DataFrame(filtered_reviews, columns=['review'])
df_filtered['voted_up'] = df_training['voted_up'].astype(int)
print(df_filtered)

#plt.hist(df_filtered['voted_up'])
#plt.show()

df_train, df_test = train_test_split(df_filtered)
vectorizer = TfidfVectorizer(max_features=2000)

X_train = vectorizer.fit_transform(df_train['review'])
X_test = vectorizer.transform(df_test['review'])

Y_train = df_train['voted_up']
Y_test = df_test['voted_up']

model = LogisticRegression(max_iter=1000)
model.fit(X_train, Y_train)
print("Train acc:", model.score(X_train, Y_train))
print("Test acc:", model.score(X_test, Y_test))

P_test = model.predict(X_test)

# modularizar
def plot_cm(cm):
    classes = ['Negative', 'Positive']
    df_cm = pd.DataFrame(cm, index=classes, columns=classes)
    ax = sn.heatmap(df_cm, annot=True, fmt='g')
    ax.set_xlabel("Prediction")
    ax.set_ylabel("Objective")
    plt.title("Confusion Matrix")
    plt.show()

cm = confusion_matrix(Y_test, P_test, normalize='true')
plot_cm(cm)
