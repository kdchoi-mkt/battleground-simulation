from ..Card import Card

class MurlocWarleader(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '내 다른 멀록들이 공격력을 +2 얻습니다.'
        self.type = 'Murloc'
        self.name = '멀록 전투대장'
        self.name_eng = 'Murloc Warleader'
        self.attack = 3
        self.health = 3
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
        