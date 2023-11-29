#!/usr/bin/env python3

import re


def main():
    
    with open('../res/mycv.txt') as input_file:
        
        input_string = input_file.read()
        
        output_string = input_string
        
        # remove special characters and upper case characters
        output_string = re.sub(r'C\+\+', '', output_string)
        output_string = re.sub(r'[0-9\(\)\.,-/#&!:"%]', '', output_string)
        output_string = re.sub(r'[\f\r\n]', ' ', output_string)
        output_string = output_string.replace('  ', ' ')
        output_string = output_string.replace('  ', ' ')
        output_string = output_string.lower()
        
        # save document with spaces for comparison
        with open('../res/mycv_output_with_spaces.txt', 'w') as output_file_with_spaces:
            output_file_with_spaces.write(output_string)
        
        output_string = re.sub(r'\s', '', output_string)
        #output_string = re.sub(r'\(\)', '', output_string)
        #output_string = re.sub(r' \.', '', output_string)
        
        with open('../res/mycv_output.txt', 'w') as output_file:
            output_file.write(output_string)



if __name__ == '__main__':
    main()
    