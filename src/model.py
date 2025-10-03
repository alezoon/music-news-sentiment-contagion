from transformers import pipeline

# https://huggingface.co/j-hartmann/emotion-english-distilroberta-base
classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", return_all_scores=True)
