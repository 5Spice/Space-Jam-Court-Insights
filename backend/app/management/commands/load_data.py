import os
import json
import django
from django.core.management.base import BaseCommand
from app.dbmodels.models import Game, Player, Team, Shot
from django.db.utils import IntegrityError

# Set the DJANGO_SETTINGS_MODULE
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

# Configure Django settings before importing models
django.setup()  # Initialize Django

class Command(BaseCommand):
    help = 'Load data into the database'

    def add_arguments(self, parser):
        parser.add_argument('json_files', nargs='+', type=str, help='Paths to the JSON files to load data from')

    def handle(self, *args, **options):
        project_dir = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../.."))
        json_file_paths = options['json_files']

       # Load player names from 'players.json'
        players_data = {}
        players_json_file = '/workspaces/technical-project-deadline-09-08-23-5Spice/backend/raw_data/players.json'
        with open(players_json_file, 'r') as players_file:
            players_list = json.load(players_file)
            players_data = {player['id']: player['name'] for player in players_list}

        # Load data from the JSON files and save it to the database
        for json_file_path in json_file_paths:
            try:
                with open(json_file_path, 'r') as json_file:
                    data = json.load(json_file)
                    for game_data in data:
                        game_id = game_data['id']
                        game_date = game_data.get('date', None)
                        try:
                            existing_game = Game.objects.get(id=game_id)
                            if game_date is not None:
                                existing_game.date = game_date
                                existing_game.save()
                        except Game.DoesNotExist:
                            existing_game = Game.objects.create(id=game_id, date=game_date)

                            home_team_data = game_data.get('homeTeam', {})  # Handle missing field
                            home_team = Team.objects.create(id=home_team_data.get('id', None), game=existing_game, is_home=True)

                            away_team_data = game_data.get('awayTeam', {})  # Handle missing field
                            away_team = Team.objects.create(id=away_team_data.get('id', None), game=existing_game, is_home=False)

                            for player_data in home_team_data.get('players', []):  # Handle missing field
                                player_id = player_data['id']
                                player_name = players_data.get(player_id, '')

                                player = Player.objects.create(
                                    id=player_id,
                                    name=player_name,
                                    team=home_team,
                                    is_starter=player_data['isStarter'],
                                    minutes=player_data['minutes'],
                                    points=player_data['points'],
                                    assists=player_data['assists'],
                                    offensive_rebounds=player_data['offensiveRebounds'],
                                    defensive_rebounds=player_data['defensiveRebounds'],
                                    steals=player_data['steals'],
                                    blocks=player_data['blocks'],
                                    turnovers=player_data['turnovers'],
                                    defensive_fouls=player_data['defensiveFouls'],
                                    offensive_fouls=player_data['offensiveFouls'],
                                    free_throws_made=player_data['freeThrowsMade'],
                                    free_throws_attempted=player_data['freeThrowsAttempted'],
                                    two_pointers_made=player_data['twoPointersMade'],
                                    two_pointers_attempted=player_data['twoPointersAttempted'],
                                    three_pointers_made=player_data['threePointersMade'],
                                    three_pointers_attempted=player_data['threePointersAttempted'],
                                )

                                for shot_data in player_data['shots']:
                                    Shot.objects.create(
                                        player=player,
                                        is_make=shot_data['isMake'],
                                        location_x=shot_data['locationX'],
                                        location_y=shot_data['locationY'],
                                    )

                            for player_data in away_team_data.get('players', []):  # Handle missing field
                                player_id = player_data['id']
                                player_name = players_data.get(player_id, '')

                                player = Player.objects.create(
                                    id=player_id,
                                    name=player_name,
                                    team=away_team,
                                    is_starter=player_data['isStarter'],
                                    minutes=player_data['minutes'],
                                    points=player_data['points'],
                                    assists=player_data['assists'],
                                    offensive_rebounds=player_data['offensiveRebounds'],
                                    defensive_rebounds=player_data['defensiveRebounds'],
                                    steals=player_data['steals'],
                                    blocks=player_data['blocks'],
                                    turnovers=player_data['turnovers'],
                                    defensive_fouls=player_data['defensiveFouls'],
                                    offensive_fouls=player_data['offensiveFouls'],
                                    free_throws_made=player_data['freeThrowsMade'],
                                    free_throws_attempted=player_data['freeThrowsAttempted'],
                                    two_pointers_made=player_data['twoPointersMade'],
                                    two_pointers_attempted=player_data['twoPointersAttempted'],
                                    three_pointers_made=player_data['threePointersMade'],
                                    three_pointers_attempted=player_data['threePointersAttempted'],
                                )

                                for shot_data in player_data['shots']:
                                    Shot.objects.create(
                                        player=player,
                                        is_make=shot_data['isMake'],
                                        location_x=shot_data['locationX'],
                                        location_y=shot_data['locationY'],
                                    )

                self.stdout.write(self.style.SUCCESS(f'Data from {json_file_path} loaded successfully.'))
            except IntegrityError:
                self.stderr.write(self.style.WARNING(f'Skipping duplicate game entry with ID {game_id}.'))
            except Exception as e:
                self.stderr.write(self.style.ERROR(f'Error loading data from {json_file_path}: {str(e)}'))
