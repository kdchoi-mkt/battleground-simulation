from ..Card import Card

class BuddingGreenthumb(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '복수 (3): 양옆의 하수인들에게 영구히 +2/+1을 부여합니다.'
        self.type = 'Neutral'
        self.name = '피어나는 그린썸'
        self.name_eng = 'Budding Greenthumb'
        self.attack = 1
        self.health = 2
        self.tier = 3
        self.live = True
        self.taunt = False
        self.divine_shield = False
        self.windfury = False
        self.reborn = False
        self.frenzy = False
        self.poison = False
        self.avenge = True
        self.avenge_count = 3
        self.death_rattle = False
        self.battle_cry = False
        self.available_in_shop = True
        self.death_rattle_list = self.set_death_rattle_list()
        