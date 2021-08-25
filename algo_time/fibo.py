def fibo(n):
	if(n < 2):
		return 1
	a = 1 
	b = 1
	c = a + b
	while (n >= 2):
		c = a + b
		a = b
		b = c
		n -= 1
	return c	
	

# n을 입력받은 후
# fibo(n) 호출!
# 리턴값을 출력함
n = int(input())
print(fibo(n))