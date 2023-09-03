def isValidSubsequence(array, sequence):
    seqId = 0
    for value in array:
        if seqId == len(sequence):
            break
        #seqId apunta al indice del arreglo sequence
        #en este if estoy checando si el valor de sequence en el indice 
        #seqId es igual al value del for del arreglo principal
        if sequence[seqId] == value:
            seqId += 1

    return seqId == len(sequence)
    

