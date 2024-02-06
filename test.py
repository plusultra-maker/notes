scores=[90,87,84,96,95,89,84,84,81,93,90,88,84,84,82,95,87,80,97,96,92,89,87,84,83,72,94,93,91,88,88,85,80,76.5,94,89,88,87,84,81,79]
weight=[3,3,3,3,2,3,5,2,3,3,2,2,3,3,2,2,3,4,2,1,4,4,3,3,3,4,1,5,4,2,3,2,4,3,4,3,4,2,2,2,5]
print(len(scores))
print(len(weight))
print("The average weighted score is: ", sum([scores[i]*weight[i] for i in range(len(scores))])/sum(weight))