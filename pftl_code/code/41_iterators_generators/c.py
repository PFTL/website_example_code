class Sentence:
    def __init__(self, text):
        self.words = text.split(' ')

    def __iter__(self):
        for word in self.words:
            yield word

text = "This is a text to test our iterator"
s = Sentence(text)

for w in s:
    print(w)