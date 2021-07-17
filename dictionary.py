cabinet = {3:'blue', 100:'green', 'aa':'black'}
print(cabinet[3])
print(cabinet[100])
print(cabinet[5])  # 값이 없으면 오류

print(cabinet.get(3))
print(cabinet.get(5))  # 값이 없으면 None 출력
print(cabinet.get(5, "사용 가능"))  # 사용 가능
print(cabinet['aa'])
print(cabinet.get('aa'))

print(3 in cabinet) # True
print(5 in cabinet) # False

# add or update keys
cabinet['aa'] = 'gray'  # black -> gray

# delete keys
del cabinet['aa']
print(cabinet)

# print keys only
print(cabinet.keys())

# print values only
print(cabinet.values())

# print both keys and values
print(cabinet.items())

# delete all
cabinet.claer()
