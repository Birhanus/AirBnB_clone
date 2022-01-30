#!/usr/bin/python3
"""base model tests module"""
from unittest import TestCase
import json
import re
from uuid import UUID, uuid4
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModel(TestCase):
    ''' tests BaseModel class '''
    def test_3(self):
        ''' task 0 tests '''
        obj = BaseModel()
