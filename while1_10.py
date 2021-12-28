start_n = int(input("put first numb "))
end_n   = int(input("put second numb "))
n = start_n
if n<=end_n:
	while  n<=end_n:
		print(n)
		n += 1
elif n >= end_n:
	while n>=end_n:
		print(n)
		n -=1