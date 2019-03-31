#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Server module to run the mesa based implementation of Conway's game of life

It uses a model descirption and an agent description to compute the simulation
"""

from conwayGameOfLifeModel import ConwayGameOfLifeModel


test_model = ConwayGameOfLifeModel(4, 4)

for i in range(15):
    print("Running step {}".format(i))
    test_model.step()
