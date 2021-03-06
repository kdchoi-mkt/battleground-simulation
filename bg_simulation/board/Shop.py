from .constant import TYPE_LIST, TYPE_MATCHER, TIER_REROLL_MAX, TIER_COIN
import random


class Shop(object):
    def __init__(self, ban_type=random.sample(TYPE_LIST, 3)):
        self.tier = 1
        self.upgrade_cost = TIER_COIN[self.tier]
        self.banned_type(ban_type)
        self.reroll_minion()
        self.is_freeze = False

    def freeze(self):
        self.is_freeze = True

    def unfreeze(self):
        self.is_freeze = False

    def decrease_cost(self):
        self.upgrade_cost -= 1
        if self.upgrade_cost < 0:
            self.upgrade_cost = 0

    def banned_type(self, ban_type):
        self.ban_type = ban_type
        self.allow_type = {
            type: TYPE_MATCHER[type]
            for type in TYPE_MATCHER
            if type not in self.ban_type
        }

    def get_accessible_minion(self):
        accessible = list()

        for type in self.allow_type:
            for card in self.allow_type[type].minion_group.values():
                if (card().get_tier() <= self.tier) and (card().is_available_in_shop()):
                    accessible.append(card())

        return accessible

    def reroll_minion(self):
        accessible_minion = self.get_accessible_minion() * 3
        minion_max = TIER_REROLL_MAX[self.tier]

        self.available_minion = random.sample(accessible_minion, minion_max)
        return self.available_minion

    def upgrade_tier(self):
        self.tier += 1
        if self.tier > 6:
            self.tier = 6

        self.increase_level_coin = TIER_COIN[self.tier]

    def turn_end(self):
        self.decrease_cost()

        if self.is_freeze == True:
            self.unfreeze()
        else:
            self.reroll_minion()

    def get_upgrade_cost(self):
        return self.upgrade_cost

    def show_shop_info(self):
        return f"Tier: {self.tier}, Upgrade Cost: {self.upgrade_cost}\nSelling Minion: {self.available_minion}"

    def __str__(self):
        return (
            f"Tier: {self.tier}, \n"
            + f"Pay for Next Level: {self.upgrade_cost}\n"
            + f"Banned Type: {self.ban_type}\n"
            + f"Allowed Type: {list(self.allow_type.keys())}\n"
            + f"Available Minion: {self.available_minion}"
        )

    def __repr__(self):
        return (
            f"Tier: {self.tier}, \n"
            + f"Pay for Next Level: {self.upgrade_cost}\n"
            + f"Banned Type: {self.ban_type}\n"
            + f"Allowed Type: {list(self.allow_type.keys())}\n"
            + f"Available Minion: {self.available_minion}"
        )
