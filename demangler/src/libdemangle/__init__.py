

def search_for_longest_word_limited(dictionary_trie, mangled_document, index_start, maximum_length):
        
    # debugging:
    debug = False
    if maximum_length is not None:
        debug = True
        print(f'word search length limited to {maximum_length}')
        print(f'next 20 characters of document: {mangled_document[index_start:index_start+maximum_length]}')
    
    if maximum_length is None:
        maximum_length = len(mangled_document) - index_start
    
    while True:
        if maximum_length < 1:
            return None
        else:
            trial_word = mangled_document[index_start:index_start+maximum_length]
            
            if debug:
                print(f'trial_word={trial_word}')
            
            if dictionary_trie.has_key(trial_word):
                return trial_word
            else:
                maximum_length -= 1
    
    
def search_for_longest_word(dictionary_trie, mangled_document, start_index, end_index):
    
    while True:
        if end_index - start_index < 1:
            return None
        else:
            trial_word = mangled_document[start_index:end_index]
            
            if dictionary_trie.has_key(trial_word):
                return trial_word
            else:
                end_index -= 1
        
     
def search_for_word(dictionary_trie, mangled_document_slice):
    
    slice_length = len(mangled_document_slice)
    
    while True:
        trial_word = mangled_document_slice[:slice_length]
        #print(trial_word)
        #print(slice_length)
        
        if dictionary_trie.has_key(trial_word):
            print(f'found search hit: {trial_word}')
            return trial_word
        else:
            if slice_length > 1:
                slice_length -= 1
            else:
                return None