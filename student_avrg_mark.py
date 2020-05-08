"""
hacker-rank-problem:find the percentage of
given input with some student name and their mark..

task:take input a integer:n,then take n time space separated input
with student name and mark then store the data a dictionary..
input a name as input exists in dictionary and
print the fraction average mark in 2 decimal floating point..
note:print just the average mark in a single line
 
 Example:input::>
 3
 Mishu 78.5 60 82.5
 Raju 69 67 82.5
 Shipla 79 68.5 83
 Raju
 
 Output::>
 72.83
"""
def avrg_mark(key,collection):
	total = collection[key]
	avrg_mark = sum(total)/len(total)
	return "%.2f"%avrg_mark

n = int(input())
mark_dict = {}
while n>0:
	mark_list = list(map(str,input().split(" ")))
	name = mark_list[0]
	marks = [float(num) for num in mark_list[1:]]
	mark_dict[name] = marks
	n-=1
	
student_name = input()
print(avrg_mark(student_name,mark_dict))