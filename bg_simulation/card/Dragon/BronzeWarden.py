from ..Card import Card

class BronzeWarden(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '천상의 보호막, 환생'
        self.type = 'Dragon'
        self.name = '청동 감시자'
        self.name_eng = 'Bronze Warden'
        self.attack = 2
        self.health = 1
        self.tier = 3
        self.live = True
        self.taunt = False
        self.divine_shield = True
        self.windfury = False
        self.reborn = True
        self.frenzy = False
        self.poison = False
        self.avenge = False
        self.avenge_count = 0
        self.death_rattle = False
        self.battle_cry = False
        self.available_in_shop = True
        self.death_rattle_list = self.set_death_rattle_list()
        