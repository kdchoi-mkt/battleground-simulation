from ..Card import Card


class RockpoolHunter(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = "전투의 함성: 아군 멀록에게 +1/+1을 부여합니다."
        self.type = "Murloc"
        self.name = "바위웅덩이 사냥꾼"
        self.name_eng = "Rockpool Hunter"
        self.attack = 2
        self.health = 3
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

    def trigger_before_battle_cry(self, mine, index):
        if mine.get_live_card_num() > 0:
            card = mine.get_live_card(index)
            if card.get_type() == "Murloc":
                card.gain_health(1)
                card.gain_attack(1)
