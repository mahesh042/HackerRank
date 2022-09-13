
def minion_game(string):
    c1 =0
    c2=0
    vowels="aeiouAEIOU"

    for i in range(len(s)):
        if s[i] in vowels:

            c1 = c1 + (len(s)-i)
        else:
 
            c2 = c2 + (len(s)-i)
 
    if c1>c2:
        print("Kevin",c1)
 
    elif c2>c1:
        print("Stuart",c2)
    else:
        print('Draw')


if __name__ == '__main__':
  s = input()
  minion_game(s)
