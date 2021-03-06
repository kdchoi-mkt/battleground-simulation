from ..Card import Card

class Sellemental(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '이 하수인을 팔면, 2/2 정령을 내 손으로 가져옵니다.'
        self.type = 'Elemental'
        self.name = '판다네 정령'
        self.name_eng = 'Sellemental'
        self.attack = 2
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
        