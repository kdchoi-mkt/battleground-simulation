from ..Card import Card

class StrongshellScavenger(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '전투의 함성: 내 도발 하수인들에게 +2/+2를 부여합니다.'
        self.type = 'Neutral'
        self.name = '튼튼껍질 청소부'
        self.name_eng = 'Strongshell Scavenger'
        self.attack = 2
        self.health = 3
        self.tier = 5
        self.live = True
        self.taunt = True
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
        