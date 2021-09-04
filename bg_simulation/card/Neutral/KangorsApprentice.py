from ..Card import Card


class KangorsApprentice(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '죽음의 메아리: 이번 전투에서 가장 먼저 죽은 아군 기계 둘을 소환합니다.'
        self.type = 'Neutral'
        self.name = '칸고르의 수습생'
        self.name_eng = 'Kangors Apprentice'
        self.attack = 3
        self.health = 6
        self.tier = 5
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
        self.dead_mech = list()

    def when_dead(self, mine, opponent, dead):
        if dead.get_type() == 'Mech':
            self.dead_mech.append(dead)

    def _summon_dead_mech(self, mine, opponent):
        index = mine.get_card_list().index(self)
        for card in self.dead_mech[:2]:
            # print(card)
            card.reset()
            self._summon_card(mine, card, index)

    def set_death_rattle_list(self) -> list:
        return [
            self._summon_dead_mech
        ]
