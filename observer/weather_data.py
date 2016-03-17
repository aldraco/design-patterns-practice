class WeatherData(object):
    """A subscriber class to the weather station. 
    This class also has subscribers of its own."""

    temperature = None
    humidity = None
    pressure = None

    subscribers = []
    changed = False

    def __init__(self, station):
        """Upon creation, it automatically adds itself to the station."""
        station.register_observer(self)
        print "Registered with the station."

    # has to update all of the displays with new information
    def notify_weather_change(self, temp, humid, press):
        self.temperature = temp
        self.humidity = humid
        self.pressure = press
        print "Received weather information:"
        print temp, humid, press

        if self.changed:
            for subscriber in self.subscribers:
                subscriber.receive_weather_information(temp, humid, press)

    def _has_changed(self):
        self.changed = True

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def unsubscribe(self, subscriber):
        self.subscribers.remove(subscriber)

    def _check_tolerance(self, tolerance):
        # will allow different displays to not be notified if the change isn't large enough
        pass