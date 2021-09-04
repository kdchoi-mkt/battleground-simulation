from ..Card import Card

class RazorfenGeomancer(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '전투의 함성: 혈석을 얻습니다.'
        self.type = 'Quilboar'
        self.name = '가시덩굴 흙점쟁이'
        self.name_eng = ' Razorfen Geomancer'
        self.attack = 3
        self.health = 1
        self.tier = 1
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
        