
class ReturnStatus:

    def __init__(self, success=True, skip_url=False):
        self.success = success
        self.skip_url = skip_url

        if success and skip_url:
            raise Exception("Bad status, can't success and skip url")


class NumberedToken:

    def __init__(self, token: str, number: int):
        self.token = token
        self.number = number
