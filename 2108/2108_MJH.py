import sys
input = sys.stdin.readline

# begin input
N = int(input().strip())
numbers = [0]*N
number_frq = [0]*8001  # we will use num+4000 for index
for i in range(N):
    n = int(input().strip())
    numbers[i] = n
    number_frq[n+4000] += 1
# end input

sorted_numbers = sorted(numbers)

frq_max = -1
max_freq = []
for i in range(8001):
    if frq_max <= number_frq[i]:
        if frq_max != number_frq[i]:
            frq_max = number_frq[i]
            max_freq = []
        max_freq.append(i)

max_freq.sort()

print(round(sum(numbers)/N))                   # average
print(sorted_numbers[N//2])                    # middle
if len(max_freq) == 1: print(max_freq[0]-4000) # frequent
else: print(max_freq[1]-4000)
print(sorted_numbers[N-1] - sorted_numbers[0]) # range