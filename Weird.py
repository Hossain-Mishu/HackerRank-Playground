'''
hacker-rank-problem: check if the given number is Weird or not Weird
'''

n = int(input())
if n%2==0 and n>20:
	print("Not Weird")
elif n%2==0 and n in range(2,5):
	print("Not Weird")
elif n%2==0 and n in range(6,21):
	print("Weird")
elif n%2==1:
	print("Weird")
