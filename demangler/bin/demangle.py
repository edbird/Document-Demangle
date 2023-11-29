#!/usr/bin/env python3


import json
import pygtrie

from libdemangle import search_for_longest_word_limited


class SystemState():
    
    def __init__(self, index_start, maximum_word_search_length):
        self.words = []
        self.index_start = index_start
        self.maximum_word_search_length = maximum_word_search_length
        


def main():

    #dictionary = load_dictionary_file()
    dictionary = load_shorter_dictionary_file()
    
    mangled_document = load_mangled_document()
    
    demangled_document = demangle_document(dictionary, mangled_document)
        
    save_demangled_document(demangled_document)
    
    

# the iteration function (treated like it is a recursive function)
def find_next_word(system_state, dictionary_trie, mangled_document):
    
    words = system_state.words
    index_start = system_state.index_start
    maximum_length = system_state.maximum_word_search_length
    
    word = search_for_longest_word_limited(dictionary_trie, mangled_document, index_start, maximum_length)
    print(f'found word: {word}')
        
    if word is None:
        pass
    else:
        words.append(word)
            
       
def demangle_document(dictionary_trie, mangled_document):
    
    print(f'demangling document of length {len(mangled_document)}')
    
    index_end = len(mangled_document)
    #maximum_word_search_length = index_end - index_start
    
    system_state = SystemState(index_start=0, maximum_word_search_length=None)
    
    while True:
        
        # termination condition
        if system_state.index_start == index_end:
            break
        
        number_of_words_found = len(system_state.words)
        find_next_word(system_state, dictionary_trie, mangled_document)
        number_of_words_found_after = len(system_state.words)
        
        #print(f'number of words: {number_of_words_found} -> {number_of_words_found_after}')
        
        if number_of_words_found_after > number_of_words_found:
            # a new word has been found that implies `find_next_word` was successful
            found_word_length = len(system_state.words[-1])
            system_state.index_start += found_word_length
            
            # reset the maximum word search length
            if system_state.maximum_word_search_length is not None:
                system_state.maximum_word_search_length = None
        else:
            # new word was not found, implies `find_next_word` has failed, need to
            # backtrack
            print(f'backtrack at index_start={system_state.index_start}')
            print(f'next 20 characters of document: {mangled_document[system_state.index_start:system_state.index_start+20]}')
            
            # need to get the last found word length, there might not be a word
            if len(system_state.words) > 0:
                print(f'last word: {system_state.words[-1]}, length: {len(system_state.words[-1])}')
                last_word_length = len(system_state.words[-1])
                system_state.maximum_word_search_length = last_word_length - 1
                
                # remove last found word, and rewind state
                system_state.words.pop()
                system_state.index_start -= last_word_length
                
                # now continue searching for words, limited by a maximum length
            else:
                # there is no previously found word, and we cannot find a word
                # this means we quit with failure
                print(f'failed to demangle document')
                return None
        
    
    # construct whole document from words
    demangled_document_word_list = system_state.words
    demangled_document = ' '.join(demangled_document_word_list)
    return demangled_document
    
    
def add_word_to_demangled_document(demangled_document, next_word):
    
    if len(demangled_document) > 0:
        demangled_document += ' ' + next_word
    else:
        demangled_document += next_word
    
    return demangled_document
    

def load_dictionary_file():
    
    print(f'Loading dictionary file...')
    with open('../res/words_dictionary.json', 'r') as dictionary_input_file:
        dictionary = json.load(dictionary_input_file)
        print(f'Dictionary file loaded')
        
        dictionary_trie = pygtrie.StringTrie()
        
        for word in dictionary:
            #print(f'word={word}')
            dictionary_trie.update({word: None})
            
        # add custom words
        dictionary_trie.update({'letchworth': None})
        dictionary_trie.update({'uk': None})
            
        return dictionary_trie
    
    
def load_shorter_dictionary_file():
    
    print(f'Loading dictionary file...')
    with open('../res/words_dictionary_10000_with_cv_words.txt', 'r') as dictionary_input_file:
        print(f'Dictionary file loaded')
        
        dictionary_trie = pygtrie.StringTrie()
        
        for word in dictionary_input_file:
            word = word.strip()
            #print(f'word={word}')
            dictionary_trie.update({word: None})
            
        # add custom words
        dictionary_trie.update({'letchworth': None})
        dictionary_trie.update({'uk': None})
            
        return dictionary_trie
        
        
def load_mangled_document():
    
    print(f'Loading mangled CV')
    with open('../../mangler/res/mycv_output.txt') as input_file:
        input_string = input_file.read()
        print(f'Mangled document loaded')
        
        return input_string
            

def save_demangled_document(demangled_document):
    
    print(f'Saving demangled CV')
    with open('../res/mycv_demangled.txt', 'w') as output_file:
        output_file.write(demangled_document)
        print(f'Demangled document saved')
            





if __name__ == '__main__':
    main()
    