class NoDataError(Exception):
    def __init__(
        self, msg="Some required data is missing! Aborting character creation...\n"
    ) -> None:
        self.msg = msg
        super().__init__(self.msg)

    def __str__(self):
        return self.msg
