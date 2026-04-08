import re

STOPWORDS = ["de", "da", "do", "das", "dos", "a", "o", "e", "é"]

def text_to_glossa(text):
    text = text.lower()

    # remove pontuação
    text = re.sub(r'[^\w\s]', '', text)

    words = text.split()

    # remove palavras irrelevantes
    words = [w for w in words if w not in STOPWORDS]

    # glossa: tudo em maiúsculo
    glossa = " ".join(words).upper()

    return glossa