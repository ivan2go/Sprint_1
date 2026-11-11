world_champions = {
    2002: 'Бразилия',
    2006: 'Италия',
    2010: 'Испания',
    2014: 'Германия',
    2018: 'Франция',
}

world_champions[2022] = 'Аргентина' #апдейтим словарь

for key,value in world_champions.items(): #перечивсляем чемпионов 
    print(key, '-', value) 

country = 'Италия'
italia_is_champion = False #объявляем флаг для цикла

for key,value in world_champions.items(): #ищем country по условиям
    if value == country and key >= 2000: 
        italia_is_champion = True 
        break

if italia_is_champion == True: 
    print(f'{country} cтановилась чемпионом мира по футболу в 21 веке!')
else: 
    print(f'{country} не выигрывала чемпионат мира по футболу в 21 веке.')