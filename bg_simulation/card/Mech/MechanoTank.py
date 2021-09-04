from ..Card import Card

class MechanoTank(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '복수 (2): 생명력이 가장 높은 적 하수인에게 피해를 6 줍니다.'
        self.type = 'Mech'
        self.name = '기계보행전차'
        self.name_eng = 'Mechano-Tank'
        self.attack = 6
        self.health = 3
        self.tier = 4
        self.live = True
        self.taunt = False
        self.divine_shield = False
        self.windfury = False
        self.reborn = False
        self.frenzy = False
        self.poison = False
        self.avenge = True
        self.avenge_count = 2
        self.death_rattle = False
        self.battle_cry = False
        self.available_in_shop = True
        self.death_rattle_list = self.set_death_rattle_list()
        