#!/usr/bin/python

from models.view import View

class News():
    def get(self, pairs):
        
        if 'action' not in pairs:
            self.get_news_category('top-news')
        else:
            action = pairs.getvalue('action')
            if action == 'top-news':
                self.get_news_category('top-news')
            elif action == 'politics':
                self.get_news_category('politics')
            elif action == 'tech':
                self.get_news_category('tech')
            elif action == 'sports':
                self.get_news_category('sports')
            else: #default
                self.get_news_category('top-news')

    def get_news_category(self, category):

        view_model = View()

        if category == 'top-news':
            # get latest 5 headlines
            # store into data dictionary
            data = {'title': 'top-news'}
        else:
            # get latest 5 'category' headlines
            # store into data dictionary
            data = {'title': category}
        
        view_model.print_header()
        view_model.get_view('header', data)
        view_model.get_view('navbar', data)
        view_model.get_view('news_category', data)
        view_model.get_view('footer', data)


