import uuid
import requests


def getValidator(deviceID, versionID=None):
    """
    Generate a validator.

    :param deviceID: The device identified, UUID format prefixed with "LDID-".
    :param versionID: The version identifier taken from LunarCRUSH website.

    :return: validator URL parameter.
    """
    versionID = list(versionID or "GtlZn1NfoVuhQ4p9mdveb26zFPBrwyTMXRCJUIAY7giqc3SLOWD80xHKE5sjka")
    letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456790")

    return "".join([letters[versionID.index(char)] for char in list("".join((deviceID.split("-"))[1:]))])


def getURL(version=None, deviceID=None, versionID=None):
    """
    Generate a LunarCRUSH API URL with valid parameters.

    :param version: LunarCRUSH version, defaults to "lunar-20211013"
    :param deviceID: The device identified, UUID format prefixed with "LDID-". Generates random if null.
    :param versionID: The version identifier taken from LunarCRUSH website. Defaults to "lunar-20211013"'s ID. This is only required if LunarCRUSH updates their site.
    """
    base = "https://api.lunarcrush.com/v2?requestAccess=lunar&platform=web&device=Firefox&"
    deviceID = deviceID or ("LDID-" + str(uuid.uuid4()))
    version = version or "lunar-20211013"
    params = [
        f"deviceId={deviceID}",
        f"validator={getValidator(deviceID, versionID)}",
        f"clientVersion={version}"
    ]

    return base + "&".join(params)


def getKey(version=None, deviceID=None, versionID=None):
    """
    Generate a LunarCRUSH API key.

    :param version: LunarCRUSH version, defaults to "lunar-20211013"
    :param deviceID: The device identified, UUID format prefixed with "LDID-". Generates random if null.
    :param versionID: The version identifier taken from LunarCRUSH website. Defaults to "lunar-20211013"'s ID. This is only required if LunarCRUSH updates their site.
    """

    response = requests.get(getURL(version, deviceID, versionID))
    json = response.json()
    return json["token"]
