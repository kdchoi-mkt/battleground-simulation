from ..Card import Card

class Amalgadon(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '전투의 함성: 다른 아군 하수인의 종족 하나당 무작위로 적응합니다.'
        self.type = 'All'
        self.name = '흉합체'
        self.name_eng = 'Amalgadon'
        self.attack = 6
        self.health = 6
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
        