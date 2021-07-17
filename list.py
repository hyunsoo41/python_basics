num = [10,20,30]
print(num)
print(num.index(20))  # 1

num.append('fourth')
print(num)  # [10,20,30,fourth]

num.insert(1, 'second')
print(num)  # [10,second,20,30,fourth]

print(num.pop())
print(num)  # [10,second,20,30]

print(num.count('second'))  # 1

# 정렬
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)  # [1,2,3,4,5]

num_list.reverse()  # [5,4,3,2,1]
print(num_list)

# 모두 지우기 
#num_list.clear()  # []

# 다양한 자료형 함께 사용
mix_list = ["이름", 20, True]

# 리스트 확장
num_list.extend(mix_list)
print(num_list)  # [5,2,4,3,1,'이름',20,True]
