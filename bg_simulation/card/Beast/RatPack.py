from ..Card import Card

class RatPack(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '죽음의 메아리: 이 하수인의 공격력만큼 1/1 쥐를 소환합니다.'
        self.type = 'Beast'
        self.name = '쥐 떼'
        self.name_eng = 'Rat Pack'
        self.attack = 2
        self.health = 2
        self.tier = 3
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
        