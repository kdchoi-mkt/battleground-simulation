from ..Card import Card


class SelflessHero(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = "죽음의 메아리: 무작위 아군 하수인에게 천상의 보호막을 부여합니다."
        self.type = "Neutral"
        self.name = "헌신적인 영웅"
        self.name_eng = "Selfless Hero"
        self.attack = 2
        self.health = 1
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
        self.death_rattle = True
        self.battle_cry = False
        self.available_in_shop = True
        self.death_rattle_list = self.set_death_rattle_list()

    def _give_ds(self, mine, opponent):
        if mine.get_live_card_num() > 0:
            card = mine.get_live_card()
            card.set_divine_shield(True)

    def set_death_rattle_list(self) -> list:
        return [self._give_ds]
