from ..Card import Card

class FoeReaper4000(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '공격하는 대상 양옆의 하수인들에게도 피해를 줍니다.'
        self.type = 'Mech'
        self.name = '전투 절단기 4000'
        self.name_eng = 'Foe Reaper 4000'
        self.attack = 6
        self.health = 9
        self.tier = 6
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
        