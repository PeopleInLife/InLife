__author__ = 'jonathan'
from handlers.base import BaseHandler
import tornado.web

import logging
logger = logging.getLogger('boilerplate.' + __name__)


class Error404Handler(tornado.web.ErrorHandler, BaseHandler):
    def get(self):
        self.set_status(status_code=404)
        self.render("404.html", page=None)
