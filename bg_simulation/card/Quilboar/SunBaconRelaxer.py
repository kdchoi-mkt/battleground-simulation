from ..Card import Card

class SunBaconRelaxer(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '이 하수인을 팔면, 혈석을 2개 얻습니다.'
        self.type = 'Quilboar'
        self.name = '땡볕의 피서객'
        self.name_eng = 'Sun-Bacon Relaxer'
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
        