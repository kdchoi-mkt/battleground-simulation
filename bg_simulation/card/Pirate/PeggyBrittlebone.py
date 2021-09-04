from ..Card import Card

class PeggyBrittlebone(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '내 손으로 카드를 가져온 후에, 다른 무작위 해적에게 +1/+1을 부여합니다.'
        self.type = 'Pirate'
        self.name = '허드렛일 약골'
        self.name_eng = 'Peggy Brittlebone'
        self.attack = 5
        self.health = 3
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
        