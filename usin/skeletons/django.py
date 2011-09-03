# -*- encoding: utf-8 -*-

import os
from paste.script import templates
from paste.script.templates import var

class DjangoBuildout(templates.Template):
    
    special_tpl_files = {
        'gitignore' : '.gitignore',
    }
    
    summary = u'Skeleton to start Django project with Buildout'
    required_templates = []
    _template_dir = 'templates/django_buildout'
    use_cheetah = True

    vars = (
    )

    def rename_files(self, output_dir):
        for f_tpl, f_real in self.special_tpl_files.items():
            f_tpl = os.path.join(output_dir, f_tpl)
            f_real = os.path.join(output_dir, f_real)
            os.rename(f_tpl, f_real)

    def post(self, command, output_dir, vars):
        self.rename_files(output_dir)
