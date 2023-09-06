import unittest

from format import format

class TestRemoveDarkModeImages(unittest.TestCase):
    def test_only_darkmode(self) -> None:
        raw_text = \
'''
text before
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="darkmode_image_link">
</picture>
text after
'''
        expected_formatted_text = \
'''
text before
<picture>
</picture>
text after
'''
        self.assertEqual(expected_formatted_text, format(raw_text))
        
    def test_only_darkmode_shuffled_order(self) -> None:
        raw_text = \
'''
text before
<picture>
  <source srcset="darkmode_image_link" media="(prefers-color-scheme: dark)">
</picture>
text after
'''
        expected_formatted_text = \
'''
text before
<picture>
</picture>
text after
'''
        self.assertEqual(expected_formatted_text, format(raw_text))
        
    def test_no_darkmode(self) -> None:
        raw_text = \
'''
text before
<picture>
  <source media="(prefers-color-scheme: light)" srcset="lightmode_image_link">
</picture>
text after
'''
        expected_formatted_text = raw_text
        self.assertEqual(expected_formatted_text, format(raw_text))
        
    def test_empty(self) -> None:
        raw_text = \
'''
text before
<picture>
</picture>
text after
'''
        expected_formatted_text = raw_text
        self.assertEqual(expected_formatted_text, format(raw_text))
        
    def test_darkmode_at_the_beginnig(self) -> None:
        raw_text = \
'''
text before
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="darkmode_image_link">
  <source media="(prefers-color-scheme: light)" srcset="lightmode_image_link">
</picture>
text after
'''
        expected_formatted_text = \
'''
text before
<picture>
  <source media="(prefers-color-scheme: light)" srcset="lightmode_image_link">
</picture>
text after
'''
        self.assertEqual(expected_formatted_text, format(raw_text))
        
    def test_darkmode_at_the_end(self) -> None:
        raw_text = \
'''
text before
<picture>
  <source media="(prefers-color-scheme: light)" srcset="lightmode_image_link">
  <source media="(prefers-color-scheme: dark)" srcset="darkmode_image_link">
</picture>
text after
'''
        expected_formatted_text = \
'''
text before
<picture>
  <source media="(prefers-color-scheme: light)" srcset="lightmode_image_link">
</picture>
text after
'''
        self.assertEqual(expected_formatted_text, format(raw_text))
        
    def test_darkmode_in_the_middle(self) -> None:
        raw_text = \
'''
text before
<picture>
  <source media="(prefers-color-scheme: light)" srcset="lightmode_image_link">
  <source media="(prefers-color-scheme: dark)" srcset="darkmode_image_link">
  <img alt="alternative text" src="image_link">
</picture>
text after
'''
        expected_formatted_text = \
'''
text before
<picture>
  <source media="(prefers-color-scheme: light)" srcset="lightmode_image_link">
  <img alt="alternative text" src="image_link">
</picture>
text after
'''
        self.assertEqual(expected_formatted_text, format(raw_text))
        
    def test_darkmode_with_tabs(self) -> None:
        raw_text = \
'''
text before
<picture>
\t<source media="(prefers-color-scheme: light)" srcset="lightmode_image_link">
\t<source media="(prefers-color-scheme: dark)" srcset="darkmode_image_link">
\t<img alt="alternative text" src="image_link">
</picture>
text after
'''
        expected_formatted_text = \
'''
text before
<picture>
\t<source media="(prefers-color-scheme: light)" srcset="lightmode_image_link">
\t<img alt="alternative text" src="image_link">
</picture>
text after
'''
        self.assertEqual(expected_formatted_text, format(raw_text))
        
    def test_darkmode_with_ignore_comment(self) -> None:
        raw_text = \
'''
text before
<!-- setup: let darkmode -->
<picture>
  <source media="(prefers-color-scheme: light)" srcset="lightmode_image_link">
  <source media="(prefers-color-scheme: dark)" srcset="darkmode_image_link">
  <img alt="alternative text" src="image_link">
</picture>
text after
'''
        expected_formatted_text = raw_text
        self.assertEqual(expected_formatted_text, format(raw_text))
        
    def test_no_darkmode_with_ignore_comment(self) -> None:
        raw_text = \
'''
text before
<!-- setup: let darkmode -->
<picture>
  <source media="(prefers-color-scheme: light)" srcset="lightmode_image_link">
</picture>
text after
'''
        expected_formatted_text = raw_text
        self.assertEqual(expected_formatted_text, format(raw_text))
    

if __name__ == '__main__':
    unittest.main()