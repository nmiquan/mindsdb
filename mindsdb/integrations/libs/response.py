from pandas import DataFrame

from mindsdb.api.mysql.mysql_proxy.libs.constants.response_type import RESPONSE_TYPE


class HandlerResponse:
    def __init__(self, resp_type: RESPONSE_TYPE, data_frame: DataFrame = None,
                 error_code: int = 0, error_message: str = None):
        self.resp_type = resp_type
        self.data_frame = data_frame
        self.error_code = error_code
        self.error_message = error_message

    @property
    def type(self):
        return self.resp_type