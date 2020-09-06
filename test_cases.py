import os
import unittest
import json
from flaskr import create_app
from models import Account, setup_db, db


class AccountTestCase(unittest.TestCase):
    """This class represents the resource test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "bank_test"
        self.db = db
        # self.database_path = "postgres://{}:{}@{}/{}".format(
            # 'santarabantoosoo', 123, 'localhost:5432', self.database_name)
        database_path = 'postgresql://postgres:123456@localhost:5432/{}'.format(self.database_name)
        setup_db(self.app, database_path)

        self.new_account = {
            'first_name': "Omar",
            'last_name': "Gaber",
            'balance': 5000
        }
        with self.app.app_context():
            new_account = Account(**self.new_account)
            self.db.session.add(new_account)
            self.db.session.commit()

    def tearDown(self):
        """Executed after each test"""
        pass


    # TODO add tests for endpoints and errors.  
    def test_get_all_accounts(self):
        res = self.client().get('/accounts')
        data = json.loads(res.data)
        self.assertTrue(data['accounts'])
        self.assertEqual(res.status_code, 200)

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()



