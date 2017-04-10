from setuptools import setup

setup(name='timesheet_todoist',
      version='1.0',
      description='Displays timesheet items for a given day',
      url='http://code.rand.org/rubin/timesheet-todoist',
      author='Jamie Todd Rubin',
      author_email='rubin@rand.org',
      license='MIT',
      packages=['timesheet_todoist'],
      package_dir={'timesheet_todoist': 'timesheet_todoist'},
      install_requires=[
        'parsedatetime',
        'mytime'
      ],
      scripts=['bin/timesheet'],
      include_package_data=True,
      zip_safe=False)
