import simpleai
from simpleai.machine_learning import Attribute, ClassificationProblem, NaiveBayes

class Sentence(object):
    def __init__(self, language, text):
        self.language = language
        self.text = text

class OnlineCorpusReader(object):
    def __init__(self):
        self.input_files = [("english", "text.en"),
                            ("spanish", "text.es")]

    def __iter__(self):
        for language, filename in self.input_files:
            for text in open(filename):
                yield Sentence(language, text.lower())

class LetterCount(Attribute):
    def __init__(self, letter):
        self.letter = letter
        self.name = "Counts for letter {!r}".format(letter)

    def __call__(self, sentence):
        return sentence.text.count(self.letter)

for letter in "abcdefghijklmnopqrstuvwxyz":
    attribute = LetterCount(letter)

def attribute_count_a(observation):
    return observation.text.count("a")

class LanguageClassificationProblem(ClassificationProblem):
    def __init__(self):
        super(LanguageClassificationProblem, self).__init__()
        for letter in "abcdefghijklmnopqrstuvwxyz":
            attribute = LetterCount(letter)
            self.attributes.append(attribute)

    def target(self, sentence):
        return sentence.language

input_files = [("english", "europarl-v7.es-en.en"),
               ("spanish", "europarl-v7.es-en.es")]

dataset = OnlineCorpusReader()
problem = LanguageClassificationProblem()
classifier = NaiveBayes(dataset, problem)

test = Sentence(None, "is this an english sentence?")
print classifier.classify(test)
test = Sentence(None, "es esta una oracion en espanol?")
print classifier.classify(test)

