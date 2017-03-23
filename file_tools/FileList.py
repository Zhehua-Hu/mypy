#!/usr/bin/env python
# coding=utf-8
"""
Provide FileList Class
"""

import os
import argparse


def get_contained_files(folder, search_type="NotRecursive",
                        suffix_filter=None, include_hidden=False):
    """
        Get Contained files
    :param folder:
    :param search_type:
    :param suffix_filter:
    :param include_hidden:
    :return:
    """

    _files_path = []
    _ret_files_path = []
    _suffix_filter = []

    # Make suffix to be ALL upper
    if suffix_filter != None:
        for item in suffix_filter:
            _suffix_filter.append(item.upper())

    if search_type != "Recursive":
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            if os.path.isfile(file_path):
                if len(_suffix_filter) != 0:
                    if file_path.split(".")[-1].upper() in _suffix_filter:
                        _files_path.append(file_path)
                else:
                    _files_path.append(file_path)
    else:
        for root, dirs, filenames in os.walk(folder):
            for filename in filenames:
                if not include_hidden:
                    if not filename.startswith('.'):  # not hiden file in Linux
                        if len(_suffix_filter) != 0:
                            if filename.split(".")[-1].upper() in _suffix_filter:
                                _files_path.append(os.path.join(root, filename))
                        else:
                            _files_path.append(os.path.join(root, filename))
                else:
                    if len(_suffix_filter) != 0:
                        if filename.split(".")[-1].upper() in _suffix_filter:
                            _files_path.append(os.path.join(root, filename))
                    else:
                        _files_path.append(os.path.join(root, filename))

    _files_path.sort()  # sort to increase'

    if include_hidden:
        _ret_files_path = _files_path
    else:
        for item in _files_path:
            satisfied = True
            for piece in item.split(os.sep):
                if piece.startswith('.'):
                    satisfied = False
            if satisfied:
                _ret_files_path.append(item)

    return _ret_files_path, len(_ret_files_path)


class FileList:
    """
    class: provide file(eg.images,videos) list management
    """

    _cur_idx = 0
    _file_cnt = 0

    def __init__(self, folder, search_type="NotRecursive",
                 suffix_filter=None, include_hidden=False):
        self.dirname = folder
        self._files_path, self._file_cnt = get_contained_files(folder,
                                                               search_type=search_type,
                                                               suffix_filter=suffix_filter,
                                                               include_hidden=include_hidden)

    def get_files_path_list(self):
        return self._files_path

    def first_file(self):
        return self._files_path[0]

    def next_file(self):
        self._cur_idx += 1
        self._cur_idx = self.safe_limit(self._cur_idx)
        return self._files_path[self._cur_idx]

    def previous_file(self):
        self._cur_idx -= 1
        self._cur_idx = self.safe_limit(self._cur_idx)
        return self._files_path[self._cur_idx]

    def get_cur_file_path(self):
        return self._files_path[self._cur_idx]

    def safe_limit(self, idx):
        if idx > self._file_cnt - 1:
            return self._file_cnt - 1
        elif idx < 0:
            return 0
        else:
            return idx

    def is_empty(self):
        if self._file_cnt > 0:
            return False
        else:
            return True

    def __repr__(self):
        for item in self.__dict__.items():
            print("%s : %s" % item)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("files_path_arg", help="Path of files", type=str)
    args = parser.parse_args()
    flist = FileList(args.files_path_arg)

## Test
    # test_path = "/home/zhehua/Github/mypy/test/file_tools/FileList"

    # flist = FileList(test_path, search_type="Recursive")
    # flist = FileList(test_path, search_type="Recursive", include_hidden=True)
    # flist = FileList(test_path, search_type="Recursive", include_hidden=True, suffix_filter=["Txt"])
    # flist = FileList(test_path, search_type="NotRecursive")
    # flist = FileList(test_path, search_type="NotRecursive", include_hidden=True)
    # flist = FileList(test_path, search_type="NotRecursive", include_hidden=True, suffix_filter=["Txt"])

    # for item in flist.get_files_path_list():
    #     print(item)
