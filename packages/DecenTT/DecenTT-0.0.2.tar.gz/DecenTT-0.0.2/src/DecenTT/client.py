from DecenTT.DecenTTErrors import InvalidCallback, TopicIncompatibleType
from DecenTT.IPFS import Client as iClient  # Equipped with list of topics
from DecenTT.MQTT import Client as mClient


class Client:
    """
        Which Client ??
        0:          MQTT Client
        1:          IPFS Client

    """

    def __init__(
            self,
            host: str,
            port: int = 1883,
            username: str = None,
            password: str = None,
            on_connect=None,
            on_publish=None,
            on_message=None,
            log_path: str = ".",
            keyword: str = "secure/"
    ) -> None:
        self.__keyword = keyword
        self.clients = [
            mClient(
                host=host,
                port=port,
                username=username,
                password=password,
                on_connect=on_connect,
                on_publish=on_publish,
                on_message=on_message,
                log_path=log_path
            ),

            iClient()
        ]

    # Mock Switcher
    def __which(self, topic: str):
        if self.__keyword in topic: return self.clients[1]
        return self.clients[0]

    def __map_clients_to_topic(self, topic: list) -> tuple:
        client_0_list = list()
        client_1_list = list()
        for t_i in topic:
            if self.__keyword in str(t_i[0]):
                client_1_list.append(t_i[0])
            else:
                client_0_list.append(t_i)

        return client_0_list, client_1_list

    def subscribe(self, topic: any, callback):

        # check for the validity of the topic as data_structure
        if not (isinstance(topic, list) or isinstance(topic, str)):
            raise TopicIncompatibleType

        # check for valid callback
        if not ('function' in str(type(callback))):
            raise InvalidCallback(callback)

        if isinstance(topic, list):
            c0_topics, c1_topics = self.__map_clients_to_topic(topic= list(topic))
            self.clients[0].subscribe(topic=c0_topics, callback=callback)
            self.clients[1].subscribe(topic=c1_topics, callback=callback)
            return

        client = self.__which(topic=topic)
        client.subscribe(topic=topic, callback=callback)

    def publish(self, topic: str, payload: str):
        client = self.__which(topic=topic)
        client.publish(topic=topic, payload=payload)
