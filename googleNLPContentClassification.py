from google.cloud import language


def classify_text(text):
    client = language.LanguageServiceClient()
    document = language.Document(content=text, type_=language.Document.Type.PLAIN_TEXT)

    response = client.classify_text(document=document)

    for category in response.categories:
        print("=" * 80)
        print(f"category  : {category.name}")
        print(f"confidence: {category.confidence:.0%}")
    
text = (
    "Ukraine and its western allies have categorically rejected the planned annexation of the four regions – Donetsk, Luhansk and much of Kherson and Zaporizhzhia, a swathe of Ukrainian land that contains heavy industry, rich farmland and a critical freshwater conduit for Crimea."
)
classify_text(text)

#At this case, it won't return any result for us. Because we only have one sentence and cannot analyse anything. 

text = (
    "Python is an interpreted, high-level, general-purpose programming language. "
    "Created by Guido van Rossum and first released in 1991, "
    "Python's design philosophy emphasizes code readability "
    "with its notable use of significant whitespace."
)
classify_text(text)
#This will return 
# ================================================================================
# category  : /Computers & Electronics/Programming
# confidence: 99%
# ================================================================================
# category  : /Science/Computer Science
# confidence: 99%
