from ..Card import Card

class SewerRat(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '죽음의 메아리: 도발 능력이 있는 2/3 거북이를 소환합니다.'
        self.type = 'Beast'
        self.name = '하수도 쥐'
        self.name_eng = 'Sewer Rat'
        self.attack = 3
        self.health = 2
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
        self.death_rattle = True
        self.battle_cry = False
        self.available_in_shop = True
        self.death_rattle_list = self.set_death_rattle_list()
        