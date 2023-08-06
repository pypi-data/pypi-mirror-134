class FileTooBigWarning(Warning):
    """
    Raised when a file is too big to be processed
    """

    pass


class FileNotFoundError(Exception):
    """
    Raised when a file is not found
    """

    pass


class UploadError(Exception):
    """
    Raised when an upload error occurs
    """

    pass


class DeleteError(Exception):
    """
    Raised when an delete error occurs
    """

    pass
