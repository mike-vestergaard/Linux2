
from flask import config
from mysql.connector import connection
import hello
import unittest
import mysql.connector




# def test_sample_single_word():
#     l = ('foo', 'bar', 'foobar')
#     word = hello.sample(l)
#     assert word in l

class TestConnection(unittest.TestCase):
    """Oracle MySQL for Python Connector tests."""

    connection = None
    # conn = mysql.connection
    # cursor = conn.cursor()
    # connection = mysql.connector.connect(
    #     user = 'root',
    #     password = 'password',
    #     host = 'localhost',
    #     database = 'test'
    #     auth_plugin = 'mysql_native_password'
    # )

    # def setUp(self):
    #     self.connection = mysql.connector.connect(**connection)

    def setUp(self):
        config = mysql.connector.connect(
            user = 'root',
            password = 'password',
            host = 'localhost',
            database = 'our_users',
            auth_plugin = 'mysql_native_password'
        )
        self.connection = mysql.connector.connect(**config())   

#mysql.connector.connect

    def tearDown(self):
        if self.connection is not None and self.connection.is_connected():
            self.connection.close()

    def test_connection(self):
        self.assertTrue(self.connection.is_connected())

if __name__ == '__main__':
    unittest.main()
