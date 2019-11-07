import os
import requests


URL = 'http://archive.ics.uci.edu/ml/machine-learning-databases/00331/sentiment%20labelled%20sentences.zip'

class DownloadCompressedFile:

    def get_url(self, url):
        r = requests.get(url, stream = True)
        if r.status_code != 200:
            raise IOError(f'Unable to download {url}, HTTP {r.status_code}')
        return r
    
    def save_to_filepath(self, dirname, filename):
       
        full_path = os.path.join(dirname, filename)
        
        try:
            os.mkdir(dirname)
        except OSError as e:
            print(f'Error: {dirname} : {e.strerror}')
        
        print(f'Dowloading file:{filename}')

        with self.get_url(URL) as r, open(full_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size = 102400):
                if chunk:
                    f.write(chunk)

    def run(self):
        dirname = '.\dest'
        filename = 'sentiment_labelled_sentences.zip'
        self.save_to_filepath(dirname, filename)

if __name__ == '__main__':
    obj = DownloadCompressedFile()
    obj.run()
    


            

