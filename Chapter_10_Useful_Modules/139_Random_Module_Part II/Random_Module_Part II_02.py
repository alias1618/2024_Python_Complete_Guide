import random

sentence = "Hi this is just a sentence"

chosen_index = random.randrange(0, len(sentence))
print(f"Chosen index: {chosen_index}")
print(f"Character at chosen index: {sentence[chosen_index]}")