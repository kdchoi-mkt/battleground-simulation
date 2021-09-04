from ..Card import Card

class Gemsplitter(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '아군 하수인이 천상의 보호막을 잃은 후에, 혈석을 얻습니다.'
        self.type = 'Quilboar'
        self.name = '혈석절단자'
        self.name_eng = 'Gemsplitter'
        self.attack = 2
        self.health = 4
        self.tier = 3
        self.live = True
        self.taunt = False
        self.divine_shield = True
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
        