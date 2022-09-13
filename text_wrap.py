from math import ceil


def wrap(string, max_width):
    
    a = '-'.join(string)
    b = a.split('-')
    str_length = len(b)
    
    index1 = 0
    index2 = 1
    lst = []
    
    while index2:
        lst.append(string[index1*max_width:index2*max_width])
        index1 +=1
        index2 +=1
        if index2 == ceil(len(b)/max_width)+1:
            break
        
    return '\n'.join(map(str, lst))

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
