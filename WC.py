import matplotlib.pyplot as plt
from wordcloud import WordCloud
text = "If I could invent a superhero, I would invent one called Disappointment Panda. He'd wear a cheesy eye mask and a shirt that was way too small for his big panda belly, and his superpower would be to tell people harsh truths about themselves that they needed to hear but didn't want to accept. He would go door-to-door like a Bible salesman and ring doorbells and say things like, “Sure, making a lot of money makes you feel good, but it won't make your kids love you,” or “If you have to ask yourself if you trust your wife, then you probably don't,” or “What you consider ‘friendship’ is really just your constant attempts to impress people.” Then he'd tell the homeowner to have a nice day and saunter on down to the next house. It would be awesome. And sick. And sad. And uplifting. And necessary. After all, the greatest truths in life are usually the most unpleasant to hear. Disappointment Panda would be the hero that none of us would want but all of us would need. He'd be the proverbial vegetables to our mental diet of junk food. He'd make our lives better despite making us feel worse. He'd make us stronger by tearing us down, brighten our future by showing us the darkness. Listening to him would be like watching a movie where the hero dies in the end: you love it even more despite making you feel horrible, because it feels real. So while we're here, allow me to put on my Disappointment Panda mask and drop another unpleasant truth on you: We suffer for the simple reason that suffering is biologically useful."
rem = (" and", " And", " or", " He'd", " he'd", " don't", " won't", " us ", "feel", "make")

for i in rem:
    text = text.replace(i," ")


def plot_cloud(wordcloud):
    plt.figure(figsize=(50,40))
    plt.imshow(wordcloud, interpolation = "bilinear") 
    plt.axis("off")
    plt.show()


wordcloud = WordCloud(width = 3000,
                      height = 2000,
                      max_words = 500,
                      min_font_size = 3).generate(text)
print("Image Creation Successful")
plot_cloud(wordcloud)
