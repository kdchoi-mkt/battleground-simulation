from ..Card import Card

class WrathWeaver(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '내가 악마를 낸 후에, 내 영웅에게 피해를 1 주고 +2/+2를 얻습니다.'
        self.type = 'Neutral'
        self.name = '분노의 명인'
        self.name_eng = 'Wrath Weaver'
        self.attack = 1
        self.health = 3
        self.tier = 1
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
        