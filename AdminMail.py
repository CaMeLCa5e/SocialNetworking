#!/usr/bin/python

import img

from google.appengine.apu import images
from google.appengine.api import memcache
from handlers.AuthenticatedHandler import *

from utilities.AppProperties import AppProperties # not actually using this ##

class AdminMail(AuthenticatedHandler):

		def execute(self):
				method = self.request.method
				user = self.values['user']
				self.values['tab'] = '/admin'

				if user.rol != 'admin':
					self.forbidden()
					return

				if method =='GET':

						app = self.get_application()
						self.values['m'] = self.get_param('m')
						if not app:
								app = model.Application()
						self.values['app'] = app
						self.values['mail_contact'] 		= self.not_none(app.mail_contact)
						self.values['mail_subject_prefix']	= self.not_none(app.mail_subject_prefix)
						self.values['mail_sender']			= self.not_none(app.mail_sender)
						self.values['mail_footer']			= self.not_none(app.mail_footer)
						self.render('templates/module/admin/admin-mail.html')
				elif self.auth():
						app = self.get_application()
						if not app:
								app = model.Application()
						app.mail_subject_prefix				= self.get_param('mail_subject_prefix')
						app.mail_contact					= self.get_param('mail_contact')
						app.mail_sender						= self.get_param('mail_sender')
						app.mail_footer						= self.get_param('mail_footer')
						app.put()
						memcache.delete('app')
						AppProperties().updateJinjaEnv()
						self.redirect('/module/admin.mail?m=' +self.getLocale('Updated'))














