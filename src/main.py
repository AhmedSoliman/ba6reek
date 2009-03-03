import lettersReplacements
import filters


def main():
    word = "3'aly 3layh"
    normalizedWord = filters.normalize(word)
    print filters.generatePlainReplacement(normalizedWord)
    
    
if __name__ == "__main__":
    main()