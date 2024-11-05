#    This file is part of the Compressor distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in <
# https://github.com/1Danish-00/CompressorQueue/blob/main/License> .

from decouple import config

try:
    APP_ID = config("APP_ID", "10419615")
    API_HASH = config("API_HASH", "412bca750b8004784adeeafb98e991c5")
    BOT_TOKEN = config("BOT_TOKEN", "7882507899:AAHVLoQJ7mCnihdxlMTiI0LkMV7cmbXd5no")
    DEV = 1995886602
    OWNER = config("OWNER", "7077099034 ")
    FFMPEG = config(
        "FFMPEG",
        default='ffmpeg -i "{}" -preset superfast -c:v libx265 -crf 28 -map 0:v -c:a aac -map 0:a -c:s copy -map 0:s? "{}"',
    )
    THUMB = config(
        "THUMBNAIL", default="https://telegra.ph/file/eb6b1f4fe1e5e4a013534.jpg"
    )
except Exception as e:
    print("Environment vars Missing")
    print("something went wrong")
    print(str(e))
    exit()
