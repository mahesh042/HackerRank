def count_substring(string, sub_string):
    result = 0
    for i in range(0, len(string)):
        if string.find(sub_string,i) == i:
            result +=1


    return (result)
    

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
