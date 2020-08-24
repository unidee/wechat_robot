import time
from util.week import determine_date
from util.basic_functions import read_file2list

path = 'word_data.csv'


class WordInfo:
    def __init__(self, word, review_date, review_times):
        self.word = word
        self.review_date = review_date
        self.review_times = review_times
        self.interval = 0  # int
        self.possibility = 1.00

    def determine(self, date_today):
        t_today_strp = time.strptime(date_today, '%Y-%m-%d')
        t_today = time.mktime(t_today_strp)
        t_review_date_strp = time.strptime(self.review_date, '%Y-%m-%d')
        t_review_date = time.mktime(t_review_date_strp)
        self.interval = (t_today - t_review_date) // 86400
        self.possibility = 0.8 ** int(self.review_times) + 0.04 * self.interval
        if self.possibility > 1:
            self.possibility = 1


def get_word():
    word_info_ls = []
    word_list = read_file2list(path)
    for word in word_list:
        word_info = WordInfo(word.split(',')[0], word.split(',')[1], word.split(',')[2])
        word_info.determine(determine_date())
        word_info_ls.append(word_info)
    return word_info_ls


if __name__ == '__main__':
    word_info_list = get_word()
    raise Exception('test')
