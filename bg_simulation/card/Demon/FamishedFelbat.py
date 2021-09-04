from ..Card import Card

class FamishedFelbat(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '내 턴이 끝날 때, 아군 악마들이 밥의 선술집에 있는 하수인을 잡아먹습니다. 그 하수인의 능력치를 얻습니다.'
        self.type = 'Demon'
        self.name = '굶주린 지옥박쥐'
        self.name_eng = 'Famished Felbat'
        self.attack = 9
        self.health = 5
        self.tier = 6
        self.live = True
        self.taunt = False
        self.divine_shield = False
        self.windfury = False
        self.reborn = False
        self.frenzy = False
        self.poison = False
        self.avenge = False
        self.avenge_count = 0
        self.death_rattle = False
        self.battle_cry = False
        self.available_in_shop = True
        self.death_rattle_list = self.set_death_rattle_list()
        