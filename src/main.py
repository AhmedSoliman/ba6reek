#!/usr/bin/env python
import sys
import filters


def main():
    if len(sys.argv) < 2:
        print "Usage:%s <franko string>" % sys.argv[0]
        sys.exit(1)
    
    word = sys.argv[1]
    normalizedWord = filters.normalize(word)
    print filters.generatePlainReplacement(normalizedWord)
    
    
if __name__ == "__main__":
    main()
