#!/usr/bin/env python
# !-*-coding:utf-8 -*-
# !@Time    :2022/1/12 15:20
# !@Author  : murInj
# !@Filer    : .py
class chessEnv:
    # TODO:init
    def __init__(self, chessName):
        pass

    def __getActionSpace(self):
        pass

    def __getObserveSpace(self):
        pass

    def __step(self):
        pass

    def __gender(self):
        pass

    def __reset(self):
        pass

    def __isTerminal(self):
        pass

    def __beforeUpdate(self):
        pass

    def __afterUpdate(self):
        pass

    def __gameoverInfo(self):
        pass

    def __gameoverUpdate(self):
        pass

    def __oneRound(self):
        self.__reset()
        while not self.__isTerminal():
            self.__beforeUpdate()
            self.__step()
            self.__gender()
            self.__afterUpdate()
        self.__gameoverInfo()
        self.__gameoverUpdate()
