from ..Card import Card

class ArmofTheEmpire(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '아군 도발 하수인이 공격당할 때마다 그 하수인에게 영구히 공격력을 +2 부여합니다.'
        self.type = 'Neutral'
        self.name = '제국의 무장'
        self.name_eng = 'Arm of the Empire'
        self.attack = 4
        self.health = 4
        self.tier = 3
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
        self.battle_cry = False
        self.available_in_shop = True
        self.death_rattle_list = self.set_death_rattle_list()
        