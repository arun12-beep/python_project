str="My name is Arun khatri. I live in Ktm currently. But my hometown is Dharan. I love my Dharan"
sentence=str.split(".")
all_words=[]
for s in sentence:
    clean_s=s.strip()
    words=clean_s.split(" ")
    all_words.extend(words)
print("splitting sentence by sentence:")
print(sentence)
print("splitting words by words:")
print(all_words)