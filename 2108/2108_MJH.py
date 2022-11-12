import sys
input = sys.stdin.readline

# begin input
N = int(input().strip())
numbers = [0]*N
number_set = set()
for i in range(N):
    numbers[i] = int(input().strip())
    number_set.add(numbers[i])
# end input

sorted_numbers = sorted(numbers)
count = []

for n in number_set:
    count.append(sorted_numbers.count(n))

print(sum(numbers) // N)                     # average
print(sorted_numbers[N//2])                  # middle
print()
print(sorted_numbers[N] - sorted_numbers[0]) # range