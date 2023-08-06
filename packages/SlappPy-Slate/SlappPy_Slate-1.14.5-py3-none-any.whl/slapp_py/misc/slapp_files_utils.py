import glob
from os.path import join
from typing import List, Optional, Generator

from battlefy_toolkit.caching.fileio import load_json_from_file

from slapp_py.core_classes.player import Player
from slapp_py.core_classes.source import Source
from slapp_py.core_classes.team import Team
from slapp_py.slapp_runner.slapipes import SLAPP_DATA_FOLDER

TOURNEY_INFO_SAVE_DIR = join(SLAPP_DATA_FOLDER, "tourney_info")
TOURNEY_TEAMS_SAVE_DIR = join(SLAPP_DATA_FOLDER, "tourney_teams")
STAGES_SAVE_DIR = join(TOURNEY_INFO_SAVE_DIR, "stages")


def get_slapp_files_matching(pattern: str, directory: str = SLAPP_DATA_FOLDER) -> List[str]:
    return sorted(glob.glob(join(directory, pattern))) or []


def get_latest_slapp_files_matching(pattern: str, directory: str = SLAPP_DATA_FOLDER) -> Optional[str]:
    files = get_slapp_files_matching(pattern, directory)
    if files:
        return files[-1]
    else:
        return None


def get_latest_snapshot_sources_file() -> Optional[str]:
    return get_latest_slapp_files_matching(f'Snapshot-Sources-*.json')


def get_latest_snapshot_players_file() -> Optional[str]:
    return get_latest_slapp_files_matching(f'Snapshot-Players-*.json')


def get_latest_snapshot_teams_file() -> Optional[str]:
    return get_latest_slapp_files_matching(f'Snapshot-Teams-*.json')


def get_latest_sources_yaml_file() -> Optional[str]:
    return get_latest_slapp_files_matching(f'sources.yaml')


def load_latest_snapshot_sources_file() -> Optional[List[Source]]:
    file = get_latest_snapshot_sources_file()
    if file:
        print('Loading sources from ' + file)
        loaded = load_json_from_file(file)
        return [Source.from_dict(d) for d in loaded]
    else:
        print('Sources file not found.')
        return None


def load_latest_snapshot_players_file() -> Optional[List[Player]]:
    file = get_latest_snapshot_players_file()
    if file:
        print('Loading players from ' + file)
        loaded = load_json_from_file(file)
        return [Player.from_dict(d) for d in loaded]
    else:
        print('Players file not found.')
        return None


def load_latest_snapshot_teams_file() -> Optional[List[Team]]:
    file = get_latest_snapshot_teams_file()
    if file:
        print('Loading teams from ' + file)
        loaded = load_json_from_file(file)
        return [Team.from_dict(d) for d in loaded]
    else:
        print('Teams file not found.')
        return None


def enumerate_latest_snapshot_sources_file() -> Generator[Source, None, None]:
    file = get_latest_snapshot_sources_file()
    if file:
        print('Loading sources from ' + file)
        loaded = load_json_from_file(file)
        for d in loaded:
            yield Source.from_dict(d)
    else:
        print('Sources file not found.')
