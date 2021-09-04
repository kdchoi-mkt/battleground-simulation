from ..Card import Card

class PrimalfinLookout(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '전투의 함성: 내 전장에 다른 멀록이 있으면, 멀록을 발견합니다.'
        self.type = 'Murloc'
        self.name = '원시지느러미 망꾼'
        self.name_eng = 'Primalfin Lookout'
        self.attack = 3
        self.health = 2
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
        self.battle_cry = True
        self.available_in_shop = True
        self.death_rattle_list = self.set_death_rattle_list()
        