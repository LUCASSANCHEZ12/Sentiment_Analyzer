import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# downloading the stopwords from nltk
nltk.download('stopwords')
# donwloading the resource word_tokenize
nltk.download('punkt')
# donwloading the resource wordnet
nltk.download('wordnet')

# setting the stopwords dictionary to english language
stop_words_es = set(stopwords.words('english'))

def find_stopwords(text):
    # tokenizing the text 
    words = word_tokenize(text)
    # filtering the stopwords from the text
    filtered_words = [word for word in words if word not in stop_words_es]
    # joining the text again 
    return " ".join(filtered_words)


def filter_review(reviews):
  #Tokenize the text
  tokens = word_tokenize(reviews)

  #Remove stop words
  filtered_tokens = [token for token in tokens if token not in stop_words_es]

  #Lemmatize the tokens (to mantain the context)
  lemmatizer = WordNetLemmatizer()
  lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]

  #Join the tokens back into a string
  processed_text = ' '.join(lemmatized_tokens)
  return processed_text