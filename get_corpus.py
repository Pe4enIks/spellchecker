import sys
import gensim
import warnings

class InvalidArgumentsCount(Exception):
    """Exception raised for errors in the arguments count.

    Attributes:
        message -- explanation of the error
    """
    def __init__(self, message="Usage: python get_corpus.py <wiki_dump_file> <result_file>"):
        self.message = message
        super().__init__(self.message)

def get_corpus(input_file, output_file):
    """Function get corpus from input_file and write in output_file

    Arguments:
        input_file -- dump file from wiki .xml.bz2
        output_file -- result text file
    """
    with open(output_file, "w", encoding="utf-8") as output:
        print("Wiki corpus loading start")
        wiki = gensim.corpora.WikiCorpus(input_file, lower=True, article_min_tokens=5)
        print("Wiki corpus loading end")
        print("Articles processing start")
        for i, text in enumerate(wiki.get_texts()):
            output.write(bytes(' '.join(text), 'utf-8').decode('utf-8') + '\n')
            if i+1 % 10000 == 0:
                print(f"{i+1} articles")
        print("Articles processing end")

if __name__ == '__main__':
    warnings.filterwarnings("ignore")
    if len(sys.argv) != 3:
        raise InvalidArgumentsCount()
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    get_corpus(input_file, output_file)
