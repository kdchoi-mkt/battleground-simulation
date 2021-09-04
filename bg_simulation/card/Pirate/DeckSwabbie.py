from ..Card import Card

class DeckSwabbie(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '전투의 함성: 밥의 선술집을 강화하는 비용이 (1) 감소합니다.'
        self.type = 'Pirate'
        self.name = '갑판 청소부'
        self.name_eng = 'Deck Swabbie'
        self.attack = 2
        self.health = 2
        self.tier = 1
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
        