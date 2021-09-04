from ..Card import Card

class DamagedGolem(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '-'
        self.type = 'Mech'
        self.name = '손상된 골렘'
        self.name_eng = 'Damaged Golem'
        self.attack = 2
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
        