from ..Card import Card

class Charlga(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '내 턴이 끝날 때, 다른 모든 아군 하수인에게 혈석을 냅니다.'
        self.type = 'Quilboar'
        self.name = '차를가'
        self.name_eng = 'Charlga'
        self.attack = 4
        self.health = 4
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
        self.battle_cry = False
        self.available_in_shop = True
        self.death_rattle_list = self.set_death_rattle_list()
        