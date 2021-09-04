from ..Card import Card

class ReanimatingRattler(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '전투의 함성: 아군 야수에게 환생을 부여합니다.'
        self.type = 'Beast'
        self.name = '되살리는 방울뱀'
        self.name_eng = 'Reanimating Rattler '
        self.attack = 6
        self.health = 2
        self.tier = 4
        self.live = True
        self.taunt = False
        self.divine_shield = False
        self.windfury = False
        self.reborn = True
        self.frenzy = False
        self.poison = False
        self.avenge = False
        self.avenge_count = 0
        self.death_rattle = False
        self.battle_cry = True
        self.available_in_shop = True
        self.death_rattle_list = self.set_death_rattle_list()
        