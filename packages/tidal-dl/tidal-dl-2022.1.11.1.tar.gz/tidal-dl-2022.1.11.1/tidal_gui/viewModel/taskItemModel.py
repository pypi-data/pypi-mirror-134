#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :  taskItemModel.py
@Date    :  2021/9/14
@Author  :  Yaronzz
@Version :  1.0
@Contact :  yaronhuang@foxmail.com
@Desc    :
"""
import _thread
import os

import aigpy.stringHelper
from tidal_dl import Type
from tidal_dl.model import Album, Track, Video, Playlist

from tidal_gui.tidalImp import tidalImp
from tidal_gui.view.taskItemView import TaskItemView
from tidal_gui.viewModel.viewModel import ViewModel
from tidal_gui.viewModel.downloadItemModel import DownloadItemModel
from PyQt5.QtWidgets import QListWidget, QListWidgetItem, QWidget, QScrollArea, QVBoxLayout, QPushButton
import time


class TaskItemModel(ViewModel):
    def __init__(self, data):
        super(TaskItemModel, self).__init__()
        self.view = TaskItemView()
        self.data = data
        self.downloadModelList = []
        self.path = ''

        if isinstance(data, Album):
            self.__initAlbum__(data)
        elif isinstance(data, Track):
            self.__initTrack__(data)
        elif isinstance(data, Video):
            self.__initVideo__(data)
        elif isinstance(data, Playlist):
            self.__initPlaylist__(data)

        self.view.connectButton('retry', self.__btnFuncRetry__)
        self.view.connectButton('cancel', self.__btnFuncCancel__)
        self.view.connectButton('delete', self.__btnFuncDelete__)
        self.view.connectButton('open', self.__btnFuncOpen__)

        self.SIGNAL_REFRESH_VIEW.connect(self.__refresh__)

    def __refresh__(self, stype: str, text: str):
        if stype == "setPic":
            self.view.setPic(text)
        elif stype == "addListItem":
            for index, item in enumerate(text):
                downItem = DownloadItemModel(index + 1, item, self.path)
                self.view.addListItem(downItem.view)
                self.downloadModelList.append(downItem)

    def __btnFuncRetry__(self):
        for item in self.downloadModelList:
            item.retry()

    def __btnFuncCancel__(self):
        for item in self.downloadModelList:
            item.stopDownload()

    def __btnFuncDelete__(self):
        for item in self.downloadModelList:
            item.stopDownload()

    def __btnFuncOpen__(self):
        if self.path == '':
            return
        if os.path.exists(self.path):
            os.startfile(self.path)

    def __initAlbum__(self, data: Album):
        self.path = tidalImp.getBasePath(data)
        
        title = data.title
        desc = f"by {tidalImp.getArtistsNames(data.artists)} " \
               f"{tidalImp.getDurationString(data.duration)} " \
               f"Track-{data.numberOfTracks} " \
               f"Video-{data.numberOfVideos}"
        self.view.setLabel(title, desc)

        def __thread_func__(model: TaskItemModel, album: Album):
            cover = tidalImp.getCoverData(album.cover, '1280', '1280')
            model.SIGNAL_REFRESH_VIEW.emit('setPic', cover)

            msg, tracks, videos = tidalImp.getItems(album.id, Type.Album)
            if not aigpy.stringHelper.isNull(msg):
                model.view.setErrmsg(msg)
                return

            model.SIGNAL_REFRESH_VIEW.emit('addListItem', tracks + videos)
            print('__initAlbum__')
            time.sleep(1)

        _thread.start_new_thread(__thread_func__, (self, data))

    def __initTrack__(self, data: Track):
        pass

    def __initVideo__(self, data: Video):
        pass

    def __initPlaylist__(self, data: Playlist):
        pass
