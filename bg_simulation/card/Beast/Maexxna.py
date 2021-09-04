from ..Card import Card

class Maexxna(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '독성'
        self.type = 'Beast'
        self.name = '맥스나'
        self.name_eng = 'Maexxna'
        self.attack = 2
        self.health = 8
        self.tier = 6
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
        