# -*- coding: cp1251 -*-
# 1
print("Введите строку:")
st = input().lower()
obrst = st[::-1]
if st == obrst:
    print('YES')
else: 
    print('NO')
    
#2 
print("Введите строку с пробелами")

st = input()

while st.find('  ') > 0:
    st = st.replace('  ',' ')
    
print(st)
