"""
Sklearn pipeline for basic sentiment analysis

Steps:
    1. Load data
    2. Use ordinal encoder for sentiments -> 0,1
    3. Split data into train test
    4. create pipleline with:
        a. CountVectorizer
        b. TfidfTransformer
        c. SVC
    5. Define paramenters for GridSearchCV
    6. Run the training (fit)
    7. Save the best estimators
"""
import os

import joblib
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.metrics import classification_report
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OrdinalEncoder
from sklearn.svm import SVC
from textblob import TextBlob

BASE_PATH = os.path.abspath(os.path.dirname(__file__))
DATASET_FILE_NAME = "sentiment analysis dataset.csv"
ARTIFACTS_PATH = os.path.join(BASE_PATH, "artifacts", "pipeline")


def lemma(sentence: str):
    return [word.lemma for word in TextBlob(sentence.lower()).words]


if __name__ == "__main__":
    if not os.path.exists(ARTIFACTS_PATH):
        os.makedirs(ARTIFACTS_PATH)

    df = pd.read_csv(os.path.join(BASE_PATH, DATASET_FILE_NAME))

    # sampling for checking pipeline
    df = df.iloc[:30000]
    enc = OrdinalEncoder()
    df[["sentiment"]] = enc.fit_transform(df[["sentiment"]])

    X_train, X_test, y_train, y_test = train_test_split(
        df["review"], df["sentiment"], test_size=0.2
    )
    # X_test.to_csv(os.path.join(ARTIFACTS_PATH, "X_test.csv"), index=False)
    # y_test.to_csv(os.path.join(ARTIFACTS_PATH, "y_test.csv"), index=False)
    print(f'Number of train data is {len(X_train)} and test data for X is {len(X_test)}')
    print(f'Number of train data is {len(y_train)} and test data for y is {len(y_test)}')

    pipe = Pipeline(
        [
            ("count_vectorizer", CountVectorizer(analyzer=lemma)),
            ("tf_idf_transformer", TfidfTransformer()),
            ("svc", SVC()),
        ]
    )
    parameters = {
        "count_vectorizer__ngram_range": [(1, 1), (1, 2)],
        "tf_idf_transformer__use_idf": (True, False),
        "svc__kernel": ("rbf",),
        "svc__C": [10,],
    }
    clf = GridSearchCV(pipe, parameters)
    clf.fit(X_train.values, y_train.values)
    print(clf)
    print(clf.best_estimator_)

    predictions = clf.predict(X_test.values)
    print(classification_report(y_test, predictions))

    joblib.dump(clf.best_estimator_, os.path.join(ARTIFACTS_PATH, "pipeline.joblib"))
