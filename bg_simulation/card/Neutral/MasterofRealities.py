from ..Card import Card

class MasterofRealities(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '도발, 아군 정령이 능력치를 얻은 후에, +1/+1을 얻습니다.'
        self.type = 'Neutral'
        self.name = '현실 왜곡사 '
        self.name_eng = 'Master of Realities'
        self.attack = 6
        self.health = 6
        self.tier = 6
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
        