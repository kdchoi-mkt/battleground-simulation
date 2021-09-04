from ..Card import Card

class HalfShell(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '도발'
        self.type = 'Beast'
        self.name = '등딱지거북'
        self.name_eng = 'Half-Shell'
        self.attack = 2
        self.health = 3
        self.tier = 1
        self.live = True
        self.taunt = True
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
        