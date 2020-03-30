import pprint
import re  # noqa: F401

import six

from kubeflow.aijob.models.v1_replica_spec import V1ReplicaSpec  # noqa: F401,E501


class V1AIJobSpec(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'active_deadline_seconds': 'int',
        'backoff_limit': 'int',
        'clean_pod_policy': 'str',
        'tf_replica_specs': 'dict(str, V1ReplicaSpec)',
        'pytorch_replica_specs': 'dict(str, V1ReplicaSpec)',
        'mxnet_replica_specs': 'dict(str, V1ReplicaSpec)',
        'ttl_seconds_after_finished': 'int'
    }

    attribute_map = {
        'active_deadline_seconds': 'activeDeadlineSeconds',
        'backoff_limit': 'backoffLimit',
        'clean_pod_policy': 'cleanPodPolicy',
        'tf_replica_specs': 'tfReplicaSpecs',
        'pytorch_replica_specs': 'pytorchReplicaSpecs',
        'mxnet_replica_specs': 'mxReplicaSpecs',
        'ttl_seconds_after_finished': 'ttlSecondsAfterFinished'
    }

    def __init__(self, active_deadline_seconds=None, backoff_limit=None,
            clean_pod_policy=None, ttl_seconds_after_finished=None,
            tf_replica_specs=None, pytorch_replica_specs=None,
            mxnet_replica_specs):
        self._active_deadline_seconds = None
        self._backoff_limit = None
        self._clean_pod_policy = None
        self._tf_replica_specs = None
        self._ttl_seconds_after_finished = None
        self.discriminator = None

        if active_deadline_seconds is not None:
            self.active_deadline_seconds = active_deadline_seconds
        if backoff_limit is not None:
            self.backoff_limit = backoff_limit
        if clean_pod_policy is not None:
            self.clean_pod_policy = clean_pod_policy
        # @TODO: support Tensorflow, Pytorch, Mxnet, Hovarod
        self.tf_replica_specs = tf_replica_specs
        self.pytorch_replica_specs = pytorch_replica_specs
        self.mxnet_replica_specs = mxnet_replica_specs

        if ttl_seconds_after_finished is not None:
            self.ttl_seconds_after_finished = ttl_seconds_after_finished

    @property
    def active_deadline_seconds(self):
        """Gets the active_deadline_seconds of this V1AIJobSpec.  # noqa: E501

        Specifies the duration (in seconds) since startTime during which the job can remain active before it is terminated. Must be a positive integer. This setting applies only to pods where restartPolicy is OnFailure or Always.  # noqa: E501

        :return: The active_deadline_seconds of this V1AIJobSpec.  # noqa: E501
        :rtype: int
        """
        return self._active_deadline_seconds

    @active_deadline_seconds.setter
    def active_deadline_seconds(self, active_deadline_seconds):
        """Sets the active_deadline_seconds of this V1AIJobSpec.

        Specifies the duration (in seconds) since startTime during which the job can remain active before it is terminated. Must be a positive integer. This setting applies only to pods where restartPolicy is OnFailure or Always.  # noqa: E501

        :param active_deadline_seconds: The active_deadline_seconds of this V1AIJobSpec.  # noqa: E501
        :type: int
        """

        self._active_deadline_seconds = active_deadline_seconds

    @property
    def backoff_limit(self):
        """Gets the backoff_limit of this V1AIJobSpec.  # noqa: E501

        Number of retries before marking this job as failed.  # noqa: E501

        :return: The backoff_limit of this V1AIJobSpec.  # noqa: E501
        :rtype: int
        """
        return self._backoff_limit

    @backoff_limit.setter
    def backoff_limit(self, backoff_limit):
        """Sets the backoff_limit of this V1AIJobSpec.

        Number of retries before marking this job as failed.  # noqa: E501

        :param backoff_limit: The backoff_limit of this V1AIJobSpec.  # noqa: E501
        :type: int
        """

        self._backoff_limit = backoff_limit

    @property
    def clean_pod_policy(self):
        """Gets the clean_pod_policy of this V1AIJobSpec.  # noqa: E501

        Defines the policy for cleaning up pods after the TFJob completes. Defaults to Running.  # noqa: E501

        :return: The clean_pod_policy of this V1AIJobSpec.  # noqa: E501
        :rtype: str
        """
        return self._clean_pod_policy

    @clean_pod_policy.setter
    def clean_pod_policy(self, clean_pod_policy):
        """Sets the clean_pod_policy of this V1AIJobSpec.

        Defines the policy for cleaning up pods after the TFJob completes. Defaults to Running.  # noqa: E501

        :param clean_pod_policy: The clean_pod_policy of this V1AIJobSpec.  # noqa: E501
        :type: str
        """

        self._clean_pod_policy = clean_pod_policy

    @property
    def tf_replica_specs(self):
        """Gets the tf_replica_specs of this V1AIJobSpec.  # noqa: E501

        A map of TFReplicaType (type) to ReplicaSpec (value). Specifies the TF cluster configuration. For example,   {     \"PS\": ReplicaSpec,     \"Worker\": ReplicaSpec,   }  # noqa: E501

        :return: The tf_replica_specs of this V1AIJobSpec.  # noqa: E501
        :rtype: dict(str, V1ReplicaSpec)
        """
        return self._tf_replica_specs

    @tf_replica_specs.setter
    def tf_replica_specs(self, tf_replica_specs):
        """Sets the tf_replica_specs of this V1AIJobSpec.

        A map of TFReplicaType (type) to ReplicaSpec (value). Specifies the TF cluster configuration. For example,   {     \"PS\": ReplicaSpec,     \"Worker\": ReplicaSpec,   }  # noqa: E501

        :param tf_replica_specs: The tf_replica_specs of this V1AIJobSpec.  # noqa: E501
        :type: dict(str, V1ReplicaSpec)
        """
        #if tf_replica_specs is None:
        #    raise ValueError("Invalid value for `tf_replica_specs`, must not be `None`")  # noqa: E501

        self._tf_replica_specs = tf_replica_specs

    @property
    def pytorch_replica_specs(self):
        return self._pytorch_replica_specs

    @pytorch_replica_specs.setter
    def pytorch_replica_specs(self, pytorch_replica_specs):
        #if pytorch_replica_specs is None:
        #    raise ValueError("Invalid value for `pytorch_replica_specs`, must not be `None`")  # noqa: E501

        self._pytorch_replica_specs = pytorch_replica_specs

    @property
    def mxnet_replica_specs(self):
        return self._mxnet_replica_specs

    @mxnet_replica_specs.setter
    def mxnet_replica_specs(self, mxnet_replica_specs):
        self._mxnet_replica_specs = mxnet_replica_specs

    @property
    def ttl_seconds_after_finished(self):
        """Gets the ttl_seconds_after_finished of this V1AIJobSpec.  # noqa: E501

        Defines the TTL for cleaning up finished TFJobs (temporary before kubernetes adds the cleanup controller). It may take extra ReconcilePeriod seconds for the cleanup, since reconcile gets called periodically. Defaults to infinite.  # noqa: E501

        :return: The ttl_seconds_after_finished of this V1AIJobSpec.  # noqa: E501
        :rtype: int
        """
        return self._ttl_seconds_after_finished

    @ttl_seconds_after_finished.setter
    def ttl_seconds_after_finished(self, ttl_seconds_after_finished):
        """Sets the ttl_seconds_after_finished of this V1AIJobSpec.

        Defines the TTL for cleaning up finished TFJobs (temporary before kubernetes adds the cleanup controller). It may take extra ReconcilePeriod seconds for the cleanup, since reconcile gets called periodically. Defaults to infinite.  # noqa: E501

        :param ttl_seconds_after_finished: The ttl_seconds_after_finished of this V1AIJobSpec.  # noqa: E501
        :type: int
        """

        self._ttl_seconds_after_finished = ttl_seconds_after_finished

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(V1AIJobSpec, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1AIJobSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
