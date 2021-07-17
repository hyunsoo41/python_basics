def profile(name, age, *language):
  print('Name : {}\tage : {}\t'.format(name, age), end=' ')  # end=' ' 줄바꿈을 하지않음
  for lang in language:
    print(lang, end=' ')
  print()
    
profile("Iron man", 20, "python", "C", "Java")
profile("Thor", 25, "Kotlin", "Swift")
