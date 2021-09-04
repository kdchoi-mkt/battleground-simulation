from ..Card import Card

class Bannerboar(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '내 턴이 끝날 때, 양옆의 가시멧돼지에게 혈석을 냅니다.'
        self.type = 'Quilboar'
        self.name = '깃발멧돼지'
        self.name_eng = 'Bannerboar '
        self.attack = 1
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
        