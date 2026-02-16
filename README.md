# NLP HW3 — Taaghche Sentiment Analysis & NER

This repository contains the implementation and report for an NLP course homework focused on **Persian text processing** on the **Taaghche comments dataset**. It covers:

1. **Document-level sentiment classification** (Negative / Neutral / Positive)
2. **Word/token-level sequence labeling (NER-style tagging)** using crawled book metadata (book name, author, translator, publisher)
3. A lightweight **web crawler + extractor** for collecting Taaghche book-page metadata to support entity list construction and labeling.

> Report: see `document/Report.pdf` (source: `document/Report.tex`).

---

## Repository Structure

- `DocClassifier_Base.ipynb`  
  Baseline **document sentiment classifier** (TF‑IDF + Logistic Regression), including preprocessing, class balancing, hyperparameter search, and evaluation.

- `DocClassifier_transformer.ipynb`  
  Transformer-based **document sentiment classifier** using a Persian BERT model (e.g., `HooshvareLab/bert-fa-base-uncased`) with TensorFlow / Hugging Face.

- `WordClassifier_Base.ipynb`  
  Baseline **token-level classifier** (sequence labeling) using classical preprocessing + a **BiLSTM**-style model for entity tagging.

- `WordClassifier_Transformer.ipynb`  
  Transformer-based **token-level classifier** (BERT for token classification).

- `crawler/`
  - `crawler.py`: downloads Taaghche book pages by iterating over book IDs and saving HTML files
  - `extractor.py`: parses saved HTML pages, extracts embedded JSON-LD, and writes book metadata to CSV

- `document/`
  - `Report.pdf`: compiled project report
  - `Report.tex`: LaTeX source of the report and explanations
  - `img/`: figures used in the report

Other directories (e.g., `datasets/`, `resources/`, `stopwords/`) are used by the notebooks for data and assets; exact contents may depend on how/where the notebooks were executed (local/Colab/Kaggle).

---

## Methods (High-Level)

### 1) Document Sentiment Classification
- **Labeling**: ratings are mapped to sentiment classes via thresholds (negative/neutral/positive).
- **Preprocessing**: Persian-character filtering and whitespace normalization.
- **Class balancing**: downsampling to equalize class sizes.
- **Baseline**: TF‑IDF + Logistic Regression (GridSearch over `ngram_range`, `max_features`, `C`).
- **Transformer**: fine-tuning a Persian BERT model for sequence classification.

### 2) Crawling & Metadata Extraction
- Crawls Taaghche book pages (by numeric ID range).
- Extracts JSON-LD metadata (book name, author(s), translator(s), publisher).
- Outputs CSV chunks for later analysis / entity list creation.

### 3) Token-Level Tagging (NER-style)
- Creates labels for tokens using book metadata fields and a BIO tagging scheme (e.g., `B-Author`, `I-Author`, `O`, etc.).
- Trains:
  - a baseline BiLSTM model
  - a transformer token-classification model

---

## Results (from the report)
The report includes experiments and evaluation (classification report, confusion matrix, and overall metrics). In the baseline document sentiment setup (TF‑IDF + Logistic Regression), the reported accuracy is approximately **0.61** on the evaluated split (see `document/Report.tex` / `document/Report.pdf` for full details and figures).

---

## How to Run

### Option A — Open the notebooks
Run the notebooks in Jupyter/Colab/Kaggle:
- `DocClassifier_Base.ipynb`
- `DocClassifier_transformer.ipynb`
- `WordClassifier_Base.ipynb`
- `WordClassifier_Transformer.ipynb`

Because the notebooks were executed in different environments (paths like Colab/Kaggle appear in the report), you may need to adjust:
- dataset paths (e.g., `datasets/taghche.csv`)
- output paths
- GPU/runtime settings

### Option B — Run the crawler
From the repository root:

```bash
pip install requests beautifulsoup4 pandas
python crawler/crawler.py
python crawler/extractor.py
```

This produces:
- HTML pages in `book_pages/`
- extracted CSV files in `output_csv/`

> Note: Be mindful of rate limits and respectful crawling. The script uses delays and threading; you may want to reduce concurrency depending on network/policy constraints.

---

## Dependencies (common)
Typical packages used across notebooks/scripts include:
- `pandas`, `numpy`, `scikit-learn`
- `tensorflow` (transformer notebooks)
- `transformers`
- `hazm` (Persian preprocessing/tokenization)
- `beautifulsoup4`, `requests`
- `matplotlib`, `seaborn`, `plotly`

---

## Authors
- Ilia Hashemi Rad  
- AmirMohammad Fakhimi  
- AmirMahdi Namjoo  

(See the report for identifiers and full submission details.)

---

## License
This project is licensed under the terms of the `LICENSE` file in this repository.
