# The Observer pattern is useful when you need a one-to- many dependency between objects:


class NewsPublisher:
    def __init__(self):
        self._subscribers = set()
        self._latest_news = None

    def attach(self, subscriber):
        self._subscribers.add(subscriber)

    def detach(self, subscriber):
        self._subscribers.discard(subscriber)

    def notify(self):
        for subscriber in self._subscribers:
            subscriber.update(self._latest_news)

    def add_news(self, news):
        self._latest_news = news
        self.notify()


class NewsSubscriber:
    def __init__(self, name):
        self.name = name

    def update(self, news):
        print(f"{self.name} received news : {news}")


# usage
publisher = NewsPublisher()

subscriber1 = NewsSubscriber("New York Times")
subscriber2 = NewsSubscriber("Washington Post")
subscriber3 = NewsSubscriber("Wall Street Journal")

publisher.add_news("NASA successfully launches new Mars rover!")
# All three subscribers will receive the news

publisher.detach(subscriber2)
publisher.add_news("Stock market reaches all-time high!")
# only subscribers 1 and 3 will receive this news
