#!c:/SDK/Anaconda2/python.exe
# encoding:utf-8
# Author: cumulus13
# email: cumulus13@gmail.com

from __future__ import print_function
import requests
from bs4 import BeautifulSoup as bs
from make_colors import make_colors
from pydebugger.debug import debug
import re
import os
import sys
if sys.version_info.major == 3:
	raw_input = input
import traceback
#sys.excepthook = traceback.format_exc
import clipboard
from pprint import pprint
from safeprint import print as sprint
import argparse
from pause import pause
from PyQt5 import Qt
from PyQt5.QtGui import QPixmap, QImage, QIcon, QFont
from PyQt5.QtWidgets import QDialog, QApplication, QLabel, QTableWidgetItem, QAbstractScrollArea, QAbstractItemView, QTableWidget, QHeaderView, QPushButton, QScrollArea
from PyQt5.QtCore import *
from details_gui import *
from screenshot import * 
import qdarkstyle
import ast

class Details(QDialog):
	def __init__(self, data = []):
		if sys.version_info.major == 3:
			super().__init__()
		else:
			super(Details, self).__init__()
		
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)
		self.ui.l_next.hide()
		self.ui.l_previous.hide()
		
		app_path = ""

		for i in data.get('path'):
			app_path += i[0] + "/"
		app_path = app_path[:-1]
		#self.ui.setWindowTitle("Detail {0} {1}".format(data.get('title').strip(), app_path))
		_translate = QCoreApplication.translate
		self.setWindowTitle(_translate("Dialog", "Detail | {0} {1}".format(data.get('title').encode('utf-8').strip(), app_path)))
		
		self.ui.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
		self.ui.scrollArea.installEventFilter(self)
		
		#self.scrollArea = QtWidgets.QScrollArea(self.ui.horizontalLayoutWidget)
		#self.ui.hl_screenshot.addWidget(self.scrollArea)
		
		self.ui.l_next.setGeometry(QtCore.QRect(360, 570, 50, 50))
		self.ui.l_next.setPixmap(QPixmap(os.path.join(os.path.dirname(__file__), 'next.png')))
		self.ui.l_next.setScaledContents(True)
		self.ui.l_next.setStyleSheet("background-color: rgba(0,0,0,0%)")
		#self.ui.l_next.installEventFilter(self)
		
		self.ui.l_previous.setGeometry(QtCore.QRect(20, 570, 50, 50))
		self.ui.l_previous.setPixmap(QPixmap(os.path.join(os.path.dirname(__file__), 'previous.png')))
		self.ui.l_previous.setScaledContents(True)
		self.ui.l_previous.setStyleSheet("background-color: rgba(0,0,0,0%)")
		#self.ui.l_previous.installEventFilter(self)
		
		self.ui.l_next.mousePressEvent = self.move_next_Scroll
		self.ui.l_previous.mousePressEvent =  self.move_previous_Scroll
		
		#self.qs = QScrollArea(self)
		#hb = self.qs.horizontalScrollBar()
		
		#self.ui.scrollArea.horizontalScrollBar().value()
		
		
		if data:
			poster_url = 'http:' + data.get('poster')
			#poster_url = 'http:' + '//apkmb.com/wp-content/uploads/2020/06/Fing-Network-Tools-Pro-Mod-Apk.jpg'
			img_data = requests.get(poster_url).content
			self.ui.l_poster.setText("")
			img_poster = QImage()
			img_poster.loadFromData(img_data)
			#img_poster.width = self.ui.l_poster.width()
			#img_poster.height= self.ui.l_poster.height() -  100			
			img_item = QPixmap(img_poster)
			
			#img_item.scaled(self.ui.l_poster.width(), self.ui.l_poster.height())
			#img_item.width = self.ui.l_poster.width()
			#img_item.height= self.ui.l_poster.height() -  100
			self.ui.l_poster.setPixmap(img_item)
			self.ui.l_poster.setScaledContents(True)
			
			self.ui.c_name.setText(data.get('title').strip())
			self.ui.c_name.setStyleSheet("QLabel { background-color : red; color : white; }")
			self.ui.c_version.setText(data.get('version'))
			data_category = data.get('category')
			category = ""
			if len(data_category) == 1:
				category = data_category[0].get('name')
			else:
				for i in data_category:
					category += i.get('name') + ", "
				category = category[:-2]
			self.ui.c_category.setText(category)
			self.ui.c_update.setText(data.get('data_app').get('Updated'))
			self.ui.c_playstore.setText(data.get('data_app').get('Get it on').get('link'))
			self.ui.c_developer.setText(data.get('data_app').get('Developer').get('name'))
			self.ui.c_requirements.setText(data.get('data_app').get('Requirements'))
			
			self.ui.e_description.setText(data.get('description'))
			
			whatsnew = []
			data_whatsnew = data.get('whats_new')
			n_w = 1
			for i in data_whatsnew:
				if len(str(n_w)) == 1:
					number = "0" + str(n_w)
				else:
					number = str(n_w)
				whatsnew.append(number + ". " + i)
				n_w += 1
			self.ui.e_whatsnew.setText("\n".join(whatsnew))
			
			features = []
			data_features = data.get('features')
			n_f = 1
			for i in data_features:
				if len(str(n_f)) == 1:
					number = "0" + str(n_f)
				else:
					number = str(n_f)
				features.append(number + ". " + i)
				n_f += 1
			self.ui.e_features.setText("\n".join(features))
			
			function = []
			data_function = data.get('function')
			n_f = 1
			for i in data_function:
				if len(str(n_f)) == 1:
					number = "0" + str(n_f)
				else:
					number = str(n_f)
				function.append(number + ". " + i)
				n_f += 1
			self.ui.e_function.setText("\n".join(function))
			
			mod_info = []
			data_modinfo = data.get('mod_info')
			n_f = 1
			for i in data_modinfo:
				if len(str(n_f)) == 1:
					number = "0" + str(n_f)
				else:
					number = str(n_f)
				mod_info.append(number + ". " + i)
				n_f += 1
			self.ui.e_modinfo.setText("\n\n".join(mod_info))
			self.ui.e_modinfo.setStyleSheet("QTextEdit { background-color : red; color : white; }")
			
			data_screenshoot = data.get('screenshot')
			for i in data_screenshoot:
				ls_name = QtWidgets.QLabel(self.ui.horizontalLayoutWidget)
				ls_name.setObjectName("screenshot_{0}".format(data_screenshoot.index(i)))
				ls_name.installEventFilter(self)
				
				screenshot_url = 'http:' + i
				screenshot_img_data = requests.get(screenshot_url).content
				img_screenshot = QImage()
				img_screenshot.loadFromData(screenshot_img_data)
				screenshot_img_item = QPixmap(img_screenshot)
				ls_name.setPixmap(screenshot_img_item)
				ls_name.setScaledContents(True)
				ls_name.setFixedSize(100, 190)
				self.ui.hl_screenshot.addWidget(ls_name)
				
				
			data_related = data.get('related')
			for i in data_related:
				self.vlw = QtWidgets.QWidget(self)
				self.vlw.setGeometry(QtCore.QRect(0, 0, 0, 0))
				self.vlw.setObjectName("vlw_{0}".format(data_related.index(i)))
				self.hlw = QtWidgets.QHBoxLayout(self.vlw)
				self.hlw.setContentsMargins(0, 0, 0, 0)
				self.hlw.setObjectName("hlw_{0}".format(data_related.index(i)))
				
				related_name_1 = QtWidgets.QLabel(self.vlw)
				related_name_1.setText(data_related[data_related.index(i)].get('name'))
				
				related_name_1.setObjectName("related_{0}".format(data_related.index(i)))
				related_name_1.installEventFilter(self)
				related_name_1.setToolTip(data_related[data_related.index(i)].get('name'))
				
				screenshot_url_related = 'http:' + data_related[data_related.index(i)].get('thumb')
				screenshot_img_related_data = requests.get(screenshot_url_related).content
				img_screenshot_related = QImage()
				img_screenshot_related.loadFromData(screenshot_img_related_data)
				screenshot_img_item_related = QPixmap(img_screenshot_related)
				related_name_1.setPixmap(screenshot_img_item_related)
				related_name_1.setScaledContents(True)
				related_name_1.setFixedSize(50, 50)
					
				related_name_2 = QtWidgets.QLabel(self.vlw)
				related_name_2.setText(data_related[data_related.index(i)].get('name'))
				
				related_name_2.setObjectName("related_{0}".format(data_related.index(i) + 1))
				related_name_2.installEventFilter(self)
				related_name_2.setToolTip(data_related[data_related.index(i)].get('name'))
				
				related_name_2.setFixedSize(370, 50)
				related_name_2.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
				
				self.hlw.addWidget(related_name_1)
				self.hlw.addWidget(related_name_2)
				
				self.ui.hl_related.addWidget(self.vlw)
				
			data_downloads = data.get('download_links')
			for i in data_downloads:
				download_link = QPushButton(self.ui.horizontalLayoutWidget)
				download_link.setObjectName("download_{0}".format(data_downloads.index(i)))
				download_link.setIcon(QIcon(os.path.join(os.path.dirname(__file__), 'download.png')))
				
				download_url = i.get('link')
				download_name = i.get('name')
				download_link.setText(download_name)
				download_link.setFont(QFont('Impact', 9))
				download_link.setToolTip(download_url)
				download_link.setToolTipDuration(2000)
				self.ui.vl_download.addWidget(download_link)			
	
	def move_next_Scroll(self, event):
		#if not self.ui.scrollArea.horizontalScrollBar().value() == self.ui.scrollArea.horizontalScrollBar().maximum():
		self.ui.scrollArea.horizontalScrollBar().setValue(self.ui.scrollArea.horizontalScrollBar().value() + 30)
	def move_previous_Scroll(self, event):
		#if not self.ui.scrollArea.horizontalScrollBar().value() == 0:
		self.ui.scrollArea.horizontalScrollBar().setValue(self.ui.scrollArea.horizontalScrollBar().value() - 30)
		
		
	def eventFilter(self, object, event):
		#print("object.objectName() =", object.objectName())
		if event.type() == QEvent.Enter:
			#print("object.objectName() =", object.objectName())
			if object.objectName() == re.compile('screenshot_\d{0,2}') or object.objectName() == 'scrollArea':
				self.ui.l_next.show()
				self.ui.l_previous.show()
			self.stop = True
			#print('program stop is', self.stop)
			return True
		elif event.type() == QEvent.Leave:
			if object.objectName() == re.compile('screenshot_\d{0,2}') or object.objectName() == 'scrollArea':
				self.ui.l_next.hide()
				self.ui.l_previous.hide()
			self.stop = False
			#print('program stop is', self.stop)
		elif event.type() == QEvent.MouseButtonPress:
			if object.objectName() == re.compile('screenshot_\d{0,2}') or object.objectName() == 'scrollArea':
				self.ui.l_next.show()
				self.ui.l_previous.show()
		return False	
			

