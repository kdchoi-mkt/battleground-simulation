from ..Card import Card

class SouthseaStrongarm(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '전투의 함성: 아군 해적에게 이번 턴에 내가 산 해적 하나당 +1/+1을 부여합니다.'
        self.type = 'Pirate'
        self.name = '남쪽바다 폭력배'
        self.name_eng = 'Southsea Strongarm'
        self.attack = 4
        self.health = 3
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
        self.death_rattle = False
        self.battle_cry = True
        self.available_in_shop = True
        self.death_rattle_list = self.set_death_rattle_list()
        