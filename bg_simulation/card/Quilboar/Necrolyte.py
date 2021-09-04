from ..Card import Card

class Necrolyte(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '전투의 함성: 아군 하수인을 선택합니다. 그 하수인이 자신의 양옆에 있는 하수인들의 혈석을 모두 가져옵니다.'
        self.type = 'Quilboar'
        self.name = '강령사'
        self.name_eng = 'Necrolyte '
        self.attack = 3
        self.health = 3
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
        