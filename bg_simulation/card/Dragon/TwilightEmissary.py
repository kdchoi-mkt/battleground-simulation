from ..Card import Card

class TwilightEmissary(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '도발, 전투의 함성: 아군 용족에게 +2/+2를 부여합니다.'
        self.type = 'Dragon'
        self.name = '황혼의 사절'
        self.name_eng = 'Twilight Emissary'
        self.attack = 4
        self.health = 4
        self.tier = 3
        self.live = True
        self.taunt = True
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
        