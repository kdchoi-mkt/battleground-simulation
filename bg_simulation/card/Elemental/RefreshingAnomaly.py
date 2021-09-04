from ..Card import Card


class RefreshingAnomaly(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '전투의 함성: 내 다음 새로고침의 비용이 (0)이 됩니다.'
        self.type = 'Elemental'
        self.name = '원기회복의 변형물'
        self.name_eng = 'Refreshing Anomaly'
        self.attack = 1
        self.health = 4
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
