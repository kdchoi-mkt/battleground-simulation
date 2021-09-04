from ..Card import Card

class SeafoodSlinger(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '전투의 함성: 멀록을 황금 멀록으로 만듭니다.'
        self.type = 'Neutral'
        self.name = '해산물 투척꾼'
        self.name_eng = 'Seafood Slinger'
        self.attack = 5
        self.health = 10
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
        self.battle_cry = True
        self.available_in_shop = True
        self.death_rattle_list = self.set_death_rattle_list()
        