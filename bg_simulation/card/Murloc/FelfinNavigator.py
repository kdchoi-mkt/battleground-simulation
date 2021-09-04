from ..Card import Card

class FelfinNavigator(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '전투의 함성: 내 다른 멀록들에게 +1/+1을 부여합니다.'
        self.type = 'Murloc'
        self.name = '지옥지느러미 길잡이'
        self.name_eng = 'Felfin Navigator'
        self.attack = 4
        self.health = 4
        self.tier = 3
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
        self.battle_cry = True
        self.available_in_shop = True
        self.death_rattle_list = self.set_death_rattle_list()
        