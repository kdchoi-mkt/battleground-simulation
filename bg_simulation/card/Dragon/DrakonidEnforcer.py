from ..Card import Card

class DrakonidEnforcer(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '아군 하수인이 천상의 보호막을 잃은 후에, +2/+2를 얻습니다.'
        self.type = 'Dragon'
        self.name = '용기병 집행자'
        self.name_eng = 'Drakonid Enforcer'
        self.attack = 3
        self.health = 6
        self.tier = 4
        self.live = True
        self.taunt = False
        self.divine_shield = True
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
        