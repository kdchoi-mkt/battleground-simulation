from ..Card import Card

class MurlocScout(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '-'
        self.type = 'Murloc'
        self.name = '멀록 정찰병'
        self.name_eng = 'Murloc Scout'
        self.attack = 1
        self.health = 1
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
        self.available_in_shop = False
        self.death_rattle_list = self.set_death_rattle_list()
        