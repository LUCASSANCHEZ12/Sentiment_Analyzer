import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from Stopwords import find_stopwords, filter_review

# Reading the dataset for training
df_training = pd.read_csv('dataset_training.csv')

reviews = df_training['review'].astype(str)
filtered_reviews = reviews.apply(filter_review)
print(filtered_reviews)
