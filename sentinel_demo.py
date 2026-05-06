#!/usr/bin/env python3

from typing import List
from narrative_core import ThemeEngine, PlotActions, NarrativeState
from worlds import (
    ShadowMetropolis,
    StellarOdyssey,
    AncientKingdom,
)
from characters import (
    HeroCharacter,
    AntiheroCharacter,
    MentorCharacter,
    TricksterCharacter,
)
from story_generator import StoryEngine, StoryPlot, StoryVisualizer


class InteractiveStorySimulator:

    @staticmethod
    def run_shadow_metropolis_demo() -> None:
        StoryVisualizer.print_header("DEMO: SHADOW METROPOLIS")

        world = ShadowMetropolis()
        hero = HeroCharacter(name="Alex")
        trickster = TricksterCharacter(name="MysteriousGuide")

        engine = StoryEngine(world, [hero, trickster], theme="noir")
        narrative = engine.generate_story(episodes=3)

        StoryVisualizer.print_narrative(narrative)

    @staticmethod
    def run_stellar_odyssey_demo() -> None:
        StoryVisualizer.print_header("DEMO: STELLAR ODYSSEY")

        world = StellarOdyssey()
        hero = HeroCharacter(name="Commander")
        mentor = MentorCharacter(name="AncientOne")

        engine = StoryEngine(world, [hero, mentor], theme="sci-fi")
        narrative = engine.generate_story(episodes=4)

        StoryVisualizer.print_narrative(narrative)

    @staticmethod
    def run_ancient_kingdom_demo() -> None:
        StoryVisualizer.print_header("DEMO: ANCIENT KINGDOM")

        world = AncientKingdom()
        hero = HeroCharacter(name="Warrior")
        antihero = AntiheroCharacter(name="Rogue")

        engine = StoryEngine(world, [hero, antihero], theme="fantasy")
        narrative = engine.generate_story(episodes=5)

        StoryVisualizer.print_narrative(narrative)


if __name__ == "__main__":
    InteractiveStorySimulator.run_shadow_metropolis_demo()
