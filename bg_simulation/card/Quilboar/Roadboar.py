from ..Card import Card

class Roadboar(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '광폭: 혈석을 얻습니다.'
        self.type = 'Quilboar'
        self.name = '길멧돼지'
        self.name_eng = 'Roadboar'
        self.attack = 1
        self.health = 4
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
        self.death_rattle = False
        self.battle_cry = False
        self.available_in_shop = True
        self.death_rattle_list = self.set_death_rattle_list()
        