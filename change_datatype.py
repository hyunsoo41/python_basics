# 자료구조의 변경
menu = {"coffe", "milk", "juice"}
print(menu, type(menu))  # {'coffe','milk','juice'} <class 'set'>

menu = list(menu)
print(menu, type(menu))  # ['coffe','milk','juice'] <class 'list'>

menu = tuple(menu)
print(menu, type(menu)) # ('coffe','milk','juice') <class 'tuple'>

menu = set(menu)
print(menu, type(menu))
