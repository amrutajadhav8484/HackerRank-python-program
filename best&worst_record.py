Problem statement:Maria plays college basketball and wants to go pro. Each season she maintains a record of her play. 
She tabulates the number of times she breaks her season record for most points and least points in a game. Points scored in 
the first game establish her record for the season, and she begins counting from there
def breakingRecords(scores):
    # Write your code here
    score=scores[0]
    high_count=0
    low_count=0
    min1=score
    max1=score
    for i in range(1,len(scores)):
        if scores[i]<min1:
            low_count+=1;
            min1=scores[i]
        elif scores[i]>max1:
            high_count+=1
            max1=scores[i]
    return(high_count,low_count)
