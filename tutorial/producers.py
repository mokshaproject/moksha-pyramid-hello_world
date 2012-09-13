import datetime
import moksha.hub.api.producer


class HelloWorldProducer(moksha.hub.api.producer.PollingProducer):
    frequency = datetime.timedelta(seconds=2)

    def poll(self):
        self.send_message('hello_world', "Hello World!")

