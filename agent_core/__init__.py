#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dataclasses import dataclass, field
from typing import Any, List, Optional, Tuple, Dict
from enum import Enum
import random


class PlotActionType(Enum):
    QUEST = "quest"
    BETRAY = "betray"
    REVEAL = "reveal"
    FIGHT = "fight"
    LOVE = "love"
    MYSTERY = "mystery"


@dataclass(frozen=True)
class PlotActions:
    QUEST = PlotActionType.QUEST
    BETRAY = PlotActionType.BETRAY
    REVEAL = PlotActionType.REVEAL
    FIGHT = PlotActionType.FIGHT
    LOVE = PlotActionType.LOVE
    MYSTERY = PlotActionType.MYSTERY

    ALL_ACTIONS = (
        PlotActionType.QUEST,
        PlotActionType.BETRAY,
        PlotActionType.REVEAL,
        PlotActionType.FIGHT,
        PlotActionType.LOVE,
        PlotActionType.MYSTERY,
    )

    @classmethod
    def get_tension(cls, action: PlotActionType) -> int:
        tension_map = {
            PlotActionType.QUEST: 3,
            PlotActionType.BETRAY: 5,
            PlotActionType.REVEAL: 2,
            PlotActionType.FIGHT: 4,
            PlotActionType.LOVE: 2,
            PlotActionType.MYSTERY: 3,
        }
        return tension_map.get(action, 1)

    @classmethod
    def get_description(cls, action: PlotActionType) -> str:
        desc_map = {
            PlotActionType.QUEST: "开启新任务线",
            PlotActionType.BETRAY: "背叛或反转",
            PlotActionType.REVEAL: "揭露隐藏信息",
            PlotActionType.FIGHT: "战斗或冲突",
            PlotActionType.LOVE: "情感发展",
            PlotActionType.MYSTERY: "谜题或线索",
        }
        return desc_map.get(action, "未知动作")


@dataclass(frozen=True)
class NarrativeState:
    location: str
    tension_level: int
    story_phase: str


@dataclass(frozen=True)
class ThemePerception:
    current_theme: str
    mood: str
    setting: str


@dataclass(frozen=True)
class NarrativeResult:
    new_state: NarrativeState
    tension_added: int
    success: bool


class ThemeEngine:
    THEMES = ["noir", "sci-fi", "fantasy", "mystery", "romance"]

    def __init__(self, theme: str = "noir"):
        if theme not in self.THEMES:
            raise ValueError(f"Theme must be one of {self.THEMES}")
        self._current_theme = theme
        self._theme_weights = self._initialize_weights(theme)

    def _initialize_weights(self, theme: str) -> Dict[PlotActionType, float]:
        base_weights = {action: 1.0 for action in PlotActions.ALL_ACTIONS}

        if theme == "noir":
            base_weights[PlotActionType.BETRAY] = 2.0
            base_weights[PlotActionType.REVEAL] = 1.5
        elif theme == "sci-fi":
            base_weights[PlotActionType.QUEST] = 2.0
            base_weights[PlotActionType.MYSTERY] = 1.5
        elif theme == "fantasy":
            base_weights[PlotActionType.FIGHT] = 2.0
            base_weights[PlotActionType.LOVE] = 1.5
        elif theme == "mystery":
            base_weights[PlotActionType.REVEAL] = 2.5
            base_weights[PlotActionType.MYSTERY] = 2.0
        elif theme == "romance":
            base_weights[PlotActionType.LOVE] = 3.0
            base_weights[PlotActionType.QUEST] = 1.5

        return base_weights

    @property
    def current_theme(self) -> str:
        return self._current_theme

    def select_plot_action(self) -> PlotActionType:
        actions = list(PlotActions.ALL_ACTIONS)
        weights = [self._theme_weights[a] for a in actions]
        return random.choices(actions, weights=weights)[0]

    def get_mood(self) -> str:
        mood_map = {
            "noir": "dark",
            "sci-fi": "futuristic",
            "fantasy": "magical",
            "mystery": "suspenseful",
            "romance": "emotional",
        }
        return mood_map.get(self._current_theme, "neutral")


class StoryWorld:
    def __init__(
        self,
        initial_state: NarrativeState,
        theme_engine: Optional[ThemeEngine] = None
    ):
        self._state = initial_state
        self._theme = theme_engine or ThemeEngine()

    @property
    def state(self) -> NarrativeState:
        return self._state

    @property
    def tension_level(self) -> int:
        return self._state.tension_level

    def get_theme(self) -> str:
        return self._theme.current_theme

    def execute_action(self, action: PlotActionType) -> NarrativeResult:
        raise NotImplementedError

    def perceive(self) -> ThemePerception:
        raise NotImplementedError


class Character:
    def __init__(self, name: str = "Character"):
        self.name = name
        self._morality_score = 50
        self._current_location = "unknown"

    @property
    def morality_score(self) -> int:
        return self._morality_score

    @property
    def current_location(self) -> str:
        return self._current_location

    def set_location(self, location: str) -> None:
        self._current_location = location

    def update_morality(self, delta: int) -> None:
        self._morality_score = max(0, min(100, self._morality_score + delta))

    def make_choice(self, perception: ThemePerception) -> PlotActionType:
        raise NotImplementedError
