import sys
import warnings

class InvalidArgumentsCount(Exception):
    """Exception raised for errors in the arguments count.

    Attributes:
        message -- explanation of the error
    """
    def __init__(self, message="Usage: python build_dict_file.py <wiki_text_file> <dictionary_text_file>"):
        self.message = message
        super().__init__(self.message)

def get_dict(input_file):
    """Function read corpus text file and return dictionary

    Arguments:
        input_file -- corpus text file e.g. ru_wiki.txt
    """
    print("Get dict start")
    dct = set()
    with open(input_file, "r", encoding="utf-8") as f:
        lines = [line.rstrip() for line in f]
        count = 0
        for line in lines:
            count += 1
            for word in line.split():
                dct.add(word)
            if count % 100000 == 0:
                print(f"Processed {count} lines")
    print("Get dict end")
    return dct

def write_dict(dictionary, output_file):
    """Function write all words from dictionary into output_file

    Arguments:
        dictionary -- set of all words in corpus
        output_file -- text file of words from dictionary
    """
    print("Write dict start")
    with open(output_file, "w", encoding="utf-8") as f:
        for el in dictionary:
            f.write(el + ' ')
        f.write('\n')
    print("Write dict end")

if __name__ == '__main__':
    warnings.filterwarnings("ignore")
    if len(sys.argv) != 3:
        raise InvalidArgumentsCount()
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    dct = get_dict(input_file)
    write_dict(dct, output_file)
