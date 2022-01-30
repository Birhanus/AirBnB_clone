#!/usr/bin/python3
""" file_storage tests module s"""
from unittest import TestCase
import json
import re
from uuid import UUID, uuid4
from datetime import datetime
from time import sleep
import os

from models import storage, BaseModel, FileStorage


class TestFileStorage(TestCase):
    ''' tests FileStorage class '''
    def test_5(self):
        ''' tests task 4 '''
        FS_dict = FileStorage.__dict__
        FS__path = '_FileStorage__file_path'
        FS__objs = '_FileStorage__objects'
        FS_path = FS_dict[FS__path]
        FS_objs = FS_dict[FS__objs]

        self.assertTrue(type(FS_path) is str and FS_path)
        self.assertTrue(type(FS_objs) is dict)
        self.assertTrue(getattr(storage, FS__path))
        self.assertTrue(getattr(storage, FS__objs) is storage.all())

        FS_objs.clear()

        oobjs = storage.all()
        oobjs_cp = oobjs.copy()
        obj = BaseModel()
        storage.new(obj)
        self.assertTrue(oobjs is storage.all())
        self.assertEqual(len(oobjs.keys()), 1)
        self.assertTrue(set(storage.all().keys())
                        .difference(set(oobjs_cp.keys())) ==
                        {'BaseModel.{}'.format(obj.id)})

        oobjs_cp = oobjs.copy()
        # storage.new(obj)
        self.assertTrue(oobjs is storage.all())
        self.assertEqual(oobjs, oobjs_cp)

        obj = BaseModel()
        storage.new(obj)
        self.assertEqual(len(oobjs.keys()), 2)

        # check serialization
        oobjs_cp = oobjs.copy()
        storage.save()
        self.assertTrue(os.path.isfile(FS_path))
        with open(FS_path, 'r') as file:
            js_objs = json.load(file)
            self.assertTrue(type(js_objs) is dict)
            self.assertEqual(len(js_objs.keys()), 2)
            self.assertTrue(all(v in oobjs.keys() for v in js_objs.keys()))
        storage.all().clear()
        storage.reload()

        for k, v in oobjs_cp.items():
            oobjs_cp[k] = v.to_dict()
        oobjs_cp2 = storage.all().copy()
        for k, v in oobjs_cp2.items():
            oobjs_cp2[k] = v.to_dict()
        self.assertEqual(oobjs_cp, oobjs_cp2)

        oobjs_cp = storage.all().copy()
        os.remove(FS_path)
        storage.reload()
        self.assertEqual(oobjs_cp, storage.all())

        obj = BaseModel()
        kid = 'BaseModel.{}'.format(obj.id)
        self.assertTrue(kid in storage.all() and storage.all()[kid] is obj)
        sleep(.01)
        now = datetime.utcnow()
        obj.updated_at = now
        obj.save()
        storage.all().clear()
        storage.reload()
        oobjs = storage.all()
        storage.reload()  # insignificant reload
        oobjs2 = storage.all()

        self.assertEqual(obj.to_dict(), storage.all()[kid].to_dict())
        self.assertFalse(obj is storage.all()[kid].to_dict())
        obj = BaseModel(1, 2, 3)
        kid = 'BaseModel.{}'.format(obj.id)
        self.assertTrue(kid in storage.all() and storage.all()[kid] is obj)

        obj = BaseModel(id=str(uuid4()), created_at=now.isoformat(),
                        updated_at=now.isoformat())
        kid = 'BaseModel.{}'.format(obj.id)
        self.assertFalse(kid in storage.all())
        self.assertFalse(obj in storage.all().values())
