#-*- coding: utf-8 -*
import sys
import os
script_path = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, script_path+"/../")
import juicypipe
import unittest
import StringIO
import pipe
import shutil

class JuicypipeTest(unittest.TestCase):
    def setUp(self):
        self.DATA_DIR = script_path+"/dummy_data"
        os.mkdir(self.DATA_DIR)

    def tearDown(self):
        shutil.rmtree(self.DATA_DIR)


    def test_json_load(self):
        filepath = self.DATA_DIR + "/json_dummy.json"
        with open(filepath, "w+") as f:
            f.write("\n".join([
                '{"name": "Alice", "age": 26}',
                '{"name": "Bob", "age": 3}'
            ]))
        self.assertEqual(
            len(juicypipe.json_load(filepath) | pipe.as_list),
            2
        )
        self.assertDictEqual(
            juicypipe.json_load(filepath)|pipe.first,
            {u"name": u"Alice", u"age": 26}
        )

    def test_json_dump(self):
        """json_dumpで出力してjson_loadで復元できる"""
        filepath = self.DATA_DIR + "/json_dummy.json"
        source = [
            {u"place": u"Tokyo", u"times": 5},
            {u"place": u"Sapporo", u"times": 3},
            {u"place": u"Sendai", u"times": 14},
            {u"place": u"Fukuoka", u"times": 1}
        ]
        source | juicypipe.json_dump(filepath)
        self.assertEqual(
            len(juicypipe.json_load(filepath) | pipe.as_list ),
            4
        )
        self.assertEqual(
            juicypipe.json_load(filepath) | pipe.first,
            source[0]
        )
