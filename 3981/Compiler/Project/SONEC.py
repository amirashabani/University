import sys

def main():
    filepath = 'test.sonec'

    if(len(sys.argv) >= 2):
        filepath = sys.argv[1]

    print(filepath)

if __name__ == "__main__":
    main()
