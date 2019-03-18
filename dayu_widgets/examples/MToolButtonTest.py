#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

from dayu_widgets.MDivider import MDivider
from dayu_widgets.MFieldMixin import MFieldMixin
from dayu_widgets.MToolButton import MToolButton
from dayu_widgets.MTheme import global_theme
from dayu_widgets.qt import *


class MToolButtonTest(QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(MToolButtonTest, self).__init__(parent)
        self._init_ui()

    def _init_ui(self):
        button3 = MToolButton(icon=MIcon('left_line.svg'), size=MView.LargeSize)
        button4 = MToolButton(icon=MIcon('right_line.svg'), size=MView.DefaultSize)
        button5 = MToolButton(icon=MIcon('up_line.svg'), size=MView.SmallSize)
        button6 = MToolButton(icon=MIcon('down_line.svg'), size=MView.TinySize)

        button2 = MToolButton(icon=MIcon('detail_line.svg'))
        button2.setEnabled(False)
        button7 = MToolButton(icon=MIcon('trash_line.svg'), icon_checked=MIcon('trash_line.svg', '#2d8cf0'),
                              checkable=True)

        button_trash = MToolButton(icon=MIcon('trash_line.svg'), icon_only=False)
        button_trash.setText('Delete')
        button_login = MToolButton(icon=MIcon('user_line.svg'), icon_only=False)
        button_login.setText('Login')
        button_male = MToolButton(icon=MIcon('male.svg'), icon_checked=MIcon('male.svg', global_theme.get('male')), icon_only=False, checkable=True)
        button_male.setText('Male')

        button_lay = QHBoxLayout()
        button_lay.addWidget(button_trash)
        button_lay.addWidget(button_login)
        button_lay.addWidget(button_male)

        sub_lay1 = QHBoxLayout()
        sub_lay1.addWidget(button3)
        sub_lay1.addWidget(button4)
        sub_lay1.addWidget(button5)
        sub_lay1.addWidget(button6)
        sub_lay1.addStretch()
        sub_lay2 = QHBoxLayout()
        sub_lay2.addWidget(button2)
        sub_lay2.addWidget(button7)

        main_lay = QVBoxLayout()
        main_lay.addWidget(MDivider('different button_size'))
        main_lay.addLayout(sub_lay1)
        main_lay.addWidget(MDivider('disabled'))
        main_lay.addWidget(button2)
        main_lay.addWidget(MDivider('checkable'))
        main_lay.addWidget(button7)
        main_lay.addWidget(MDivider('text icon'))
        main_lay.addLayout(button_lay)
        main_lay.addStretch()
        self.setLayout(main_lay)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    test = MToolButtonTest()
    test.show()
    sys.exit(app.exec_())
