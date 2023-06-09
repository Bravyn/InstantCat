import stanza
#stanza.download('en')
nlp = stanza.Pipeline(
    lang= 'en',
    processors= 'tokenize, sentiment'
)

def sentiment_analyzer(text):
    sentiment = 0
    document = nlp(text)
    for sentence in document.sentences:
        sentiment += sentence.sentiment

    return sentiment

sentiment_analyzer("I love you")
