import sys

CONFIGURE_VIEWADAPTOR_TRACE = False
CONFIGURE_MAINWINDOW_TRACE = False
CONFIGURE_COMMUNICATOR_TRACE = False
CONFIGURE_APPLICATION_TRACE = False
CONFIGURE_MAIN_TRACE = False
CONFIGURE_PRINT_COMMUNICATION_DUMP = False

CONFIGURE_GUI_INFO = False

CONFIGURE_VIEWADAPTOR_RETRANSLATE_KEYS = True
CONFIGURE_SLEEPED_OPTIMIZATION = True
CONFIGURE_NO_RESTORE = False
CONFIGURE_CONSOLE_RETRANSLATE = True 
CONFIGURE_SCREEN_SAVER_TRANSLATE = True

CONFIGURE_WITHOUT_EVALCACHE_NOTIFIES = False
CONFIGURE_NO_EMBEDING_WINDOWS = False

if sys.platform == "win32" or sys.platform == "win64":
	# TODO: Эта опция падает на винде, видимо из-за некоректной передачи данных 
	CONFIGURE_SCREEN_SAVER_TRANSLATE = False

if sys.platform == "darwin":
	# TODO: Пока непонял, как на маке сделать встраиваемые окна.
	CONFIGURE_NO_EMBEDING_WINDOWS = True


DEBUG_MODE = False

def verbose(en):
	global CONFIGURE_VIEWADAPTOR_TRACE
	global CONFIGURE_MAINWINDOW_TRACE
	global CONFIGURE_COMMUNICATOR_TRACE
	global CONFIGURE_APPLICATION_TRACE
	global CONFIGURE_MAIN_TRACE
	global DEBUG_MODE

	CONFIGURE_VIEWADAPTOR_TRACE = en
	CONFIGURE_MAINWINDOW_TRACE = en
	CONFIGURE_COMMUNICATOR_TRACE = en
	CONFIGURE_APPLICATION_TRACE = en
	CONFIGURE_MAIN_TRACE = en
	DEBUG_MODE = en

def info(en):
	global CONFIGURE_GUI_INFO

	CONFIGURE_GUI_INFO = en