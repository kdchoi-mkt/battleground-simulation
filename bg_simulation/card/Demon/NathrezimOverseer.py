from ..Card import Card


class NathrezimOverseer(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = "전투의 함성: 아군 악마에게 +2/+2를 부여합니다."
        self.type = "Demon"
        self.name = "나스레짐 감독관"
        self.name_eng = "Nathrezim Overseer"
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
        self.battle_cry = True
        self.available_in_shop = True
        self.death_rattle_list = self.set_death_rattle_list()

    def trigger_before_battle_cry(self, mine, index):
        if mine.get_live_card_num() > 0:
            card = mine.get_live_card(index)
            if card.get_type() == "Demon":
                card.gain_health(2)
                card.gain_attack(2)
