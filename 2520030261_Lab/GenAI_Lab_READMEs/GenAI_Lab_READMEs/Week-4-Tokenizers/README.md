# Week 4 – Tokenizer Lab: BPE, WordPiece and SentencePiece

## Aim
Implement and compare three pretrained subword tokenizers—BPE, WordPiece, and SentencePiece—using English, Telugu, and Hindi text. Observe token pieces, token IDs, and token counts.

## Tokenizers used
| Approach | Pretrained tokenizer |
|---|---|
| BPE (byte-level BPE) | `gpt2` |
| WordPiece | `bert-base-multilingual-cased` |
| SentencePiece (XLM-R tokenizer) | `xlm-roberta-base` |

This practical compares real pretrained tokenizers. The models have different vocabularies and training data, so the results reflect both tokenizer design and model training.

## Files
- `tokenizer_comparison.py` – loads the three tokenizers and compares their output.
- `requirements.txt` – Python dependencies.

## Requirements
- Python 3.10 or later (recommended)
- VS Code
- Internet connection for the first download of pretrained tokenizer files
- The lab virtual environment in the repository root

## Setup
Open the Week 4 folder in VS Code and activate the environment:

```powershell
..\.myenv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

The `requirements.txt` file should contain:

```text
transformers
sentencepiece
```

## Run

```powershell
python tokenizer_comparison.py
```

On the first run, the Hugging Face tokenizer files are downloaded. Wait for all three tokenizers to load.

## Expected output
For each of English, Telugu, and Hindi, the program prints:
- Input text
- Tokens produced by each tokenizer
- Token IDs
- Token count

The exact tokens, IDs, and counts depend on the pretrained tokenizer files.

## Viva topics
- Meaning and purpose of tokenization
- Word-level versus subword-level tokens
- Basic BPE merging idea
- WordPiece subword splitting
- SentencePiece as a tokenizer framework
- Why token counts vary across languages and vocabularies
- Difference between token count and character count
