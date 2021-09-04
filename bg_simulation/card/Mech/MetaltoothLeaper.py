from ..Card import Card


class MetaltoothLeaper(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = "전투의 함성: 내 다른 기계들에게 공격력을 +2 부여합니다."
        self.type = "Mech"
        self.name = "강철니 표범로봇"
        self.name_eng = "Metaltooth Leaper"
        self.attack = 3
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
        self.battle_cry = True
        self.available_in_shop = True
        self.death_rattle_list = self.set_death_rattle_list()

    def trigger_before_battle_cry(self, mine, index):
        for card in mine.get_card_list():
            if card.get_type() == "Mech":
                card.gain_attack(2)
