#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mesa import Agent

""" 
Module that describe a cell in Conway's game of life
"""

class CellAgent(Agent):
    """
    Class representating the cell Agent using the mesa agent based model framework
    """

    def __init__(self, unique_id, state, model):
        """
        Constructor
        """

        super().__init__(unique_id, model)

        self.futur_state    = state
        self.current_state  = state


    def step(self):
        """
        Method that defines how the agent should evolve during this iteration of the model

        This is where we'll implement the Conway's game of life algorithm:
            - Case 1: Any live cell with fewer than two live neighbours dies (referred to as underpopulation or exposure[1]).
            - Case 2: Any live cell with more than three live neighbours dies (referred to as overpopulation or overcrowding).
            - Case 3: Any live cell with two or three live neighbours lives, unchanged, to the next generation.
            - Case 4: Any dead cell with exactly three live neighbours will come to life.
            - Case 5: Any dead cell with less or more than 3 live neighbours stay dead
        
        Warning: The new state is not applied here. We just determine it. It will be applied in the
        advance method. We have to do that in order to make sure that the next state of each agent
        is based on the current state of its neighbours and not on the futur state if it has already
        been ccomputed
        """
        
        nb_neighbours_alive = 0

        for neighbour in self.model.grid.iter_neighbors(self.pos, moore=True,
                include_center=False):
            if neighbour.current_state == 1:
                nb_neighbours_alive += 1

        # Case 1, 2 and 3: cell is alive
        if self.current_state == 1:
            # Case 1 and 2: cell has less than 2 or more than 3 neighbours alive
            if (nb_neighbours_alive < 2) or (nb_neighbours_alive > 3):
                self.futur_state = 0
            # Case 3 : cell has 2 or 3 neighbours alive
            else:
                self.futur_state = 1

        # Case 4 and 5: cell is dead
        elif self.current_state == 0:
            # Case 4: cell has 3 neighbours alive
            if nb_neighbours_alive == 3:
                self.futur_state = 1
            # Case 5: cell has less or more than 3 neighbours alive       
            else:
                self.futur_state = 0
        
        print("Agent {} [coordinates={} ; State={} ; FuturState={}]".format(self.unique_id,
            self.pos, self.current_state, self.futur_state))


    def advance(self):
        """
        Method that apply the new state to the agent
        """
        self.current_state = self.futur_state
        self.futur_state = None


