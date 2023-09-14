'''
Will Anderson
9/14/2023

Selection Statements, Loops, and Nested Loops
'''

user_num = int(input('Enter an upper bound for a check: '))

sum_total = 0
deficient = 0
perfect = 0
abundant = 0
for i in range(1, user_num + 1):
	sum_total = 0
	for j in range(1, i):
		if (i % j) == 0:
			sum_total += j
	if (sum_total < i):
		deficient += 1
	if (sum_total == i):
		perfect += 1
	if (sum_total > i):
		abundant += 1
		
print(f'Between 1 and {user_num} there are')
print(f'{deficient} deficient numbers')
print(f'{perfect} perfect numbers')
print(f'{abundant} abundant numbers')		

