import re, datetime, pytz

# def caps(s):
#     s = re.split('(\W)', s)
#     string_list = []
#     for letter in s:
#         string_list.append(letter.capitalize())
# 
#     return ''.join(x for x in string_list)
# 
# 
# print(caps(string))

#
# def swap_case(s):
#     s = list(s.strip())
#     string_list = []
#     for __ in s:
#         if __.isupper():
#             __ = __.lower()
#             print(__)
#         else:
#             __ = __.upper()
#
#         string_list.append(__)
#     return ''.join(m for m in string_list)
#
# s = input()
# print(swap_case(s))

# def mutate(string, pos, char):
#     string = list(string.strip())
#     string[int(pos)] = char
#     return ''.join(m for m in string)
#
#
# print(mutate(s1, p, c))

# s = input("input first : ").strip()
# s2 = input("input more : ").strip()

#
# def count_string(string, sub_string):
#     string = ''.join(x for x in string).split()
#     sub_string = ''.join(z for z in sub_string).split()
#     return len(string) + len(sub_string)
#
#
# print(count_string(s, s2))
#
# def solution(a):
#     # a as a list
#     imperfect = []
#     for num in a:
#         num_list = []
#         for x in range(1, num+1):
#             if num % x == 0:
#                 num_list.append(x)
#         # pop function is remove last item in list
#         num_list.pop()
#
#         total = sum(num_list)
#         if total != num:
#             print(f"hai, {total} - asli = {num}")
#             if not (total >= num):
#                 imperfect.append(num)
#
#     return len(imperfect)
#
#
# print(solution([2, 3, 4, 6]))


# inp = int(input("berikan masukan angka : "))
#
# match inp:
#     case inp if 10 < inp < 20:
#         print('one')
#     case inp if inp == 20:
#         print('twenty')
#     case _:
#         print('default')

# list1 = []
# list2 = []
#
# for i in range(10):
#     if i % 2 == 0:
#         list1.append(f'{i}-{i+10}')
#     else:
#         list2.append(f'{i}-{i+10}')
#
#
# print(len(list1) + len(list2))
# print(list1)
# print(list2)
# print(datetime.timedelta())

# a = [i for i in range(5)]
# b = []

# for bb in range(5, 0):
#   if bb % 2 == 0:
#       bb += 0.5
#   b.append(bb)
# print(bb)

# print(b)
# code = input("masukan kode : ")
# while True:
#     data = ['sqpZr8VF9IPKwhQ3', 'X6nEJqlYUw952jid', '4caQIkwl6GrNe218', 'js2Zq4otIJQSWwKg']
#     if code in data:
#         code = input("maaf karena kode sudah ada, masukan kode lagi : ")
#     else:
#         break
# print(code)

# data = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
#
# print(data[7:5:-1])
# print(min(sum([11,22]), max(abs(-30),2)))
# print("{0}{1}{0}".format("abra", "cad"))
# nums = [-1, 2, -3, 4, -5]

# print(all([abs(i) < 3 for i in nums]))

# def fun(n):
#     return n + fun(n - 1) if n > 0 else 0
#
#
# if __name__ == '__main__':
#     n = 10
#     print(fun(n))

# string = 'I am an Indian, by birth.'
# sub = 'Birth'
#
#
# def finds(string, sub):
#     count = 0
#     for i in range(len(string) - len(sub) + 1):
#         if string[i:i + len(sub)] == sub:
#             print(string[i:i + len(sub)])
#             count += 1
#     return count
#
#
# print(finds(string, sub))

#
# def alphanum(s):
#     for i in range(len(s)):
#         if s[i].isalnum():
#             return True
#             break
#     return False
#
#
# def alpha(s):
#     for i in range(len(s)):
#         if s[i].isalpha():
#             return True
#             break
#     return False
#
#
# def digits(s):
#     for i in range(len(s)):
#         if s[i].isdigit():
#             return True
#             break
#     return False
#
#
# def lowercase(s):
#     for i in range(len(s)):
#         if s[i].islower():
#             return True
#             break
#     return False
#
#
# def uppercase(s):
#     for i in range(len(s)):
#         if s[i].isupper():
#             return True
#             break
#     return False
#
#
# if __name__ == '__main__':
#     s = 'qA2'
#     print(alphanum(s))
#     print(alpha(s))
#     print(digits(s))
#     print(lowercase(s))
#     print(uppercase(s))

# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()
#
#     checked = list(student_marks[query_name])
#     per = sum(checked)/len(checked)
#     print("{:.2f}".format(per))


# for i in range(1, int(input()) + 1):  # More than 2 lines will result in 0 score. Do not leave a blank line also
#     print(int(((10 ** i - 1) / 9) ** 2))

from functools import reduce

num = int(input("Masukan Angka Bebas : "))
num = list(range(1, num+1))
print(num)
num = reduce(lambda x, y: x*y, num)
print(num)

