# -*- coding: utf-8 -*-

from .keywordgroup import KeywordGroup


class _ToastKeywords(KeywordGroup):
    def get_toast(self):
        """
        获取Toast中的消息
        :return: message of toast
        """
        toast_msg = self._current_application().toast.get_message()
        return toast_msg

    def make_toast(self, msg):
        """
        弹出Toast消息
        :param msg: Toast中弹出的消息
        """
        self._current_application().toast.show(msg)
