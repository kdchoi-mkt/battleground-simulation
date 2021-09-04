from ..Card import Card

class GentleDjinni(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '도발, 죽음의 메아리: 다른 무작위 정령을 소환합니다. 그 정령을 복사하여 내 손에도 가져옵니다.'
        self.type = 'Elemental'
        self.name = '온화한 신령'
        self.name_eng = 'Gentle Djinni'
        self.attack = 4
        self.health = 5
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
        self.death_rattle = True
        self.battle_cry = False
        self.available_in_shop = True
        self.death_rattle_list = self.set_death_rattle_list()
        