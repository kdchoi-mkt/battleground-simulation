from ..Card import Card

class MenagerieJug(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '전투의 함성: 종족이 서로 다른 무작위 아군 하수인 셋에게 +2/+2을 부여합니다.'
        self.type = 'Neutral'
        self.name = '박물관 주전자'
        self.name_eng = 'Menagerie Jug'
        self.attack = 3
        self.health = 3
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
        self.battle_cry = True
        self.available_in_shop = True
        self.death_rattle_list = self.set_death_rattle_list()
        