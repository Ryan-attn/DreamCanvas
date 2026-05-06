#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dataclasses import dataclass, field
from typing import Any, List, Optional
import random

from agent_core import (
    Character,
    PlotActionType,
    PlotActions,
    StoryWorld,
    ThemeEngine,
    ThemePerception,
)


@dataclass
class Chapter:
    chapter_number: int
    title: str
    scenes: List[str]
    action: PlotActionType
    tension_added: int


@dataclass
class StoryPlot:
    title: str
    chapters: List[Chapter]
    theme: str
    tension_level: int
    cliffhanger_probability: float = 0.5
    branching_enabled: bool = False
    alternate_endings: List[str] = field(default_factory=list)


class StoryEngine:
    def __init__(
        self,
        world: StoryWorld,
        characters: List[Character],
        theme: str = "noir",
        branching: bool = False
    ):
        self._world = world
        self._characters = characters
        self._theme_engine = ThemeEngine(theme)
        self._branching = branching
        self._chapters: List[Chapter] = []

    @property
    def world(self) -> StoryWorld:
        return self._world

    @property
    def characters(self) -> List[Character]:
        return self._characters

    def generate_story(self, episodes: int = 5) -> StoryPlot:
        self._chapters = []
        title = self._generate_title()

        for i in range(episodes):
            chapter = self._generate_chapter(i + 1)
            self._chapters.append(chapter)

            perception = self._world.perceive()
            for character in self._characters:
                action = character.make_choice(perception)
                self._world.execute_action(action)

        return StoryPlot(
            title=title,
            chapters=self._chapters,
            theme=self._theme_engine.current_theme,
            tension_level=self._world.tension_level,
            cliffhanger_probability=self._calculate_cliffhanger(),
            branching_enabled=self._branching,
            alternate_endings=self._generate_alternate_endings() if self._branching else []
        )

    def _generate_title(self) -> str:
        title_templates = [
            "The {adjective} {noun}",
            "{noun} of {place}",
            "The {adjective} {profession}",
            "A {number} {adjective} Journey",
            "When {noun} Falls",
        ]

        adjectives = ["Shadow", "Silent", "Forgotten", "Eternal", "Broken", "Hidden", "Crimson", "Ancient"]
        nouns = ["Promise", "Dream", "Secret", "Truth", "Shadow", "Light", "Echo", "Destiny"]
        professions = ["Seeker", "Wanderer", "Guardian", "Stranger", "Sentinel", "Oracle"]
        places = ["Tomorrow", "Oblivion", "Memories", "Fortune", "Chaos", "Harmony"]
        numbers = ["One", "Two", "Three", "Seven", "Nine", "Twelve"]

        template = random.choice(title_templates)
        title = template.format(
            adjective=random.choice(adjectives),
            noun=random.choice(nouns),
            profession=random.choice(professions),
            place=random.choice(places),
            number=random.choice(numbers)
        )

        return title

    def _generate_chapter(self, number: int) -> Chapter:
        action = self._theme_engine.select_plot_action()

        scene_templates = [
            "在{location}，{event}",
            "{character}面对着{callback}的{callback2}",
            "一个新的威胁在{location}出现",
            "{character}发现了关于{callback}的秘密",
            "在{location}的遭遇改变了一切",
        ]

        locations = ["Downtown", "Harbor", "Uptown", "Slums", "Rooftops"]
        if hasattr(self._world, 'LOCATIONS'):
            locations = self._world.LOCATIONS

        callbacks = ["过去", "预言", "真相", "秘密", "命运"]
        callbacks2 = ["考验", "选择", "敌人", "盟友", "谜题"]
        events = ["故事开始展开", "冲突爆发", "意外相遇", "重大发现", "危机降临"]

        scenes = []
        for _ in range(random.randint(2, 4)):
            template = random.choice(scene_templates)
            scene = template.format(
                location=random.choice(locations),
                character=self._characters[0].name if self._characters else "Hero",
                callback=random.choice(callbacks),
                callback2=random.choice(callbacks2),
                event=random.choice(events)
            )
            scenes.append(scene)

        chapter_title = self._generate_chapter_title(action)

        return Chapter(
            chapter_number=number,
            title=chapter_title,
            scenes=scenes,
            action=action,
            tension_added=PlotActions.get_tension(action)
        )

    def _generate_chapter_title(self, action: PlotActionType) -> str:
        title_map = {
            PlotActionType.QUEST: "新的征程",
            PlotActionType.BETRAY: "背叛的代价",
            PlotActionType.REVEAL: "真相大白",
            PlotActionType.FIGHT: "激烈冲突",
            PlotActionType.LOVE: "情感纠葛",
            PlotActionType.MYSTERY: "迷雾重重",
        }
        return title_map.get(action, "未知的篇章")

    def _calculate_cliffhanger(self) -> float:
        high_tension_actions = [PlotActionType.BETRAY, PlotActionType.FIGHT]
        action_count = sum(1 for c in self._chapters if c.action in high_tension_actions)
        return min(1.0, action_count * 0.15)

    def _generate_alternate_endings(self) -> List[str]:
        endings = [
            "英雄胜利，邪恶被消灭",
            "悲剧结局，英雄牺牲",
            "开放式结局，命运未知",
            "反派获胜，世界陷入黑暗",
            "双重结局，善恶难辨",
        ]
        return random.sample(endings, min(3, len(endings)))


