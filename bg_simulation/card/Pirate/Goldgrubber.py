from ..Card import Card

class Goldgrubber(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '내 턴이 끝날 때, 아군 황금 하수인 하나당 +2/+2를 얻습니다.'
        self.type = 'Pirate'
        self.name = '황금 애호가'
        self.name_eng = 'Goldgrubber'
        self.attack = 2
        self.health = 2
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
        