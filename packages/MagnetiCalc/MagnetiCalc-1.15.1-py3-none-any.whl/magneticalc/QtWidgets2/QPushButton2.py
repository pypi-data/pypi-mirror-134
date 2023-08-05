""" QPushButton2 module. """

#  ISC License
#
#  Copyright (c) 2020–2022, Paul Wilhelm, M. Sc. <anfrage@paulwilhelm.de>
#
#  Permission to use, copy, modify, and/or distribute this software for any
#  purpose with or without fee is hereby granted, provided that the above
#  copyright notice and this permission notice appear in all copies.
#
#  THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
#  WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
#  MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
#  ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
#  WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
#  ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
#  OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

from typing import Callable, Optional
import qtawesome as qta
from PyQt5.QtWidgets import QPushButton


class QPushButton2(QPushButton):
    """ QPushButton2 class. """

    def __init__(
            self,
            text: str,
            icon: str,
            clicked: Optional[Callable] = None,
            css: Optional[str] = None
    ) -> None:
        """
        Initializes a QPushButton.

        @param text: Text
        @param icon: Icon name
        @param clicked: Callback for button click
        @param css: Additional CSS (optional)
        """
        QPushButton.__init__(self)

        self.setText(text)

        if icon != "":
            self.setIcon(qta.icon(icon))

        if clicked is not None:
            self.clicked.connect(clicked)  # type: ignore

        if css is not None:
            self.setStyleSheet(css)
