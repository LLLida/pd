## Начало работы с проектом

```bash
python -m venv .venv
```

```bash
source ./.venv/bin/activate
```

Качаем зависимости:
```bash
pip install -r DEPENDENCIES.txt
```

## Примеры

Ранжирование документов по TF-IDF

```bash
python ranking/tfidf.py --path=docs/ml --prompt="deep residual" --num_matches=5
```
