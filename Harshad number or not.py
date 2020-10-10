#https://www.facebook.com/permalink.php?story_fbid=107317871142097&id=100055916535575
#Subscribed by Code House
@Hacktoberfest 2020
@C++
num = int(input())
sum = 0
temp = num
while(temp > 0):
	sum += temp % 10
	temp = int(temp / 10)
res = num % sum
if(res == 0):
	print(“Harshad Number”);
else:
	print(“Not Harshad Number”);
