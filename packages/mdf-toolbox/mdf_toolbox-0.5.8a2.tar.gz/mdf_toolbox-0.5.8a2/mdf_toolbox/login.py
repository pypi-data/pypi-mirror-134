import os
import json
import sys

from six import print_
import globus_sdk
from mdf_toolbox.client import MDFConnectClient
from mdf_toolbox.data_publication import DataPublicationClient
from globus_nexus_client import NexusClient

AUTH_SCOPES = {
    "transfer": "urn:globus:auth:scope:transfer.api.globus.org:all",
    "search": "urn:globus:auth:scope:search.api.globus.org:search",
    "search_ingest": "urn:globus:auth:scope:search.api.globus.org:all",
    "data_mdf": "urn:globus:auth:scope:data.materialsdatafacility.org:all",
    "publish": ("https://auth.globus.org/scopes/"
                "ab24b500-37a2-4bad-ab66-d8232c18e6e5/publish_api"),
    "connect": "https://auth.globus.org/scopes/c17f27bb-f200-486a-b785-2a25e82af505/connect",
    "petrel": "https://auth.globus.org/scopes/56ceac29-e98a-440a-a594-b41e7a084b62/all",
    "mdf_connect": "https://auth.globus.org/scopes/c17f27bb-f200-486a-b785-2a25e82af505/connect",
    "groups": "urn:globus:auth:scope:nexus.api.globus.org:groups"
}


