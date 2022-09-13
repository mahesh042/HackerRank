def print_formatted(number):
    for i in range(1,number+1):
       

        last_num = bin(number+1)[2:]
        width = len(bin((number))[2:])
        num_length = len(str(number))

        print('{}{}{}{}'.format(str(i).rjust(width), oct(i)[2:].rjust(width+1), ((hex(i)[2:]).upper()).rjust(width+1), bin(i)[2:].rjust(width+1)))
        

        
        
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
