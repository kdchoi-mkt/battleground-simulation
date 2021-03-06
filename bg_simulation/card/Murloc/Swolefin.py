from ..Card import Card


class Swolefin(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = "전투의 함성: 다른 아군 멀록 하나당 +2/+1을 얻습니다."
        self.type = "Murloc"
        self.name = "근육지느러미"
        self.name_eng = "Swolefin"
        self.attack = 4
        self.health = 2
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
        self.battle_cry = True
        self.available_in_shop = True
        self.death_rattle_list = self.set_death_rattle_list()

    def trigger_before_battle_cry(self, mine: "Player", index: int):
        for card in mine.get_card_list():
            if card.get_type() == "Murloc":
                self.gain_attack(2)
                self.gain_health(1)
