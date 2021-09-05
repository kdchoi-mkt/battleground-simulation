from ..Card import Card


class BristlebackKnight(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = "질풍, 천상의 보호막, 광폭: 천상의 보호막을 얻습니다."
        self.type = "Quilboar"
        self.name = "뾰족털 기사"
        self.name_eng = "Bristleback Knight"
        self.attack = 4
        self.health = 8
        self.tier = 5
        self.live = True
        self.taunt = False
        self.divine_shield = True
        self.windfury = True
        self.reborn = False
        self.frenzy = False
        self.poison = False
        self.avenge = False
        self.avenge_count = 0
        self.death_rattle = False
        self.battle_cry = False
        self.available_in_shop = True
        self.death_rattle_list = self.set_death_rattle_list()

    def trigger_frenzy(self):
        self.set_divine_shield(True)
