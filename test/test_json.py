"""
Test the parsing of (mocked) data from statsbomb API routes
"""
import datetime

import statsbombapi.json as sb_json
import data


def test_competitions():
    reference = [
        (
            sb_json.Competition(
                id=1,
                name="Brythonic Premier League",
                country_name="Dumnonia",
                gender=sb_json.Gender.MALE,
            ),
            sb_json.Season(id=1, name="560/561"),
            sb_json.DataUpdate(
                match_updated=datetime.datetime(2020, 1, 30, 2, 24, 23, 296715),
                match_available=datetime.datetime(2020, 1, 30, 2, 24, 23, 296715),
            ),
        ),
        (
            sb_json.Competition(
                id=1,
                name="Brythonic Premier League",
                country_name="Dumnonia",
                gender=sb_json.Gender.MALE,
            ),
            sb_json.Season(id=2, name="561/562"),
            sb_json.DataUpdate(
                match_updated=datetime.datetime(2000, 12, 1, 23, 0),
                match_available=datetime.datetime(2000, 12, 1, 23, 0),
            ),
        ),
        (
            sb_json.Competition(
                id=2,
                name="Wessex Men's Championship",
                country_name="Wessex",
                gender=sb_json.Gender.MALE,
            ),
            sb_json.Season(id=2, name="561/562"),
            sb_json.DataUpdate(
                match_updated=datetime.datetime(2000, 12, 1, 23, 0),
                match_available=datetime.datetime(2000, 12, 1, 23, 0),
            ),
        ),
        (
            sb_json.Competition(
                id=3,
                name="Wessex Women's Championship",
                country_name="Wessex",
                gender=sb_json.Gender.FEMALE,
            ),
            sb_json.Season(id=2, name="561/562"),
            sb_json.DataUpdate(
                match_updated=datetime.datetime(2000, 12, 1, 23, 0),
                match_available=datetime.datetime(2000, 12, 1, 23, 0),
            ),
        ),
    ]

    for version in ["v2"]:
        assert set(reference) == set(
            sb_json.parse_competitions(data.COMPETITIONS[version])
        )


def test_matches():
    reference = [
        sb_json.Match(
            id=1234,
            competition=sb_json.Competition(
                id=4, name="League Ān", country_name="Mercia", gender=None
            ),
            season=sb_json.Season(id=3, name="639/640"),
            date=datetime.date(640, 1, 1),
            kick_off=datetime.time(15, 0),
            match_week=35,
            status=sb_json.MatchStatus.SCHEDULED,
            competition_stage=sb_json.CompetitionStage(id=1, name="Regular Season"),
            home_team=sb_json.Team(
                id=101,
                name="Warwick Wanderers",
                gender=sb_json.Gender.MALE,
                country=sb_json.Country(id=3, name="Mercia"),
            ),
            away_team=sb_json.Team(
                id=102,
                name="Tamworth Rovers",
                gender=sb_json.Gender.MALE,
                country=sb_json.Country(id=3, name="Mercia"),
            ),
            home_score=None,
            away_score=None,
            referee=sb_json.Referee(id=123, name="None", country=None),
            metadata=sb_json.MatchMetadata(),
            last_updated=datetime.datetime(2019, 9, 1, 10, 48, 29, 321435),
        ),
        sb_json.Match(
            id=4321,
            competition=sb_json.Competition(
                id=4, name="League Ān", country_name="Mercia", gender=None
            ),
            season=sb_json.Season(id=3, name="655/656"),
            date=datetime.date(655, 10, 15),
            kick_off=datetime.time(18, 0),
            match_week=14,
            status=sb_json.MatchStatus.AVAILABLE,
            competition_stage=sb_json.CompetitionStage(id=1, name="Regular Season"),
            home_team=sb_json.Team(
                id=101,
                name="Warwick Wanderers",
                gender=sb_json.Gender.MALE,
                country=sb_json.Country(id=3, name="Mercia"),
            ),
            away_team=sb_json.Team(
                id=234,
                name="Whitby United",
                gender=sb_json.Gender.MALE,
                country=sb_json.Country(id=4, name="Northumbria"),
            ),
            home_score=1,
            away_score=3,
            referee=sb_json.Referee(
                id=454,
                name="St. Bede",
                country=sb_json.Country(id=4, name="Northumbria"),
            ),
            metadata=sb_json.MatchMetadata(
                data_version="1.1.0", xy_fidelity_version="2", shot_fidelity_version="2"
            ),
            last_updated=datetime.datetime(2020, 2, 11, 11, 18, 7, 21000),
        ),
    ]

    for version in ["v3"]:
        assert set(reference) == set(sb_json.parse_matches(data.MATCHES[version]))


def test_lineups():
    reference = (
        sb_json.Lineup(
            team=sb_json.Team(id=9876, name="Some Home Team", gender=None, country=None),
            lineup=(
                (
                    sb_json.Player(
                        id=4546,
                        name="Some Person",
                        birth_date="1992-01-01",
                        gender=sb_json.Gender.MALE,
                        height=173.0,
                        weight=63.0,
                        country=sb_json.Country(id=11, name="Someplace"),
                        nickname=None,
                    ),
                    sb_json.PlayerLineup(jersey_number=21),
                ),
                (
                    sb_json.Player(
                        id=6628,
                        name="Some Person",
                        birth_date="1992-01-01",
                        gender=sb_json.Gender.MALE,
                        height=176.0,
                        weight=73.0,
                        country=sb_json.Country(id=178, name="Someplace"),
                        nickname="Somey",
                    ),
                    sb_json.PlayerLineup(jersey_number=10),
                ),
            ),
        ),
        sb_json.Lineup(
            team=sb_json.Team(id=3257463, name="Some Away Team", gender=None, country=None),
            lineup=(
                (
                    sb_json.Player(
                        id=9745,
                        name="Some Person",
                        birth_date="1993-01-01",
                        gender=sb_json.Gender.MALE,
                        height=172.0,
                        weight=73.0,
                        country=sb_json.Country(id=11, name="Someplace"),
                        nickname="Somey",
                    ),
                    sb_json.PlayerLineup(jersey_number=32),
                ),
                (
                    sb_json.Player(
                        id=27341,
                        name="Some Person",
                        birth_date="1986-01-01",
                        gender=sb_json.Gender.MALE,
                        height=166.0,
                        weight=67.0,
                        country=sb_json.Country(id=45, name="Someplace"),
                        nickname="Somey",
                    ),
                    sb_json.PlayerLineup(jersey_number=21),
                ),
            ),
        ),
    )

    for version in ["v2"]:
        assert set(reference) == set(sb_json.parse_lineups(data.LINEUPS[version]))
