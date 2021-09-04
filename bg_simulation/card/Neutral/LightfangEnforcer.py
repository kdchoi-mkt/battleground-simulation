from ..Card import Card

class LightfangEnforcer(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '내 턴이 끝날 때, 모든 아군 종족에게 각각 +2/+2를 부여합니다. (종족마다 하나씩)'
        self.type = 'Neutral'
        self.name = '빛송곳니 집행자'
        self.name_eng = 'Lightfang Enforcer'
        self.attack = 2
        self.health = 2
        self.tier = 5
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
        