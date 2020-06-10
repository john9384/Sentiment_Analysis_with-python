import string
from collections import Counter
import matplotlib.pyplot as plt


def sentiment(stopwords, text):
    arr_stopwords = stopwords.split()
    lower_case = text.lower()
    cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))
    tokenized_words = cleaned_text.split()

    final_words = []

    for word in tokenized_words:
        if word not in arr_stopwords:
            final_words.append(word)

    emotion_list = []
    with open('emotions.txt', 'r') as file:
        for line in file:
            clear_line = line.replace('\n', '').replace(',', '').replace("'", '').strip()
            word, emotion = clear_line.split(':')

            if word in final_words:
                emotion_list.append(emotion)
    return emotion_list


def plot_graph(emotion_list):
    count = Counter(emotion_list)
    fig, axs = plt.subplots()
    axs.bar(count.keys(), count.values())
    fig.autofmt_xdate()
    plt.savefig('graph.png')
    plt.show()


text = open('read.txt', encoding='utf-8').read()


def analysis(speech):
    stopwords = open('stopwords.txt', encoding='utf-8').read()
    emotion_list = sentiment(stopwords, speech)
    plot_graph(emotion_list)


analysis(text)
