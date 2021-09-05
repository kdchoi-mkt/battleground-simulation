from ..Card import Card


class Voidwalker(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = "도발"
        self.type = "Demon"
        self.name = "공허 방랑자"
        self.name_eng = "Voidwalker"
        self.attack = 1
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
        self.available_in_shop = False
        self.death_rattle_list = self.set_death_rattle_list()
