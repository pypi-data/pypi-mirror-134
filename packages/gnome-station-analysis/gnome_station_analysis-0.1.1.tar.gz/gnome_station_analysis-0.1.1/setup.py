from distutils.core import setup

setup(
name="gnome_station_analysis",
    version="0.1.1",
    author="GNOME team in Kraków",
    author_email="gregory.lukasiewicz@gmail.com",
    packages=["gnome_station_analysis"],
    #scripts = glob('bin/*'),
    url="https://github.com/gregorylukasiewicz/gnome_station_analysis",
    download_url = "https://github.com/gregorylukasiewicz/gnome_station_analysis/archive/refs/tags/v_0.1.tar.gz",
    description="GNOME Station Analysis Tools",
    install_requires=["numpy", "matplotlib", "regex", "glob2", "scipy"],
)
