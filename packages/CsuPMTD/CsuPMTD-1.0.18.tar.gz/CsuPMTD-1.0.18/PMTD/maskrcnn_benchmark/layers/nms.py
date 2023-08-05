# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved.
# from ._utils import _C
import ctypes
import os
abPath = os.path.abspath(__file__)
_C = ctypes.CDLL(abPath[0:-14] + '/_C.cpython-36m-x86_64-linux-gnu.so')

from PMTD.maskrcnn_benchmark.apex.apex import amp

# Only valid with fp32 inputs - give AMP the hint
nms = amp.float_function(_C.nms)

# nms.__doc__ = """
# This function performs Non-maximum suppresion"""
