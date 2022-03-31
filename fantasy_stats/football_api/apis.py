from flask_restful import Api

from football_api.resources.players_resource import (
    PlayersResource,
    PLAYERS_ENDPOINT
)
from football_api.resources.seasons_resource import (
    SeasonsResource,
    SEASONS_ENDPOINT
)
from football_api.resources.teams_resource import (
    TeamsResource,
    TEAMS_ENDPOINT
)
from football_api.resources.stats_resources import (
    StatsResource,
    StatsPlayerResource,
    StatsSeasonResource,
    STATS_ENDPOINT,
    STATS_PLAYER_ENDPOINT,
    STATS_SEASON_ENDPOINT,
)


def init_api(app):
    """
    Function that init flask restful api
    :param app: Flask initialized app
    """

    api = Api(app)
    api.add_resource(PlayersResource, PLAYERS_ENDPOINT, f"{PLAYERS_ENDPOINT}/<id>")
    api.add_resource(SeasonsResource, SEASONS_ENDPOINT)
    api.add_resource(TeamsResource, TEAMS_ENDPOINT, f"{TEAMS_ENDPOINT}/<id>")
    api.add_resource(StatsResource, STATS_ENDPOINT)
    api.add_resource(StatsPlayerResource, STATS_PLAYER_ENDPOINT)
    api.add_resource(StatsSeasonResource, STATS_SEASON_ENDPOINT)

    return app
