class Unit:
  def __init__(self, name, hp, damage):
    self.name = name
    self.hp = hp
    self.damage = damage
    print("{0} 유닛이 생성되었습니다.".format(self.name))
    print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))
    
class AttackUnit(Unit):
  def __init__(self, name, hp, damage): # 상속
    Unit.__init__(self, name, hp) # 상속받은것을 정의해줘야함
    self.damage = damage
    
  def attack(self, location):
    print('{} : {} 방향으로 공격합니다. [공격력 {}]'.format(self.name, location, self.damage))
    
  def damaged(self, damage):
    print('{} : {} 데미지를 입었습니다.'.format(self.name, damage))
    self.hp -= damage
    print('{} : HP {}'.format(self.name, self.hp))
    if self.hp <= 0:
      print('{} has been destroied'.format(self.name))
      
firebat1 = AttackUnit('Firebat', 50, 16)
firebat1.attack('5시')

firebat1.damaged(25)
firebat1.damaged(25)

