import sys
import warnings
import string

class InvalidArgumentsCount(Exception):
    """Exception raised for errors in the arguments count.

    Attributes:
        message -- explanation of the error
    """
    def __init__(self, message="Usage: python check_messages.py <dictionary_text_file>"):
        self.message = message
        super().__init__(self.message)

def get_dict(input_file):
    """Function read dictionary text file and return dictionary

    Arguments:
        input_file -- dictionary text file e.g. ru_wiki_dict.txt
    """
    dct = []
    with open(input_file, "r", encoding="utf-8") as f:
        line = f.readline()
        count = 0
        for word in line.rstrip().split():
            count += 1
            dct.append(word)
    return dct

def check_messages(dictionary):
    """Function read line from input, check all words in line and print incorrect words

    Arguments:
        dictionary -- dictionary list
    """
    while True:
        print("Enter your message")
        message = input()
        if message == "!exit":
            break
        message = delete_punctuation(message.rstrip().lower()).split()
        for word in message:
            if word not in dictionary:
                print(f"{word} incorrect")

def delete_punctuation(message):
    """Function which delete all punctuation symbols from string

    Arguments:
        message -- string
    """
    table = message.maketrans({key: " " for key in string.punctuation})
    return message.translate(table)

if __name__ == '__main__':
    warnings.filterwarnings("ignore")
    if len(sys.argv) != 2:
        raise InvalidArgumentsCount()
    input_file = sys.argv[1]
    dct = get_dict(input_file)
    check_messages(dct)
