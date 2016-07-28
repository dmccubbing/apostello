import json

from channels import Group


def ws_connect(message):
    Group('sms_notification').add(message.reply_channel)


def ws_disconnect(message):
    Group('sms_notification').discard(message.reply_channel)
