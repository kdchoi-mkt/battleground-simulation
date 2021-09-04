from ..card.Mech import DeflectoBot, GreaseBot, HarvestGolem, Pupbot, MechanoEgg, OmegaBuster
from ..card.All import Amalgadon
from ..card.Neutral import KangorsApprentice
from ..board import Player

# The example is from https://www.youtube.com/watch?v=0z2LHdBiFOs, 10:35
# Note that the Golden Minion is not implemented yet.


class Opponent(Player):
    def __init__(self):
        self.card_list = [
            DeflectoBot().set_ability(4, 3),
            DeflectoBot().set_ability(4, 3),
            HarvestGolem().set_ability(4, 4, taunt=True),
            Pupbot().set_ability(16, 9),
            HarvestGolem().set_ability(
                11, 12, taunt=True, divine_shield=True),
            GreaseBot().set_ability(4, 6),
            GreaseBot().set_ability(3, 6)
        ]
        self.health = 9
        self.live = True
        self.coin = 3
        self.tier = 6


class Mine(Player):
    def __init__(self):
        self.card_list = [
            OmegaBuster().set_ability(8, 10, taunt=True, divine_shield=True),
            DeflectoBot().set_ability(6, 4),
            DeflectoBot().set_ability(11, 7),
            MechanoEgg().set_ability(0, 10),
            Amalgadon().set_ability(19, 21, poison=True, divine_shield=True, windfury=True, ),
            Amalgadon().set_ability(10, 7),
            KangorsApprentice()
        ]
        self.health = 1
        self.live = True
        self.coin = 3
        self.tier = 6
