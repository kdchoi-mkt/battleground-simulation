from ..Card import Card

class Ghastcoiler(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '죽음의 메아리: 무작위 죽음의 메아리 하수인을 둘 소환합니다.'
        self.type = 'Beast'
        self.name = '섬뜩한 방울뱀'
        self.name_eng = 'Ghastcoiler'
        self.attack = 7
        self.health = 7
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
        self.death_rattle = True
        self.battle_cry = False
        self.available_in_shop = True
        self.death_rattle_list = self.set_death_rattle_list()
        