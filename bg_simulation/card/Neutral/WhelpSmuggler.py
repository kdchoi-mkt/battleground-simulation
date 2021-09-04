from ..Card import Card

class WhelpSmuggler(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '아군 용족이 공격력을 얻은 후에, 그 용족에게 생명력을 +2 부여합니다.'
        self.type = 'Neutral'
        self.name = '새끼용 밀수꾼'
        self.name_eng = 'Whelp Smuggler'
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
        