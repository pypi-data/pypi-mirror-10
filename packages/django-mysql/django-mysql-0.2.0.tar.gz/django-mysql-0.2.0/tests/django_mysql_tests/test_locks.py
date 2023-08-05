# -*- coding:utf-8 -*-
from threading import Thread

from django.db import connection
from django.test import TestCase
from django.utils.six.moves import queue

from django_mysql.exceptions import TimeoutError
from django_mysql.locks import Lock


class LockTests(TestCase):

    @classmethod
    def setUpClass(cls):
        super(LockTests, cls).setUpClass()

        cls.supports_lock_info = (
            connection.is_mariadb and connection.mysql_version >= (10, 0, 7)
        )
        if cls.supports_lock_info:
            with connection.cursor() as cursor:
                cursor.execute(
                    """SELECT COUNT(*) FROM INFORMATION_SCHEMA.PLUGINS
                       WHERE PLUGIN_NAME = 'metadata_lock_info'""")
                cls.lock_info_preinstalled = (cursor.fetchone()[0] > 0)
                if not cls.lock_info_preinstalled:
                    cursor.execute("INSTALL SONAME 'metadata_lock_info'")

    @classmethod
    def tearDownClass(cls):
        if cls.supports_lock_info and not cls.lock_info_preinstalled:
            with connection.cursor() as cursor:
                cursor.execute("UNINSTALL SONAME 'metadata_lock_info'")
        super(LockTests, cls).tearDownClass()

    def test_simple(self):
        mylock = Lock("mylock")
        self.assertFalse(mylock.is_held())

        with mylock:
            self.assertTrue(mylock.is_held())
            self.assertTrue(Lock("mylock").is_held())

            cursor = connection.cursor()
            cursor.execute("SELECT CONNECTION_ID();")
            own_connection_id = cursor.fetchone()[0]
            self.assertEqual(mylock.holding_connection_id(),
                             own_connection_id)

        self.assertFalse(mylock.is_held())
        self.assertFalse(Lock("mylock").is_held())

    import_time_lock = Lock('defined_at_import_time')

    def test_error_on_unneeded_exit(self):
        mylock = Lock("mylock")
        self.assertFalse(mylock.is_held())
        with self.assertRaises(ValueError) as cm:
            mylock.__exit__(None, None, None)
        self.assertIn("unheld lock", str(cm.exception))

    def test_defined_at_import_time(self):
        import_time_lock = self.import_time_lock

        self.assertFalse(import_time_lock.is_held())

        with import_time_lock:
            self.assertTrue(import_time_lock.is_held())

            cursor = connection.cursor()
            cursor.execute("SELECT CONNECTION_ID();")
            own_connection_id = cursor.fetchone()[0]
            self.assertEqual(import_time_lock.holding_connection_id(),
                             own_connection_id)

        self.assertFalse(import_time_lock.is_held())

    def test_timeout_with_threads(self):
        to_me = queue.Queue()
        to_you = queue.Queue()

        def lock_until_told():
            with Lock('threading_test'):
                to_me.put("Locked")
                to_you.get(True)

        threading_test = Lock('threading_test', 0.05)
        self.assertTrue(not threading_test.is_held())

        other_thread = Thread(target=lock_until_told)
        other_thread.start()
        try:
            item = to_me.get(True)
            self.assertEqual(item, "Locked")

            cursor = connection.cursor()
            cursor.execute("SELECT CONNECTION_ID();")
            own_connection_id = cursor.fetchone()[0]

            self.assertTrue(threading_test.is_held())
            self.assertNotEqual(threading_test.holding_connection_id(),
                                own_connection_id)

            with self.assertRaises(TimeoutError):
                with threading_test:
                        pass

            to_you.put("Stop")
        finally:
            other_thread.join()

        self.assertFalse(threading_test.is_held())
        with threading_test:
            pass

    def test_threads_concurrent_access(self):
        """
        Test that the same lock object can be used in multiple threads, allows
        the definition of a lock upfront in a module.
        """
        to_me = queue.Queue()
        to_you = queue.Queue()
        the_lock = Lock('THElock', 0.05)

        def check_it_lock_it():
            self.assertFalse(the_lock.is_held())
            with the_lock:
                to_me.put("Locked")
                to_you.get(True)

        other_thread = Thread(target=check_it_lock_it)
        other_thread.start()
        try:
            item = to_me.get(True)
            self.assertEqual(item, "Locked")

            cursor = connection.cursor()
            cursor.execute("SELECT CONNECTION_ID()")
            own_connection_id = cursor.fetchone()[0]

            self.assertTrue(the_lock.is_held())
            self.assertNotEqual(the_lock.holding_connection_id(),
                                own_connection_id)

            with self.assertRaises(TimeoutError):
                with the_lock:
                    pass

            to_you.put("Stop")
        finally:
            other_thread.join()

        with the_lock:
            pass

    def test_holding_more_than_one(self):
        conn = connection
        supports_multiple_locks = (
            (conn.is_mariadb and conn.mysql_version >= (10, 0, 2)) or
            (not conn.is_mariadb and conn.mysql_version >= (5, 7))
        )
        if not supports_multiple_locks:
            self.skipTest(
                "Only MySQL 5.7+ and MariaDB 10.0.2+ have the ability to hold "
                "more than one named lock"
            )

        lock_a = Lock("a")
        lock_b = Lock("b")
        with lock_a, lock_b:
            self.assertTrue(lock_a.is_held())

    def test_multi_connection(self):
        lock_a = Lock("a")
        lock_b = Lock("b", using='other')

        with lock_a, lock_b:
            # Different connections = can hold > 1!
            self.assertTrue(lock_a.is_held())
            self.assertTrue(lock_b.is_held())

    def test_held_with_prefix(self):
        if not self.supports_lock_info:
            self.skipTest(
                "Only MariaDB 10.0.7+ has the metadata_lock_info plugin on "
                "which held_with_prefix relies"
            )

        self.assertEqual(Lock.held_with_prefix(''), {})
        self.assertEqual(Lock.held_with_prefix('mylock'), {})

        with Lock('mylock-alpha') as lock:
            self.assertEqual(
                Lock.held_with_prefix(''),
                {'mylock-alpha': lock.holding_connection_id()}
            )
            self.assertEqual(
                Lock.held_with_prefix('mylock'),
                {'mylock-alpha': lock.holding_connection_id()}
            )
            self.assertEqual(
                Lock.held_with_prefix('mylock-beta'),
                {}
            )

        self.assertEqual(Lock.held_with_prefix(''), {})
        self.assertEqual(Lock.held_with_prefix('mylock'), {})
