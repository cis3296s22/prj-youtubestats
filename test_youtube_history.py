import shutil
from unittest import TestCase
import unittest
import os
from numpy import empty
from grapher import Grapher
from youtube_history import Analysis

# USE THE SMALLEST TAKEOUT FILE YOU HAVE FOR RUNNING THIS TEST SUITE!!!
takeout_path=r"C:\Users\Tyler\OneDrive\CIS3296\Takeout"
path_to_json = r"D:\School\CIS3296\youtubestats\data\raw\00001.info.json"
path_to_wordcloud = r"D:\School\CIS3296\youtubestats\static\images\wordcloud.png"
ran_path = r"D:\School\CIS3296\youtubestats\data\ran"
raw_path = r"D:\School\CIS3296\youtubestats\data\raw"

class TestAnalysis(unittest.TestCase):
# setup, will remove all the files in ran and raw and set up the analysis object
    def remove_folder_contents(path):
        for filename in os.listdir(path):
            if not filename.__contains__("gitignore"):
                file_path = os.path.join(path, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                except Exception as e:
                    print('Failed to delete %s. Reason: %s' % (file_path, e))

    remove_folder_contents(raw_path)
    remove_folder_contents(ran_path)
    analysis = Analysis(outpath='data', delay=0, takeout=takeout_path)
    analysis.run()

# analysis object test
    def test_data_download(self):
        self.assertTrue(os.path.exists(path_to_json))
    
    def test_full_df(self):
        self.assertFalse(self.analysis.df.empty)

    def test_wordcloud_image(self):
        self.assertTrue(os.path.exists(path_to_wordcloud))

    def test_total_time(self):
        self.assertTrue(self.analysis.formatted_time is not None)

    def test_best_worst(self):
        self.assertTrue(self.analysis.worst_per_decile is not None)
        self.assertTrue(self.analysis.best_per_decile is not None)

    def test_emojis(self):
        self.assertTrue(self.analysis.emojis is not None)

    def test_best_worst(self):
        self.assertTrue(self.analysis.oldest_videos is not None)
        self.assertTrue(self.analysis.oldest_upload is not None)

    def test_three_randoms(self):
        self.assertTrue(self.analysis.HD is not None)
        self.assertTrue(self.analysis.UHD is not None)
        self.assertTrue(self.analysis.top_uploaders is not None)
        self.assertTrue(self.analysis.most_played_artist is not None)
        self.assertTrue(self.analysis.funny is not None)

# graph object test  
    def graph_set_up(self):
        grapher = Grapher(self.analysis.df, self.analysis.tags)
        return grapher

    def test_avg_rate_plot(self):
        grapher = self.graph_set_up()
        grapher.average_rating()
        self.assertTrue(grapher.avg_rate_plot is not None)

    def test_duration_plot(self):
        grapher = self.graph_set_up()
        grapher.duration()
        self.assertTrue(grapher.duration_plot is not None)
    
    def test_views_plot(self):
        grapher = self.graph_set_up()
        grapher.views()
        self.assertTrue(grapher.views_plot is not None)

    def test_tags_plot(self):
        grapher = self.graph_set_up()
        grapher.gen_tags_plot()
        self.assertTrue(grapher.tags_plot is not None)

if __name__ == '__main__':
    unittest.main()