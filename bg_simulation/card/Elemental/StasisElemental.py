from ..Card import Card

class StasisElemental(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '전투의 함성:밥의 선술집에 다른 무작위 정령을 추가하고 빙결 상태로 만듭니다.'
        self.type = 'Elemental'
        self.name = '정지장 정령'
        self.name_eng = 'Stasis Elemental'
        self.attack = 4
        self.health = 4
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
        self.battle_cry = True
        self.available_in_shop = True
        self.death_rattle_list = self.set_death_rattle_list()
        