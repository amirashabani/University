import sys
import antlr4
from SONECLexer import SONECLexer

def main():
    file_path = 'example.sonec'

    if(len(sys.argv) >= 2):
        file_path = sys.argv[1]

    with open(file_path, 'r') as input_file, open('output.txt', 'w') as output_file:
        lexer = SONECLexer(input_file)
        stream = antlr4.CommonTokenStream(lexer)
        print(stream.tokens)

if __name__ == "__main__":
    main()

