from staticfiles.finders import AppDirectoriesFinder
from staticfiles.storage import AppStaticStorage

class LegacyAppStaticStorage(AppStaticStorage):
    source_dir = 'media'

class AppMediaFinder(AppDirectoriesFinder):
    storage_class = LegacyAppStaticStorage
