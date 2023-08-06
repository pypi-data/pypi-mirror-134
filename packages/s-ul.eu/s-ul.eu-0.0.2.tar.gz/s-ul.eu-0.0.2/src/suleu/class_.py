import random
import string
import warnings
from os import remove
from os.path import getsize

import clipboard
import dta
import requests
from PIL import ImageGrab

from . import errors


class Upload:
    """
    A normal upload class
    """

    def __init__(self, token):
        """
        Initialize the upload class

        Keyword arguments:
                token -- the token that you can get from s-ul.eu

        Return: None
        """
        if token is None:
            raise TypeError("Token cannot be None!")
        self.__token = token
        self.__wizard = True

    def file_upload(self, file, raw=False):
        """Upload a file to the server

        Keyword arguments:
                file -- the path of the file you want to upload
                raw -- if you want to return the raw response

        Return: Dictionary that converted to attributes

        Return attributes:
                domain -- the domain of the host
                filename -- the filename that can be accessed with your domain
                protocol -- protocol that you can access
                __url -- the full __url that you can access
                extension -- the extension of the file
        """

        try:
            if getsize(file) >= 209714177:
                warnings.warn(
                    "Files is way too big! s-ul.eu server may reject this file!",
                    errors.FileTooBigWarning,
                )
        except FileNotFoundError:
            raise errors.FileNotFoundError("File not found!")
        if not raw:
            return dta.Dict2Attr(
                self.__upload(file=file, token=self.__token, wizard=self.__wizard)
            )
        return self.__upload(file=file, token=self.__token, wizard=self.__wizard)

    def clipboard_upload(self, raw=False):
        """
        Upload a file from clipboard

        Keyword arguments:
                raw -- if you want to return the raw response

        Return: Dictionary that converted to attributes or raw response

        Return attributes:
                domain -- the domain of the host
                filename -- the filename that can be accessed with your domain
                protocol -- protocol that you can access
                __url -- the full __url that you can access
                extension -- the extension of the file
        """
        filename = "".join(random.sample(string.ascii_letters + string.digits, 10))
        content = open(filename, "wb")
        content.write(bytes(clipboard.paste(), "utf-8"))
        content.close()
        if not raw:
            return dta.Dict2Attr(
                self.__upload(
                    file=filename,
                    token=self.__token,
                    wizard=self.__wizard,
                    clipboard=True,
                )
            )
        return self.__upload(
            file=filename, token=self.__token, wizard=self.__wizard, clipboard=True
        )

    def image_clipboard_upload(self, raw=False):
        """Image upload from clipboard

        Keyword arguments:
                raw -- raw response
        Return: Dictionary that converted to attributes or raw response
        """

        picture = ImageGrab.grabclipboard()
        filename = "".join(random.sample(string.ascii_letters + string.digits, 10))
        picture.save(filename)
        if not raw:
            return dta.Dict2Attr(
                self.__upload(
                    file=filename,
                    token=self.__token,
                    wizard=self.__wizard,
                    clipboard=True,
                )
            )
        return self.__upload(
            file=filename, token=self.__token, wizard=self.__wizard, clipboard=True
        )

    def __upload(self, file, token, wizard=True, clipboard=False):
        """
        Private method that uploads the file
        """

        try:
            res = requests.post(
                "https://s-ul.eu/api/v1/upload",
                files={"file": open(file, "rb")},
                params={"key": str(token), "wizard": "true" if wizard else "false"},
            )
            if res.status_code != 200:
                raise errors.UploadError(res.status_code)
            if clipboard:
                remove(file)
            return res.json()
        except Exception as e:
            raise errors.UploadError(e)


class Delete:
    """A class for deleting files"""

    def __init__(self, token):
        """Initialize the class

        Keyword arguments:
                token -- the token that you can get from s-ul.eu
        Return: None
        """
        if token is None:
            raise TypeError("Token cannot be None!")
        self.__token = token
        self.__url = "https://s-ul.eu/delete.php"

    def delete(self, file, raw=False):
        """Delete a file from the server

        Keyword arguments:
                file -- the filename that you want to delete
        Return: None
        """
        if not raw:
            return dta.Dict2Attr(self.__delete(file=file, token=self.__token))
        return self.__delete(file=file, token=self.__token)

    def __delete(self, file, token):
        """
        Private method that deletes the file
        """

        try:
            res = requests.get(self.__url, params={"key": token, "file": file})
            if res.status_code != 200:
                raise errors.DeleteError(f"{res.status_code} {res.json()}")
        except Exception as e:
            raise errors.DeleteError(e)
