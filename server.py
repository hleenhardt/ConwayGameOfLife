#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Server module to run the mesa based implementation of Conway's game of life

It uses a model descirption and an agent description to compute the simulation
"""

from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.UserParam import UserSettableParameter
from conwayGameOfLifeModel import ConwayGameOfLifeModel

# Size in pixel of a cell in the visualization
CELL_WIDTH  = 5
CELL_HEIGHT = 5


def agent_portrayal(agent):
    """
    Fonction describing how a given agent should be displayed on the visualization
    """

    portrayal = {
            "Shape"  : "rect",
            "Color"  : "blue" if agent.is_alive is True else "white",
            "Filled" : "true",
            "Layer"  : 0,
            "w"      : CELL_WIDTH,
            "h"      : CELL_HEIGHT,
    }

    return portrayal



# Size of the grid in cell (so number of cell = width * height)
grid_width  = 50
grid_height = 50

# Size of the canvas to draw all the cell 
grid_width_in_pixel  = grid_width * CELL_WIDTH
grid_height_in_pixel = grid_height * CELL_HEIGHT

# Settable parameter that allow the user to choose the density of cell alive initialy
dead_alive_slider = UserSettableParameter('slider', "Percentage of cell alive", 50, 0, 100, 1)

# Parameters of the Conway's game of life model
model_params = {
        "grid_width"  : grid_width,
        "grid_height" : grid_height,
        "percentage_of_cell_alive" : dead_alive_slider
}

# HTML canvas use to visualize the model
grid = CanvasGrid(agent_portrayal, grid_width, grid_height, grid_width_in_pixel,
        grid_height_in_pixel)

# Web server to see the visualization
server = ModularServer(
            ConwayGameOfLifeModel, 
            [grid], 
            "Conway's game of life model",
            model_params
)
