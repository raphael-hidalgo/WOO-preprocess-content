import emoji
import string
import re
from nltk.stem.snowball import FrenchStemmer
stemmer = FrenchStemmer()
from nltk.corpus import stopwords
stopWords = set(stopwords.words('french'))

def deEmojify(text):
    regrex_pattern = re.compile(pattern = "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags = re.UNICODE)
    return regrex_pattern.sub(r'',text)

def all_text(i):
    table = str.maketrans(dict.fromkeys(string.punctuation))  # OR {key: None for key in string.punctuation}
    i = str(i).lower()
    emo = emoji.distinct_emoji_lis(i)
    emo = " ".join(emo)
    i = deEmojify(i)
    i = emo +' '+ i
    i = emoji.demojize(i, delimiters=(':', ': '), language='fr')
    i = i.split(sep='#')[0]
    i = i.replace('_',' ')
    i = i.replace('\n','')
    i = i.replace('  ',' ')
    i = i.translate(table)
    i = i.strip()
    return i

def stop_words(i):
    clean = []
    for word in i.split():
        if word not in stopWords:
            clean.append(word)
    return " ".join(clean)

def stemmered(i):
    l = []
    for word in i.split():
        l.append(stemmer.stem(word))
    return " ".join(l)

def remove_accents(i):
    i = re.sub(u"[àáâãäå]", 'a', i)
    i = re.sub(u"[èéêë]", 'e', i)
    i = re.sub(u"[ìíîï]", 'i', i)
    i = re.sub(u"[òóôõö]", 'o', i)
    i = re.sub(u"[ùúûü]", 'u', i)
    i = re.sub(u"[ýÿ]", 'y', i)
    i = re.sub(u"[ß]", 'ss', i)
    i = re.sub(u"[ñ]", 'n', i)
    return i

def preprocess_content(data.content):
    return data.content.apply(all_text).apply(remove_accents).apply(stop_words).apply(stemmered)
