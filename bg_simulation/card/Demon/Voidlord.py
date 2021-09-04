from ..Card import Card

class Voidlord(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '도발, 죽음의 메아리: 도발 능력이 있는 1/3 악마를 셋 소환합니다.'
        self.type = 'Demon'
        self.name = '공허 군주'
        self.name_eng = 'Voidlord'
        self.attack = 3
        self.health = 9
        self.tier = 5
        self.live = True
        self.taunt = True
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
        