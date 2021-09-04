from ..Card import Card

class Houndmaster(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '전투의 함성: 아군 야수에게 +2/+2와 도발을 부여합니다.'
        self.type = 'Neutral'
        self.name = '사냥개조련사'
        self.name_eng = 'Houndmaster'
        self.attack = 4
        self.health = 3
        self.tier = 3
        self.live = True
        self.taunt = True
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
        