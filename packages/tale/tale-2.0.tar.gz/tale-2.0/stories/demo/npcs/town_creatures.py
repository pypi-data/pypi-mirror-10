# coding=utf-8
"""
Creatures living in the central town.

'Tale' mud driver, mudlib and interactive fiction framework
Copyright by Irmen de Jong (irmen@razorvine.net)
"""
from __future__ import absolute_import, print_function, division, unicode_literals
import random
from tale import lang, mud_context
from tale.npc import NPC, Monster
from tale.base import heartbeat
from tale.util import message_nearby_locations
from tale.errors import ActionRefused


@heartbeat
class VillageIdiot(NPC):
    def init(self):
        self.beats_before_drool = 4

    def heartbeat(self, ctx):
        # note: this village idiot NPC uses a heartbeat mechanism to drool at certain moments.
        # This is less efficient than using a deferred (as the town crier NPC does) because
        # the driver has to call all heartbeats every tick even though they do nothing yet.
        # It's here for example sake.
        self.beats_before_drool -= 1
        if self.beats_before_drool <= 0:
            self.beats_before_drool = random.randint(10, 20)
            target = random.choice(list(self.location.livings))
            if target is self:
                self.location.tell("%s drools on %sself." % (lang.capital(self.title), self.objective))
            else:
                title = lang.capital(self.title)
                self.location.tell("%s drools on %s." % (title, target.title),
                                   specific_targets=[target], specific_target_msg="%s drools on you." % title)


class TownCrier(NPC):
    def init(self):
        # note: this npc uses the deferred feature to yell stuff at certain moments.
        # This is the preferred way (it's efficient).
        mud_context.driver.defer(2, self.do_cry)

    def do_cry(self, ctx):
        self.tell_others("{Title} yells: welcome everyone!")
        message_nearby_locations(self.location, "Someone nearby is yelling: welcome everyone!")
        ctx.driver.defer(random.randint(20, 40), self.do_cry)

    def notify_action(self, parsed, actor):
        greet = False
        if parsed.verb in ("hi", "hello"):
            greet = True
        elif parsed.verb == "say":
            if "hello" in parsed.args or "hi" in parsed.args:
                greet = True
        elif parsed.verb == "greet" and self in parsed.who_info:
            greet = True
        if greet:
            self.tell_others("{Title} says: \"Hello there, %s.\"" % actor.title)


class WalkingRat(Monster):
    def init(self):
        super(WalkingRat, self).init()
        mud_context.driver.defer(2, self.do_idle_action)
        mud_context.driver.defer(4, self.do_random_move)

    def do_idle_action(self, ctx):
        if random.random() < 0.5:
            self.tell_others("{Title} wiggles %s tail." % self.possessive)
        else:
            self.tell_others("{Title} sniffs around and moves %s whiskers." % self.possessive)
        ctx.driver.defer(random.randint(5, 15), self.do_idle_action)

    def do_random_move(self, ctx):
        directions_with_way_back = [d for d, e in self.location.exits.items() if e.target.exits]  # avoid traps
        for tries in range(3):
            direction = random.choice(directions_with_way_back)
            exit = self.location.exits[direction]
            try:
                exit.allow_passage(self)
            except ActionRefused:
                continue
            else:
                self.tell_others("{Title} scurries away to the %s." % direction)
                self.move(exit.target, self)
                break
        ctx.driver.defer(random.randint(10, 20), self.do_random_move)
