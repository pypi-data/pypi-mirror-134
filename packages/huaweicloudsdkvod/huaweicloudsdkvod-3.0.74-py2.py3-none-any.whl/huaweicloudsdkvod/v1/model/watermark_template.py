# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WatermarkTemplate:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'id': 'str',
        'status': 'int',
        'dx': 'str',
        'dy': 'str',
        'position': 'str',
        'width': 'str',
        'height': 'str',
        'create_time': 'str',
        'image_url': 'str',
        'type': 'str',
        'watermark_type': 'str',
        'image_process': 'str',
        'timeline_start': 'str',
        'timeline_duration': 'str'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'status': 'status',
        'dx': 'dx',
        'dy': 'dy',
        'position': 'position',
        'width': 'width',
        'height': 'height',
        'create_time': 'create_time',
        'image_url': 'image_url',
        'type': 'type',
        'watermark_type': 'watermark_type',
        'image_process': 'image_process',
        'timeline_start': 'timeline_start',
        'timeline_duration': 'timeline_duration'
    }

    def __init__(self, name=None, id=None, status=None, dx=None, dy=None, position=None, width=None, height=None, create_time=None, image_url=None, type=None, watermark_type=None, image_process=None, timeline_start=None, timeline_duration=None):
        """WatermarkTemplate - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._id = None
        self._status = None
        self._dx = None
        self._dy = None
        self._position = None
        self._width = None
        self._height = None
        self._create_time = None
        self._image_url = None
        self._type = None
        self._watermark_type = None
        self._image_process = None
        self._timeline_start = None
        self._timeline_duration = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if dx is not None:
            self.dx = dx
        if dy is not None:
            self.dy = dy
        if position is not None:
            self.position = position
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if create_time is not None:
            self.create_time = create_time
        if image_url is not None:
            self.image_url = image_url
        if type is not None:
            self.type = type
        if watermark_type is not None:
            self.watermark_type = watermark_type
        if image_process is not None:
            self.image_process = image_process
        if timeline_start is not None:
            self.timeline_start = timeline_start
        if timeline_duration is not None:
            self.timeline_duration = timeline_duration

    @property
    def name(self):
        """Gets the name of this WatermarkTemplate.

        水印模板名称。

        :return: The name of this WatermarkTemplate.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WatermarkTemplate.

        水印模板名称。

        :param name: The name of this WatermarkTemplate.
        :type: str
        """
        self._name = name

    @property
    def id(self):
        """Gets the id of this WatermarkTemplate.

        水印模板配置id。

        :return: The id of this WatermarkTemplate.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WatermarkTemplate.

        水印模板配置id。

        :param id: The id of this WatermarkTemplate.
        :type: str
        """
        self._id = id

    @property
    def status(self):
        """Gets the status of this WatermarkTemplate.

        启用状态。  取值为： - 0：停用 - 1：启用

        :return: The status of this WatermarkTemplate.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this WatermarkTemplate.

        启用状态。  取值为： - 0：停用 - 1：启用

        :param status: The status of this WatermarkTemplate.
        :type: int
        """
        self._status = status

    @property
    def dx(self):
        """Gets the dx of this WatermarkTemplate.

        水印图片相对输出视频的水平偏移量。  默认值是0。

        :return: The dx of this WatermarkTemplate.
        :rtype: str
        """
        return self._dx

    @dx.setter
    def dx(self, dx):
        """Sets the dx of this WatermarkTemplate.

        水印图片相对输出视频的水平偏移量。  默认值是0。

        :param dx: The dx of this WatermarkTemplate.
        :type: str
        """
        self._dx = dx

    @property
    def dy(self):
        """Gets the dy of this WatermarkTemplate.

        水印图片相对输出视频的垂直偏移量。  默认值是0。

        :return: The dy of this WatermarkTemplate.
        :rtype: str
        """
        return self._dy

    @dy.setter
    def dy(self, dy):
        """Sets the dy of this WatermarkTemplate.

        水印图片相对输出视频的垂直偏移量。  默认值是0。

        :param dy: The dy of this WatermarkTemplate.
        :type: str
        """
        self._dy = dy

    @property
    def position(self):
        """Gets the position of this WatermarkTemplate.

        水印的位置。

        :return: The position of this WatermarkTemplate.
        :rtype: str
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this WatermarkTemplate.

        水印的位置。

        :param position: The position of this WatermarkTemplate.
        :type: str
        """
        self._position = position

    @property
    def width(self):
        """Gets the width of this WatermarkTemplate.

        水印图片宽。

        :return: The width of this WatermarkTemplate.
        :rtype: str
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this WatermarkTemplate.

        水印图片宽。

        :param width: The width of this WatermarkTemplate.
        :type: str
        """
        self._width = width

    @property
    def height(self):
        """Gets the height of this WatermarkTemplate.

        水印图片高。

        :return: The height of this WatermarkTemplate.
        :rtype: str
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this WatermarkTemplate.

        水印图片高。

        :param height: The height of this WatermarkTemplate.
        :type: str
        """
        self._height = height

    @property
    def create_time(self):
        """Gets the create_time of this WatermarkTemplate.

        创建时间。

        :return: The create_time of this WatermarkTemplate.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this WatermarkTemplate.

        创建时间。

        :param create_time: The create_time of this WatermarkTemplate.
        :type: str
        """
        self._create_time = create_time

    @property
    def image_url(self):
        """Gets the image_url of this WatermarkTemplate.

        水印图片下载url。

        :return: The image_url of this WatermarkTemplate.
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        """Sets the image_url of this WatermarkTemplate.

        水印图片下载url。

        :param image_url: The image_url of this WatermarkTemplate.
        :type: str
        """
        self._image_url = image_url

    @property
    def type(self):
        """Gets the type of this WatermarkTemplate.

        水印图片格式类型。

        :return: The type of this WatermarkTemplate.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this WatermarkTemplate.

        水印图片格式类型。

        :param type: The type of this WatermarkTemplate.
        :type: str
        """
        self._type = type

    @property
    def watermark_type(self):
        """Gets the watermark_type of this WatermarkTemplate.

        水印类型，当前只支持Image（图片水印）。

        :return: The watermark_type of this WatermarkTemplate.
        :rtype: str
        """
        return self._watermark_type

    @watermark_type.setter
    def watermark_type(self, watermark_type):
        """Sets the watermark_type of this WatermarkTemplate.

        水印类型，当前只支持Image（图片水印）。

        :param watermark_type: The watermark_type of this WatermarkTemplate.
        :type: str
        """
        self._watermark_type = watermark_type

    @property
    def image_process(self):
        """Gets the image_process of this WatermarkTemplate.

        type设置为Image时有效。  目前包括： - Original：只做简单缩放，不做其他处理 - Transparent：图片底色透明 - Grayed：彩色图片变灰

        :return: The image_process of this WatermarkTemplate.
        :rtype: str
        """
        return self._image_process

    @image_process.setter
    def image_process(self, image_process):
        """Sets the image_process of this WatermarkTemplate.

        type设置为Image时有效。  目前包括： - Original：只做简单缩放，不做其他处理 - Transparent：图片底色透明 - Grayed：彩色图片变灰

        :param image_process: The image_process of this WatermarkTemplate.
        :type: str
        """
        self._image_process = image_process

    @property
    def timeline_start(self):
        """Gets the timeline_start of this WatermarkTemplate.

        水印开始时间。

        :return: The timeline_start of this WatermarkTemplate.
        :rtype: str
        """
        return self._timeline_start

    @timeline_start.setter
    def timeline_start(self, timeline_start):
        """Sets the timeline_start of this WatermarkTemplate.

        水印开始时间。

        :param timeline_start: The timeline_start of this WatermarkTemplate.
        :type: str
        """
        self._timeline_start = timeline_start

    @property
    def timeline_duration(self):
        """Gets the timeline_duration of this WatermarkTemplate.

        水印持续时间。

        :return: The timeline_duration of this WatermarkTemplate.
        :rtype: str
        """
        return self._timeline_duration

    @timeline_duration.setter
    def timeline_duration(self, timeline_duration):
        """Sets the timeline_duration of this WatermarkTemplate.

        水印持续时间。

        :param timeline_duration: The timeline_duration of this WatermarkTemplate.
        :type: str
        """
        self._timeline_duration = timeline_duration

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
        if not isinstance(other, WatermarkTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
