"""
WiP.

Soon.
"""

# region [Imports]

import os
import re
import sys
import json
import queue
import math
import base64
import pickle
import random
import shelve
import dataclasses
import shutil
import asyncio
import logging
import sqlite3
import platform
import importlib
import subprocess
import inspect

from time import sleep, process_time, process_time_ns, perf_counter, perf_counter_ns
from io import BytesIO, StringIO
from abc import ABC, ABCMeta, abstractmethod
from copy import copy, deepcopy
from enum import Enum, Flag, auto, unique
from time import time, sleep
from pprint import pprint, pformat
from pathlib import Path
from string import Formatter, digits, printable, whitespace, punctuation, ascii_letters, ascii_lowercase, ascii_uppercase
from timeit import Timer
from typing import TYPE_CHECKING, Union, Callable, Iterable, Optional, Mapping, Any, IO, TextIO, BinaryIO, Hashable, Generator, Literal, TypeVar, TypedDict, AnyStr
from zipfile import ZipFile, ZIP_LZMA
from datetime import datetime, timezone, timedelta
from tempfile import TemporaryDirectory
from textwrap import TextWrapper, fill, wrap, dedent, indent, shorten
from functools import wraps, partial, lru_cache, singledispatch, total_ordering, cached_property
from importlib import import_module, invalidate_caches
from contextlib import contextmanager, asynccontextmanager, nullcontext, closing, ExitStack, suppress
from statistics import mean, mode, stdev, median, variance, pvariance, harmonic_mean, median_grouped
from collections import Counter, ChainMap, deque, namedtuple, defaultdict
from urllib.parse import urlparse
from importlib.util import find_spec, module_from_spec, spec_from_file_location
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from importlib.machinery import SourceFileLoader
from weakref import WeakSet

import PySide6


from PySide6.QtCore import (QByteArray, QTimer, QCoreApplication, QDate, QDateTime, QEvent, QLocale, QMetaObject, QModelIndex, QModelRoleData, QMutex,
                            QMutexLocker, QObject, QPoint, QRect, QRecursiveMutex, QRunnable, QSettings, QSize, QThread, QThreadPool, QTime, QUrl,
                            QWaitCondition, Qt, QAbstractItemModel, QAbstractListModel, QAbstractTableModel, Signal, Slot)

from PySide6.QtGui import (QAction, QBrush, QColor, QGuiApplication, QConicalGradient, QCursor, QFont, QFontDatabase, QFontMetrics, QGradient, QIcon, QImage,
                           QKeySequence, QLinearGradient, QPainter, QPalette, QPixmap, QRadialGradient, QTransform)

from PySide6.QtWidgets import (QApplication, QBoxLayout, QCheckBox, QColorDialog, QColumnView, QComboBox, QDateTimeEdit, QDialogButtonBox,
                               QDockWidget, QDoubleSpinBox, QFontComboBox, QFormLayout, QFrame, QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
                               QLCDNumber, QLabel, QLayout, QLineEdit, QListView, QListWidget, QMainWindow, QMenu, QMenuBar, QMessageBox,
                               QProgressBar, QProgressDialog, QPushButton, QSizePolicy, QSpacerItem, QSpinBox, QStackedLayout, QStackedWidget,
                               QStatusBar, QStyledItemDelegate, QSystemTrayIcon, QTabWidget, QTableView, QTextEdit, QTimeEdit, QToolBox, QTreeView,
                               QVBoxLayout, QWidget, QAbstractItemDelegate, QAbstractItemView, QAbstractScrollArea, QRadioButton, QFileDialog, QButtonGroup)
from gidapptools.gidapptools_qt.resources.placeholder import QT_PLACEHOLDER_IMAGE
from gidapptools.gidapptools_qt.debug.event_analyzer import EventAnalyzer, JsonOutputter
if TYPE_CHECKING:
    from gidapptools.gidapptools_qt.resources.resources_helper import PixmapResourceItem
    from gidapptools.meta_data.interface import MetaInfo
# endregion[Imports]

# region [TODO]


# endregion [TODO]

# region [Logging]


# endregion[Logging]

# region [Constants]

THIS_FILE_DIR = Path(__file__).parent.absolute()

# endregion[Constants]


class GidQtApplication(QApplication):

    def __init__(self,
                 argvs: list[str] = sys.argv,
                 icon: Union["PixmapResourceItem", QPixmap, QImage, str, QIcon] = None):
        super().__init__(self.argv_hook(argvs))
        self.main_window: QMainWindow = None
        self.sys_tray: QSystemTrayIcon = None
        self.icon = self._icon_conversion(icon)
        self.extra_windows = WeakSet()

    @classmethod
    def with_pre_flags(cls,
                       argvs: list[str] = sys.argv,
                       icon: Union["PixmapResourceItem", QPixmap, QImage, str, QIcon] = None,
                       pre_flags: dict[Qt.ApplicationAttribute:bool] = None,
                       desktop_settings_aware: bool = True):
        QGuiApplication.setDesktopSettingsAware(desktop_settings_aware)
        for flag, value in pre_flags.items():
            cls.setAttribute(flag, value)
        return cls(argvs=argvs, icon=icon)

    def setup(self) -> "GidQtApplication":
        self.setWindowIcon(self.icon)
        return self

    def argv_hook(self, argvs: list[str]) -> list[str]:
        return argvs

    @staticmethod
    def _icon_conversion(icon: Union["PixmapResourceItem", QPixmap, QImage, str, QIcon] = None) -> Optional[QIcon]:
        if icon is None:
            return QT_PLACEHOLDER_IMAGE.icon

        if isinstance(icon, QIcon):
            return icon

        if isinstance(icon, (QPixmap, QImage, str)):
            return QIcon(icon)

        return icon.get_as_icon()

    def show_about_qt(self) -> None:
        self.aboutQt()

    def _get_about_text(self) -> str:
        text_parts = {"Name": self.applicationDisplayName(),
                      "Author": self.organizationName(),
                      "Link": f'<a href="{self.organizationDomain()}">{self.organizationDomain()}</a>',
                      "Version": self.applicationVersion()}

        return '<br>'.join(f"<b>{k:<20}:</b>{v:>50}" for k, v in text_parts.items())

    def show_about(self) -> None:
        title = f"About {self.applicationDisplayName()}"
        text = self._get_about_text()
        QMessageBox.about(self.main_window, title, text)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.applicationDisplayName()!r})"


# region[Main_Exec]
if __name__ == '__main__':
    app = GidQtApplication(sys.argv)
    m = QMainWindow()
    m.show()
    app.exec_()

# endregion[Main_Exec]
