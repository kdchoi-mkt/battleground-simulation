from ..Card import Card

class Khadgar(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '하수인을 소환하는 내 카드들이 하수인을 두 배로 소환합니다.'
        self.type = 'Neutral'
        self.name = '카드가'
        self.name_eng = 'Khadgar'
        self.attack = 2
        self.health = 2
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
        