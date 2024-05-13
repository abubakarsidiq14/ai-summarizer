from nltk.tokenize import sent_tokenize
from summarizer import summarize
def generate_summary(text):
    sentences = summarize("Title", text)
    summary = summarize(text)
    return summary
