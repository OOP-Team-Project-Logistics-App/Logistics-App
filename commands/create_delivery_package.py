class CreateDeliveryPackageCommand:
    id = 1
    pass  # id += 1

    def __init__(self, params, app_data):
        self.params = params
        self.app_data = app_data

    def execute(self):
        # check if we have expected number of parameters, if yes, assign parameters
        pass
