#!/usr/bin/python3
""" Module for testing file storage"""
import MySQLdb
import unittest
from models.base_model import BaseModel
from models import storage
import os


class test_fileStorage(unittest.TestCase):
    """ Class to test the file storage method """

    def setUp(self):
        """ Set up test environment """
        del_list = []
        for key in storage._FileStorage__objects.keys():
            del_list.append(key)
        for key in del_list:
            del storage._FileStorage__objects[key]

    def tearDown(self):
        """ Remove storage file at end of tests """
        try:
            os.remove('file.json')
        except:
            pass

    def test_obj_list_empty(self):
        """ __objects is initially empty """
        self.assertEqual(len(storage.all()), 0)

    def test_new(self):
        """ New object is correctly added to __objects """
        new = BaseModel()
        for obj in storage.all().values():
            temp = obj
        self.assertTrue(temp is obj)

    def test_all(self):
        """ __objects is properly returned """
        new = BaseModel()
        temp = storage.all()
        self.assertIsInstance(temp, dict)

    def test_base_model_instantiation(self):
        """ File is not created on BaseModel save """
        new = BaseModel()
        self.assertFalse(os.path.exists('file.json'))

    def test_empty(self):
        """ Data is saved to file """
        new = BaseModel()
        thing = new.to_dict()
        new.save()
        new2 = BaseModel(**thing)
        self.assertNotEqual(os.path.getsize('file.json'), 0)

    def test_save(self):
        """ FileStorage save method """
        new = BaseModel()
        storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload(self):
        """ Storage file is successfully loaded to __objects """
        new = BaseModel()
        storage.save()
        storage.reload()
        for obj in storage.all().values():
            loaded = obj
        self.assertEqual(new.to_dict()['id'], loaded.to_dict()['id'])

    @unittest.skip("Skipping test: reloading from an empty file")
    def test_reload_empty(self):
        """ Load from an empty file """
        with open('file.json', 'w') as f:
            pass
        with self.assertRaises(ValueError):
            storage.reload()

    @unittest.skip("Skipping test: reloading from an empty file")
    def test_reload_from_nonexistent(self):
        """ Nothing happens if file does not exist """
        self.assertEqual(storage.reload(), None)

    def test_base_model_save(self):
        """ BaseModel save method calls storage save """
        new = BaseModel()
        new.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_type_path(self):
        """ Confirm __file_path is string """
        self.assertEqual(type(storage._FileStorage__file_path), str)

    def test_type_objects(self):
        """ Confirm __objects is a dict """
        self.assertEqual(type(storage.all()), dict)

    def test_key_format(self):
        """ Key is properly formatted """
        new = BaseModel()
        _id = new.to_dict()['id']
        for key in storage.all().keys():
            temp = key
        self.assertEqual(temp, 'BaseModel' + '.' + _id)

    def test_storage_var_created(self):
        """ FileStorage object storage created """
        from models.engine.file_storage import FileStorage
        print(type(storage))
        self.assertEqual(type(storage), FileStorage)

    def test_create_state(self):
        """Test create State command in console"""
        db = MySQLdb.connect(host='localhost', user='hbnb_test', passwd='hbnb_test_pwd', db='hbnb_test_db')

        cursor = db.cursor()
        cursor.execute('SELECT COUNT(*) FROM states')
        initial_count = cursor.fetchone()[0]
    
        create State name="California"

        cursor.execute('SELECT COUNT(*) FROM states')
        updated_count = cursor.fetchone()[0]

        self.assertEqual(updated_count, initial_count + 1)

    def test_create_place(self):
        """Test create Place command in console"""
        db = MySQLdb.connect(host='localhost', user='hbnb_test', passwd='hbnb_test_pwd', db='hbnb_test_db')

        cursor = db.cursor()
        cursor.execute('SELECT COUNT(*) FROM places')
        initial_count = cursor.fetchone()[0]

        create Place city_id="0001" user_id="0001" name="My_little_house"
        
        cursor.execute('SELECT COUNT(*) FROM places')
        updated_count = cursor.fetchone()[0]

        self.assertEqual(updated_count, initial_count + 1)

    def test_create_user(self):
        """Test create User command in console"""
        db = MySQLdb.connect(host='localhost', user='hbnb_test', passwd='hbnb_test_pwd', db='hbnb_test_db')

        cursor = db.cursor()
        cursor.execute('SELECT COUNT(*) FROM users')
        initial_count = cursor.fetchone()[0]

        create User email="test@example.com" password="12345"

        cursor.execute('SELECT COUNT(*) FROM users')
        updated_count = cursor.fetchone()[0]

        self.assertEqual(updated_count, initial_count + 1)
