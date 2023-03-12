"""
Inference pipeline for basic sentiment analysis

Steps:
    1. Load values from the artifacts folder
    2. Load pipeline from the artifacts folder
    3. predict values
"""
import os
import pandas as pd
import joblib
from .pipeline import lemma
from textblob import TextBlob


# def lemma(sentence: str):
#     return [word.lemma for word in TextBlob(sentence.lower()).words]

def predict(input_review): 
    # BASE_PATH = os.path.abspath(os.path.dirname(__file__))
    # ARTIFACTS_PATH = os.path.join(BASE_PATH, "artifacts", "pipeline")
    classifier = joblib.load(os.path.join("model","pipeline.joblib"))
    predictions = classifier.predict(input_review)
    print(predictions)
    return predictions
# review = input("Enter review: ").strip()
# while True:
#     if review == '' or review == '\n':
#         review = input("It is left blank, please enter your review: ").strip()
#     else:
#         break
# input_review = []
# input_review.append(review.strip())
# bad review
# input_review =["Regarding characters, Bocchi is… Not the best. She has social anxiety and plays guitar, and that is her ENTIRE personality. I’m not kidding, watch this show and it’s clear that Bocchi has nothing even resembling a personality outside of these two traits. The other characters are similarly one-dimensional — Ryo is quiet and says funny things sometimes. Basically, just imagine Ayanami Rei if she made jokes. There you go. Nijika is the most realistic character, which isn’t really a compliment, but at least she isn’t just based off of one trope. Oh, speaking of tropes, the other girl, Kita, is an extrovert. Yup… That’s all she is. Now, I don’t mind tropes. In fact, I enjoy them quite a bit. But the way this show executes them is just lazy at best, and pathetic and worst. The OP is actually quite good, and a few of the songs are as well (my favorite is the one played by the psychedelic rock band in one of the last episodes). The always-changing art direction is a bit of a messy subject, as sometimes it strikes gold, but most of the time just falls flat. My main problem with Bocchi, though, is that it’s just… too many things at once. It tries to be funny and engaging, while also trying to be touching and sweet, and additionally tries to be unique and interesting. Not that it’s impossible for these aspects to work well together — I mean, look at Haruhi. But Bocchi really is just unsuccessful with all of the things it tries to be and just comes out being just “okay”. I really do think Bocchi could have been a better anime, but with the way it turned out, all in all, it’s just pretty average. To close this off, I really don’t recommend you watch this show if you haven’t already. It’s just another cute girls show, except now it’s #relatable as well! As much as I’m picking on it, I didn’t dislike it, per say, but I definitely didn’t enjoy it. That’s enough from me, though.I hated it."]


# predictions = classifier.predict(X_test["review"].values)
# print(accuracy_score(y_test["sentiment"].values, predictions))
# print(classification_report(y_test["sentiment"].values, predictions))
