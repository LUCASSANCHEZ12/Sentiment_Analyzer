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
stop_words_en = set(stopwords.words('english'))
# Define additional stopwords
additional_exclusions = {'persona', 'team', 'minecraft', 'arma', 'bean', 'boss','ps4','wild','moon','2d','wasteland','ultra','military','editor','allows','solid','journey','expert','bungie','season','terraria','minor','hunting','kojima','deck','destiny','remaster','complain','fall','slay','gta','atlus','spire','terrarium','rockstar','biome','mafia','castle',
                         'access','instead','idea','sorry','ca','dlc','dayz','until','valve','tutorial','concept','swing','horde','regionlockchina','unless','sims','ark','was','company','customer','state','software','advertised','region','survivor','2016','fighter','headshot','zombie','alpha','trailer','planet','pubg','microtransactions','payday','too','camping','ubisoft','galaxy','rome','skyrim','vr','h1z1','vegas','warband','flight','creation','forum','netcode','sky','elite','china','chinese','hero','policy','pile','untill','zombies','xcom','rust','capcom'}

stop_words_en = stop_words_en.union(additional_exclusions)

def filter_review(reviews):
  #Tokenize the text
  tokens = word_tokenize(reviews.lower())

  #Remove stop words
  filtered_tokens = [token for token in tokens if token not in stop_words_en]

  #Lemmatize the tokens (to mantain the context)
  lemmatizer = WordNetLemmatizer()
  lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
  
  # Remove extra words after lemmatizer
  final_tokens = [token for token in lemmatized_tokens if token not in stop_words_en]

  #Join the tokens back into a string
  processed_text = ' '.join(final_tokens)
  return processed_text