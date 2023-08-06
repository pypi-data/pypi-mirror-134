import setuptools, os
setuptools.setup(
    name="olgamrl_Python_Gui_p2",  # Replace with your own PyPi
    version="1.0",
    author="Olga M",
    author_email="olga.meltsin@example.com",
    description="A small gui example package",
    url="https://pypi.org/manage/projects/",
    install_requires=['docker','flask'],
    packages=['ContainerDetails'],
    scripts=['ContainerDetails/expose.py', 'ContainerDetails/list_expose.py'],
    python_requires='>=3.9',
)
