from ..Card import Card

class Pupbot(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '천상의 보호막'
        self.type = 'Mech'
        self.name = '아기늑대로봇'
        self.name_eng = 'Pupbot'
        self.attack = 2
        self.health = 1
        self.tier = 1
        self.live = True
        self.taunt = False
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
        