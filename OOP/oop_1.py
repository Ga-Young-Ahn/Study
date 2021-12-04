hero_name = ['아이언맨', '데드풀', '울버린']
hero_health = [100, 200, 150]
hero_damage = [100, 200, 150]
hero_inventory = [
    {'gold' : 500, 'weapon' : '레이저'},
    {'gold' : 500, 'weapon' : '장검'},
    {'gold' : 500, 'weapon' : '칼'}
]

monster_name = ['고블린', '드래곤', '뱀파이어']
monster_health = [100, 200, 150]
monster_damage = [100, 200, 150]
monster_inventory = [
    {'gold' : 500, 'weapon' : '레이저'},
    {'gold' : 500, 'weapon' : '레이저'},
    {'gold' : 500, 'weapon' : '레이저'}
]

def hero_dies(hero_index):
    del hero_name[hero_index]
    del hero_health[hero_index]
    del hero_damage[hero_index]
    
    
hero_dies(0)

template = \
    '''
    히어로 이름:{}
    히어로 체력:{}
    히어로 데미지:{}
    히어로 인벤토리:{}
    '''
       
print(template.format(hero_name[0],
                      hero_health[0],
                      hero_damage[0],
                      hero_inventory[0]))


heroes = [
    {'name':'아이언맨', 'health':100, 'damage':200},
    {'name':'데드풀', 'health':200, 'damage':100},
    {'name':'울버린', 'health':150, 'damage':300}
]

monsters = [
    {'name':'고블린', 'health':100, 'damage':200},
    {'name':'드래곤', 'health':200, 'damage':100},
    {'name':'뱀파이어', 'health':150, 'damage':300}
]

print('#아이언맨 삭제 전')
print(heroes)
del heroes[0]
print('#아이언맨 삭제 후')
print(heroes)


class Character:
    def __init__(self, name, health, damage):
        self.name = name
        self.health =health
        self.damage = damage
        
    def __repr__(self):
        return self.name
    
heroes = []
heroes.append(Character('아이언맨', 100, 200))
heroes.append(Character('데드풀', 300, 30))
heroes.append(Character('울버린', 200, 50))

print('히어로 리스트 확인')
print(heroes)
print('히어로 데이터 확인')
for hero in heroes:
    print(hero.__dict__)
    
del heroes[0]

print('히어로 리스트 재확인')
print(heroes)
print('히어로 데이터 재확인')
for hero in heroes:
    print(hero.__dict__)