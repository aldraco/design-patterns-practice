import random
import time

# The weather station should emit a steady stream of random temperature information
# (alternately, could connect to weatherunderground's API)

class WeatherStation(object):
    """Concrete class that pushes data to a weather_data class, to which 
    Observers can subscribe and display data in different ways."""

    observers = []
    temperature = None
    humidity = None
    pressure = None
    switched_on = False
    changed = False

    def go(self):
        self.switched_on = True
        while self.switched_on:
            self._fetch_weather()

    def switch_off(self):
        self.switched_on = False

    def measurements_changed(self):
        """Called when the measurements change."""
        self._set_changed()
        self._notify_observers()

    def _set_changed(self):
        self.changed = True

    def _notify_observers(self):
        if self.changed:
            for observer in self.observers:
                # requires subscribers to simply implement this function to get data
                observer.notify_weather_change(self.temperature, self.humidity, self.pressure)
            self.changed = False


    def register_observer(self, new_observer):
        self.observers.append(new_observer)

    def deregister_observer(self, observer):
        self.observers.remove(observer)

    def _fetch_weather(self):
        # in the future this will go to an API
        self.temperature = random.randint(30, 90)
        self.humidity = random.randint(0, 100)
        self.pressure = random.randint(0, 100)
        self.measurements_changed()


