from ..Card import Card

class RipsnarlCaptain(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '다른 아군 해적이 공격할 때마다 그 해적에게 +2/+2를 부여합니다.'
        self.type = 'Pirate'
        self.name = '선장 으르렁니'
        self.name_eng = 'Ripsnarl Captain'
        self.attack = 4
        self.health = 5
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
        