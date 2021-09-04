from ..Card import Card

class RecyclingWraith(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '내가 정령을 낸 후에, 내 다음 새로고침의 비용이 (0)이 됩니다.'
        self.type = 'Elemental'
        self.name = '재활용 망령'
        self.name_eng = 'Recycling Wraith'
        self.attack = 5
        self.health = 4
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
        