from ..Card import Card

class OldMurkEye(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '돌진, 전장의 다른 멀록 하나당 공격력을 +1 얻습니다.'
        self.type = 'Murloc'
        self.name = '늙은 거먹눈 멀록'
        self.name_eng = 'Old Murk-Eye'
        self.attack = 2
        self.health = 4
        self.tier = 2
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
        