def login(credentials=None, clear_old_tokens=False, **kwargs):
    """Login to Globus services

    Arguments:
    credentials (str or dict): A string filename, string JSON, or dictionary
                                   with credential and config information.
                               By default, looks in ~/mdf/credentials/globus_login.json.
        Contains:
        app_name (str): Name of script/client. This will form the name of the token cache file.
        services (list of str): Services to authenticate with.
                                Services are listed in AUTH_SCOPES.
        client_id (str): The ID of the client, given when registered with Globus.
                         Default is the MDF Native Clients ID.
    clear_old_tokens (bool): If True, delete old token file if it exists, forcing user to re-login.
                             If False, use existing token file if there is one.
                             Default False.

    Returns:
    dict: The clients and authorizers requested, indexed by service name.
          For example, if login() is told to auth with 'search'
            then the search client will be in the 'search' field.
    """
    NATIVE_CLIENT_ID = "98bfc684-977f-4670-8669-71f8337688e4"
    DEFAULT_CRED_FILENAME = "globus_login.json"
    DEFAULT_CRED_PATH = os.path.expanduser("~/.mdf/credentials")

    def _get_tokens(client, scopes, app_name, force_refresh=False):
        token_path = os.path.join(DEFAULT_CRED_PATH, app_name + "_tokens.json")
        if force_refresh:
            if os.path.exists(token_path):
                os.remove(token_path)
        if os.path.exists(token_path):
            with open(token_path, "r") as tf:
                try:
                    tokens = json.load(tf)
                    # Check that requested scopes are present
                    # :all scopes should override any scopes with lesser permissions
                    # Some scopes are returned in multiples and should be separated
                    existing_scopes = []
                    for sc in [val["scope"] for val in tokens.values()]:
                        if " " in sc:
                            existing_scopes += sc.split(" ")
                        else:
                            existing_scopes.append(sc)
                    permissive_scopes = [scope.replace(":all", "")
                                         for scope in existing_scopes
                                         if scope.endswith(":all")]
                    missing_scopes = [scope for scope in scopes.split(" ")
                                      if scope not in existing_scopes
                                      and not any([scope.startswith(per_sc)
                                                   for per_sc in permissive_scopes])
                                      and not scope.strip() == ""]
                    # If some scopes are missing, regenerate tokens
                    # Get tokens for existing scopes and new scopes
                    if len(missing_scopes) > 0:
                        scopes = " ".join(existing_scopes + missing_scopes)
                        os.remove(token_path)
                except ValueError:
                    # Tokens corrupted
                    os.remove(token_path)
        if not os.path.exists(token_path):
            try:
                os.makedirs(DEFAULT_CRED_PATH)
            except (IOError, OSError):
                pass
            client.oauth2_start_flow(requested_scopes=scopes, refresh_tokens=True)
            authorize_url = client.oauth2_get_authorize_url()

            print_("It looks like this is the first time you're accessing this service.",
                   "\nPlease log in to Globus at this link:\n", authorize_url)
            auth_code = input("Copy and paste the authorization code here: ").strip()

            # Handle 401s
            try:
                token_response = client.oauth2_exchange_code_for_tokens(auth_code)
            except globus_sdk.GlobusAPIError as e:
                if e.http_status == 401:
                    print_("\nSorry, that code isn't valid."
                           " You can try again, or contact support.")
                    sys.exit(1)
                else:
                    raise
            tokens = token_response.by_resource_server

            os.umask(0o077)
            with open(token_path, "w") as tf:
                json.dump(tokens, tf)
            print_("Thanks! You're now logged in.")

        return tokens

    if type(credentials) is str:
        try:
            with open(credentials) as cred_file:
                creds = json.load(cred_file)
        except IOError:
            try:
                creds = json.loads(credentials)
            except ValueError:
                raise ValueError("Credential string unreadable")
    elif type(credentials) is dict:
        creds = credentials
    else:
        try:
            with open(os.path.join(os.getcwd(), DEFAULT_CRED_FILENAME)) as cred_file:
                creds = json.load(cred_file)
        except IOError:
            try:
                with open(os.path.join(DEFAULT_CRED_PATH, DEFAULT_CRED_FILENAME)) as cred_file:
                    creds = json.load(cred_file)
            except IOError:
                raise ValueError("Credentials/configuration must be passed as a "
                                 + "filename string, JSON string, or dictionary, or provided in '"
                                 + DEFAULT_CRED_FILENAME
                                 + "' or '"
                                 + DEFAULT_CRED_PATH
                                 + "'.")

    native_client = globus_sdk.NativeAppAuthClient(creds.get("client_id", NATIVE_CLIENT_ID),
                                                   app_name=creds.get("app_name", "unknown"))

    servs = []
    for serv in creds.get("services", []):
        serv = serv.lower().strip()
        if type(serv) is str:
            servs += serv.split(" ")
        else:
            servs += list(serv)
    # Translate services into scopes, pass bad/unknown services
    scopes = " ".join([AUTH_SCOPES.get(sc, "") for sc in servs])

    all_tokens = _get_tokens(native_client, scopes, creds.get("app_name", "unknown"),
                             force_refresh=clear_old_tokens)

    clients = {}
    if "transfer" in servs:
        try:
            transfer_authorizer = globus_sdk.RefreshTokenAuthorizer(
                                        all_tokens["transfer.api.globus.org"]["refresh_token"],
                                        native_client)
            clients["transfer"] = globus_sdk.TransferClient(authorizer=transfer_authorizer)
        # Token not present
        except KeyError:
            print_("Error: Unable to retrieve Transfer tokens.\n"
                   "You may need to delete your old tokens and retry.")
            clients["transfer"] = None
        # Other issue
        except globus_sdk.GlobusAPIError as e:
            print_("Error: Unable to create Transfer client (" + e.message + ").")
            clients["transfer"] = None
        # Remove processed service
        servs.remove("transfer")

    if "search_ingest" in servs:
        try:
            ingest_authorizer = globus_sdk.RefreshTokenAuthorizer(
                                        all_tokens["search.api.globus.org"]["refresh_token"],
                                        native_client)
            clients["search_ingest"] = globus_sdk.SearchClient(authorizer=ingest_authorizer)
        # Token not present
        except KeyError:
            print_("Error: Unable to retrieve Search (ingest) tokens.\n"
                   "You may need to delete your old tokens and retry.")
            clients["search_ingest"] = None
        # Other issue
        except globus_sdk.GlobusAPIError as e:
            print_("Error: Unable to create Search (ingest) client (" + e.message + ").")
            clients["search_ingest"] = None
        # Remove processed service
        servs.remove("search_ingest")
        # And redundant service
        try:
            servs.remove("search")
        # No issue if it isn't there
        except Exception:
            pass
    elif "search" in servs:
        try:
            search_authorizer = globus_sdk.RefreshTokenAuthorizer(
                                        all_tokens["search.api.globus.org"]["refresh_token"],
                                        native_client)
            clients["search"] = globus_sdk.SearchClient(authorizer=search_authorizer)
        # Token not present
        except KeyError:
            print_("Error: Unable to retrieve Search tokens.\n"
                   "You may need to delete your old tokens and retry.")
            clients["search"] = None
        # Other issue
        except globus_sdk.GlobusAPIError as e:
            print_("Error: Unable to create Search client (" + e.message + ").")
            clients["search"] = None
        # Remove processed service
        servs.remove("search")

    if "data_mdf" in servs:
        try:
            mdf_authorizer = globus_sdk.RefreshTokenAuthorizer(
                                    all_tokens["data.materialsdatafacility.org"]["refresh_token"],
                                    native_client)
            clients["data_mdf"] = mdf_authorizer
        # Token not present
        except KeyError:
            print_("Error: Unable to retrieve MDF/NCSA tokens.\n"
                   "You may need to delete your old tokens and retry.")
            clients["data_mdf"] = None
        # Other issue
        except globus_sdk.GlobusAPIError as e:
            print_("Error: Unable to create MDF/NCSA Authorizer (" + e.message + ").")
            clients["data_mdf"] = None
        # Remove processed service
        servs.remove("data_mdf")

    if "publish" in servs:
        try:
            publish_authorizer = globus_sdk.RefreshTokenAuthorizer(
                                        all_tokens["publish.api.globus.org"]["refresh_token"],
                                        native_client)
            clients["publish"] = DataPublicationClient(authorizer=publish_authorizer)
        # Token not present
        except KeyError:
            print_("Error: Unable to retrieve Publish tokens.\n"
                   "You may need to delete your old tokens and retry.")
            clients["publish"] = None
        # Other issue
        except globus_sdk.GlobusAPIError as e:
            print_("Error: Unable to create Publish client (" + e.message + ").")
            clients["publish"] = None
        # Remove processed service
        servs.remove("publish")

    if "connect" in servs:
        try:
            mdf_authorizer = globus_sdk.RefreshTokenAuthorizer(
                                    all_tokens["mdf_dataset_submission"]["refresh_token"],
                                    native_client)
            clients["connect"] = mdf_authorizer
        # Token not present
        except KeyError:
            print_("Error: Unable to retrieve MDF Connect tokens.\n"
                   "You may need to delete your old tokens and retry.")
            clients["connect"] = None
        # Other issue
        except globus_sdk.GlobusAPIError as e:
            print_("Error: Unable to create MDF Connect Authorizer (" + e.message + ").")
            clients["connect"] = None
        # Remove processed service
        servs.remove("connect")

    # if "mdf_connect" in servs:
    #     try:
    #         mdf_authorizer = globus_sdk.RefreshTokenAuthorizer(
    #                                 all_tokens["mdf_dataset_submission"]["refresh_token"],
    #                                 native_client)
    #         clients["mdf_connect"] = MDFConnectClient(authorizer=mdf_authorizer)
    #     # Token not present
    #     except KeyError:
    #         print_("Error: Unable to retrieve MDF Connect tokens.\n"
    #                "You may need to delete your old tokens and retry.")
    #         clients["mdf_connect"] = None
    #     # Other issue
    #     except globus_sdk.GlobusAPIError as e:
    #         print_("Error: Unable to create MDF Connect Client (" + e.message + ").")
    #         clients["mdf_connect"] = None
    #     # Remove processed service
    #     servs.remove("mdf_connect")

    if "petrel" in servs:
        try:
            mdf_authorizer = globus_sdk.RefreshTokenAuthorizer(
                                    all_tokens["petrel_https_server"]["refresh_token"],
                                    native_client)
            clients["petrel"] = mdf_authorizer
        # Token not present
        except KeyError:
            print_("Error: Unable to retrieve MDF/Petrel tokens.\n"
                   "You may need to delete your old tokens and retry.")
            clients["petrel"] = None
        # Other issue
        except globus_sdk.GlobusAPIError as e:
            print_("Error: Unable to create MDF/Petrel Authorizer (" + e.message + ").")
            clients["petrel"] = None
        # Remove processed service
        servs.remove("petrel")

    if "groups" in servs:
        try:
            groups_authorizer = globus_sdk.RefreshTokenAuthorizer(
                                        all_tokens["nexus.api.globus.org"]["refresh_token"],
                                        native_client)
            clients["groups"] = NexusClient(authorizer=groups_authorizer)
        # Token not present
        except KeyError:
            print_("Error: Unable to retrieve Groups tokens.\n"
                   "You may need to delete your old tokens and retry.")
            clients["groups"] = None
        # Other issue
        except globus_sdk.GlobusAPIError as e:
            print_("Error: Unable to create Groups client (" + e.message + ").")
            clients["groups"] = None
        # Remove processed service
        servs.remove("groups")

    # Warn of invalid services
    if servs:
        print_("\n".join(["Unknown or invalid service: '" + sv + "'." for sv in servs]))

    return clients