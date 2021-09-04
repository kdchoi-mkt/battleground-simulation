from ..Card import Card

class BrinyBootlegger(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '내 턴이 끝날 때, 내 전장에 다른 해적이 있으면 황금 동전을 내 손으로 가져옵니다.'
        self.type = 'Pirate'
        self.name = '짠내 나는 밀수꾼'
        self.name_eng = 'Briny Bootlegger'
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
        self.battle_cry = False
        self.available_in_shop = True
        self.death_rattle_list = self.set_death_rattle_list()
        