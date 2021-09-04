from ..Card import Card

class SaltyLooter(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '내가 해적을 낼 때마다 +1/+1을 얻습니다.'
        self.type = 'Pirate'
        self.name = '바다의 노략꾼'
        self.name_eng = 'Salty Looter'
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
        self.avenge = False
        self.avenge_count = 0
        self.death_rattle = False
        self.battle_cry = False
        self.available_in_shop = True
        self.death_rattle_list = self.set_death_rattle_list()
        