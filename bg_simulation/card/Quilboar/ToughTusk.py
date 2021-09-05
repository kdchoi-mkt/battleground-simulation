from ..Card import Card


class ToughTusk(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = "이 하수인에게 혈석을 낸 후에, 다음 전투 동안 천상의 보호막을 얻습니다."
        self.type = "Quilboar"
        self.name = "튼튼엄니"
        self.name_eng = "Tough Tusk"
        self.attack = 4
        self.health = 3
        self.tier = 2
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
