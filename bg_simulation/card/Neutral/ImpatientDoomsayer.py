from ..Card import Card

class ImpatientDoomsayer(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '복수 (3): 무작위 악마를 내 손으로 가져옵니다.'
        self.type = 'Neutral'
        self.name = '성급한 파멸의 예언자 '
        self.name_eng = 'Impatient Doomsayer'
        self.attack = 2
        self.health = 6
        self.tier = 3
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
        