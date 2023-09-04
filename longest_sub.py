def longestBalancedSubstring(string):
    open = []
    close = []
    for i in string:
        if i == "(":
            open.append(1)
        else:
            close.append(1)

    return(len(open) + len(close))/2
    
    
    pass

#This problem is suposed to be solved using stacks, my solution is not using stacks because I don't know how to use them yet
#I will come back to this problem later and solve it using stacks :)