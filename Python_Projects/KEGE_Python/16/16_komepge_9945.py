# Определите, сколько символов * выведет эта процедура при вызове F(127):
# Условия задачи:
# def F(n):
#    print('*')
#    if n > 1:
#       F(n-2)
#       F(n // 2)
#       print('*')
#    print('*')

def F(n):
   global otvet   # Глобальная переменная
   otvet += '*'
   if n > 1:
      F(n-2)
      F(n // 2)
      otvet += '*'
   otvet += '*'

otvet = ''
F(127)
print(len(otvet))