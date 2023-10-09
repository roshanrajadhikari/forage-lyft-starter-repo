from battery.battery import Battery


class NubbinBattery(Battery):
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self):
        date_of_next_service = self.last_service_date + 4
        if date_of_next_service < self.current_date:
            return True
        else:
            return False
