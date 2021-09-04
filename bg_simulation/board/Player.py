import random


class Player(object):
    def __init__(
        self,
        card_list,
        health: int = 40,
    ):
        # Card List: Set of Card()
        self.card_list = card_list
        self.health = health
        self.live = True
        self.coin = 3
        self.tier = 1

    def lose_health(
        self,
        damage: int,
    ):
        self.health -= damage

        if self.health < 0:
            self.live = False

    def trigger_lose_ds(self, opponent, targeted):
        for card in self.get_live_card_list():
            card.when_lose_ds(self, opponent, targeted)

    def trigger_targeted(self, opponent, targeted):
        for card in self.get_live_card_list():
            card.when_targeted(self, opponent, targeted)

    def trigger_dead(self, opponent, dead):
        for card in self.get_live_card_list():
            card.when_dead(self, opponent, dead)

    def trigger_summon(self, targeted):
        for card in self.get_live_card_list():
            card.when_summon(self, targeted)

    def trigger_start_of_combat(self, opponent):
        for card in self.get_live_card_list():
            card.trigger_start_of_combat(self, opponent)

    def decrease_coin(self, cost):
        self.coin -= cost

    def upgrade_tier(self):
        self.tier += 1
        if self.tier > 6:
            self.tier = 6

    def set_coin(self, coin):
        self.coin = coin

    def get_coin(self):
        return self.coin

    def get_card_num(self):
        return len(self.card_list)

    def get_live_card_num(self):
        return len(self.get_live_card_list())

    def get_taunt_live_card_num(self):
        return len(self.get_live_taunt_card_list())

    def get_card_list(self):
        return self.card_list

    def get_live_card_list(self):
        return [card for card in self.card_list if card.is_live()]

    def get_live_taunt_card_list(self):
        return [card for card in self.get_live_card_list() if card.is_taunt()]

    def get_live_card(self, index=None):
        if index == None:
            return random.choice(self.get_live_card_list())
        else:
            return self.get_live_card_list()[index]

    def attack(self):
        return sum(card.get_tier() for card in self.get_live_card_list()) + self.tier

    def show_field_info(self):
        return f"Health: {self.health}, Coin: {self.coin}\nCard: {self.get_card_list()}"

    def show_live_cards(self):
        live_str = str()
        for card in self.get_live_card_list():
            live_str += f"이름: {card.get_name()}, 공격력: {card.get_attack()}, 체력: {card.get_health()}\n"
        return live_str

    def __repr__(self):
        return f"Health: {self.health}, Card: {self.get_card_num()}\n\
Live Card: {self.get_live_card_list()}"
