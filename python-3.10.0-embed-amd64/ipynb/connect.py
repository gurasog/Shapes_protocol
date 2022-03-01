def nim_app():
	from pywinauto.application import Application
	app = Application(backend='uia')
	app = app.connect(title='NIM Eclipse E4')
	return app