class WordsFromFile:
    def __init__(self, filename):
        self.filename = filename

    def __iter__(self):
        with open(self.filename, 'r') as f:
            for line in f:
                words = line.split(' ')
                for word in words:
                    yield word

words = WordsFromFile('/home/aquiles/Documents/Web/pftl_articles/articles/22_Step_by_step_qt.rst.md')
for w in words:
    for c in words:
        print(w, c)