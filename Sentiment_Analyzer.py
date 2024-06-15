import nltk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from Stopwords import find_stopwords, filter_review

# Reading the dataset for training
df_training = pd.read_csv('dataset_training.csv')