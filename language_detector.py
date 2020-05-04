'''
hacker-rank-problem:detect lanugage from given input word..
if word endswith po then it is FILIPINO
if word endswith desu or masu then it is JAPANESE
if word endswith mndia then it is KOREAN
'''

#take input how many time check
input_time = int(input())

#define a list to hold input sentence
sentence =[]

#now take input for each attempts
while input_time >0:
    line = str(input())
    sentence.append(line)
    input_time -= 1

#access each sentence and check if it ends with('po','desu','masu','mnida')
for word in sentence:
    if word.endswith('po'):
        print("FILIPINO")

    elif word.endswith('desu') or word.endswith('masu'):
        print("JAPANESE")

    elif word.endswith('mnida'):
        print("KOREAN")
    
