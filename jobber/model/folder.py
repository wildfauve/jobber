from functools import reduce
from pymonad.tools import curry
from .folder_spec import command, model, repo, util
from jobber.util import file_manager

test_folder_location = 'tests'

def create_folders(cfg):
    layer_fns = [command, model, repo, util]

    return list(map(create_folder, reduce(folder_locations_for_layer(cfg), layer_fns, [])))


@curry(3)
def folder_locations_for_layer(cfg, list_of_folders, layer):
    return list_of_folders + [[cfg.project_name()] + layer.location] + [[test_folder_location] + layer.test_location]



def create_folder(path):
    return file_manager.create_folder(path)
