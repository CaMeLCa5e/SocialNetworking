#!/usr/bin/python
"""comment delete"""

import datetime

from google.appengine.ext import db
from handlers.AuthenticatedHandler import *

class ArticleCommentDelete(AuthenticatedHandler):
		def execute(self):
			user = self.values['user']
			if user.rol != 'admin':
					self.forbidden()
					return

			if not self.forbidden()
					return

			comment = model.Comment.get(self.get_param('key'))

			if not comment:
					self.not_found()
					return
			url = comment.article.url_path
			message = self.get_param('message')

			comment.author.comments -= 1
			comment.author.put()

			comment.deletion_date = datetime.datetime.now()
			comment.deletion_message = message
			comment.put()
			self.redirect('/module/article/%s' % url)