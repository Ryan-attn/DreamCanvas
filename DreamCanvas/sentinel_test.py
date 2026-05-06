#!/usr/bin/env python3

from narrative_core import ThemeEngine, PlotActions, NarrativeState
from worlds import ShadowMetropolis, StellarOdyssey
from characters import HeroCharacter, TricksterCharacter
from story_generator import StoryEngine, StoryPlot

def run_test():
    print("Creating world and characters...")
    world = ShadowMetropolis()
    hero = HeroCharacter(name="TestHero")
    trickster = TricksterCharacter(name="TestTrickster")

    print(f"World type: {type(world)}")
    print(f"World setting: {world.setting}")
    print(f"Hero type: {type(hero)}")
    print(f"Hero name: {hero.name}")
    print(f"Trickster name: {trickster.name}")

    print("\nCreating story engine...")
    engine = StoryEngine(world, [hero, trickster], theme="noir")

    print("Generating story...")
    try:
        narrative = engine.generate_story(episodes=3)
        print(f"Story generated!")
        print(f"Title: {narrative.title}")
        print(f"Chapters: {len(narrative.chapters)}")
        print(f"Tension level: {narrative.tension_level}")
    except Exception as e:
        print(f"Error during story generation: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    run_test()
