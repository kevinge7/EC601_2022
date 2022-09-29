from google.cloud import language


def analyze_text_sentiment(text):
    client = language.LanguageServiceClient()
    document = language.Document(content=text, type_=language.Document.Type.PLAIN_TEXT)

    response = client.analyze_sentiment(document=document)

    sentiment = response.document_sentiment
    results = dict(
        text=text,
        score=f"{sentiment.score:.1%}",
        magnitude=f"{sentiment.magnitude:.1%}",
    )
    for k, v in results.items():
        print(f"{k:10}: {v}")
    
text = "First on CNN: European security officials observed Russian Navy ships in vicinity of Nord Stream pipeline leaks"
analyze_text_sentiment(text)

#the result is 
#text      : First on CNN: European security officials observed Russian Navy ships in vicinity of Nord Stream pipeline leaks
#score     : -40.0%
#magnitude : 40.0%
