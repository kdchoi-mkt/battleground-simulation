from ..Card import Card


class HolyMecherel(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = "다른 아군 하수인이 천상의 보호막을 잃은 후에, 천상의 보호막을 얻습니다."
        self.type = "Mech"
        self.name = "천상의 기계멀록"
        self.name_eng = "Holy Mecherel"
        self.attack = 8
        self.health = 4
        self.tier = 5
        self.live = True
        self.taunt = False
        self.divine_shield = True
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

    def when_lose_ds(self, mine: "Player", opponent: "Player", targeted: Card):
        if targeted != self:
            self.set_divine_shield(True)
