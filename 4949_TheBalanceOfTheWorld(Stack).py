# 백준 4949 김은비 

while True:
	parSeq = input()
	if parSeq == '.':
		break
	S = []
	res = True
	for p in parSeq:
		if p == '(' or p == '[':
			S.append(p)
		elif p == ')':
			if not S or S[-1] == '[':
				res = False
				break
			elif S[-1] == '(':
				S.pop()
					
		elif p == ']':
			if not S or S[-1] == '(':
				res = False
				break
			elif S[-1] == '[':
				S.pop()
					
	if not S and res == True:
		print("yes")
	else: 
		print("no")
