from transformers import pipeline  

# Load pre-trained model
classifier = pipeline("text-classification", model="mrm8488/bert-tiny-finetuned-fake-news")

def predict_news(news_text):
    result = classifier(news_text)
    return result[0]["label"]  # Returns "LABEL_0" (Real) or "LABEL_1" (Fake)
