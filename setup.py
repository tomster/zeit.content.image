from setuptools import setup, find_packages

setup(
    name='zeit.content.image',
    version='2.0.0.dev0',
    author='gocept',
    author_email='mail@gocept.com',
    url='https://svn.gocept.com/repos/gocept-int/zeit.cms',
    description="ZEIT Image",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    license='gocept proprietary',
    namespace_packages=['zeit', 'zeit.content'],
    install_requires=[
        'cssselect',
        'Pillow',
        'gocept.form',
        'setuptools',
        'zeit.cms>=2.14.0.dev0',
        'zeit.imp>=0.15.0.dev0',
        'zeit.wysiwyg',
        'zope.app.appsetup',
        'zope.app.testing',
        'zope.component',
        'zope.formlib',
        'zope.interface',
        'zope.publisher',
        'zope.security',
        'zope.testing',
    ],
    entry_points={
        'fanstatic.libraries': [
            'zeit_content_image=zeit.content.image.browser.resources:lib',
        ],
    },
)