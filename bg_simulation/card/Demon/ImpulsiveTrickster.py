from ..Card import Card


class ImpulsiveTrickster(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = "죽음의 메아리: 아군 하수인에게 이 하수인의 최대 생명력을 부여합니다."
        self.type = "Demon"
        self.name = "충동적인 마귀"
        self.name_eng = "Impulsive Trickster "
        self.attack = 2
        self.health = 2
        self.original_health = 2
        self.tier = 1
        self.live = True
        self.taunt = False
        self.divine_shield = False
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

    def gain_health(self, health):
        Card.gain_health(health)
        self.original_health += health

    def _give_health(self, mine, opponent):
        if mine.get_live_card_num() > 0:
            card = mine.get_live_card()
            card.gain_health(self.original_health)

    def set_death_rattle_list(self) -> list:
        return [self._give_health]
