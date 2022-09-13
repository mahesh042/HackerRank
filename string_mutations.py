def mutate_string(string, position, character):
    str_split = ('-'.join(string))
    letter_list = str_split.split('-')
    letter_list[position] = character
    string = ''.join(letter_list)
    
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
