from PyPDF2 import PdfReader
import nltk

def index_document(path):
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
        break


    # print(text)
    # print('-------------------------------------')

    # делим текст на слова
    words = nltk.word_tokenize(text)
    words.remove

    stopwords = { ',', '.', '!', '?', '(', ')' }
    words = [word for word in words if not word.lower() in stopwords]

    terms = {}
    for word in words:
        # отсекаем короткие слова
        if len(word) > 2:
            if not word in terms:
                terms[word] = 1
            else:
                terms[word] += 1
    return terms
