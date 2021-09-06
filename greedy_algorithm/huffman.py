import heapq

def huffman_cost(l): #l 은 주어진 리스트
	H = []
	cost = 0
	
	for x in range(len(l)):
		heapq.heappush(H, (l[x], str(x)))
		
	while(len(H) > 1):
		a = heapq.heappop(H)
		b = heapq.heappop(H)
		heapq.heappush(H,(a[0] + b[0], '('+a[1] + ' ' + b[1] + ')'))
	tree_string = heapq.heappop(H)[1]
	count = 0
	temp = ''
	
	for i in range(len(tree_string)):
		if(tree_string[i] == '('):
			count += 1
			temp = ''
		
		if(tree_string[i] == ')'):
			count -= 1
			temp = ''
			
		if(tree_string[i] == ' '):
			temp = ''
			
		if(tree_string[i] not in '() '):
			temp += tree_string[i] #2자리 숫자를 위해 임시 변수 temp
			if(tree_string[i+1] in '() '):
				cost += l[int(temp)] * count
				
	return cost
		
	
data = list(map(int, input().split()))

print(huffman_cost(data))
