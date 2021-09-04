from ..Card import Card

class Scallywag(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '죽음의 메아리: 1/1 해적을 소환합니다. 그 해적이 즉시 공격합니다.'
        self.type = 'Pirate'
        self.name = '뱃사람'
        self.name_eng = 'Scallywag'
        self.attack = 2
        self.health = 1
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
        self.death_rattle = True
        self.battle_cry = False
        self.available_in_shop = True
        self.death_rattle_list = self.set_death_rattle_list()
        