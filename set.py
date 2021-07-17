# 집합 (set)
# 중복 안됨, 순서 없음
my_set = {1,2,3,3,3}
print(my_set)

java = {"a", "b", "c"}
python = set(["a", "d"])

# 교집합 
print(java & python)
print(java.intersection(python))  # {'a'}

# 합집합 
print(java | python)
print(java.union(python))  # {'a','b','c','d'}

#차집합
print(java - python)
print(java.difference(python))  # {'b','c'}

java.add('e')
print(python)  # {'a','e','d'}

python.remove('b')
