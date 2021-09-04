from ..Card import Card

class TavernTempest(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '전투의 함성: 다른 무작위 정령을 내 손으로 가져옵니다.'
        self.type = 'Elemental'
        self.name = '선술집 폭풍우'
        self.name_eng = 'Tavern Tempest'
        self.attack = 4
        self.health = 4
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
        self.battle_cry = True
        self.available_in_shop = True
        self.death_rattle_list = self.set_death_rattle_list()
        