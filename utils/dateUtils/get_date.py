import datetime


class GetDate:
    def __init__(self):
        self.now_time = datetime.datetime.now()

    def get_now_time(self, formatting):
        """
        自定义获取当前时间的格式
        :Args:
         - formatting: "%Y-%m-%d %H:%M:%S"
        """
        return self.now_time.strftime(formatting)

    def get_timestamp(self):
        """
        时间戳
        """
        return self.now_time.timestamp()


if __name__ == '__main__':
    ob_date = GetDate()
    print(ob_date.get_now_time("%Y-%m-%d"))
    print(ob_date.get_timestamp())