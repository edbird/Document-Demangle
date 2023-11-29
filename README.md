# Document-Demangle
Document De-mangler

# Project Structure

- `mangler`: Contains code to mangle an input document
- `demangler`: Contains code to de-mangle the mangled document
- look at `demangler/res/mycv_demangled.txt` to see the demangled output
- look at `mangler/res/mycv_output_with_space.txt` to see the original document with postprocessing to remove numbers and special characters, double spaces...
- look at `mangler/res/mycv_output.txt` to see the input to the demangler, this is the same as the above document but with the final remaining spaces removed

Mangling is done by removing all numbers and special characters. A copy of the mangled document *with spaces* is saved for later comparison to the demanged document.

# Findings
The dictionary file I downloaded contains a large number of spurious words such as 'u' and 'r', among others like 'amt'. Some of these appear to be abbreviations or slang.

What sometimes happens is that a sequence such as "i am", which is "iam" matches to something spurious like "iam". Or "i am a" might match to "ama". This throws off the reconstruction of the document.

Removing these "false positive" words are removed from the dictionary fixes this but this is not an elegant solution.

A better solution would probably be to maximize some cost function, where the cost is proportional to some transition probabilities between different words.

For example: 'hello' -> 'world' should have a high transition weight because 'hello world' is a commonly used phrase.

# An example of when it goes wrong:

i am the leads oft ware engineer anda rchitect quant developer with ac amb ridge based hedge fundi have built and contributed significantly tot hede

- eg: `lead software` matches to `leads oft ware`

# Dictionary Choice

- I found that using the 10000 word list from MIT (https://www.mit.edu/~ecprice/wordlist.10000) in combination with custom words worked reasonably well
- A dictionary which is too large tends to contain more spurious positive matches like 'u' and 'y'
- The custom words were added by scanning the original document and ensuring all words are contained in the dictionary
- There were some words like 'hertfordshire' which were not in this dictionary
- What is perhaps surprising is how easy it is for a document to be re-assembled incorrectly, something which could be corrected using a predictive text algorithm

