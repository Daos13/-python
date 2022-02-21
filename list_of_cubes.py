#i = 8
#i = i**3
# print(i)


# numbers = list(range(1, 1000))
numbers = list(range(1, 30))
print(numbers)

#odd_cubes = []
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
odd_cubes = []
cube = []
for number in numbers:
    if number % 2 != 0:
       odd_cubes.append(number**3)
       # odd_cubes.append(number**3)
for cube in odd_cubes[-1]:


    print(odd_cubes)


print(odd_cubes[-1])

# for cube in odd_cubes:
  #  if cube % 7 == 0:
   #   print(cube)
     # cube = (cube + 17)

#
#
# while (cube > 0):
  #  dig = n % 10
   # sum = sum + dig
   # n = n // 10
   # print(sum)
   # if sum % 7 == 0:
    # ns = ns.append(n)
# print(ns)
