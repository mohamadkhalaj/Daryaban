import dropbox
from decouple import config
from dropbox.exceptions import ApiError, AuthError
from dropbox.files import WriteMode


def backup(LOCALFILE, BACKUPPATH, dbx):
    with open(LOCALFILE, "rb") as f:
        try:
            dbx.files_upload(f.read(), BACKUPPATH, mode=WriteMode("add", None), autorename=True, mute=True)
            url = str(dbx.sharing_create_shared_link_with_settings(BACKUPPATH).url).split("?")[0] + "?raw=1"
            return url
        except ApiError as err:
            if err.error.is_path() and err.error.get_path().error.is_insufficient_space():
                print("ERROR: Cannot back up; insufficient space.")
            elif err.user_message_text:
                print(err.user_message_text)
            else:
                print(err)

            return ""


def uploudImage(LOCALFILE, BACKUPPATH):
    TOKEN = config("DBX_TOKEN")
    APP_KEY = config("DBX_APP_KEY")
    APP_SECRET = config("DBX_APP_SECRET")
    REFRESH_TOKEN = config("DBX_REFRESH_TOKEN")

    if len(TOKEN) == 0:
        print(
            "ERROR: Looks like you didn't add your access token. Open up backup-and-restore-example.py in a text editor and paste in your token in line 14."
        )
        return ""

    dbx = dropbox.Dropbox(TOKEN, app_key=APP_KEY, app_secret=APP_SECRET, oauth2_refresh_token=REFRESH_TOKEN)
    try:
        dbx.users_get_current_account()
    except AuthError as err:
        print("ERROR: Invalid access token; try re-generating an access token from the app console on the web.")
        return ""

    return backup(LOCALFILE, BACKUPPATH, dbx)
