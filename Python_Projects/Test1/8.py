k=0
a=0
for x1 in 'АВР':
    for x2 in 'АВР':
        for x3 in 'АВР':
            for x4 in 'АВР':
                for x5 in 'АВР':
                    for x6 in 'АВР':
                        for x7 in 'АВР':
                            s=x1+x2+x3+x4+x5+x6+x7
                            # проверяем что наша комбинация сорержит А-3 шт., В-2шт., Р-2шт.
                            if s.count('А')==3 and s.count('В')==2 and s.count('Р')==2:
                                a += 1
                                if s[0] == 'В' and s.count('ААА')==1 and s.count('РР')==0 and a % 2 == 0:
                                    k=a
                                  
print(k)