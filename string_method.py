python = "Python is Amazing"
print(python.lower())  # python is amazing
print(python.upper())  # PYTHON IS AMAZING
print(python[0].isupper())  # 대문자인지 확인 -> True
print(len(python))
print(python.replace("Python","Java"))

index = python.index("n")
print(index)  # 5
index = pythonn.index("n", index + 1)
print(index)  # 15

print(python.find("n")  # 5
print(python.find("Java")  # -1
print(python.index("Java")  # 오류

print(python.count("n")  # 2
