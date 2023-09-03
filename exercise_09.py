words = []

for i in range(5):
    words.append(input(f"Enter word {i+1}: "))

new_string = ' '.join(words)

print("\nList of words:", words)
print("Resultant string:", new_string)
