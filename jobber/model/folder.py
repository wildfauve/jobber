from functools import reduce
from pymonad.tools import curry
from .folder_spec import initialiser, command, model, repo, util, shared
from jobber.util import file_manager, fn

test_folder_location = 'tests'

def create_folders(cfg):
    layer_fns = [initialiser, command, model, repo, util, shared]

    return list(map(create_folder, reduce(folder_locations_for_layer(cfg), layer_fns, [])))


@curry(3)
def folder_locations_for_layer(cfg, list_of_folders, layer):
    return list_of_folders + fn.remove_none([main_folder(cfg, layer)] + [test_folder(cfg, layer)])


def main_folder(cfg, layer):
    return [cfg.project_name()] + layer.location if hasattr(layer, 'location') else None


def test_folder(cfg, layer):
    return [test_folder_location] + layer.test_location if hasattr(layer, 'test_location') else None


def create_folder(path):
    return file_manager.create_folder(path)
