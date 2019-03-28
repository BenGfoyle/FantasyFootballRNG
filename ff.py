#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 16:32:03 2019

@author: BenGfoyle
"""

#import random
import pandas as pd

load = lambda : pd.read_excel("fantasy.xls")
save = lambda df: df.to_excel("fantasy.xls", index=False)

#==============================================================================
def getPlayer(team):
    df = load()
    teamPlayers = df[df["p_owned"] == team]#all data of players in A
    teamPlayers = teamPlayers[["p_name"]]
    return teamPlayers

#==============================================================================

#==============================================================================
def getTeam(player):
    df = load()
    team = df[df["p_name"] == player]#all data of players in A
    teamName = team[["p_owned"]]
    return teamName

#==============================================================================

#==============================================================================
def getBudget(team):
    df = load()
    team = df[df["t_name"] == team]
    budget = team[["t_budget"]]
    return budget

#==============================================================================
    
#==============================================================================
def getTeamPrice(team):
    df = load()
    team = df[df["t_name"] == team]
    price = team[["t_teamprice"]]
    return price
#==============================================================================
    
#==============================================================================
def getPlayerPrice(player):
    df = load()
    person = df[df["p_name"] == player]
    price = person[["p_price"]]
    return price
#==============================================================================
    
#==============================================================================
def setPlayerPrice(player,newPrice):
    df = load()
    df.loc[df["p_name"] == player, "p_price"] = newPrice
    save(df)
#==============================================================================
    
#==============================================================================
def setPlayerOwnership(player,newPrice):
    df = load()
    df.loc[df["p_name"] == player, "p_price"] = newPrice
    save(df)
#==============================================================================

   
setPlayerPrice("Elbert",0)
