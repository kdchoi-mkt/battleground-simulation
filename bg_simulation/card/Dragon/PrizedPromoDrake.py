from ..Card import Card

class PrizedPromoDrake(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '기선 제압: 아군 용족 하나당 양옆의 하수인들에게 +1/+1을 부여합니다.'
        self.type = 'Dragon'
        self.name = '귀중한 고취비룡 '
        self.name_eng = 'Prized Promo-Drake'
        self.attack = 5
        self.health = 5
        self.tier = 4
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
        