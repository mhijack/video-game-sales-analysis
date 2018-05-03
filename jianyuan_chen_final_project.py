
# coding: utf-8

# # Step 1a: Identify the information in the file your program will read
# This file is shared by the Gregory Smith on their [Open Data page](https://www.kaggle.com/gregorut/videogamesales). It contains information about a list of video games with sales greater than 100,000 copies.
# 
# Each row represents one market with its:
# 
#  - rank
#  - name
#  - platform
#  - year
#  - genre
#  - publisher
#  - NA_sales
#  - EU_sales
#  - JP_sales
#  - other_sales
#  - global_sales
# 
#  
# ### Step 1b: Write a description of what your program will produce
# Ideas for what program might produce:
#  1. a list of all the sports games
#  2. a list of all the games that are published by Nintendo
#  3. the number of games that are published by Nintendo
#  4. total NA sales of all games
#  5. line graph of total Nintendo games sold in NA, EU, JP and Other regions
# 
# ### Step 1c: Write or draw examples of what your program will produce
# 
# ```python
# # 1
# expect(main('Global Video Game Sales in Millions.csv'), 
#         ['Wii Sports',
#          'Wii Fit',
#          'FIFA 16',
#          'FIFA 14'])
# # 2
# expect(main('Global Video Game Sales in Millions.csv'),
#         ['Wii Sports',
#          'Tetris',
#          'Super Mario Bros.',
#          'Super Mario Land'])
# # 3
# expect(main('Global Video Game Sales in Millions.csv'), 350)
# # 4
# expect(main('Global Video Game Sales in Millions.csv'), 105.15)
# # 5
# expect(main('Global Video Game Sales in Millions.csv'), )
# ```
# 

# ### Step 2a - Design data definitions
# 
# From the information available, the information we need to solve the problem are:
# name,
# genre,
# publisher,
# na_sales,
# eu_sales,
# jp_sales. 
# So, that's all we'll store in our data definition. We'll call our games type `Game`.

# In[119]:


# Analysis Program Template
from cs103 import *
from typing import NamedTuple, List
import matplotlib.pyplot as pyplot
import numpy as np
import csv


##################
# Data Definitions

Game = NamedTuple('Game', [('name', str),
                           ('genre', str),
                           ('publisher', str),
                           ('na', float),
                           ('eu', float),
                           ('jp', float)])
# interp. information about a game with its rank ('rank') in terms of sale,
# name ('name'), publisher ('publisher'), 
# copies sold in North America ('na'), Europe ('eu'), Japan ('jp'), 
# other regions ('other').

# these are crucial information because 

G1 = Game('Wii Sports', 'Sports', 'Nintendo', 41.49, 29.02, 3.77)
G2 = Game('Super Mario Bros.', 'Platform', 'Nintendo', 29.08, 3.58, 6.81)
G3 = Game('Mario Kart Wii', 'Racing', 'Nintendo', 15.85, 12.88, 3.79)
# G4 = Game('Kinect Adventures!', 'Misc', 'Microsoft Game Studios', 14.97, 4.94, 0.24)
# G5 = Game('Grand Theft Auto V', 'Action', 'Take-Two Interactive', 7.01, 9.27, 0.97)
# template based on compound
def fn_for_game(g: Game) -> ...:
    return ...(g.name,
               g.genre,
               g.publisher,
               g.na,
               g.eu,
               g.jp)

# List[Game]
# interp. a list of games

LOG0 = []
LOG1 = [G1, G2, G3]

# template based on arbitrary-sized and the reference rule
def fn_for_log(log: List[Game]) -> ...:
    # description of the acc
    acc = ... # type: List[Game]
    for g in log:
        ...(acc, fn_for_game(g))

    return ...(acc)


# In[120]:


###########
# Functions


# ------- helper functions --------
@typecheck
def is_nintendo(log: List[Game]) -> List[Game]:
    """
    returns a list containing only Nintendo games
    """
    lon = [] # type: List[Game]
    for game in log:
        if game.publisher == 'Nintendo':
            lon.append(game)
    return lon

@typecheck
def na_sum(lon: List[Game]) -> float:
    """
    returns the sum of north america sales
    """
    # return 0 # body of the stub
    na_sum = 0
    for game in lon:
        na_sum += game.na
    return na_sum
    
@typecheck
def eu_sum(lon: List[Game]) -> float:
    """
    returns the sum of europe sales
    """
    # return 0 # body of the stub
    eu_sum = 0
    for game in lon:
        eu_sum += game.eu
    return eu_sum

@typecheck
def jp_sum(lon: List[Game]) -> float:
    """
    returns the sum of europe sales
    """
    # return 0 # body of the stub
    jp_sum = 0
    for game in lon:
        jp_sum += game.jp
    return jp_sum
# ------- end of helper functions --------

# -------- main analysis functions -------
def analyze(log: List[Game]) -> None:
    """
    display a bar graph showing the North America, Europe, and Japan slaes of Nintendo game 
    """
    nintendo_game = is_nintendo(log) # type List[Game]
    na = na_sum(nintendo_game) # type float
    eu = eu_sum(nintendo_game) # type float
    jp = jp_sum(nintendo_game) # type float
    los = [na, eu, jp]
    objects = ['NA', 'EU', 'JP']
    y_pos = np.arange(len(objects))
    
    pyplot.bar(y_pos, los, align='center', alpha=0.5)
    pyplot.xticks(y_pos, objects)
    pyplot.ylabel('sales')
    pyplot.title('Nintendo Game Sales in Different Regions')
    pyplot.show()

def read(filename: str) -> List[Game]:
    """    
    reads the information in the file and returns a list of the Games
    """
    # return []
    # template from HtDAP
    # log contains the result so far
    log = [] # type: List[Game]

    with open(filename) as csvfile:

        reader = csv.reader(csvfile)
        next(reader) # skip header line

        for row in reader:
            g = Game(row[1], row[4], row[5], float(row[6]), float(row[7]), float(row[8]))
            
            log.append(g)

    return log

def main(filename: str) -> ...:
    """
    Reads the file from given filename, analyzes the data,
    returns the result
    """
    # template based on function composition
    return analyze(read(filename))

main('global-video-game-sales-in-millions.csv')
# -------- end of main analysis functions -----


# Begin testing
start_testing()
# Examples and tests for main
expect(..., ...)
# Examples and tests for read
expect(read('GlobalVideoGameSales_test1.csv'), [G1])
expect(read('GlobalVideoGameSales_test2.csv'), [G2, G3])

# Examples and tests for is_nintendo
expect(is_nintendo(read('GlobalVideoGameSales_test2.csv')), [G2, G3])
# Examples and tests for na_sum
expect(na_sum(is_nintendo(read('GlobalVideoGameSales_test2.csv'))), 44.93)

# Examples and tests for eu_sum
expect(eu_sum(is_nintendo(read('GlobalVideoGameSales_test2.csv'))), 16.46)
# Examples and tests for jp_sum
expect(jp_sum(is_nintendo(read('GlobalVideoGameSales_test2.csv'))), 10.6)
# show testing summary
# Examples and tests for analyze
# expect(analyze(read('Workbook1.csv')), ...)
summary()

