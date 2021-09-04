from ..Card import Card

class Leapfrogger(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '죽음의 메아리: 아군 야수에게 +2/+2와 이 죽음의 메아리를 부여합니다.'
        self.type = 'Beast'
        self.name = '폴짝개구리 '
        self.name_eng = 'Leapfrogger'
        self.attack = 3
        self.health = 3
        self.tier = 2
        self.live = True
        self.taunt = False
        self.divine_shield = False
        self.windfury = False
        self.reborn = False
        self.frenzy = False
        self.poison = False
        self.avenge = False
        self.avenge_count = 0
        self.death_rattle = True
        self.battle_cry = False
        self.available_in_shop = True
        self.death_rattle_list = self.set_death_rattle_list()
        