class Screenshot(QDialog):
	def __init__(self, data = []):
		if sys.version_info.major == 3:
			super().__init__()
		else:
			super(Screenshot, self).__init__()
		
		self.ui = Ui_screenshot_dialog()
		self.ui.setupUi(self)
		
		self.horizontalLayoutWidget = QtWidgets.QWidget(self)
		self.horizontalLayoutWidget.setGeometry(QtCore.QRect(500, 10, 121, 631))
		self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
		self.hl_screenshot = QtWidgets.QHBoxLayout(self.ui.scrollAreaWidgetContents)
		self.hl_screenshot.setContentsMargins(0, 0, 0, 0)
		self.hl_screenshot.setObjectName("hl_screenshot")		
		
		self.l_next = QtWidgets.QLabel(self)
		self.l_next.setGeometry(QtCore.QRect(630, 470, 47, 13))
		self.l_next.setObjectName("l_next")
		self.ui.l_next.setPixmap(QPixmap(os.path.join(os.path.dirname(__file__), 'next.png')))
		self.ui.l_next.setScaledContents(True)
		self.ui.l_next.setStyleSheet("background-color: rgba(0,0,0,0%)")
		
		self.l_previous = QtWidgets.QLabel(self)
		self.l_previous.setGeometry(QtCore.QRect(30, 470, 47, 13))
		self.l_previous.setObjectName("l_previous")
		self.ui.l_previous.setPixmap(QPixmap(os.path.join(os.path.dirname(__file__), 'previous.png')))
		self.ui.l_previous.setScaledContents(True)
		self.ui.l_previous.setStyleSheet("background-color: rgba(0,0,0,0%)")		
		
		data_screenshoot = data.get('screenshot')
		if data_screenshoot:
			for i in data_screenshoot:
				ls_name = QtWidgets.QLabel(self.ui.horizontalLayoutWidget)
				ls_name.setObjectName("screenshot_{0}".format(data_screenshoot.index(i)))
				ls_name.installEventFilter(self)
				
				screenshot_url = 'http:' + i
				screenshot_img_data = requests.get(screenshot_url).content
				img_screenshot = QImage()
				img_screenshot.loadFromData(screenshot_img_data)
				screenshot_img_item = QPixmap(img_screenshot)
				ls_name.setPixmap(screenshot_img_item)
				ls_name.setScaledContents(True)
				ls_name.setFixedSize(100, 190)
				self.hl_screenshot.addWidget(ls_name)
		
		
		
	
