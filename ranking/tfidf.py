from argparse import ArgumentParser
import glob
import os

from index_pdf import index_document

argparser = ArgumentParser(prog='tf-idf', description='TF-IDF по папке с пдфками')
argparser.add_argument('--path', help='Путь к папке с пдфками')
argparser.add_argument('--prompt', default='?', help='Поисковый запрос')
args = argparser.parse_args()

document_paths = glob.glob(os.path.join(args.path, '*.pdf'))

print('Indexing...')
index = [(path, index_document(path)) for path in document_paths]
print('Done!')

all_terms = {}
for doc in index:
    for word, freq in doc[1].items():
        if not word in all_terms:
            all_terms[word] = freq
        else:
            all_terms[word] += freq

prompt = input('Enter search prompt: ') if args.prompt == '?' else args.prompt
scores = [0.0 for _ in index]

for word in prompt.split(' '):
    for i, doc in enumerate(index):
        terms = doc[1]
        if not word in terms:
            continue
        tf = terms[word]
        df = all_terms[word]
        scores[i] += tf/df

print('Documents:')
sorted_documents = list(zip(index, scores))
sorted_documents.sort(key=lambda x: x[1], reverse=True)
for doc in sorted_documents[:3]:
    print(f'{doc[0][0]} => {doc[1]}')
