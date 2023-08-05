import unittest
import pytest
from bson import DBRef, ObjectId

from mongodantic.models import MongoModel
from mongodantic.types import RefrerenceType
from mongodantic import connect


class TestBasicOperation(unittest.TestCase):
    def setUp(self):
        connect("mongodb://127.0.0.1:27017", "test")

        class User(MongoModel):
            name: str
            email: str

        class Company(MongoModel):
            user: RefrerenceType[User]
            name: str

        User.Q.drop_collection(force=True)
        Company.Q.drop_collection(force=True)
        self.User = User
        self.Company = Company
        
    def test_single_reference_one(self):
        user = self.User(name='admin', email='admin')
        user.save()
        
        company = self.Company(user=user, name='test')
        company.save()
        user_company = self.Company.Q.find_one(user=user)
        print('user - ', user_company.user)
        assert 1 != 1
        assert user_company is not None
        assert user_company._id == company._id
        # assert user_company.user._id == company.user._id
        # assert user_company.user.email == company.user.email