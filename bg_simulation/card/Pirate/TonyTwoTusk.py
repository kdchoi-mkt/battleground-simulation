from ..Card import Card

class TonyTwoTusk(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '복수 (5): 다른 아군 해적을 영구히 황금 하수인으로 만듭니다.'
        self.type = 'Pirate'
        self.name = '쌍엄니 토니'
        self.name_eng = 'Tony Two-Tusk'
        self.attack = 4
        self.health = 6
        self.tier = 5
        self.live = True
        self.taunt = False
        self.divine_shield = False
        self.windfury = False
        self.reborn = False
        self.frenzy = False
        self.poison = False
        self.avenge = True
        self.avenge_count = 5
        self.death_rattle = False
        self.battle_cry = False
        self.available_in_shop = True
        self.death_rattle_list = self.set_death_rattle_list()
        