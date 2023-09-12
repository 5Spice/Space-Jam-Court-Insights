# -*- coding: utf-8 -*-
"""Contains models related to stats"""
from django.db import models

# Define fields and relations for game, players, and teams
class Game(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateField(null=True)

class Player(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    team = models.ForeignKey('Team', on_delete=models.CASCADE, null=True)
    is_starter = models.BooleanField(default=False)
    minutes = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    offensive_rebounds = models.IntegerField(default=0)
    defensive_rebounds = models.IntegerField(default=0)
    steals = models.IntegerField(default=0)
    blocks = models.IntegerField(default=0)
    turnovers = models.IntegerField(default=0)
    defensive_fouls = models.IntegerField(default=0)
    offensive_fouls = models.IntegerField(default=0)
    free_throws_made = models.IntegerField(default=0)
    free_throws_attempted = models.IntegerField(default=0)
    two_pointers_made = models.IntegerField(default=0)
    two_pointers_attempted = models.IntegerField(default=0)
    three_pointers_made = models.IntegerField(default=0)
    three_pointers_attempted = models.IntegerField(default=0)

class Team(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    game = models.ForeignKey('Game', on_delete=models.CASCADE, null=True, default=None)
    is_home = models.BooleanField(default=False) 

class Shot(models.Model):
    id = models.BigAutoField(primary_key=True)  # Explicitly set primary key to BigAutoField
    player = models.ForeignKey('Player', on_delete=models.CASCADE)
    is_make = models.BooleanField()
    location_x = models.DecimalField(max_digits=5, decimal_places=2)
    location_y = models.DecimalField(max_digits=5, decimal_places=2)
