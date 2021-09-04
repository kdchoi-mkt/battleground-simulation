from ..Card import Card

class DynamicDuo(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '도발, 다른 가시멧돼지에게 혈석을 낸 후에, +1/+1을 얻습니다.'
        self.type = 'Quilboar'
        self.name = '환상의 짝꿍'
        self.name_eng = 'Dynamic Duo'
        self.attack = 3
        self.health = 4
        self.tier = 4
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
        