from ..Card import Card

class KingBagurgle(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '전투의 함성과 죽음의 메아리: 내 다른 멀록들에게 +2/+2를 부여합니다.'
        self.type = 'Murloc'
        self.name = '왕 므라옳옳'
        self.name_eng = 'King Bagurgle'
        self.attack = 6
        self.health = 3
        self.tier = 5
        self.live = True
        self.taunt = False
        self.divine_shield = False
        self.windfury = False
        self.reborn = False
        self.frenzy = False
        self.poison = False
        self.avenge = False
        self.avenge_count = 0
        self.death_rattle = True
        self.battle_cry = False
        self.available_in_shop = True
        self.death_rattle_list = self.set_death_rattle_list()
        