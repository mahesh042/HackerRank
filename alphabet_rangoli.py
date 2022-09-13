import string,math

def print_rangoli(size):
    a = (string.ascii_lowercase)
    b = '-'.join(a)
    alphabets = b.split('-')
    lst = []
    lst1 = []
    lst2 = []
    
    for i in range(size):
        lst.append(alphabets[(size-1)-i])
        lst1.append(alphabets[(size-1)-i])
    
    for j in range(size):    
        lst.append(alphabets[j])
        lst1.append(alphabets[j])
    
    lst.remove('a')
    lst1.remove('a')

    first_len = len(lst)
    first_len_lst1 = len(lst1)

    lst_out = ('-'.join(lst))
    lst1_out = ('-'.join(lst1))
    
    if size == 1:
        print(lst1[0])
    
    else:
    
        k = 0
        while lst1:
            mid_element = math.ceil(len(lst2)/2)
            if k == 0:
                lst2.append(lst1[k])

            
            if k == 1:
                lst2.append(lst1[k])
                lst2.append(lst1[k-1])
            if k > 1:
                lst2.insert(k,lst1[k])
                lst2.insert(k,lst1[-k])
                lst2[mid_element],lst2[mid_element+1] = lst2[mid_element+1],lst2[mid_element]
            str_len = ('-'.join(lst2))
            no_of_letters = (2*size) -1
            no_of_underscores = no_of_letters -1
            total = no_of_underscores + no_of_letters
            right = (str_len.center(total,'-'))
            print(right)

            k = k +1
            if k == size:
                break

        
    
        while lst:
            mid_element = math.floor(len(lst)/2)
            del(lst[mid_element])
            del(lst[mid_element - 1])

            if len(lst)== 2:
                print(lst[-1])

            str_len = ('-'.join(lst))

            no_of_letters = (2*size) -1
            no_of_underscores = no_of_letters -1
            total = no_of_underscores + no_of_letters
    
            right = (str_len.center(total,'-'))

            print(right)

            if len(lst) == 1:
                break

n = int(input())
print_rangoli(n)
