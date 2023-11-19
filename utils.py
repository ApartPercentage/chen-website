import pickle

with open("models/1/cv.pkl", "rb") as tokenized:
  tokenizer = pickle.load(tokenized)

with open("models/1/clf.pkl", "rb") as email_model:
  esc_model = pickle.load(email_model)
#tokenizer = pickle.load(open("models/1/cv.pkl", "rb"))
#esc_model = pickle.load(open("models/1/clf.pkl", "rb"))

def esc_prediction(email):
  tokenized_email = tokenizer.transform([email])
  prediction = esc_model.predict(tokenized_email)
  prediction = 1 if prediction == 1 else -1
  return prediction