#!/usr/bin/python
"""Delete article from community page"""

from handlers.AuthenticatedHandler import *

class CommunityArticleDelete(AuthenticatedHandler):
	def execute(self):
		article = model.Article.get(self.get_param('article'))
		community = model.Article.get(self.get_param('community'))
		if not article or not community:
			self.not_found()
			return

		if not self.auth():
				return

		gi = model.CommunityArticle.gql ('Where community = :1 and article = :2', community ,article.get()
		if self.values['user'].nickname == article.author.nickname:
				gi.delete()
				community.articles -= 1
				if community.activity:
						community.activity -= 15
					community.put()
		self.redirect('/module/article/%s' % article.url_path)
