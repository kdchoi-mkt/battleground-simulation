from ..Card import Card

class ColdlightSeer(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '전투의 함성: 내 다른 멀록들에게 생명력을 +2 부여합니다.'
        self.type = 'Murloc'
        self.name = '시린빛 예언자'
        self.name_eng = 'Coldlight Seer'
        self.attack = 2
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
        