class Board(object):
    """Board Object integrates `Player` and `Shop`"""

    def __init__(self, player, shop):
        self.player = player
        self.shop = shop
        self.max_coin = 3
        self.minion_cost = 3
        self.reroll_cost = 1
        self.hand = list()

    def upgrade_tier(self):
        if self.player.get_coin() >= self.shop.get_upgrade_cost():
            self.player.decrease_coin(self.shop.get_upgrade_cost())
            self.player.upgrade_tier()
            self.shop.upgrade_tier()

    def reroll_item(self):
        if self.player.get_coin() >= self.reroll_cost:
            self.shop.reroll_minion()
            self.player.decrease_coin(self.reroll_cost)

    def purchase_item(self, index):
        if index in range(0, len(self.shop.available_minion)):
            if self.player.get_coin() >= self.minion_cost:
                self.hand.append(self.shop.available_minion.pop(index))
                self.player.decrease_coin(self.minion_cost)

    def hand_to_field(self, hand_index, field_index):
        if (
            hand_index in range(0, len(self.hand))
            and field_index in range(0, self.player.get_card_num() + 1)
            and self.player.get_card_num() < 7
        ):
            card = self.hand.pop(hand_index)
            # 전투의 함성은 소환 전 / 후로 나뉨
            card.trigger_before_battle_cry(self.player, field_index)
            self.player.card_list.insert(field_index, card)
            card.trigger_after_battle_cry(self.player)

    def freeze_shop(self):
        self.shop.freeze()

    def unfreeze_shop(self):
        self.shop.unfreeze()

    def turn_end(self):
        self._adjust_coin()
        self.shop.turn_end()

    def get_player(self):
        return self.player

    def _adjust_coin(self):
        self.max_coin += 1
        if self.max_coin > 10:
            self.max_coin = 10
        self.player.set_coin(self.max_coin)

    def __repr__(self):
        return f"Shop) \n{self.shop.show_shop_info()}\n\
=========================================\n\
Field) \n{self.player.show_field_info()}"
