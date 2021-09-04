from ..Card import Card

class BrannBronzebeard(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '내 전투의 함성 능력이 2번 발동합니다.'
        self.type = 'Neutral'
        self.name = '브란 브론즈비어드'
        self.name_eng = 'Brann Bronzebeard'
        self.attack = 2
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
        self.battle_cry = False
        self.available_in_shop = True
        self.death_rattle_list = self.set_death_rattle_list()
        