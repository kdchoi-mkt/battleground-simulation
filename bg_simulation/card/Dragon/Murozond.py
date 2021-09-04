from ..Card import Card

class Murozond(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '전투의 함성: 방금 전투한 상대편의 무작위 하수인을 내 손으로 가져옵니다.'
        self.type = 'Dragon'
        self.name = '무르도즈노'
        self.name_eng = 'Murozond'
        self.attack = 5
        self.health = 5
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
        