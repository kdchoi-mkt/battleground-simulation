from ..Card import Card

class RedWhelp(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '기선 제압: 아군 용족만큼 무작위 적 하수인에게 피해를 줍니다.'
        self.type = 'Dragon'
        self.name = '새끼 붉은용'
        self.name_eng = 'Red Whelp'
        self.attack = 1
        self.health = 2
        self.tier = 1
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
        