from ..Card import Card

class Groundshaker(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '이 하수인에게 혈석을 낸 후에, 다음 전투 동안 내 다른 아군 하수인들에게 공격력을 +2 부여합니다.'
        self.type = 'Quilboar'
        self.name = '지면진동자'
        self.name_eng = 'Groundshaker'
        self.attack = 2
        self.health = 6
        self.tier = 4
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
        