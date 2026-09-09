# 🔍 Word Prediction

A modern **Word Autocomplete** web application built using **Python** and **Streamlit**. The application suggests English words based on the prefix entered by the user using a preprocessed English dictionary dataset.
li
---
Live Demo: https://word-prediction-4dg9f7u2dwcdadzxfu4at9.streamlit.app/

## 🚀 Features

- 🔎 Real-time word autocomplete
- 📚 Uses a preprocessed English dictionary
- ⚡ Fast word loading using Pickle (`words.pkl`)
- 🎨 Modern blue-themed Streamlit UI
- 🧹 Clean and organized codebase
- 📝 Dataset preprocessing using Jupyter Notebook

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Pandas
- Pickle
- Jupyter Notebook

---

## ⚙️ How It Works

1. Load the English word dataset.
2. Preprocess the dataset in Jupyter Notebook.
3. Store the cleaned words as `words.pkl`.
4. Load the pickle file in the Streamlit application.
5. Perform **prefix-based matching** using Python's `startswith()` method.
6. Display the top matching suggestions.

---

## 📊 Algorithm

The current version uses **Prefix Matching**.

```text
User Input
      │
      ▼
Load words.pkl
      │
      ▼
startswith(prefix)
      │
      ▼
Top Suggestions
```

**Time Complexity:** `O(n)`

where `n` is the total number of words in the dataset.

---

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/vishchopra227/Word-Prediction.git
```

Move into the project folder:

```bash
cd Word-Prediction
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## 💡 Example

**Input**

```text
cric
```

**Output**

```text
cricket
cricketer
cricketing
```
