from ..Card import Card

class CobaltScalebane(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '내 턴이 끝날 때, 다른 무작위 아군 하수인에게 공격력을 +3 부여합니다.'
        self.type = 'Dragon'
        self.name = '푸른비늘혈족 맹독전사'
        self.name_eng = 'Cobalt Scalebane'
        self.attack = 5
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
        