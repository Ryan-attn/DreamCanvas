#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
from typing import List, Optional
from agent_core import (
    Character,
    PlotActionType,
    PlotActions,
    ThemePerception,
)


class HeroCharacter(Character):
    CHARACTER_TYPE = "hero"

    def __init__(self, name: str = "Hero"):
        super().__init__(name)
        self._morality_score = 85
        self._courage_score = 80

    @property
    def character_type(self) -> str:
        return self.CHARACTER_TYPE

    @property
    def courage_score(self) -> int:
        return self._courage_score

    def make_choice(self, perception: ThemePerception) -> PlotActionType:
        if perception.mood == "dark":
            return PlotActionType.FIGHT
        elif perception.mood == "suspenseful":
            return PlotActionType.QUEST
        else:
            return PlotActionType.QUEST


class AntiheroCharacter(Character):
    CHARACTER_TYPE = "antihero"

    def __init__(self, name: str = "Antihero"):
        super().__init__(name)
        self._morality_score = 45
        self._conflict_score = 70

    @property
    def character_type(self) -> str:
        return self.CHARACTER_TYPE

    @property
    def conflict_score(self) -> int:
        return self._conflict_score

    def make_choice(self, perception: ThemePerception) -> PlotActionType:
        if random.random() > 0.5:
            return PlotActionType.BETRAY
        elif perception.mood == "dark":
            return PlotActionType.MYSTERY
        else:
            return PlotActionType.REVEAL


class MentorCharacter(Character):
    CHARACTER_TYPE = "mentor"

    def __init__(self, name: str = "Mentor"):
        super().__init__(name)
        self._morality_score = 90
        self._wisdom_score = 95

    @property
    def character_type(self) -> str:
        return self.CHARACTER_TYPE

    @property
    def wisdom_score(self) -> int:
        return self._wisdom_score

    def make_choice(self, perception: ThemePerception) -> PlotActionType:
        return PlotActionType.QUEST


class TricksterCharacter(Character):
    CHARACTER_TYPE = "trickster"

    def __init__(self, name: str = "Trickster"):
        super().__init__(name)
        self._morality_score = 55
        self._chaos_score = 75

    @property
    def character_type(self) -> str:
        return self.CHARACTER_TYPE

    @property
    def chaos_score(self) -> int:
        return self._chaos_score

    def make_choice(self, perception: ThemePerception) -> PlotActionType:
        return PlotActionType.REVEAL


class ShadowCharacter(Character):
    CHARACTER_TYPE = "shadow"

    def __init__(self, name: str = "Shadow"):
        super().__init__(name)
        self._morality_score = 15
        self._fear_score = 60

    @property
    def character_type(self) -> str:
        return self.CHARACTER_TYPE

    def make_choice(self, perception: ThemePerception) -> PlotActionType:
        return PlotActionType.BETRAY


class ShapeshifterCharacter(Character):
    CHARACTER_TYPE = "shapeshifter"

    def __init__(self, name: str = "Shapeshifter"):
        super().__init__(name)
        self._morality_score = 50
        self._identity_score = 50

    @property
    def character_type(self) -> str:
        return self.CHARACTER_TYPE

    def make_choice(self, perception: ThemePerception) -> PlotActionType:
        return PlotActionType.MYSTERY
