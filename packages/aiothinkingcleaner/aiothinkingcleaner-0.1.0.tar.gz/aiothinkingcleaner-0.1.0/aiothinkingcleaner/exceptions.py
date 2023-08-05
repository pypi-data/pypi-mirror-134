from asyncio import TimeoutError


class ThinkingCleanerError(Exception):
    pass


class TCErrorResponse(ThinkingCleanerError):
    pass


class TCCommandFailed(ThinkingCleanerError):
    pass
