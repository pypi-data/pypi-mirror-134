# -*- coding: utf-8 -*-
# @Author   : Ecohnoch(xcy)
# @File     : __init__.py.py
# @Function : TODO

from code2api.loginInstance import login
from code2api.algorithms.face_recognition import face_recognition
from code2api.algorithms.face_detection import face_detection
from code2api.algorithms.face_attribute import face_attribute
from code2api.algorithms.speaker_recognition import speaker_recognition
from code2api.algorithms.face_generation import face_generation
from code2api.algorithms.random_number import random_number
from code2api.algorithms.remove_bg import remove_bg

from code2api.algorithms.new_algorithm import new_algorithm
from code2api.algorithms.cod_cpd import cod_cpd
from code2api.algorithms.salient_object_detection import salient_object_detection
from code2api.algorithms.landmark_detection import landmark_detection
from code2api.algorithms.binary_segmentation import binary_segmentation
from code2api.algorithms.face_attribute_x import face_attribute_x
from code2api.algorithms.text_generation import text_generation
from code2api.algorithms.github_avatar_generation import github_avatar_generation
from code2api.algorithms.anime_gan_v2 import anime_generation
from code2api.algorithms.maze_generation import maze_generation
from code2api.algorithms.hrnet_landmark_detection import hrnet_landmark_detection
from code2api.algorithms.textbox import textbox_generate_sentence
from code2api.algorithms.sod import sod


from code2api.scripts.algorithm_scripts.algorithms import parse_algorithm
from code2api.scripts.enroll_service import enroll

__version__ = 'v1.1.5'
__author__  = 'Ecohnoch'
__email__   = 'chuyuan@code2api.club'