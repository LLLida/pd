from argparse import ArgumentParser
import glob
import os

from index_pdf import index_document

argparser = ArgumentParser(prog='tf-idf', description='TF-IDF по папке с пдфками')
argparser.add_argument('--path', help='Путь к папке с пдфками')
argparser.add_argument('--prompt', default='?', help='Поисковый запрос')
argparser.add_argument('--num_matches', default=3, type=int, help='Количество лучших документов, которые нужно вывести')
args = argparser.parse_args()

document_paths = glob.glob(os.path.join(args.path, '*.pdf'))

print('Indexing...')
documents = [index_document(path) for path in document_paths]
print('Done!')

all_terms = {}
for doc in documents:
    for word, freq in doc.terms.items():
        if not word in all_terms:
            all_terms[word] = freq
        else:
            all_terms[word] += freq

prompt = input('Enter search prompt: ') if args.prompt == '?' else args.prompt

for word in prompt.split(' '):
    for doc in documents:
        if not word in doc.terms:
            continue
        tf = doc.terms[word]
        df = all_terms[word]
        doc.score += tf/df

print('Documents:')
documents.sort(key=lambda x: x.score, reverse=True)
for doc in documents[:args.num_matches]:
    print(f'{doc.path}: {doc.title} => {doc.score:.2f}')
