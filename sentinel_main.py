#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

        scenarios = [
            ("ShadowMetropolis", ShadowMetropolis, [
                HeroCharacter,
                TricksterCharacter,
            ]),
        ]

        for world_name, world_class, character_classes in scenarios:
            world = world_class()
            print(f"\n{world_name} with characters:")

            narratives: List[StoryPlot] = []
            for character_class in character_classes:
                character = character_class(name=f"Hero_{character_class.__name__}")
                story_engine = StoryEngine(world, [character], theme="noir")
                narrative = story_engine.generate_story(episodes=3)
                narratives.append(narrative)
                world = world_class()

            StoryVisualizer.print_narrative_comparison(narratives)

    @staticmethod
    def run_stellar_odyssey_demo() -> None:
        StoryVisualizer.print_header("DEMO: STELLAR ODYSSEY")

        world = StellarOdyssey()
        character_classes = [
            HeroCharacter,
            MentorCharacter,
        ]

        narratives: List[StoryPlot] = []
        for character_class in character_classes:
            world = StellarOdyssey()
            character = character_class(name=f"Space_{character_class.__name__}")
            story_engine = StoryEngine(world, [character], theme="sci-fi")
            narrative = story_engine.generate_story(episodes=4)
            narratives.append(narrative)

        StoryVisualizer.print_narrative_comparison(narratives)

    @staticmethod
    def run_ancient_kingdom_demo() -> None:
        StoryVisualizer.print_header("DEMO: ANCIENT KINGDOM")

        character_classes = [
            HeroCharacter,
            AntiheroCharacter,
        ]

        narratives: List[StoryPlot] = []
        for character_class in character_classes:
            world = AncientKingdom()
            character = character_class(name=f"Legend_{character_class.__name__}")
            story_engine = StoryEngine(world, [character], theme="fantasy")
            narrative = story_engine.generate_story(episodes=5)
            narratives.append(narrative)

        StoryVisualizer.print_narrative_comparison(narratives)

    @staticmethod
    def run_theme_comparison_demo() -> None:
        StoryVisualizer.print_header("THEME COMPARISON: ALL GENRES")

        themes = ["noir", "sci-fi", "fantasy", "mystery"]

        for theme_name in themes:
            world = ShadowMetropolis()
            hero = HeroCharacter(name="TestHero")
            trickster = TricksterCharacter(name="TestTrickster")

            engine = StoryEngine(world, [hero, trickster], theme=theme_name)
            narrative = engine.generate_story(episodes=3)

            print(f"\nTheme: {theme_name.upper()}")
            StoryVisualizer.print_narrative(narrative)

    @staticmethod
    def run_branching_demo() -> None:
        StoryVisualizer.print_header("BRANCHING NARRATIVE DEMO")

        world = ShadowMetropolis()
        hero = HeroCharacter(name="BranchHero")
        antihero = AntiheroCharacter(name="BranchAntihero")

        engine = StoryEngine(world, [hero, antihero], theme="noir", branching=True)
        narrative = engine.generate_story(episodes=6)

        print(f"\nBranching Story: {narrative.title}")
        StoryVisualizer.print_full_narrative(narrative)


def run_all_demos() -> None:
    print("\n" + "=" * 70)
    print("DREAMCANVAS STORY GENERATION DEMOS")
    print("=" * 70)

    demo_shadow_metropolis()
    demo_stellar_odyssey()
    demo_ancient_kingdom()
    demo_themes()
    demo_branching_narrative()

    print("\n" + "=" * 70)
    print("ALL DEMOS COMPLETED")
    print("=" * 70)


def demo_shadow_metropolis() -> None:
    print("\n[DEMO] ShadowMetropolis")

    world = ShadowMetropolis()
    assert world.world_type == "urban"
    assert world.setting == "ShadowMetropolis"

    hero = HeroCharacter(name="Alex")
    assert hero.character_type == "hero"
    assert hero.morality_score > 70

    trickster = TricksterCharacter(name="MysteriousGuide")
    assert trickster.character_type == "trickster"

    engine = StoryEngine(world, [hero, trickster], theme="noir")
    narrative = engine.generate_story(episodes=2)

    assert narrative.title is not None
    assert len(narrative.chapters) >= 2

    print("  [PASS] ShadowMetropolis")


def demo_stellar_odyssey() -> None:
    print("\n[DEMO] StellarOdyssey")

    world = StellarOdyssey()
    assert world.world_type == "space"
    assert world.setting == "StellarOdyssey"

    hero = HeroCharacter(name="Commander")
    mentor = MentorCharacter(name="AncientOne")

    engine = StoryEngine(world, [hero, mentor], theme="sci-fi")
    narrative = engine.generate_story(episodes=3)

    assert narrative.tension_level > 0

    print("  [PASS] StellarOdyssey")


def demo_ancient_kingdom() -> None:
    print("\n[DEMO] AncientKingdom")

    world = AncientKingdom()
    assert world.world_type == "fantasy"

    hero = HeroCharacter(name="Warrior")
    antihero = AntiheroCharacter(name="Rogue")

    engine = StoryEngine(world, [hero, antihero], theme="fantasy")
    narrative = engine.generate_story(episodes=4)

    assert narrative.cliffhanger_probability > 0

    print("  [PASS] AncientKingdom")


def demo_themes() -> None:
    print("\n[DEMO] Theme Engine")

    themes = ["noir", "sci-fi", "fantasy", "mystery", "romance"]

    for theme in themes:
        engine = ThemeEngine(theme)
        assert engine.current_theme == theme

        action = engine.select_plot_action()
        assert action is not None

    print("  [PASS] Theme Engine")


def demo_branching_narrative() -> None:
    print("\n[DEMO] Branching Narrative")

    world = ShadowMetropolis()
    hero = HeroCharacter(name="Player")
    trickster = TricksterCharacter(name="Guide")

    engine = StoryEngine(world, [hero, trickster], theme="noir", branching=True)
    narrative = engine.generate_story(episodes=3)

    assert narrative.branching_enabled is True
    assert len(narrative.alternate_endings) > 0

    print("  [PASS] Branching Narrative")


if __name__ == "__main__":
    InteractiveStorySimulator.run_shadow_metropolis_demo()
    InteractiveStorySimulator.run_stellar_odyssey_demo()
    InteractiveStorySimulator.run_ancient_kingdom_demo()
    InteractiveStorySimulator.run_theme_comparison_demo()
    InteractiveStorySimulator.run_branching_demo()
