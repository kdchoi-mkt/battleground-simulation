from ..Card import Card

class SaltscaleHoncho(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '내가 멀록을 낸 후에, 다른 아군 멀록 둘에게 생명력을 +1 부여합니다.'
        self.type = 'Murloc'
        self.name = '소금비늘 우두머리 '
        self.name_eng = 'Saltscale Honcho '
        self.attack = 3
        self.health = 2
        self.tier = 2
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
        