class StoryVisualizer:
    ANSI_COLORS = {
        'reset': '\033[0m',
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'magenta': '\033[95m',
        'cyan': '\033[96m',
        'white': '\033[97m',
        'bold': '\033[1m',
    }

    @classmethod
    def print_header(cls, title: str) -> None:
        width = 70
        print(cls.ANSI_COLORS['bold'] + cls.ANSI_COLORS['cyan'])
        print('=' * width)
        print(f"{title:^70}")
        print('=' * width)
        print(cls.ANSI_COLORS['reset'])

    @classmethod
    def print_narrative(cls, story: StoryPlot) -> None:
        cls.print_header(story.title)

        print(f"\n{cls.ANSI_COLORS['bold']}主题:{cls.ANSI_COLORS['reset']} {cls.ANSI_COLORS['magenta']}{story.theme.upper()}{cls.ANSI_COLORS['reset']}")
        print(f"{cls.ANSI_COLORS['bold']}张力等级:{cls.ANSI_COLORS['reset']} {cls.ANSI_COLORS['yellow']}{story.tension_level}{cls.ANSI_COLORS['reset']}")
        print(f"{cls.ANSI_COLORS['bold']}悬念概率:{cls.ANSI_COLORS['reset']} {cls.ANSI_COLORS['cyan']}{story.cliffhanger_probability:.0%}{cls.ANSI_COLORS['reset']}")

        for chapter in story.chapters:
            cls._print_chapter(chapter)

    @classmethod
    def _print_chapter(cls, chapter: Chapter) -> None:
        print(f"\n{cls.ANSI_COLORS['bold']}{cls.ANSI_COLORS['green']}")
        print(f"第{chapter.chapter_number}章: {chapter.title}")
        print(cls.ANSI_COLORS['reset'] + "-" * 50)

        for scene in chapter.scenes:
            print(f"  📖 {scene}")

        print(f"\n  🎭 动作: {chapter.action.value} | 张力: +{chapter.tension_added}")

    @classmethod
    def print_full_narrative(cls, story: StoryPlot) -> None:
        cls.print_narrative(story)

        if story.alternate_endings:
            print(f"\n{cls.ANSI_COLORS['bold']}可选结局:{cls.ANSI_COLORS['reset']}")
            for i, ending in enumerate(story.alternate_endings, 1):
                print(f"  {cls.ANSI_COLORS['yellow']}{i}. {ending}{cls.ANSI_COLORS['reset']}")

    @classmethod
    def print_narrative_comparison(cls, stories: List[StoryPlot]) -> None:
        cls.print_header("STORY COMPARISON")

        print(f"\n{cls.ANSI_COLORS['bold']}{'Title':<35} {'Theme':<15} {'Tension':<10}{cls.ANSI_COLORS['reset']}")
        print('-' * 60)

        for story in stories:
            print(f"{story.title:<35} "
                  f"{cls.ANSI_COLORS['magenta']}{story.theme:<15}{cls.ANSI_COLORS['reset']} "
                  f"{cls.ANSI_COLORS['yellow']}{story.tension_level:<10}{cls.ANSI_COLORS['reset']}")
