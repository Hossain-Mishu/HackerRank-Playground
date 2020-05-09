"""
hacker-rank-problem:take a input n,then take n time
input for command,do several operation in a list
based on command given as input,,
execute all given command on list and print
the list in a single line when given command is "print"
exmp:
5
insert 0 5
insert 1 10
insert 0 6
sort
print
append 7
sort
reverse
print

output:
[5,6,10]
[10,7,6,5]
"""

class List_Op():
	def __init__(self):
		self.collection = []
		
	def insert(self,position,value):
		self.collection.insert(int(position),int(value))
		
	def append(self,value):
		self.collection.append(int(value))
		
	def pop(self):
		self.collection.pop()
		
	def remove(self,value):
		self.collection.remove(int(value))
		
	def sort(self):
		self.collection = sorted(self.collection)
		
	def reverse(self):
		self.collection = self.collection[::-1]
		
	def print(self):
		print(self.collection)

if __name__ == '__main__':		
	collection = List_Op()
	temp_list = []

	n = int(input())
	while n>0:
		user_inp = list(map(str,input().split(" ")))
		temp_list.append(user_inp)
		n-=1
	
	for cmd in temp_list:
		if cmd[0] == "insert":
			collection.insert(cmd[1],cmd[2])
		elif cmd[0] == "append":
			collection.append(cmd[1])
		elif cmd[0] == "pop":
			collection.pop()
		elif cmd[0] == 'remove':
			collection.remove(cmd[1])
		elif cmd[0] == 'sort':
			collection.sort()
		elif cmd[0] == "reverse":
			collection.reverse()
		elif cmd[0] == "print":
			collection.print()