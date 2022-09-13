import math

string = 'WELCOME'
symbol = '.|.'
len_str = len(string)

while True:
    try:
        length,width = map(int, input().split())

        if length%2 == 0 or width != 3*length:
            print('enter odd length and width as three times length')
            continue
        elif length%2 !=0 and width == 3*length:
            for j in range(length):
                print((((2*j)+1)*symbol).center(width,'-'))
                if j ==math.floor(length/2)-1:
                    break
            print(string.center(width,'-'))
            for i in range(1,length):
                print(((length-2*i)*symbol).center(width,'-'))
                if i == math.floor(length/2):
                    break
            
    except:
  
        break
        
            
