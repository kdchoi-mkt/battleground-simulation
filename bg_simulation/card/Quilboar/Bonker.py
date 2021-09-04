from ..Card import Card

class Bonker(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '질풍, 이 하수인이 공격한 후에, 혈석을 얻습니다.'
        self.type = 'Quilboar'
        self.name = '머리 강타꾼'
        self.name_eng = 'Bonker'
        self.attack = 3
        self.health = 7
        self.tier = 4
        self.live = True
        self.taunt = False
        self.divine_shield = False
        self.windfury = True
        self.reborn = False
        self.frenzy = False
        self.poison = False
        self.avenge = False
        self.avenge_count = 0
        self.death_rattle = False
        self.battle_cry = False
        self.available_in_shop = True
        self.death_rattle_list = self.set_death_rattle_list()
        