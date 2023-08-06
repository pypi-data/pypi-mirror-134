import requests

def get_thumbnail(url, raw=True):
    """Get thumbnail

    Keyword Arguments:
        url -- the url of the file
        raw -- bool args for get the raw image or a link
    Return: the thumbnail of the file
    """
    if raw:
        return requests.get(url, params={"thumb": "1"}).content
    return url + "?thumb=1"


def get_embed(url, raw=True):
    """Get the compressed version of picture. (Because embed will fail when picture is 10MB or more)

    Keyword Arguments:
        url -- the url of the file
        raw -- bool args for get the raw image or a link
    Return: the embed of the file
    """
    if raw:
        return requests.get(url, params={"embed": "1"}).content
    return url + "?embed=1"
