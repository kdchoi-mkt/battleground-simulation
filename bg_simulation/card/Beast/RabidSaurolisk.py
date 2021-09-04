from ..Card import Card


class RabidSaurolisk(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = "내가 죽음의 메아리 하수인을 낸 후에, +1/+2를 얻습니다."
        self.type = "Beast"
        self.name = "광적인 사우로리스크"
        self.name_eng = "Rabid Saurolisk"
        self.attack = 3
        self.health = 2
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

    def when_summon(self, mine, targeted):
        if targeted.has_death_rattle == True:
            self.gain_attack(1)
            self.gain_health(2)
