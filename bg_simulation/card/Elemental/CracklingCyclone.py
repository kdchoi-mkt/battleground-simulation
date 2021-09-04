from ..Card import Card

class CracklingCyclone(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '천상의 보호막, 질풍'
        self.type = 'Elemental'
        self.name = '파지직거리는 회오리'
        self.name_eng = 'Crackling Cyclone'
        self.attack = 4
        self.health = 1
        self.tier = 3
        self.live = True
        self.taunt = False
        self.divine_shield = True
        self.windfury = True
        self.reborn = False
        self.frenzy = False
        self.poison = False
        self.avenge = False
        self.avenge_count = 0
        self.death_rattle = False
        self.battle_cry = False
        self.available_in_shop = True
        self.death_rattle_list = self.set_death_rattle_list()
        