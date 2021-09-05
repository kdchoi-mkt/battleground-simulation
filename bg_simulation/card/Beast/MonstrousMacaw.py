from ..Card import Card
import random


class MonstrousMacaw(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = "이 하수인이 공격한 후에, 무작위 아군 하수인의 죽음의 메아리 능력을 발동시킵니다."
        self.type = "Beast"
        self.name = "괴물 앵무"
        self.name_eng = "Monstrous Macaw"
        self.attack = 5
        self.health = 3
        self.tier = 3
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
        self.battle_cry = False
        self.available_in_shop = True
        self.death_rattle_list = self.set_death_rattle_list()

    def when_this_attack(self, mine: "Player", opponent: "Player", targeted: Card):
        death_rattle_minion = [
            card
            for card in mine.get_live_card_list()
            if len(card.death_rattle_list) > 0
        ]
        if len(death_rattle_minion) > 0:
            death_rattle = random.choice(death_rattle_minion)
            death_rattle.trigger_death_rattle(mine, opponent)