class apkmb(object):
	def __init__(self):
		super(apkmb, self)
		self.url = "https://apkmb.com/"
		self.session = requests.Session()
		self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
		self.session.headers.update(self.headers)
		
	def home(self, url = None, bs_object = None, search = False):
		if not bs_object:
			if not url:
				url = self.url
			a = self.session.get(url)
			b = bs(a.content, 'lxml')
		else:
			b = bs_object
		all_section = b.find('main', {'id':'main-site'}).find('div', {'class':'container'}).find_all('div', {'class':'section'})
		debug(all_section = all_section)
		sections = []
		n = 1
		for i in all_section:
			data = {}
			title = i.find('div', {'class':'title-section'})
			debug(title = title)
			if title:
				title = title.text
				if search:
					title = re.sub("\n|\t|  ", '', title)
			else:
				title = ''
			debug(title = title)

			bloque_apps = i.find('div', {'class':'bloque-apps'}).find_all('div', {'class':'bloque-app'})
			debug(bloque_apps = bloque_apps)
			for x in bloque_apps:
				alink = x.find('a')
				link = alink.get('href')
				thumb = alink.find('div', {'class':'bloque-imagen'})
				debug(thumb = thumb)
				if thumb:
					thumb = thumb.find('img').get('data-src')
				debug(thumb = thumb)
				debug(link = link)
				apptitle = alink.find('span', {'class':'title'}).text
				debug(apptitle = apptitle)
				developer = alink.find('span', {'class':'developer'})
				if developer:
					developer = developer.text
				else:
					developer = ''
				debug(developer = developer)
				date = alink.find('span', {'class':'app-date'}).text
				debug(date = date)
				data.update({
					n : {
							'link':link,
							'title':apptitle,
							'developer':developer,
							'date':date,
							'thumb':thumb
						}
				})
				n +=1
			sections.append({'title':title, 'data':data})
		debug(sections = sections)
		
		last_page, current_page = self.get_lastpages(b)
		return sections, last_page, current_page
					
	def get_lastpages(self, bs_object=None):
		if not bs_object:
			a = self.session.get(self.url)
			bs_object = bs(a.content, 'lxml')
		b = bs_object
		pagination = b.find('div', {'class':'pagination-wrap'})
		if pagination:
			pagination = pagination.find('ul', {'class':'pagination'})
		else:
			return '', ''
		debug(pagination = pagination)
		all_li = pagination.find_all('li')
		last_page = ''
		current_page = ''
		if not 'Next' in all_li[-1].find('a').text:
			last_page = all_li[-1].find('a').text
		else:
			last_page = all_li[-2].find('a').text
		debug(last_page = last_page)
		for i in all_li:
			if i.find('span'):
				current_page = i.find('span').text
				break
		debug(current_page = current_page)
		return last_page, current_page
		
	def search(self, query):
		params = {'s':query}
		a = self.session.get(self.url, params = params)
		b = bs(a.content, 'lxml')
		result, last_page, current_page = self.home(b, True)
		return result, last_page, current_page
		
	def details(self, url):
		data = {}
		a = self.session.get(url)
		b = bs(a.content, 'lxml')
		container = b.find('main', {'id':'main-site'}).find('div', {'class':'container'})
		all_path = container.find('div', {'class':'right s2'}).find('ol', {'id':'breadcrumbs'}).find_all('li')
		path = []
		for i in all_path:
			ai = i.find('a')
			path_link = ai.get('href')
			path_title = ai.get('title')
			path_text = ai.text
			path.append([path_text, path_title, path_link])
		debug(path = path)
		title = container.find('h1', {'class':'box-title'})
		if title:
			title = title.text
		debug(title = title)
		version = container.find('h4', {'class':'version'})
		if version:
			version = version.text
		category = []
		category_link = container.find('div', {'class':'categories'}).find_all('li')
		for i in category_link:
			c_a = i.find('a')
			c_link = c_a.get('href')
			c_text = c_a.text
			category.append({'link':c_link, 'name':c_text})
		debug(category = category)
		data_app = {}
		box_data_app = container.find('div', {'class':'box-data-app'})
		debug(box_data_app = box_data_app)
		all_left = box_data_app.find_all('div', {'class':'left data-app'})
		debug(all_left = all_left)
		
		for i in all_left:
			span = i.find_all('span')
			debug(span = span)
			for s in span:
				debug(s = s)
				key = s.find('b').text
				if not key or key == '':
					key = 'playstore'
				al = s.find('a')
				try:
					if not al.text:
						value = {'link':al.get('href'), 'name':'playstore'}
					else:
						value = {'link':al.get('href'), 'name':al.text}
				except:
					value = re.sub("\n", "", s.text)
					value = re.sub(key, "", s.text)
				data_app.update({key:value})
		debug(data_app = data_app)
		
		entry = container.find('div', {'class':'entry'})
		entry_limit = entry.find('div', {'class':'entry-limit'})
		all_p = entry_limit.find_all('p')
		description = all_p[0]
		if description:
			description = description.text
		debug(description = description)
		adds = {}
		adds_a = all_p[1].find('a')
		adds.update({'link':adds_a.get('href'), 'name':adds_a.text})
		debug(adds = adds)
		poster = all_p[2].find('img').get('data-src')
		debug(poster = poster)
		functions = []
		functions = all_p[4].text.encode('utf-8').split("\xe2\x80\xa2 ")
		functions = filter(None, functions)
		debug(functions = functions)
		try:
			features = all_p[6].text.encode('utf-8').split("\xe2\x80\xa2 ")
			features = filter(None, features)
			debug(features = features)
		except:
			features = ''
		
		whats_new = container.find('div', {'id':'novedades'})
		if whats_new:
			whats_new = whats_new.find('div', {'class':'box-content'})
			if whats_new:
				whats_new = whats_new.find('p')
				if whats_new:
					whats_new = whats_new.text.encode('utf-8').split("\xe2\x80\xa2 ")
				whats_new = filter(None, whats_new)	
		debug(whats_new = whats_new)
		
		screenshot = []
		div_screenshot = container.find('div', {'class':'box imagenes'})
		if div_screenshot:
			div_screenshot = div_screenshot.find('div', {'id':'slideimages'})
		if div_screenshot:
			all_images = div_screenshot.find_all('div', {'class':'px-carousel-item'})
			if all_images:
				for i in all_images:
					img = i.find('img').get('data-big-src')
					debug(img = img)
					screenshot.append(img)
		debug(screenshot = screenshot)
		
		mod_info = container.find('div', {'class':'box personalizadas'})
		if mod_info:
			mod_info = mod_info.find('div', {'class':'box-content'})
			if mod_info:
				mod_info = mod_info.find('p').text.split("; ")
		debug(mod_info = mod_info)
		
		download_links = []
		div_download = container.find('div', {'id':'download'})
		all_a = div_download.find_all('a', {'target':'_blank'}) # or {'class':'downloadAPK dapk_b'}
		for i in all_a:
			download_link = i.get('href')
			name = i.text
			download_links.append({'name':name, 'link':download_link})
		debug(download_links = download_links)
		
		related = []
		div_related = container.find('div', {'class':'box relacionados'})
		if div_related:
			all_related = div_related.find_all('div', {'class':'bloque-app'})
			for i in all_related:
				r_thumb = i.find('div', {'class': 'bloque-imagen',}).find('img')
				if r_thumb:
					r_thumb = r_thumb.get('data-src')
				r_a = i.find('a')
				r_link = r_a.get('href')
				r_name = r_a.find('span', {'class':'title'}).text
				r_developer = r_a.find('span', {'class':'developer'})
				if r_developer:
					r_developer = r_developer.text
				r_date = r_a.find('span', {'class':'app-date'}).text
				r_data = {'link':r_link, 'name':r_name, 'developer':r_developer, 'date': r_date, 'thumb': r_thumb,}
				related.append(r_data)
		debug(related = related)
		data.update({
			'path':path,
			'title':title,
			'version':version,
			'category':category,
			'data_app':data_app,
			'description':description,
			'adds':adds,
			'poster':poster,
			'function':functions,
			'features':features,
			'whats_new':whats_new,
			'screenshot':screenshot,
			'mod_info':mod_info,
			'download_links':download_links,
			'related':related,
		})
		debug(data = data)
		#clipboard.copy(str(data))
		#sys.exit()
		return data
		
	def print_nav(self):
		note = make_colors("select number to download (", 'lw', 'bl')\
			+ make_colors("[n]i = get info of n", 'b', 'lg') + ", "\
			+ make_colors("[n]ig = gui get info of n", 'b', 'lc') + ", "\
			+ make_colors("[n]s = show screenshot only of n", "b", 'ly') + ", "\
			+ make_colors("[n]p goto page n", 'lw', 'm') + ", "\
			+ make_colors("x|q Quit/Exit", 'lw', 'lr') + ", "\
			+ make_colors("just type want to search for", 'lr', 'lw') + ", "\
			+ make_colors("): ", 'lw', 'bl')
		q = raw_input(note)
		return q
	
	def show_detail_gui(self, data):
		#data = ast.literal_eval(data)
		#data =  self.details("https://apkmb.com/fing-network-tools/")
		app = QApplication(sys.argv)
		app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
		class_instance = Details(data)
		class_instance.show()
		app.exec_()
		
	def show_screenshot_gui(self, data):
		app = QApplication(sys.argv)
		app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
		class_instance = Screenshot(data)
		class_instance.show()
		app.exec_()
		
	def navigator(self, url = None, search = False, download_path = ".", print_list = True):
		if search:
			result, last_page, current_page = self.search(search)
		else:
			result, last_page, current_page = self.home(url)
		choices = [['b', 'ly'], ['b', 'lg'], ['b', 'lc'], ['lw', 'lm']]
		
		if print_list:
			for i in result:
				print(make_colors(i.get('title').upper(), 'lw', 'bl'))
				fore, back = choices[result.index(i)]
				data = i.get('data')
				for x in data:
					number = x
					if len(str(x)) == 1:
						number = "0" + str(x)
					else:
						number = str(x)
					debug(title = data.get(x).get('title'))
					title = re.sub(" Free Download", "", data.get(x).get('title'))
					try:
						print(make_colors(number + ".", 'lw', 'bl') + " " + make_colors(title, fore, back) + " [" + make_colors(data.get(x).get('date'), 'lr', 'lw') + "]")
					except:
						sprint(make_colors(number + ".", 'lw', 'bl') + " " + make_colors(title, fore, back) + " [" + make_colors(data.get(x).get('date'), 'lr', 'lw') + "]")
		q = self.print_nav()
		if q:
			q = str(q).strip()
			if str(q).isdigit():
				pass
			elif q[-1:] == 'p':
				number = q[:-1]
				if not number:
					number = raw_input(make_colors("Select Number :", 'lw', 'bl') + " ")
				return self.navigator(self.url + 'page/' + str(int(current_page) + 1) + "/")
			elif q[-1:] == 'i':
				number = q[:-1]
				if not number:
					number = raw_input(make_colors("Select Number :", 'lw', 'bl') + " ")
				for i in result:
					if int(number) in i.get('data').keys():
						self.details(i.get('data').get(int(number)).get('link'))
						break
				return self.navigator(search = search, download_path = download_path)
			elif q[-1:] == 's':
				number = q[:-1]
				if not number:
					number = raw_input(make_colors("Select Number :", 'lw', 'bl') + " ")
				for i in result:
					if int(number) in i.get('data').keys():
						data_detail = self.details(i.get('data').get(int(number)).get('link'))
						self.show_screenshot_gui(data_detail)
						break			
			elif q[-2:] == 'ig':
				number = q[:-2]
				if not number:
					number = raw_input(make_colors("Select Number :", 'lw', 'bl') + " ")				
				for i in result:
					if int(number) in i.get('data').keys():
						data_detail = self.details(i.get('data').get(int(number)).get('link'))
						self.show_detail_gui(data_detail)
						break
			elif q == 'x' or q == 'q':
				sys.exit(make_colors("System Exit !", 'lw', 'lr'))
			else:
				if ord(q) == '13':
					return self.navigator(download_path = download_path, print_list = False)
				else:
					return self.navigator(search = q, download_path = download_path)
		return self.navigator(download_path = download_path)
			
	def usage(self):
		parser = argparse.ArgumentParser(formatter_class = argparse.RawDescriptionHelpFormatter)
		parser.add_argument('SEARCH', help = 'What search for ', action = 'store')
		parser.add_argument('-p', '--download-path', help = 'Save download to dir', action = 'store')
		if len(sys.argv) == 1:
			parser.print_help()
		else:
			args = parser.print_help()
			self.navigator(search = args.SEARCH, download_path = args.download_path)
		
		
if __name__ == "__main__":
	c = apkmb()
	c.navigator()
	#c.show_detail_gui()
	#  c.usage()
	#c.home()
	#c.search(sys.argv[1])
	#data = c.details("https://apkmb.com/fing-network-tools/")
	#clipboard.copy(str(data))