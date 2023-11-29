#!/usr/bin/env python3

import pygtrie


def main():

    #dictionary = load_dictionary_file()
    dictionary = load_shorter_dictionary_file()
    
    cv_words = load_cv_words_document()
    
    dictionary.merge(cv_words)
    
    save_dictionary(dictionary)
    
    
def load_shorter_dictionary_file():
    
    print(f'Loading dictionary file...')
    with open('../res/words_dictionary_10000_plus.txt', 'r') as dictionary_input_file:
        
        dictionary_trie = pygtrie.StringTrie()
        
        for word in dictionary_input_file:
            word = word.strip()
            #print(f'word={word}')
            dictionary_trie.update({word: None})
            
        return dictionary_trie
        
        
def load_cv_words_document():
    
    print(f'Loading mangled CV')
    with open('../../mangler/res/mycv_output_with_spaces.txt') as input_file:
        
        dictionary_trie = pygtrie.StringTrie()
        
        for word in input_file:
            word = word.strip()
            words = word.split(' ')
            for word in words:
                dictionary_trie.update({word: None})
        
        return dictionary_trie
            

def save_dictionary(dictionary_trie):
    
    print(f'Saving demangled CV')
    with open('../res/words_dictionary_10000_with_cv_words.txt', 'w') as output_file:
        
        for word in dictionary_trie.iterkeys():
            
            output_file.write(f'{word}\n')
        
        print(f'Dictionary saved')
        
        
            





if __name__ == '__main__':
    main()
    