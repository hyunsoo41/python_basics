scores = {"math":0, "English":50, "Coding":100}
for subject, score in scores.items():
    # print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":")
    # 8칸 확보 후 왼쪽 정렬, 4칸 확보 후 오른쪽 정렬
    # 수학      :   0
    # 영어      :  50
    # 코딩      : 100

for num in range(1, 21):
    prit("waiting number: " + str(num).zfill(3))
    # waiting number: 001,002...020
