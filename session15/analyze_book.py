import random
import string


def process_file(filename, skip_header):
    """Makes a histogram that contains the words from a file.

    filename: string
    skip_header: boolean, whether to skip the Gutenberg header

    returns: map from each word to the number of times it appears.
    """
    hist = {}
    fp = open(filename, encoding='UTF8')

    if skip_header:
        skip_gutenberg_header(fp)

    strippables = string.punctuation + string.whitespace

    for line in fp:
        if line.startswith('*** END OF THIS PROJECT'):
            break

        line = line.replace('-', ' ')

        for word in line.split():
            # word could be 'Sussex.'
            word = word.strip(strippables)
            word = word.lower()

            # update the dictionary
            hist[word] = hist.get(word, 0) + 1

    return hist


def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.

    fp: open file object
    """
    for line in fp:
        if line.startswith('*** START OF THIS PROJECT'):
            break


def total_words(hist):
    """Returns the total of the frequencies in a histogram."""
    result = 0
    for v in hist.values():
        result += v
    return result
    #return sum(hist.values())


def different_words(hist):
    """Returns the number of different words in a histogram."""
    return len(hist)


def most_common(hist, excluding_stopwords=False):
    """Makes a list of word-freq pairs in descending order of frequency.

    hist: map from word to frequency

    returns: list of (frequency, word) pairs
    """
    stopwords = process_file("data/stopwords.txt", False)
    # print(stopwords.keys())
    lst = []
    for word, freq in hist.items():
        if excluding_stopwords:
            if word in stopwords:
                continue
        lst.append((freq, word))
    lst.sort(reverse = True)
    return lst


def print_most_common(hist, num=10): #Got help from https://github.com/AllenDowney/ThinkPython2/blob/master/code/analyze_book1.py
    """Prints the most commons words in a histgram and their frequencies.

    hist: histogram (map from word to frequency)
    num: number of words to print
    """
    t = most_common(hist)
    print('The most common words are:')
    for freq, word in t[:num]:
        print(word, '\t', freq)

def subtract(d1, d2): #Got help from https://github.com/AllenDowney/ThinkPython2/blob/master/code/analyze_book1.py
    """Returns a dictionary with all keys that appear in d1 but not d2.

    d1, d2: dictionaries
    """
    res = {}
    for key in d1:
        if key not in d2:
            res[key] = None
    return 


def random_word(hist): #Got help from https://github.com/AllenDowney/ThinkPython2/blob/master/code/analyze_book1.py
    """Chooses a random word from a histogram.

    The probability of each word is proportional to its frequency.
    """
    t = []
    for word, freq in hist.items():
        t.extend([word] * freq)
    return random.choice(t)

def main():
    hist = process_file('data/Pride and Prejudice.txt', skip_header=True)
    # print(hist)
    # print('Total number of words:', total_words(hist))
    # print('Number of different words:', different_words(hist))

    # t = most_common(hist, excluding_stopwords=True)
    # print('The most common words are:', t)
    t = most_common(hist)
    for freq, word in t[0:20]:
        print(word, '\t', freq)

    # words = process_file('data/words.txt', skip_header=False)

    # diff = subtract(hist, words)
    # print("The words in the book that aren't in the word list are:")
    # for word in diff.keys():
    #     print(word, end=' ')

    # print("\n\nHere are some random words from the book")
    # for i in range(100):
    #     print(random_word(hist), end=' ')


if __name__ == '__main__':
    main()
