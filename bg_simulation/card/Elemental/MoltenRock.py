from ..Card import Card

class MoltenRock(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '도발, 내가 정령을 낸 후에, 생명력을 +1 얻습니다.'
        self.type = 'Elemental'
        self.name = '녹아내린 바위'
        self.name_eng = 'Molten Rock'
        self.attack = 2
        self.health = 4
        self.tier = 2
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
        