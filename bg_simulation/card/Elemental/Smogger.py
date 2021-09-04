from ..Card import Card

class Smogger(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '전투의 함성: 아군 정령에게 내 선술집 단계만큼 능력치를 부여합니다.'
        self.type = 'Elemental'
        self.name = '매연정령'
        self.name_eng = 'Smogger'
        self.attack = 3
        self.health = 3
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
        