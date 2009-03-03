import lettersReplacements

def normalize(word):
    ''' Removes the repeating characters '''
    wordList = list(word.lower())
    for i in xrange(len(word)-1):
        k = i + 1
        while k < len(word) and wordList[i] != ' ' and wordList[i] == wordList[k]:
            wordList[k] = ''
            k = k+1
    return ''.join(wordList)

def generatePlainReplacement(word):
    wordList = list(word.lower())
    newWord = list()
    Done = False
    lastIndex = len(word) - 1
    i = 0
    while not Done:
        if lastIndex - i == -1:
            Done = True
            continue

        if lastIndex - i > 2:
            #try replacement of 3 characters
            portion = ''.join(wordList[i:i+3])
#            print "3 characters are valid. they are %s" % ''.join(portion)
            if lettersReplacements.LettersReplacement.has_key(portion):
                newWord.append(lettersReplacements.LettersReplacement[portion][0])
                i = i + 3
                continue
        if lastIndex - i > 1:
            #try replacement of 2 characters 
            portion = ''.join(wordList[i:i+2])
#            print "3 characters are valid. they are %s" % ''.join(portion)
            if lettersReplacements.LettersReplacement.has_key(portion):
                newWord.append(lettersReplacements.LettersReplacement[portion][0])
                i = i + 2
                continue
        if lastIndex - i >= 0:
            if lettersReplacements.LettersReplacement.has_key(wordList[i]):
                newWord.append(lettersReplacements.LettersReplacement[wordList[i]][0])
            else:
                newWord.append(wordList[i])
            i = i + 1
                    
    return ''.join(newWord)

#    newWord = list()
#    for i in word:
#        if lettersReplacements.LettersReplacement.has_key(i):
#            newWord.append(lettersReplacements.LettersReplacement[i][0])
#        else:
#            newWord.append(i)
#    return ''.join(newWord)



def generateProbabilities(word):
    pass