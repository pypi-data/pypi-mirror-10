import unittest
import oi


class TestOi(unittest.TestCase):

    def setUp(self):
        self.address = 'ipc:///tmp/test-programd.sock'
        self.p = oi.Program('programd', self.address)
        self.ctl = oi.CtlProgram('programctl', self.address)

    def tearDown(self):
        self.p.service.sock.close()
        self.ctl.client.sock.close()

    # --------------------------------------

    def test_new_program(self):
        self.assertIsNotNone(self.p)

    def test_new_ctl(self):
        self.assertIsNotNone(self.ctl)

    def test_add_command_for_program(self):
        self.p.add_command('test', lambda p: 'test')

    def test_add_local_command_for_ctl(self):
        self.ctl.add_command('test', lambda p: 'test')
        dest, res, err = self.ctl.call('test')

        self.assertEqual(dest, 'local')
        self.assertEqual(res, 'test')
        self.assertIsNone(err)

    def test_parse_config(self):
        self.p.config.read('./test/test_config.conf')
        c = self.p.config
        self.assertTrue('repo.01' in c.sections())
        self.assertEqual(c.get('repo.01', 'user'), 'abc')
        self.assertEqual(c.getint('repo.01', 'port'), 1234)

    def test_parse_input(self):
        tests = [
            (' 1 2 "3 4" 5 "6 7"', ('1', ['2', '3 4', '5', '6 7'])),
            ('ping', ('ping', []))
        ]
        for text, expected in tests:
            res = self.ctl.parse_input(text)
            self.assertEqual(res, expected)


class TestState(unittest.TestCase):

    def setUp(self):
        self.state = oi.State()

    def test_set_get(self):
        self.state.hello = 'world'
        self.assertEqual(self.state.hello, 'world')
