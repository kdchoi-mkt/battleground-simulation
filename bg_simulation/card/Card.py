from __future__ import annotations
import random


class Card(object):
    def __init__(self):
        self.reset()
        self.set_dict = {
            "attack": self.set_attack,
            "health": self.set_health,
            "tier": self.set_tier,
            "taunt": self.set_taunt,
            "divine_shield": self.set_divine_shield,
            "windfury": self.set_windfury,
            "reborn": self.set_reborn,
            "frenzy": self.set_frenzy,
            "poison": self.set_poison,
            "avenge": self.set_avenge,
        }

    def reset(self):
        self.type = "None"
        self.name = "None"
        self.name_eng = "None"
        self.text = ""
        self.attack = 1
        self.health = 1
        self.tier = 1
        self.live = True
        self.taunt = False
        self.divine_shield = False
        self.windfury = False
        self.reborn = False
        self.frenzy = False
        self.poison = False
        self.avenge = 0
        self.avenge_count = 0
        self.death_rattle = False
        self.battle_cry = False
        self.available_in_shop = True
        self.death_rattle_list = self.set_death_rattle_list()

    def set_death_rattle_list(self) -> list:
        return list()

    def when_lose_ds(self, mine, opponent, targeted: Card):
        """아군 하수인이 천상의 보호막을 잃은 후에"""
        pass

    def when_targeted(self, mine, opponent, targeted: Card):
        """아군 하수인이 공격 할 때"""
        pass

    def when_dead(self, mine, opponent, dead: Card):
        """아군 하수인이 죽은 후에"""
        pass

    def when_summon(self, mine, targeted):
        """아군을 소환한 후에"""
        pass

    def get_type(self):
        return self.type

    def get_name(self):
        return self.name

    def battle(self, target, mine, opponent):
        opponent.trigger_targeted(mine, target)

        target.lose_health(self, opponent, mine)
        self.lose_health(target, mine, opponent)

        self.trigger_dead(mine, opponent)
        target.trigger_dead(opponent, mine)

    def trigger_dead(self, mine, opponent):
        if self.live == False:
            self.trigger_death_rattle(mine, opponent)
            mine.trigger_dead(opponent, self)

            if self.reborn == True:
                self.reset()
                self.health = 1
                self.reborn = False

    def lose_health(self, attacker, mine, opponent):
        if self.divine_shield == True:
            self.divine_shield = False
            mine.trigger_lose_ds(opponent, self)
        else:
            if type(attacker) == int:
                self.health -= attacker
            elif attacker.is_poison() == True:
                self.health = 0
            else:
                self.health -= attacker.get_attack()

            if self.health <= 0:
                self.live = False
            else:
                if self.frenzy == True:
                    self.trigger_frenzy(self)

    def gain_health(self, health):
        self.health += health

    def trigger_frenzy(self):
        pass

    def get_text(self):
        return self.text

    def gain_attack(self, damage):
        self.attack += damage

    def set_health(self, health):
        self.health = health

    def set_attack(self, attack):
        self.attack = attack

    def get_health(self):
        return self.health

    def get_attack(self):
        return self.attack

    def set_tier(self, tier):
        self.tier = tier

    def get_tier(self):
        return self.tier

    def is_live(self):
        return self.live

    def is_taunt(self):
        return self.taunt

    def set_taunt(self, taunt):
        self.taunt = taunt

    def is_windfury(self):
        return self.windfury

    def set_windfury(self, windfury):
        self.windfury = windfury

    def is_divine_shield(self):
        return self.divine_shield

    def set_divine_shield(self, divine_shield):
        self.divine_shield = divine_shield

    def is_reborn(self):
        return self.is_reborn

    def set_reborn(self, reborn):
        self.is_reborn = reborn

    def set_frenzy(self, frenzy):
        self.frenzy = frenzy

    def set_poison(self, poison):
        self.poison = poison

    def set_avenge(self, avenge):
        self.avenge = avenge

    def get_avenge(self):
        """Return X for Avenge (X): blank"""
        return self.avenge

    def is_poison(self):
        return self.poison

    def is_death_rattle(self):
        return self.death_rattle

    def is_battle_cry(self):
        return self.battle_cry

    def is_available_in_shop(self):
        return self.available_in_shop

    def trigger_death_rattle(self, mine, opponent):
        for death_rattle in self.death_rattle_list:
            death_rattle(mine, opponent)

    def trigger_before_battle_cry(self, mine, index):
        pass

    def trigger_after_battle_cry(self, mine):
        pass

    def trigger_start_of_combat(self, mine, opponent):
        """기선 제압: 전투 시작 전에 한 번 효과 발동"""
        pass

    def __str__(self):
        return f"<Name: {self.name}, Type: {self.type}, Attack: {self.attack}, Health: {self.health}, Text: {self.text}>\n"

    def __repr__(self):
        return f"<Name: {self.name}, Type: {self.type}, Attack: {self.attack}, Health: {self.health}, Text: {self.text}>\n"

    def _randomly_choose(self, size):
        return random.randint(0, size - 1)

    def _summon_card(self, mine, card, index):
        if mine.get_live_card_num() < 7:
            mine.get_card_list().insert(index + 1, card)
            mine.trigger_summon(card)
            return True

        return False

    def set_ability(self, attack, health, **kwarg):
        self.attack = attack
        self.health = health

        for item in kwarg:
            self._check_keyword(item, kwarg[item])

        return self

    def _check_keyword(self, keyword, revise):
        if keyword in self.set_dict:
            self.set_dict[keyword](revise)
