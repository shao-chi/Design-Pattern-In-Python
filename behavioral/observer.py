import time
from abc import abstractmethod


class SubscriberInterface(object):
    def __init__(self, name) -> None:
        self.name = name

    @abstractmethod
    def update(self, publisher, message):
        return f'message "{message}" from {publisher.name}'


class PublisherInterface(object):
    def __init__(self, name) -> None:
        self.name = name
        self.subscribers = set()
        self.main_state = f"Created {self.name}"

    def addSubscriber(self, subscriber):
        self.subscribers.add(subscriber)

    def removeSubscriber(self, subscriber):
        self.subscribers.remove(subscriber)

    def notify(self):
        for subscriber in self.subscribers:
            subscriber.update(self, self.main_state)

    @abstractmethod
    def business_logic(self):
        ...


class ETL(PublisherInterface):
    def business_logic(self):
        self.main_state = 'Start running ETL'
        self.notify()

        time.sleep(2)
        self.main_state = 'Finish Extracting'
        self.notify()

        time.sleep(2)
        self.main_state = 'Finish Transforming'
        self.notify()

        time.sleep(2)
        self.main_state = 'Finish Loading'
        self.notify()

        self.main_state = 'Finish ETL'
        self.notify()


class ModelTraining(PublisherInterface):
    def business_logic(self):
        self.main_state = 'Start Training'
        self.notify()

        time.sleep(2)
        self.main_state = 'Start Evaluating'
        self.notify()

        time.sleep(2)
        self.main_state = 'Finish Training'
        self.notify()


class Logger(SubscriberInterface):
    def update(self, publisher, message):
        log = f'message "{message}" from {publisher.name}'
        print(f'Saved into {self.name} logger, LOG: {log}')


class MonitorWeb(SubscriberInterface):
    def update(self, publisher, message):
        log = super().update(publisher, message)
        print(f'Updated {self.name} web, LOG: {log}')


class User(SubscriberInterface):
    def update(self, publisher, message):
        log = super().update(publisher, message)
        print(f'Send email to {self.name} user, LOG: {log}')


if __name__ == '__main__':
    etl = ETL('ETL 1')

    nlp_model = ModelTraining('NLP Model')
    cf_model = ModelTraining('Collabrotive Filtering Model')

    logger = Logger('Logger 1')
    web = MonitorWeb('monitor.com')
    user_1 = User('John')
    user_2 = User('Grace')
    user_3 = User('Simon')

    etl.addSubscriber(logger)
    etl.addSubscriber(web)
    etl.addSubscriber(user_1)
    etl.addSubscriber(user_2)
    etl.business_logic()

    etl.removeSubscriber(user_1)
    etl.business_logic()

    nlp_model.addSubscriber(logger)
    nlp_model.addSubscriber(web)
    nlp_model.business_logic()

    cf_model.addSubscriber(user_1)
    cf_model.addSubscriber(user_2)
    cf_model.addSubscriber(user_3)
    nlp_model.business_logic()

    cf_model.removeSubscriber(user_2)
    cf_model.business_logic()
