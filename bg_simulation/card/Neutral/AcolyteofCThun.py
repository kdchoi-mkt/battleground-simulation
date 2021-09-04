from ..Card import Card

class AcolyteofCThun(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '도발, 환생'
        self.type = 'Neutral'
        self.name = '크툰의 수행사제'
        self.name_eng = 'Acolyte of C’Thun'
        self.attack = 2
        self.health = 2
        self.tier = 1
        self.live = True
        self.taunt = True
        self.divine_shield = False
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
        