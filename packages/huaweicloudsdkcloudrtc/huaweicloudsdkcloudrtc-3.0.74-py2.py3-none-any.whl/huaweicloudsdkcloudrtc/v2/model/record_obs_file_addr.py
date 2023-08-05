# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RecordObsFileAddr:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'location': 'str',
        'project_id': 'str',
        'bucket': 'str',
        'object': 'str'
    }

    attribute_map = {
        'location': 'location',
        'project_id': 'project_id',
        'bucket': 'bucket',
        'object': 'object'
    }

    def __init__(self, location=None, project_id=None, bucket=None, object=None):
        """RecordObsFileAddr - a model defined in huaweicloud sdk"""
        
        

        self._location = None
        self._project_id = None
        self._bucket = None
        self._object = None
        self.discriminator = None

        self.location = location
        self.project_id = project_id
        self.bucket = bucket
        if object is not None:
            self.object = object

    @property
    def location(self):
        """Gets the location of this RecordObsFileAddr.

        OBS Bucket所在RegionID

        :return: The location of this RecordObsFileAddr.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this RecordObsFileAddr.

        OBS Bucket所在RegionID

        :param location: The location of this RecordObsFileAddr.
        :type: str
        """
        self._location = location

    @property
    def project_id(self):
        """Gets the project_id of this RecordObsFileAddr.

        OBS Bucket所在Region的项目ID

        :return: The project_id of this RecordObsFileAddr.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this RecordObsFileAddr.

        OBS Bucket所在Region的项目ID

        :param project_id: The project_id of this RecordObsFileAddr.
        :type: str
        """
        self._project_id = project_id

    @property
    def bucket(self):
        """Gets the bucket of this RecordObsFileAddr.

        OBS的bucket名称

        :return: The bucket of this RecordObsFileAddr.
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        """Sets the bucket of this RecordObsFileAddr.

        OBS的bucket名称

        :param bucket: The bucket of this RecordObsFileAddr.
        :type: str
        """
        self._bucket = bucket

    @property
    def object(self):
        """Gets the object of this RecordObsFileAddr.

        OBS对象路径，遵守OBS Object定义。如果为空则保存到根目录

        :return: The object of this RecordObsFileAddr.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """Sets the object of this RecordObsFileAddr.

        OBS对象路径，遵守OBS Object定义。如果为空则保存到根目录

        :param object: The object of this RecordObsFileAddr.
        :type: str
        """
        self._object = object

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RecordObsFileAddr):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
