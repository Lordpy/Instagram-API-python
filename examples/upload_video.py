#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password

from InstagramAPI import InstagramAPI

video_local_path = "Your Video Path"
thumbnail_local_path = "Your Thumbnail Path"
caption = "Your Caption

InstagramAPI = InstagramAPI("username", "password")
InstagramAPI.login()  # login
InstagramAPI.uploadVideo(video_local_path, thumbnail_local_path, caption=caption)
