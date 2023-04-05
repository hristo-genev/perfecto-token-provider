import os
import sys
import json

tokens_file_path = os.getenv("PERFECTO_TOKEN_STORAGE", None)
if not tokens_file_path:
    tokens_file_path = os.path.join(os.path.expanduser('~'), "securityTokens.json")


def get_token_for_cloud(cloud_name, debug=True):
    """
    Searches for any stored token and returns it.
    The path to the file storing the tokens must be set in environment variable PERFECTO_TOKEN_STORAGE
    or placed in a securityTokens.json" file in the user home directory
    :param cloud_name: the name of the cloud taken from the UR
    without the .perfectomobile.com or .app.perfectomobile.com
    :param debug: Log debug messages
    :return: the token string or False if nothing was found
    """
    try:
        if tokens_file_path is None:
            if debug:
                print("Missing TOKEN_STORAGE variable pointing to the location of the tokens file")
            return None

        token = json.load(open(tokens_file_path))["tokens"][cloud_name]
        if debug:
            print("Found token for %s" % cloud_name)

        return token

    except KeyError as er:
        if debug:
            print("Token not found for %s" % cloud_name)
        return None
    except Exception as er:
        if debug:
            print(sys.exc_info())
    return None