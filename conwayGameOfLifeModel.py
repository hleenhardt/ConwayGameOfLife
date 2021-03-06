#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mesa import Model
from mesa.time import SimultaneousActivation
from mesa.space import SingleGrid
from cellAgent import CellAgent
from random import choices

"""
Module describing the model of the game of life
"""

class ConwayGameOfLifeModel(Model):
    """
    Class describing Conway's game of life using the mesa agent based model framowork
    
    The model contains a grid. In each cell of the grid there is an agent. The agent can be dead or
    alive. At each step of the simulation, the state of the agent can change.

    The model is responsible of creating the grid and handling the iteration of the simulation
    
    """

    def __init__(self, grid_height, grid_width, percentage_of_cell_alive):
        """
        Constructor
        """

        self.grid            = SingleGrid(grid_width, grid_height, False)
        self.scheduler       = SimultaneousActivation(self)
        self.number_of_agent = grid_width * grid_height

        # Creation of all agent
        for i in range(self.number_of_agent):

            # Randomly chooses the initial state of the agent (0 is alive and 1 is dead)
            # We use choices from the random module because it allows us to specify a distribution
            # (ie. a list of probability for each state). Choices will return a list with ne element
            # which is our state
            probability_alive = percentage_of_cell_alive / 100
            probability_dead  = 1 - probability_alive
            state = choices([0,1], [probability_dead, probability_alive])[0]
            
            # Creating the agent and adding it to the scheduler
            agent = CellAgent(i, state, self)
            self.scheduler.add(agent)

            # Adding the new agent to the grid
            agent_coordinates = self.grid.find_empty()
            self.grid.place_agent(agent, agent_coordinates)

        # Define if the simulation is running or not
        self.running = True


    def step(self):
        """
        Method to advance the model by one step. It will call the step method of each agent.
        We use a simultaneous scheduler which means we we'll be iterating through all the agent at
        once to determine their next state and then apply the new state
        """
        self.scheduler.step()
