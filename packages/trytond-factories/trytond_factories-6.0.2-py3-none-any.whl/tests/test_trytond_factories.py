
import unittest

from trytond.tests.test_tryton import DB_NAME
from trytond.tests.test_tryton import db_exist
from trytond.tests.test_tryton import create_db
from trytond.tests.test_tryton import restore_db_cache
from trytond.tests.test_tryton import backup_db_cache
from trytond.tests.test_tryton import with_transaction
from trytond.transaction import Transaction
from trytond.pool import Pool

from trytond_factories.company import Company

MODULES = [
    'account',
    'account_invoice',
    'company',
    'party',
]


class TrytondFactoriesTestCase(unittest.TestCase):
    'Test Trytond Factories'

    @classmethod
    def setUpClass(cls):
        # FIXME: Cache database is based on installed modules that is the
        # result of joining all class variables from test cases. The fact of
        # not using classical suite test forces to build database, activate
        # modules and backup it manually.
        if not db_exist(DB_NAME) and restore_db_cache('test-cache'):
            return
        create_db(lang='en')
        with Transaction().start(DB_NAME, 1, close=True) as transaction:
            pool = Pool()
            Module = pool.get('ir.module')

            records = Module.search([
                    ('name', 'in', MODULES),
                    ])
            assert len(records) == len(MODULES)

            records = Module.search([
                    ('name', 'in', MODULES),
                    ('state', '!=', 'activated'),
                    ])

            if records:
                Module.activate(records)
                transaction.commit()

                ActivateUpgrade = pool.get(
                    'ir.module.activate_upgrade',
                    type='wizard'
                )
                instance_id, _, _ = ActivateUpgrade.create()
                transaction.commit()
                ActivateUpgrade(instance_id).transition_upgrade()
                ActivateUpgrade.delete(instance_id)
                transaction.commit()
        backup_db_cache('test-cache')

    @with_transaction()
    def test_company(self):
        """Test Company factory"""
        company = Company.create(party__name='A')
        self.assertEqual(company.party.name, 'A')
