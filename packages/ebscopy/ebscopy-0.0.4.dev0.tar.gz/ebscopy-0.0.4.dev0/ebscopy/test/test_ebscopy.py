#!/usr/bin/python

from ebscopy import ebscopy
import unittest
from requests import HTTPError
import os
import re

class EnvironmentIsGoodTests(unittest.TestCase):
  def test_for_env_variables(self):
    self.assertGreater(len(os.environ['EDS_USER']), 0)
    self.assertGreater(len(os.environ['EDS_PASS']), 0)
    self.assertGreater(len(os.environ['EDS_PROFILE']), 0)
    self.assertGreater(len(os.environ['EDS_ORG']), 0)
    self.assertGreater(len(os.environ['EDS_GUEST']), 0)

class ExplicitConnectionTests(unittest.TestCase):
  # We want to strip out any environment variables so they don't get used
  def setUp(self):
    self.environ		= {}
    for env, value in os.environ.items():
       if re.match("EDS_", env):
         self.environ[env]	= value
         os.environ[env]	= ""

  # Gotta put them back!
  def tearDown(self):
    for env, value in self.environ.items():
      os.environ[env]		= value

  def test_good_explicit_connection_works(self):
    user_id		= self.environ.get("EDS_USER")
    password		= self.environ.get("EDS_PASS")
    profile		= self.environ.get("EDS_PROFILE")
    org			= self.environ.get("EDS_ORG")
    guest		= self.environ.get("EDS_GUEST")
    c			= ebscopy.Connection(user_id=user_id, password=password, profile=profile, org=org, guest=guest)
    c.connect()
    info		= c.info_data
    c.disconnect()
    self.assertIsNotNone(info)

  def test_bad_explicit_connection_breaks(self):
    with self.assertRaises(HTTPError):
      c			= ebscopy.Connection(user_id="betternotwork", password="betternotwork", profile="betternotwork", org="betternotwork", guest="n")
      c.connect()

  def test_missing_user_explicit_connection_breaks(self):
    with self.assertRaises(ValueError):
      c			= ebscopy.Connection(user_id="", password="", profile="", org="", guest="n")
      c.connect()

  def test_implict_connection_breaks(self):
    with self.assertRaises(ValueError):
      c			= ebscopy.Connection()
      c.connect()
# End of [ExplicitConnectionTests] class

class ImplicitConnectionTests(unittest.TestCase):
  def test_implicit_connection_works(self):
    c			= ebscopy.Connection()
    c.connect()
    info		= c.info_data
    c.disconnect()
    self.assertIsNotNone(info)

   # TODO: Do we need to test that an implicit connection with bad env variables doesn't work? I don't think so...

# End of [ImplicitConnectionTests] class

class SearchTests(unittest.TestCase):
  def test_search_results(self):
    c			= ebscopy.Connection()
    c.connect()
    res			= c.search("blue")

    self.assertGreater(res.stat_total_hits, 0)
    self.assertGreater(res.stat_total_time, 0)
    self.assertGreater(len(res.avail_facets_labels), 0)
    self.assertIsInstance(res.record[0], tuple)

    rec			= c.retrieve(res.record[0])

    self.assertIsInstance(rec, ebscopy.Record)
    self.assertIsInstance(rec.dbid, (unicode, str))
    self.assertIsInstance(rec.an, (unicode, str))
    self.assertIsInstance(rec.plink, (unicode, str))
    self.assertRegexpMatches(rec.plink, "^http://")
    
    c.disconnect()
# End of [SearchTests] class


class RecordTests(unittest.TestCase):
  def test_record_equality(self):
    c			= ebscopy.Connection()
    c.connect()
    res			= c.search("blue")

    rec_a		= c.retrieve(res.record[0])
    rec_b		= c.retrieve(res.record[0])
    rec_c		= c.retrieve(res.record[1])

    self.assertEqual(rec_a, rec_a)
    self.assertEqual(rec_a, rec_b)
    self.assertNotEqual(rec_a, rec_c)

    c.disconnect()
# End of [RecordTests] class

class MultiSessionTest(unittest.TestCase):
  def test_sessions(self):
    s1			= ebscopy.Session()
    s2			= ebscopy.Session()

    self.assertNotEqual(s1, s2)

    self.assertEqual(s1.connection, s2.connection)

    r1			= s1.search("blue")
    r2			= s2.search("blue")

    self.assertEqual(r1, r2)

    r3			= s1.search("red")
    r4			= s1.search("green")

    self.assertNotEqual(r3, r4)

    s1.end()

    r5			= s2.search("blue")
    self.assertEqual(r1, r5)

    s2.end()

    with self.assertRaises(HTTPError):
      r5		= s2.search("blue")


# End of [MultiSessionTest] class

# EOF
