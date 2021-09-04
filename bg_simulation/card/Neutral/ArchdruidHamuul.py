from ..Card import Card

class ArchdruidHamuul(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '전투의 함성: 밥의 선술집을 새로고침합니다. 내가 가장 많이 보유한 종족의 하수인만 생깁니다.'
        self.type = 'Neutral'
        self.name = '대드루이드 하뮬'
        self.name_eng = 'Archdruid Hamuul'
        self.attack = 4
        self.health = 4
        self.tier = 6
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
        self.battle_cry = True
        self.available_in_shop = True
        self.death_rattle_list = self.set_death_rattle_list()
        