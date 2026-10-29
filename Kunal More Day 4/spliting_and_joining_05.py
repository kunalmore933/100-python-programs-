words = "the quick brown fox".split()
print(words)
print(len(words))

print("25-11-2005".split("-"))
print("a,b,,c".split(","))

parts = "20-11-2005".split(".")
print(parts[0])
print(parts[-1])

words = ["the", "quick", "brown", "fox"]
print(" ".join(words))
print("-".join(words))
print("".join(words))
