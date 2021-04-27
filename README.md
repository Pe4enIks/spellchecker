# Instruction
## Download files
[Dump file](https://dumps.wikimedia.org/ruwiki/latest/ruwiki-latest-pages-articles-multistream.xml.bz2)

## Install all necessary packages
1. pip install sys
2. pip install gensim
3. pip install --upgrade numpy or pip install numpy(IMPORTANT: needed last version)
4. pip install python-Levenshtein
5. pip install string

## Run py files
1. python get_corpus.py ruwiki-latest-pages-articles-multistream.xml.bz2 ru_wiki.txt
2. python build_dict.py ru_wiki.txt ru_wiki_dict.txt
3. python check_messages.py ru_wiki_dict.txt

## Usage check_messages.py
You can input several messages to check it. If you want exit from program you can write "!exit".
