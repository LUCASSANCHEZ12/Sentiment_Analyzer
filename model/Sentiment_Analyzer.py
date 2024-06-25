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

# Filtering the rewviews
df_filtered = pd.DataFrame(filtered_reviews, columns=['review'])
df_filtered['voted_up'] = df_training['voted_up'].astype(int)
print(df_filtered)

# splitting the data for training and testing 
df_train, df_test = train_test_split(df_filtered)

# tokenizing and assiigning a number to each word based on frequency
vectorizer = TfidfVectorizer(max_features=2000)

# fitting the data to the vectorize
X_train = vectorizer.fit_transform(df_train['review'])
X_test = vectorizer.transform(df_test['review'])

Y_train = df_train['voted_up']
Y_test = df_test['voted_up']

#Creating the logistic model
model = LogisticRegression(max_iter=1000)

#Training the model
model.fit(X_train, Y_train)

#Testing the trained model
P_test = model.predict(X_test)

# Plotting the model
def plot_cm(cm):
    classes = ['Negative', 'Positive']
    df_cm = pd.DataFrame(cm, index=classes, columns=classes)
    ax = sn.heatmap(df_cm, annot=True, fmt='g')
    ax.set_xlabel("Prediction")
    ax.set_ylabel("Objective")
    plt.title("Confusion Matrix")
    plt.show()

cm = confusion_matrix(Y_test, P_test, normalize='true')

# Frequency of words
word_index_map = vectorizer.vocabulary_
cut = 4.5

# Show most positive and negative words of the training
print("\n\n-------------------Most positive words:")
for word, index in word_index_map.items():
    weight = model.coef_[0][index]
    if weight > cut:
        print(word, weight)
        
print("\n-------------------Most negative words:")
for word, index in word_index_map.items():
    weight = model.coef_[0][index]
    if weight < -cut:
        print(word, weight)

# Plot the distribuition of the words
plt.hist(model.coef_[0], bins=10)
plt.show()

# plot the confussion matrix of the trained model
cm = confusion_matrix(Y_test, P_test, normalize='true')
plot_cm(cm)

# Saving the model     
with open('model_1_en.pkl', 'wb') as fout:
    pickle.dump(model, fout)
    
# Saving the vectorizer
with open('vectorizer.pkl', 'wb') as fout:
    pickle.dump(vectorizer, fout)