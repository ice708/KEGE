k=0
a=0
for x1 in 'КОСУФ':
    for x2 in 'КОСУФ':
        for x3 in 'КОСУФ':
            for x4 in 'КОСУФ':
                for x5 in 'КОСУФ':
                    a += 1
                    s=x1+x2+x3+x4+x5
                    if s.count('У')==2 and s.count('Ф')==0:
                        k=a    
print(k)