from ..Card import Card

class RingMatron(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '도발, 죽음의 메아리: 3/2 임프를 둘 소환합니다.'
        self.type = 'Demon'
        self.name = '고리 조련사'
        self.name_eng = 'Ring Matron'
        self.attack = 6
        self.health = 4
        self.tier = 4
        self.live = True
        self.taunt = True
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
        