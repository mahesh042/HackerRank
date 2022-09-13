if __name__ == '__main__':
    s = input()
    lst = []


    for i in range(0, len(s)):
        if (s[i].isalnum()) == True:
            lst.append(1)
        else:
            lst.append(0)

    if sum(lst)>=1:
        print(True)
    else:
        print(False)
    
    lst.clear()

    for i in range(0, len(s)):
        if (s[i].isalpha()) == True:
            lst.append(1)
        else:
            lst.append(0)

    if sum(lst)>=1:
        print(True)
    else:
        print(False)

    lst.clear()

    for i in range(0, len(s)):
        if (s[i].isdigit()) == True:
            lst.append(1)
        else:
            lst.append(0)

    if sum(lst)>=1:
        print(True)
    else:
        print(False)
    
    lst.clear() 
    
    for i in range(0, len(s)):
        if (s[i].islower()) == True:
            lst.append(1)
        else:
            lst.append(0)

    if sum(lst)>=1:
        print(True)
    else:
        print(False)
        
    lst.clear()
    for i in range(0, len(s)):
        if (s[i].isupper()) == True:
            lst.append(1)
        else:
            lst.append(0)

    if sum(lst)>=1:
        print(True)
    else:
        print(False)
lst.clear()
