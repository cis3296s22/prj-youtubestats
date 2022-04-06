from unittest import TestCase

from youtube_history import Analysis

class TestAnalysis(TestCase):
    def setUp(self):
        self.analysis = Analysis(outpath='data', delay=0, takeout="C:\\Users\\Tyler\\OneDrive\\CIS3296\\Takeout")
    
    def test_download_data(self):
        
        self.fail()

    def test_deprecated_download_data_via_youtube_dl_login(self):
        self.fail()

    def test_df_from_files(self):
        self.fail()

    def test_make_wordcloud(self):
        self.fail()

    def test_check_df(self):
        self.fail()

    def test_total_time(self):
        self.fail()

    def test_best_and_worst_videos(self):
        self.fail()

    def test_most_emojis_description(self):
        self.fail()

    def test_funniest_description(self):
        self.fail()

    def test_three_randoms(self):
        self.fail()

    def test_compute(self):
        self.fail()

    def test_graph(self):
        self.fail()

    def test_start_analysis(self):
        self.fail()

    def test_run(self):
        self.fail()
