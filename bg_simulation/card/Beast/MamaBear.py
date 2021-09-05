from ..Card import Card


class MamaBear(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = "내가 야수를 소환할 때마다 그 야수에게 +5/+5를 부여합니다."
        self.type = "Beast"
        self.name = "엄마 곰"
        self.name_eng = "Mama Bear"
        self.attack = 5
        self.health = 5
        self.tier = 5
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

    def when_summon(self, mine: "Player", targeted: Card):
        if targeted.get_type() == "Beast":
            targeted.gain_health(5)
            targeted.gain_attack(5)
