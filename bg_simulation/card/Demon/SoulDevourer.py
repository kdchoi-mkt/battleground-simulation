from ..Card import Card

class SoulDevourer(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '전투의 함성: 아군 악마를 선택합니다. 그 악마를 제거하고 그 악마의 능력치와 3골드를 얻습니다.'
        self.type = 'Demon'
        self.name = '영혼 포식자'
        self.name_eng = 'Soul Devourer'
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
        