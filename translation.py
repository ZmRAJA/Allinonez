# ------------------------------------- https://github.com/zmraj/AutoforwardALLinONE -------------------------------------#

class Translation( object ):
    NOT_AUTH_TXT = "⚠️ <b>Unauthorized Access</b> ⚠️\nYou are not in Auth Users.  So you can't use the core " \
                   "components of this bot. Inconvenience is regretted !"
    DOWNLOAD_START = "📥<b>DOWNLOADING</b>📥<i> Plz wait..</i>"
    UPLOAD_START = "📤<b>UPLOADING</b>📤<i> Plz wait..</i>"
    SAVED_CUSTOM_THUMB_NAIL = "<b>✅ Thumbnail Saved Successfully.</b>\n<code>This file will be used in upcoming " \
                              "rename or video conversions</code> "
    SAVED_RECVD_DOC_FILE = "<b>✔️ Media Downloaded Successfully</b>"
    ACCESS_DENIED_TEXT = "You are not authorized to use this Bot."
    START_TEXT = "Hello.. <b>{}</b>\n\n<b>Myself:</b> {}\n\n<b>I can do a lot of things in your Chats</b> 😀\n\n" \
                 "<b>My Author is: </b><a href='https://t.me/LallanMovies'>                HERE</a>\n" \
                 "<b>My code can be seen: </b><a href='https://github.com'> HERE</a>\n" \
                 "<b>You can see my help: </b><a href='https://t.me/LallanMovies'>  HERE</a>\n\n" \
                 "<i> Have a nice day</i> 😍"
    SETTINGS_TEXT = "<b>These are my available options:</b>"
    THUMB_CAPTION = "<code>This image is your current thumbnail, Tap</code><b> DEL THUMB </b><code>if you wish to " \
                    "clear it !</code> "
    NO_THUMB = "⛔️ <b>No thumbnails available.</b>\n<code>Upload an image to save it !" \
               "!</code> "
    DEL_CUSTOM_THUMB_NAIL = "✅ <b>Thumbnail cleared successfully.</b>\n<code>Thumbnail won't be available to the " \
                            "downloading media, unless you upload an image !</code> "
    DEL_THUMB_CONFIRM = "⚠️ <b>Do you wish to remove thumbnail?</b>\n<code>Thumbnail won't be available in the files " \
                        "when you delete it!</code> "
    FILE_TYPE_SELECT = "<b>Select the format for File name:</b>\n👉 {}"
    AFTER_SUCCESSFUL_UPLOAD_MSG = "<b>Attention</b>⚠️\n<code>Please Wait for Screenshots</code> "
    INPUT_ERROR = "<b>⚠️ Invalid input:</b>️\n<code>Input the file name as replay to the above message and " \
                  "check the supported extensions in welcome message !</code> "
    EXTENSIONS = ['.mkv', '.mp4', '.avi', '.webm']
    NO_SPAM_MSG = "⚠️ <b>Don't Spam Here</b>\n<code>Read the welcome message for better use of this bot !</code>"
    CAPTION_TEXT = "📍 @LallanMovies 📍"
    TRIM_WAIT = "<b>Attention</b>⚠️\n<code>Please Wait some time for a sample video. Be patient</code> 🤪"
    THANKS_MESSAGE = "<b>Thanks for using me. Have a nice day !</b>"
    MAKE_A_COPY_TEXT = "📚 <b> Can i make a copy of the same ?</b>"
    FINISHED_PROGRESS_STR = "◼️"
    UN_FINISHED_PROGRESS_STR = "◻️"
    FAILED_LINK = "<b>Failed To Fetch Youtube Data...</b>\n<code>Please try again after some time.If " \
                  "problem persists, May be your server IP got blocked by the YouTube </code>😔 "
    PROCESS_START = "Processing Youtube Url 🔎 🔎 🔎"

    CUSTOM_CAPTION_DOC = "💢<a href='https://t.me/LallanMovies'>@LallanMovies</a>💢\n" \
                         "💢<a href='https://t.me/LallanMovies'>@LallanMovies</a>💢"
    CUSTOM_CAPTION_VIDEO = "💢<a href='https://t.me/LallanMovies'>@LallanMovies</a>💢\n" \
                           "💢<a href='https://t.me/LallanMovies'>@LallanMovies</a>💢"
    URL_ERROR = "<b>⚠️ Attention :</b>\nYour URL having some HTTP Errors ! Try with different URL..."

    SUCCESSFUL_SEND = "<code>Forwarded Successfully to:</code>\n<b>{}</b>"
    FORWARD_ERROR = "<b>⚠️ Attention :</b>\n<code>Make Sure That I am Admin in Your Channel or Provided Channel " \
                    "ID is Correct.</code>"
    CHANNEL_CONFIRM = "<b>⚠️ Attention :</b>\n<code>Now I'll send messages to:</code>\n\n<b>{}</b>"
    INVALID_CHANNEL = "⚠️ <b>Attention :</b>\n<code>Invalid Channel Id Selected.\nPossible Causes of this " \
                      "error:</code>\n\n1️⃣ <b>Bot is not an admin in Your Channel</b>\n\n2️⃣ <b>You haven't entered " \
                      "a valid channel id in the config ENV.</b>\n\n3️⃣ <b>You haven't set a default channel in the " \
                      "bot for the process.</b> "
    NOT_REPLIED_TO_MESSAGE = "⚠️ <b>Attention :</b>\n<code>Replay to any message to send !</code>"
    INFO_CHANNEL = "A'm currently sending messages to:\n<b>{}</b>"
    NO_DEFAULT_SET = "⚠️ <b>Attention :</b>\n<code>No Default channels found! Set a channel first.</code>"
    LIST_CHANNELS = "<b>These are my associated chats in use:</b>\n\n<b>Channel 1:</b>\n<code>ID: {}</code>\nName: {" \
                    "}\n\n<b>Channel2:</b>\n<code>ID: {}</code>\nName: {}\n\n<b>Channel 3:</b>\n<code>ID: {" \
                    "}</code>\nName: {}\n\n<b>Channel 4:</b>\n<code>ID: {}</code>\nName: {}\n\n<b>Channel " \
                    "5:</b>\n<code>ID: {}</code>\nName: {} "
    START_APP_TEXT = "🤓 {} with Pyrogram v{} (Layer {}) started on {} 🤓"
    STOP_APP_TEXT = "🥵 Bot stopped. Bye... 🥵"
