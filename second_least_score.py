if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

list1 = list(arr)

sorted_list = sorted(list1)

sorted_list1 = list(set(sorted_list))
print(sorted_list1[-2])


if __name__ == '__main__':
    students =[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])

new = sorted([item[1] for item in students],reverse=True)
mylist = list(dict.fromkeys(new))

second_least = mylist[-2]

second_least_scorrers = []
for i in students:
    if i[1] == second_least:
        second_least_scorrers.append(i)


top_scorers1 = sorted([item[0] for item in second_least_scorrers])


print('\n'.join(top_scorers1))
