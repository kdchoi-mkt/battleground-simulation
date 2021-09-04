from ..Card import Card

class AnnoyoModule(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '합체, 도발, 천상의 보호막'
        self.type = 'Mech'
        self.name = '안녕모듈'
        self.name_eng = 'Annoy-o-Module'
        self.attack = 2
        self.health = 4
        self.tier = 4
        self.live = True
        self.taunt = True
        self.divine_shield = True
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
        