from ..Card import Card


class UnstableGhoul(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = "도발. 죽음의 메아리: 모든 하수인에게 피해를 1 줍니다."
        self.type = "Neutral"
        self.name = "불안정한 구울"
        self.name_eng = "Unstable Ghoul"
        self.attack = 1
        self.health = 3
        self.tier = 2
        self.live = True
        self.taunt = True
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

    def _hurricane(self, mine, opponent):
        for card in opponent.get_live_card_list():
            card.lose_health(1)

        for card in mine.get_live_card_list():
            card.lose_health(1)

        for card in opponent.get_live_card_list():
            card.trigger_dead(opponent, mine)

        for card in mine.get_live_card_list():
            card.trigger_dead(mine, opponent)
