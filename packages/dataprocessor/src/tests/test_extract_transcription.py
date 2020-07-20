import pickle
import unittest

from src.scripts.extract_transcription import extract_transcription, save_transcriptions


class ExtractTranscription(unittest.TestCase):
    def test_extract_sentences(self):
        path_srt_file = './src/tests/test_resources/input/merged.txt'
        with open(path_srt_file, 'rb') as file:
            content = pickle.load(file)
        transcriptions = extract_transcription(content)
        print(transcriptions)
        rejected = save_transcriptions('./src/tests/test_resources/output', transcriptions, 'chunk')
        print(len(rejected))
        self.assertEqual(len(transcriptions), 3)
        self.assertEqual('', transcriptions[0])
        self.assertEqual('मेरे प्यारे देशवासियों नमस्कार', transcriptions[1])
        self.assertEqual('कोरोना के प्रभाव से हमारी मन की बात भी अछूती नहीं रही है', transcriptions[2])


    def test_save_transcriptions(self):
        transcriptions = ['', 'मेरे प्यारे देशवासियों', 'नमस्कार', '', 'कोरोना के प्रभाव से हमारी मन की बात भी अछूती नहीं रही है', 'जब मैंने पिछली बार आपसे']
        rejected = save_transcriptions('./src/tests/test_resources/output', transcriptions, 'chunk')
        self.assertEqual(len(rejected), 2)

if __name__ == '__main__':
    unittest.main()
