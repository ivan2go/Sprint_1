def digit_root(num):
    score = []
    num = str(num)
    for i in num:
        score.append(int(i))
        
    sum_score = sum(score)
    
    if sum_score < 10:
        return sum_score
    
    else: 
        return(digit_root(sum_score))

    
    
print(digit_root(1234))
