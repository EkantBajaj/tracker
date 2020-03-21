from flask import Blueprint

class SubApp(Blueprint):

    def __init__(self, name, import_name=None, **kwargs):
        super(SubApp, self).__init__(
            name=name, import_name=import_name or name, **kwargs)