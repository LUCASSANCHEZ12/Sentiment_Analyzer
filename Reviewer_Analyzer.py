import dill as pickle
import pandas as pd
from Stopwords import filter_review

with open('model_1_en.pkl', 'rb') as fin:
    model_loaded = pickle.load(fin)

with open('vectorizer.pkl', 'rb') as fin:
    vectorizer = pickle.load(fin)


def get_prediction(text):
  processed_text = filter_review(text)
  vectorized_text = vectorizer.transform([processed_text])
  prediction = model_loaded.predict(vectorized_text)[0]
  return prediction

df_test = pd.DataFrame({ 'review': ["sex? pssssh, who needs that, just play Left For Dead 2! i got this game as a gift from a friend, have wanted it for years, its just as amazing as a thought it'd be, thank you Insert name here (you know who you are)","My boyfriend makes me play this game with him. I unwillingly have 36.8 hours on this game in the first 2 weeks I've owned it. Don't tell him I kinda like it.","im biased towards saying its a great game but its lots of fun. it being out since x360 makes it hard to find people to play with. recommend joining a discord community for that.","Best game of whatever year, would recommend for anyone that's into killing, action games","15 years later, and L4D2 is still going strong. So much replayability with the mutations. My personal favorite is by far the TAAAAANK mutation.The downside of the game is the bots. It can feel like they are coded to be in your way, walk in front of your bullets, stand with their backs against the tanks, or just refuse to go into the safe room. But despite that, the game is still great!","i really love the games valve makes","absolutely love this game but man am i tired of all the gate keeping with roles. i understand you dont want new players in leader roles but dude why is it automated on so many servers to kick you if you arent a certain level and you decide to be lets say a spotter for your buddy who is a sniper, im not a noob of war sims why is this sh*t automated. you should be able to see im doing my role properly. man this is just sad, im tired of horrible leaders who dont put down there outposts yet i get kicked bc im 4 levels to low while im communicating and doing my job. my god these communities man....","Downloaded for F2P 3 days, played less than 2 hours, ran across the map at start of the game, maps are as bare as a tree in winter, hardly anyone playing. As another review mentioned, its a circle jerk running party. Don't get me wrong, the maps are amazing and beautiful, but way to big for a simulation for 100 people. I thought Planetside 2 maps were big, but action gets intense in that game, unlike HLL.","The rules on community servers are created by a gate keeping toxic gestapo with roles. Kicked from a few servers for playing spotter role under level 30. Also, landing a recon role is as slim as landing a recon in Day of Defeat source, and may also result in a kick/ban on those servers. Not the best welcome party for community servers.","Hardly any official servers, maybe 1 US server, others are international. Make a conscious decision, do not waste your money on a game that is very barren."]})

df_test['reviews_prediccion'] = df_test['review'].apply(get_prediction)
print(df_test)
