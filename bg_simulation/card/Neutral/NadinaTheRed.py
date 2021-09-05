from ..Card import Card


class NadinaTheRed(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = "죽음의 메아리: 내 용족들에게 천상의 보호막을 부여합니다."
        self.type = "Neutral"
        self.name = "홍련의 나디나"
        self.name_eng = "Nadina the Red"
        self.attack = 7
        self.health = 4
        self.tier = 6
        self.live = True
        self.taunt = False
        self.divine_shield = True
        self.windfury = False
        self.reborn = False
        self.frenzy = False
        self.poison = False
        self.avenge = False
        self.avenge_count = 0
        self.death_rattle = True
        self.battle_cry = False
        self.available_in_shop = True
        self.death_rattle_list = self.set_death_rattle_list()

    def _give_ds(self, mine, opponent):
        for card in mine.get_live_card_list():
            if card.get_type() == "Dragon":
                card.set_divine_shield(True)

    def set_death_rattle_list(self) -> list:
        return [self._give_ds]
