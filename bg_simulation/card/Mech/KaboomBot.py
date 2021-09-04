from ..Card import Card


class KaboomBot(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = "죽음의 메아리: 무작위 적 하수인에게 피해를 4 줍니다."
        self.type = "Mech"
        self.name = "콰광로봇"
        self.name_eng = "Kaboom Bot"
        self.attack = 2
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
        self.death_rattle = True
        self.battle_cry = False
        self.available_in_shop = True
        self.death_rattle_list = self.set_death_rattle_list()

    def _attack_randomly(self, mine, opponent):
        if opponent.get_live_card_num() > 0:
            card = opponent.get_live_card()
            card.lose_health(4)
            card.trigger_dead()
