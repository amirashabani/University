import sys
from SONECLexer import SONECLexer

def main():
    file_path = 'test.sonec'

    if(len(sys.argv) >= 2):
        file_path = sys.argv[1]

    with open(file_path, 'r') as input_file:
        lexer = SONECLexer(input_file)
        print(lexer)

if __name__ == "__main__":
    main()
