# practice: list, files, loops functions
score1 = int(input())
score2 = int(input())
score3 = int(input())
score4 = int(input())
score5 = int(input())

score_list = [score1, score2, score3, score4, score5]

file = open("scores.txt", "w")

for score in score_list:
    file.write(str(score) + "\n")

file.close()

max_num = max(score_list)
min_num = min(score_list)
avg_num = sum(score_list) / len(score_list)

print(score_list)
print(max_num)
print(min_num)
print(avg_num)
