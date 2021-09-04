from ..Card import Card

class WildfireElemental(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '이 하수인이 공격하여 다른 하수인을 처치한 후에, 초과한 피해량만큼 양옆에 있는 하수인 중 하나에게 피해를 줍니다.'
        self.type = 'Elemental'
        self.name = '야생불 정령'
        self.name_eng = 'Wildfire Elemental'
        self.attack = 7
        self.health = 4
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
        