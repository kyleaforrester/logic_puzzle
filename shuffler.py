#!/usr/bin/env python3

import sys
import random

fd = sys.stdin.read()

fd = fd.replace('P0', 'Thomas')
fd = fd.replace('P1', 'HotKyle')
fd = fd.replace('P2', 'Frances')
fd = fd.replace('P3', 'Jose')
fd = fd.replace('P4', 'Jeanette')
fd = fd.replace('P5', 'Stephanie')
fd = fd.replace('P6', 'Daniel')
fd = fd.replace('P7', 'Lily')
fd = fd.replace('P8', 'Eric')
fd = fd.replace('P9', 'Lauren')


fd = fd.replace('W0', 'a hammer')
fd = fd.replace('W1', 'a gun')
fd = fd.replace('W2', 'a sword')
fd = fd.replace('W3', 'some poison')
fd = fd.replace('W4', 'a club')
fd = fd.replace('W5', 'a bomb')
fd = fd.replace('W6', 'a rope')
fd = fd.replace('W7', 'some sharp antlers')
fd = fd.replace('W8', 'a bigass candycane')
fd = fd.replace('W9', 'an icepick')

fd = fd.replace('L0', 'the closet')
fd = fd.replace('L1', 'the half-bathroom')
fd = fd.replace('L2', 'the master bedroom')
fd = fd.replace('L3', 'the guest bedroom')
fd = fd.replace('L4', 'the kitchen')
fd = fd.replace('L5', 'the garage')
fd = fd.replace('L6', 'the den')
fd = fd.replace('L7', 'the basement')
fd = fd.replace('L8', 'the attic')
fd = fd.replace('L9', 'the porch')

fd = fd.replace('M0', 'agitation')
fd = fd.replace('M1', 'anger')
fd = fd.replace('M2', 'ire')
fd = fd.replace('M3', 'jealousy')
fd = fd.replace('M4', 'envy')
fd = fd.replace('M5', 'hate')
fd = fd.replace('M6', 'dislike')
fd = fd.replace('M7', 'annoyance')
fd = fd.replace('M8', 'disdain')
fd = fd.replace('M9', 'fear')

lines = [l for l in fd.split('\n') if len(l) > 0]
random.shuffle(lines)

for l in lines:
    print(l)
