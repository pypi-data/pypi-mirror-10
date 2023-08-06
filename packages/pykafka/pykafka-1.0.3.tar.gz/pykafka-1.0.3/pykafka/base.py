"""
Author: Keith Bourgoin
"""
__license__ = """
Copyright 2015 Parse.ly, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
__all__ = ["BaseCluster", "BaseBroker", "BasePartition", "BaseTopic",
           "BaseSimpleConsumer", "BaseProducer", "BaseAsyncProducer"]
from common import CompressionType
from partitioners import random_partitioner


class BaseCluster(object):
    """A Kafka cluster.

    This is an abstraction of the cluster topology. It provides access
    to topics and brokers, which can be useful for introspection of a cluster.
    """

    @property
    def brokers(self):
        """Brokers associated with this cluster.

        :type: `dict` of {broker_id: :class:`pykafka.base.BaseBroker`}
        """
        return self._brokers

    @property
    def topics(self):
        """Topics present in this cluster.

        :type: `dict` of {topic_name: :class:`pykafka.base.BaseTopic`}
        """
        return self._topics

    def update(self):
        """Update the Cluster with metadata from Kafka.

        All updates must happen in-place. This means that if a Topic leader has
        changed, a new Topic can't be created and put into `self.topics`. That
        would break any clients that have instances of the old Topic. Instead,
        the current topic is updated seamlessly.
        """
        raise NotImplementedError


class BaseBroker(object):
    """A Kafka Broker.

    Not especially useful under normal circumstances, but can be handy
    when introspecting about a Cluster.
    """

    @property
    def id(self):
        """Id of the broker

        :type: `int`
        """
        return self._id

    @property
    def host(self):
        """Host of the broker.

        :type: `str`
        """
        return self._host

    @property
    def port(self):
        """Port the broker uses.

        :type: `int`
        """
        return self._port


class BasePartition(object):
    """A Kafka Partition.

    Each Kafka topic is split up into parts called "partitions".  When reading
    or writing a topic, you're actually reading a partition of the topic.
    Replication also happens at the partition level.

    Like Brokers, Partitions aren't useful under normal circumstances, but
    are handy to know about for debugging and introspection.
    """

    @property
    def id(self):
        """The id of this partition.

        :type: `int`
        """
        return self._id

    @property
    def leader(self):
        """The leader broker of the partition.

        :type: :class:`pykafka.base.BasePartition`
        """
        return self._leader

    @property
    def replicas(self):
        """List of brokers which has replicas of this Partition.

        :type: `list` of :class:`pykafka.base.BaseBroker`
        """
        return self._replicas

    @property
    def isr(self):
        """List of brokers which have in-sync replicas of this partition.

        :type: `list` of :class:`pykafka.base.BaseBroker`
        """
        return self._isr

    @property
    def topic(self):
        """Name of the topic to which this partition belongs.

        :type: `str`
        """
        return self._topic

    def latest_available_offsets(self):
        """Gets the latest offset for the partition.

        :return: Latest offset for the partition.
        :rtype: `int`
        """
        raise NotImplementedError

    def earliest_available_offsets(self):
        """Gets the earliest offset for the partition.

        Due to logfile rotation, this will not always be 0. Instead,
        this will get the earliest offset for which the partition has data.

        :returns: The earliest offset for the partition.
        :rtype: `int`
        """
        raise NotImplementedError


class BaseTopic(object):
    """A Kafka topic."""

    @property
    def name(self):
        """The name of the topic.

        :type: `str`
        """
        return self._name

    @property
    def partitions(self):
        """The partitions of this topic.

        :type: `dict` of {`int`: :class:`pykafka.base.BasePartition`}
        """
        return self._partitions

    def latest_offsets(self):
        """Get the latest offset for all partitions.

        :returns: The latest offset for all partitions in the topic.
        :rtype: `dict` of {:class:`pykafka.base.BasePartition`: `int`}
        """
        raise NotImplementedError

    def earliest_offsets(self):
        """Get the earliest offset for all partitions.

        Due to logfile rotation, this will not always be 0. Instead,
        this will get the earliest offset for which the partition has data.

        :returns: The earliest offset for all partitions in the topic.
        :rtype: `dict` of {:class:`pykafka.base.BasePartition`: `int`}
        """
        raise NotImplementedError


class BaseSimpleConsumer(object):
    """A simple consumer which reads data from a topic.

    This is a simple consumer useful for testing or single-process situations.
    **If multiple processes use a SimpleConsumer and read the same topic,
    they will each read copies of the data.**  Instead, use a BalancedConsumer
    to ensure each message is only read once.

    The one advantage this implementation has over a BalancedConsumer is that
    the partitions to be read can be specified. Therefore, if one has hard
    coded which processes reads which partitions, this is a useful soluton.
    """

    def __init__(self, client, topic, partitions=None):
        """Create a consumer for a topic.

        :param client: Client connection to the cluster.
        :type client: :class:`pykafka.client.KafkaClient`
        :param topic: The topic to consume from.
        :type topic: :class:`pykafka.base.BaseTopic` or :class:`str`
        :param partitions: List of partitions to consume from.
        :type partitions: Iterable of :class:`pykafka.base.BasePartition` or int
        """
        raise NotImplementedError

    def __iter__(self):
        """Iterator for messages in the consumer."""
        raise NotImplementedError

    @property
    def topic(self):
        """The topic from which data is being read.

        :type: :class:`pykafka.base.BaseTopic`
        """
        return self._topic

    @property
    def partitions(self):
        """The partitions from which data is being read.

        :type: `dict` of {`int`: :class:`kafka.base.BasePartition`}
        """
        return self._partitions

    def consume(self, timeout=None):
        """Consume a message from the topic.

        :returns: A message.
        :rtype: :class:`kafka.common.Message`
        """
        raise NotImplementedError


class BaseProducer(object):
    """A producer which writes data to a topic.

    This producer is synchronous, waiting for a response from Kafka
    before returning. For an asynchronous implementation, use
    :class:`pykafka.base.BaseAsyncProducer`
    """
    def __init__(self,
                 client,
                 topic,
                 partitioner=random_partitioner,
                 compression=CompressionType.NONE,
                 max_retries=3,
                 retry_backoff_ms=100,
                 topic_refresh_interval_ms=600000,
                 required_acks=1,
                 ack_timeout_ms=10000,
                 batch_size=200):
        """Create a Producer for a topic.

        :param client: KafkaClient used to connect to cluster.
        :param topic: The topic to produce messages for.
        :type topic: :class:`pykafka.topic.Topic`
        :para compression: Compression to use for messages.
        :type compression: :class:`kafka.common.CompressionType`
        :param max_retries: Number of times to retry sending messages.
        :param retry_backoff_ms: Interval (in milliseconds) to wait between
            retries
        :param topic_refresh_interval_ms: Time (in milliseconds) between queries
            to refresh metadata about the topic. The Producer will also refresh
            this data when the cluster changes (e.g. partitions missing, etc),
            but this is the interval for how often it actively polls for
            changes.
        :param required_acks: How many other brokers must have committed the
            data to their log and acknowledged this to the leader before a
            request is considered complete?
        :param ack_timeout_ms: Amount of time (in milliseconds) to wait for
            acknowledgment of a produce request.
        :param batch_size: Size (in bytes) of batches to send to brokers.
        """
        raise NotImplementedError

    @property
    def topic(self):
        """The topic to which data is being written.

        :type: :class:`pykafka.base.BaseTopic`
        """
        return self._topic

    @property
    def partitioner(self):
        """The partitioner used to determine which partition used.

        :type: :class:`pykafka.partitioners.BasePartitioner`
        """
        return self._partitioner

    def produce(self, messages):
        """Produce messages to the topic.

        :param messages: Iterable of messages to be published.
        :type messages: An iterable of either strings or (key, value) tuples.
            If tuples, then the `key` will be sent to the partitioner to
            determine to which partition it belongs. It will also be sent to
            Kafka and available when the message is read.
        """
        raise NotImplementedError


class BaseAsyncProducer(BaseProducer):
    """Asynchronous Producer for the Kafka Cluster.

    Asynchronously publishes messages to the Kafka cluster. Calling `produce`
    will return immediately.  Messages will be batched and published at regular
    intervals based on settings passed to the AsyncProducer.
    """
    pass
