from ..Card import Card

class MicroMummy(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '환생, 내 턴이 끝날 때, 다른 무작위 아군 하수인에게 공격력을 +1 부여합니다.'
        self.type = 'Mech'
        self.name = '초소형 미라'
        self.name_eng = 'Micro Mummy'
        self.attack = 1
        self.health = 2
        self.tier = 1
        self.live = True
        self.taunt = False
        self.divine_shield = False
        self.windfury = False
        self.reborn = True
        self.frenzy = False
        self.poison = False
        self.avenge = False
        self.avenge_count = 0
        self.death_rattle = False
        self.battle_cry = False
        self.available_in_shop = True
        self.death_rattle_list = self.set_death_rattle_list()
        