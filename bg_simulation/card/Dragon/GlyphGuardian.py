from ..Card import Card


class GlyphGuardian(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = "이 하수인은 공격할 때마다 공격력이 2배가 됩니다."
        self.type = "Dragon"
        self.name = "문양 수호자"
        self.name_eng = "Glyph Guardian"
        self.attack = 2
        self.health = 4
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

    def when_this_attack(self, mine, opponent, target):
        self.gain_attack(self.attack)
