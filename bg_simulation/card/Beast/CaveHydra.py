from ..Card import Card

class CaveHydra(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '공격하는 대상 양옆의 하수인들에게도 피해를 줍니다.'
        self.type = 'Beast'
        self.name = '동굴 히드라'
        self.name_eng = 'Cave Hydra'
        self.attack = 2
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
        