from transformers import pipeline


# https://huggingface.co/j-hartmann/emotion-english-distilroberta-base
classifier = pipeline(
    "text-classification", 
    model="j-hartmann/emotion-english-distilroberta-base",
    device=-1 # -1=CPU;0=GPU;1=GPU2;...;N=GPUN
)

