from google.cloud import language


def analyze_text_entities(text):
    client = language.LanguageServiceClient()
    document = language.Document(content=text, type_=language.Document.Type.PLAIN_TEXT)

    response = client.analyze_entities(document=document)

    for entity in response.entities:
        print("=" * 80)
        results = dict(
            name=entity.name,
            type=entity.type_.name,
            salience=f"{entity.salience:.1%}",
            wikipedia_url=entity.metadata.get("wikipedia_url", "-"),
            mid=entity.metadata.get("mid", "-"),
        )
        for k, v in results.items():
            print(f"{k:15}: {v}")
            
text = "The Cable News Network is a multinational cable news channel headquartered in Atlanta, Georgia, U.S. It is owned by CNN Global, which is part of Warner Bros. Discovery. It was founded in 1980 by American media proprietor Ted Turner and Reese Schonfeld as a 24-hour cable news channel"
analyze_text_entities(text)

# Here is the result:
#     ================================================================================
# name           : Cable News Network
# type           : ORGANIZATION
# salience       : 68.6%
# wikipedia_url  : https://en.wikipedia.org/wiki/CNN
# mid            : /m/0gsgr
# ================================================================================
# name           : CNN Global
# type           : ORGANIZATION
# salience       : 12.1%
# wikipedia_url  : -
# mid            : -
# ================================================================================
# name           : part
# type           : OTHER
# salience       : 4.5%
# wikipedia_url  : -
# mid            : -
# ================================================================================
# name           : Ted Turner
# type           : PERSON
# salience       : 3.6%
# wikipedia_url  : https://en.wikipedia.org/wiki/Ted_Turner
# mid            : /m/07hkd
# ================================================================================
# name           : Atlanta
# type           : LOCATION
# salience       : 3.1%
# wikipedia_url  : https://en.wikipedia.org/wiki/Atlanta
# mid            : /m/013yq
# ================================================================================
# name           : Georgia
# type           : LOCATION
# salience       : 2.1%
# wikipedia_url  : https://en.wikipedia.org/wiki/Georgia_(U.S._state)
# mid            : /m/0d0x8
# ================================================================================
# name           : U.S.
# type           : LOCATION
# salience       : 2.1%
# wikipedia_url  : https://en.wikipedia.org/wiki/United_States
# mid            : /m/09c7w0
# ================================================================================
# name           : Warner Bros. Discovery
# type           : OTHER
# salience       : 1.9%
# wikipedia_url  : https://en.wikipedia.org/wiki/Warner_Bros._Discovery
# mid            : /g/11nn31kl0b
# ================================================================================
# name           : cable news channel
# type           : ORGANIZATION
# salience       : 1.0%
# wikipedia_url  : -
# mid            : -
# ================================================================================
# name           : Reese Schonfeld
# type           : PERSON
# salience       : 0.7%
# wikipedia_url  : https://en.wikipedia.org/wiki/Reese_Schonfeld
# mid            : /m/069jp5
# ================================================================================
# name           : 1980
# type           : DATE
# salience       : 0.0%
# wikipedia_url  : -
# mid            : -
# ================================================================================
# name           : 1980
# type           : NUMBER
# salience       : 0.0%
# wikipedia_url  : -
# mid            : -
# ================================================================================
# name           : 24
# type           : NUMBER
# salience       : 0.0%
# wikipedia_url  : -
# mid            : -
