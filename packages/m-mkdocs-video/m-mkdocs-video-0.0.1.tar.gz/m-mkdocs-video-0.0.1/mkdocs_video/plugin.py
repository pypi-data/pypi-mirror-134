#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Author: tungdd
    Company: MobioVN
    Date created: 13/01/2022
"""
import logging
import re

from mkdocs.config import config_options
from mkdocs.plugins import BasePlugin


class Plugin(BasePlugin):
    config_scheme = (
        ("mark", config_options.Type(str, default="type:video")),
        ("css_style", config_options.Type(dict, default={
            "position": "relative",
            "width": "100%",
            "height": "22.172vw"
        }))
    )

    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger("m-mkdocs-video")

    def on_page_content(self, html, page, config, files):
        # Separate tags by strings to simplify the use of regex
        content = html
        content = re.sub(r'>\s*<', '>\n<', content)

        tags = self.find_marked_tags(content)

        for tag in tags:
            src = self.get_tag_src(tag)
            if src is None:
                continue
            repl_tag = self.create_repl_tag(src)
            esc_tag = re.sub(r'\/', "\\\\/", tag)
            html = re.sub(esc_tag, repl_tag, html)

        return html

    def get_tag_src(self, tag):
        """
        :param tag:
        :return:
        """

        result = re.search(
            r'src=\"[^\s]*\"',
            tag
        )

        return result[0][5:-1] if result is not None else None

    def create_repl_tag(self, src):
        """
        Сreate a replacement tag with the specified source and style.
        return: str
        :param src:
        :return:
        """

        style = self.config["css_style"]
        style = "; ".join(
            ["{}: {}".format(str(atr), str(style[atr])) for atr in style]
        )

        return "<iframe " \
               "src=\"{}\" " \
               "style=\"{}\" " \
               "frameborder=\"0\" " \
               "allowfullscreen>" \
               "</iframe>".format(src, style)

    def find_marked_tags(self, content):
        """
        Find image tag with marked alternative name
        return: list
        :param content:
        :return:
        """

        mark = self.config["mark"]

        return re.findall(
            r'<img alt="' + mark + '" src="[^\s]*"\s*\/>',
            content
        )
