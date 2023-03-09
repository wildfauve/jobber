from jobber.template.commands import template__table

from . import file_handler, config


def build(cfg):
    file_obj = file_handler.file_object(cfg,
                                        template_for_table_type(cfg),
                                        path_args(cfg),
                                        template_args(cfg))
    return file_handler.create_python_files(file_obj)


def template_for_table_type(cfg):
    if cfg.table_type == "hive":
        return template__table
    breakpoint()

def path_args(cfg):
    return {'project': config.project_location(cfg),
            'table_name': cfg.table_name}


def template_args(cfg: config.NewTable):
    return {'table_name': cfg.table_name,
            "table_cls_name": cfg.cls_name,
            "table_create_protocol": managed_or_unmanaged(cfg.managed),
            "prop_prefix": cfg.prop_prefix}


def managed_or_unmanaged(managed: bool):
    return "CreateManagedDeltaTableSQL" if managed else "CreateUnManagedDeltaTableSQL"