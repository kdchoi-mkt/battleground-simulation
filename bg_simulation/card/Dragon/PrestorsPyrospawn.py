from ..Card import Card

class PrestorsPyrospawn(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '다른 아군 용족이 공격할 때마다 그 대상에게 피해를 3 줍니다.'
        self.type = 'Dragon'
        self.name = '프레스톨의 화염혈족  '
        self.name_eng = 'Prestors Pyrospawn '
        self.attack = 3
        self.health = 5
        self.tier = 4
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
        