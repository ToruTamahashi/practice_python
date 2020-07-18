import unittest
import unittest_practice

releas_name = 'lesson'

class CalTest(unittest.TestCase):
    def setUp(self):
        """ 各テストの前に実行"""
        print('setup')
        self.cal = unittest_practice.Cal()

    def tearDown(self):
        """各テストの後に実行"""
        print('clean up')
        del self.cal

    # テストをスキップしたいときは↓のアノテーション
    #@unittest.skip('skip!')
    @unittest.skipIf(releas_name == 'lesson', 'skip')
    def test_add_num_and_double(self):
        cal = unittest_practice.Cal()
        # asseertEqual:TestCase内のメソッド,期待する値と戻り値が同じかテスト
        # 第一引数にテスト対象
        # 第二引数に期待する値をセット
        self.assertEqual(
            cal.add_num_and_double(1, 1),
            4
        )

    def test_add_num_and_double_raise(self):
        # 例外処理が機能しているか(ValueErrorを吐くか)テスト
        # 正常に例外メッセージが出されればok
        cal = unittest_practice.Cal()
        with self.assertRaises(ValueError):
            cal.add_num_and_double('1', '1')

