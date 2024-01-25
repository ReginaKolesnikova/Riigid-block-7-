from random import *
def failist_to_dict(f:str):
    riik_pealinn={}
    pealinn_riik={}
    riigid=[] 
    file=open(f,'r',encoding="utf-8-sig")
    for line in file:
        k,v=line.strip().split('-')
        riik_pealinn[k]=v
        pealinn_riik[v]=k 
        riigid.append(k)
        file.close()
        return riik_pealinn,pealinn_riik,riigid 

riik_pealinn,pealinn_riik,riigid=failist_to_dict("riigid_pealinnd.txt")
riigid=list(riik_pealinn.keys())
print(riigid) 

while True: 
   riik=input("Riik: ")
   print(riik_pealinn[riik])

#Составьте словарь, где перечислите часть стран Европы.
#Ключом будет страна, описанием столица или наоборот.

#При помощи функций реализуйте возможности:
# отображение столицы, если вводиться название государства и наоборот.
# если искомое слово отсутствует в словаре, дайте пользователю возможность добавить его в словарь.
# если пользователь находит ошибку в словаре, то у него должна быть возможность ее исправить.
# При желании пользователя проверить знание слов из словаря, реализуйте эту возможность  
# случайным образом появляются названия столиц/стран,
# после ввода соответствующего значения, сообщение о правильности или нет
# после окончания проверки знаний результат в %)


