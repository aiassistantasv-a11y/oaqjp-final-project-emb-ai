"""Unit tests for the EmotionDetection package."""

import unittest

from EmotionDetection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Check the dominant emotion for representative sentences."""

    def test_joy(self):
        """A happy statement should express joy."""
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result["dominant_emotion"], "joy")

    def test_anger(self):
        """An angry statement should express anger."""
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result["dominant_emotion"], "anger")

    def test_disgust(self):
        """A disgusted statement should express disgust."""
        text = "I feel disgusted just hearing about this"
        result = emotion_detector(text)
        self.assertEqual(result["dominant_emotion"], "disgust")

    def test_sadness(self):
        """A sad statement should express sadness."""
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result["dominant_emotion"], "sadness")

    def test_fear(self):
        """An afraid statement should express fear."""
        text = "I am really afraid that this will happen"
        result = emotion_detector(text)
        self.assertEqual(result["dominant_emotion"], "fear")


if __name__ == "__main__":
    unittest.main()
