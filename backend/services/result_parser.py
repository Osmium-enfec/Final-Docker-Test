class ResultParser:
    """
    Maps Docker exit codes to human-readable verdicts.
    """
    EXIT_CODE_MAP = {
        0: "SUCCESS",
        1: "RUNTIME_ERROR",
        124: "TIME_LIMIT_EXCEEDED",
    }

    @classmethod
    def parse(cls, exit_code: int) -> str:
        return cls.EXIT_CODE_MAP.get(exit_code, f"UNKNOWN_EXIT_CODE_{exit_code}")
