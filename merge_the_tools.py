def merge_the_tools(string, k):
    # your code goes here
    lst = []

    count = len(string)/k
    if len(string)%k ==0:
        i = 1
        j = 0
        while string:
            lst.append(string[j*k:i*k])
            i= i +1
            j=j +1
 
            if i ==count+1:
                break

    for i in range(len(lst)):
        a = (list(dict.fromkeys(lst[i])))
        ab = ''.join(a)
        print(ab)
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
