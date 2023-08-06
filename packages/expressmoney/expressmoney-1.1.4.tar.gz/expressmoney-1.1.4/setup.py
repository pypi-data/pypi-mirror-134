"""
py setup.py sdist
twine upload dist/expressmoney-1.1.4.tar.gz
"""
import setuptools

setuptools.setup(
    name='expressmoney',
    packages=setuptools.find_packages(),
    version='1.1.4',
    description='SDK ExpressMoney',
    author='Development team',
    author_email='dev@expressmoney.com',
    install_requires=('google-cloud-secret-manager', 'google-cloud-error-reporting', 'google-cloud-pubsub',
                      'google-cloud-tasks', 'google-cloud-storage', 'requests'),
    python_requires='>=3.7',
)
