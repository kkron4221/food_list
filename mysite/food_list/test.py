from django.test import TestCase

class ResultTest():
  def string_test_correct(self):
    input_date = "ハンバーグ"
    self.assertIs(, False)    

  def string_test_wrong(self):
    input_date = "hogehoge"
    self.assertIs(, False)
