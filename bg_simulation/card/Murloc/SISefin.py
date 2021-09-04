from ..Card import Card

class SISefin(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '복수 (3): 아군 멀록에게 영구히 독성을 부여합니다.'
        self.type = 'Murloc'
        self.name = 'SI:암살지느러미 '
        self.name_eng = 'SI:Sefin'
        self.attack = 2
        self.health = 6
        self.tier = 5
        self.live = True
        self.taunt = False
        self.divine_shield = False
        self.windfury = False
        self.reborn = False
        self.frenzy = False
        self.poison = False
        self.avenge = True
        self.avenge_count = 3
        self.death_rattle = False
        self.battle_cry = False
        self.available_in_shop = True
        self.death_rattle_list = self.set_death_rattle_list()
        