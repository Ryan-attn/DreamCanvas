#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Dict, List, Optional
from agent_core import (
    PlotActions,
    Character,
    NarrativeState,
    NarrativeResult,
    StoryWorld,
    ThemeEngine,
    ThemePerception,
)


class ShadowMetropolis(StoryWorld):
    WORLD_TYPE = "urban"
    SETTING = "ShadowMetropolis"

    LOCATIONS = ["Downtown", "Harbor", "Uptown", "Slums", "Rooftops"]

    def __init__(
        self,
        start_location: str = "Downtown",
        initial_tension: int = 0
    ):
        state = NarrativeState(
            location=start_location,
            tension_level=initial_tension,
            story_phase="introduction"
        )
        super().__init__(state, ThemeEngine("noir"))

    @property
    def world_type(self) -> str:
        return self.WORLD_TYPE

    @property
    def setting(self) -> str:
        return self.SETTING

    def execute_action(self, action: PlotActions) -> NarrativeResult:
        tension_added = PlotActions.get_tension(action)
        new_tension = self._state.tension_level + tension_added

        location_change = self._get_location_change(action)
        new_location = location_change or self._state.location

        new_phase = self._get_next_phase(new_tension)

        new_state = NarrativeState(
            location=new_location,
            tension_level=new_tension,
            story_phase=new_phase
        )
        self._state = new_state

        return NarrativeResult(
            new_state=new_state,
            tension_added=tension_added,
            success=True
        )

    def perceive(self) -> ThemePerception:
        return ThemePerception(
            current_theme=self._theme.current_theme,
            mood=self._theme.get_mood(),
            setting=self._state.location
        )

    def _get_location_change(self, action: PlotActions) -> Optional[str]:
        location_pool = [loc for loc in self.LOCATIONS if loc != self._state.location]
        if action in [PlotActions.QUEST, PlotActions.FIGHT]:
            return location_pool[0] if location_pool else self._state.location
        return None

    def _get_next_phase(self, tension: int) -> str:
        if tension < 5:
            return "introduction"
        elif tension < 15:
            return "rising_action"
        elif tension < 25:
            return "climax"
        else:
            return "conclusion"


class StellarOdyssey(StoryWorld):
    WORLD_TYPE = "space"
    SETTING = "StellarOdyssey"

    LOCATIONS = ["Nebula", "Core", "Port", "Asteroid", "Void", "Station", "Cosmic", "Unknown", "Ancient"]

    def __init__(
        self,
        start_location: str = "Nebula",
        initial_tension: int = 0
    ):
        state = NarrativeState(
            location=start_location,
            tension_level=initial_tension,
            story_phase="departure"
        )
        super().__init__(state, ThemeEngine("sci-fi"))

    @property
    def world_type(self) -> str:
        return self.WORLD_TYPE

    @property
    def setting(self) -> str:
        return self.SETTING

    def execute_action(self, action: PlotActions) -> NarrativeResult:
        tension_added = PlotActions.get_tension(action)
        new_tension = self._state.tension_level + tension_added

        location_pool = [loc for loc in self.LOCATIONS if loc != self._state.location]
        new_location = location_pool[0] if location_pool else self._state.location

        new_phase = self._get_space_phase(new_tension)

        new_state = NarrativeState(
            location=new_location,
            tension_level=new_tension,
            story_phase=new_phase
        )
        self._state = new_state

        return NarrativeResult(
            new_state=new_state,
            tension_added=tension_added,
            success=True
        )

    def perceive(self) -> ThemePerception:
        return ThemePerception(
            current_theme=self._theme.current_theme,
            mood=self._theme.get_mood(),
            setting=self._state.location
        )

    def _get_space_phase(self, tension: int) -> str:
        if tension < 5:
            return "departure"
        elif tension < 15:
            return "journey"
        elif tension < 25:
            return "discovery"
        else:
            return "return"


class AncientKingdom(StoryWorld):
    WORLD_TYPE = "fantasy"
    SETTING = "AncientKingdom"

    LOCATIONS = ["Castle", "Village", "Forest", "Mountain", "Cave", "Temple", "Battlefield", "Dungeon", "Throne"]

    def __init__(
        self,
        start_location: str = "Village",
        initial_tension: int = 0
    ):
        state = NarrativeState(
            location=start_location,
            tension_level=initial_tension,
            story_phase="prologue"
        )
        super().__init__(state, ThemeEngine("fantasy"))

    @property
    def world_type(self) -> str:
        return self.WORLD_TYPE

    @property
    def setting(self) -> str:
        return self.SETTING

    def execute_action(self, action: PlotActions) -> NarrativeResult:
        tension_added = PlotActions.get_tension(action)
        new_tension = self._state.tension_level + tension_added

        location_pool = [loc for loc in self.LOCATIONS if loc != self._state.location]
        new_location = location_pool[0] if location_pool else self._state.location

        new_phase = self._get_fantasy_phase(new_tension)

        new_state = NarrativeState(
            location=new_location,
            tension_level=new_tension,
            story_phase=new_phase
        )
        self._state = new_state

        return NarrativeResult(
            new_state=new_state,
            tension_added=tension_added,
            success=True
        )

    def perceive(self) -> ThemePerception:
        return ThemePerception(
            current_theme=self._theme.current_theme,
            mood=self._theme.get_mood(),
            setting=self._state.location
        )

    def _get_fantasy_phase(self, tension: int) -> str:
        if tension < 5:
            return "prologue"
        elif tension < 15:
            return "rising_action"
        elif tension < 25:
            return "climax"
        else:
            return "epilogue"
