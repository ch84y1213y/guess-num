import random
start = input('請決定隨機數字範圍開始值')
end = input('請決定隨機數字範圍結束值')
start = int(start)
end = int(end)

r = random.randint(start, end) #randint為函式
count = 0  
while True: #無線循迴
	count = count + 1 #快寫法可以寫成count += 1
	num = input('請猜數字: ')
	num = int(num) #型別轉換
	if num == r:
		print('你猜中了!')
		print('這是你猜的第', count, '次')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
	    print('比答案小')	
	print('這是你猜的第', count, '次') 