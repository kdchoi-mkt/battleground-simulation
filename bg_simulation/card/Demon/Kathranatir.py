from ..Card import Card

class Kathranatir(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '내 다른 악마들이 공격력을 +3 얻습니다. 내 영웅이 면역 상태가 됩니다.'
        self.type = 'Demon'
        self.name = '카트라나티르'
        self.name_eng = 'Kathranatir '
        self.attack = 7
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
        