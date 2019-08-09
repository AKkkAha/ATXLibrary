# -*- coding: utf-8 -*-

from .keywordgroup import KeywordGroup


class _ToastKeywords(KeywordGroup):
    def get_toast(self):
        """
        get the message from toast
        :return: message of toast
        """
        toast_msg = self._current_application().toast.get_message()
        return toast_msg

    def make_toast(self, msg):
        """
        make a toast on the phone
        :param msg: message of toast
        """
        self._current_application().toast.show(msg)
