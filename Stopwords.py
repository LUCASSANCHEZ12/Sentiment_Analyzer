import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# downloading the stopwords from nltk
nltk.download('stopwords')
# donwloading the resource word_tokenize
nltk.download('punkt')

# setting the stopwords dictionary to english language
stop_words_es = set(stopwords.words('english'))

def find_stopwords(text):
    # tokenizing the text 
    words = word_tokenize(text)
    # filtering the stopwords from the text
    filtered_words = [word for word in words if word not in stop_words_es]
    # joining the text again 
    return " ".join(filtered_words)

text = "This is a example text to find the stopwords."
print(find_stopwords(text))
