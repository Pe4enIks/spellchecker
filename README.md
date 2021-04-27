# Instruction
## Warning
1. Dump file ~= 4GB
2. Text corpus file ~= 8CB

## Download files
1. [Dump file](https://dumps.wikimedia.org/ruwiki/latest/ruwiki-latest-pages-articles-multistream.xml.bz2)

## Install all necessary packages
1. pip install sys
2. pip install gensim
3. pip install --upgrade numpy or pip install numpy(IMPORTANT: needed last version)
4. pip install python-Levenshtein

## Run py files
1. python get_corpus.py ruwiki-latest-pages-articles-multistream.xml.bz2 ru_wiki.txt
2. python build_dict.py ru_wiki.txt ru_wiki_dict.txt
3. python check_messages.py ru_wiki_dict.txt

## Usage check_messages.py
1. You can input several messages to check it. If you want exit from program you can write "!exit".
2. If word found in dictionary program won't print something, if word not found in dictionary program will print "word incorrect".
