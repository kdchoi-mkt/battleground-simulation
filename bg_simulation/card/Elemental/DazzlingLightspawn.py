from ..Card import Card

class DazzlingLightspawn(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '복수 (2): 이번 게임 동안 밥의 선술집에 있는 정령들이 +1/+1을 얻습니다.'
        self.type = 'Elemental'
        self.name = '눈부신 빛의 정령'
        self.name_eng = 'Dazzling Lightspawn'
        self.attack = 4
        self.health = 5
        self.tier = 4
        self.live = True
        self.taunt = False
        self.divine_shield = False
        self.windfury = False
        self.reborn = False
        self.frenzy = False
        self.poison = False
        self.avenge = True
        self.avenge_count = 2
        self.death_rattle = False
        self.battle_cry = False
        self.available_in_shop = True
        self.death_rattle_list = self.set_death_rattle_list()
        