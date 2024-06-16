import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from Stopwords import find_stopwords, filter_review

# Reading the dataset for training
df_training = pd.read_csv('dataset_training.csv')

reviews = df_training['review'].astype(str)
filtered_reviews = reviews.apply(filter_review)
#print(filtered_reviews)

df_filtered = pd.DataFrame(filtered_reviews, columns=['review'])
df_filtered['voted_up'] = df_training['voted_up'].astype(int)
print(df_filtered)

plt.hist(df_filtered['voted_up'])
plt.show()
