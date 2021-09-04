from ..Card import Card

class BirdBuddy(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '복수 (1): 내 야수들에게 +1/+1을 부여합니다.'
        self.type = 'Neutral'
        self.name = '조류의 친구'
        self.name_eng = 'Bird Buddy'
        self.attack = 4
        self.health = 4
        self.tier = 3
        self.live = True
        self.taunt = False
        self.divine_shield = False
        self.windfury = False
        self.reborn = False
        self.frenzy = False
        self.poison = False
        self.avenge = True
        self.avenge_count = 1
        self.death_rattle = False
        self.battle_cry = False
        self.available_in_shop = True
        self.death_rattle_list = self.set_death_rattle_list()
        