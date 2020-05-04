'''
hacker-rank-problem:find runner up
from an given array of score
'''

def runner_up(arr):
	refine_arr = []
	for elem in arr:
		if elem not in refine_arr:
			refine_arr.append(elem)
			
	
	refine_arr.remove(max(refine_arr))
	second_max = max(refine_arr)
	return second_max
	
if __name__ == "__main__":
	n = int(input())
	arr = list(map(int,input().split(" ")))
	second_max = runner_up(arr)
	print(second_max)