scores = [40, 89, 90, 89, 23, 90, 50]
unique_scores = []
for i in scores:
    if i not in unique_scores:
        unique_scores.append(i)
unique_scores.sort(reverse=True)
print("First best:", unique_scores[0])
print("Second best:", unique_scores[1])
