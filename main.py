from src.model import classifier
from src.data_processing import reformatData

# Testing For now
user = input("Prompt: ")

result = classifier(user, top_k=None)
result_formatted = reformatData(result)

print(f"\n{result_formatted}")