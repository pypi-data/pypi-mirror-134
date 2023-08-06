class Api:
    def __init__(self):
        self.config = {}

    def init_app(self, app):
        self.config = app.config


class GhettoApi:
    def __init__(self):
        self.lis_btn_dict = {}
        self.rec_btn_dict = {}
        self.radios_in_view_dict = {}
        self.ghetto_measure_dict = {}

    def init_lis_btn_dict(self, lis_btn_dict):
        self.lis_btn_dict = lis_btn_dict

    def init_rec_btn_dict(self, rec_btn_dict):
        self.rec_btn_dict = rec_btn_dict

    def init_radios_in_view(self, radios_in_view_dict):
        self.radios_in_view_dict = radios_in_view_dict

    def init_ghetto_measurements(self, ghetto_measure_dict):
        self.ghetto_measure_dict = ghetto_measure_dict


api = Api()
ghettoApi = GhettoApi()
