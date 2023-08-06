
from setuptools import setup, find_packages

# no import emzed here, causes trouble when installing on win, as missing packages
# are needed when importing emzed
version = (2, 12, 1)

setup(name="emzed",
      packages=find_packages(exclude=["tests", "sandbox"]),
      version="%d.%d.%dalpha" % version,
      description="Rewrite of emzed framework for LCMS data analysis",
      entry_points={
          "gui_scripts": ["emzed.workbench = emzed.workbench.main:main",
                          "emzed.inspect = emzed.cmdline:inspect",
                          ],
          "console_scripts": ["emzed.console = emzed.console:main",
                              "emzed.workbench.debug = emzed.workbench.main:main",
              ]
      },
      include_package_data=True,
      zip_safe=False,
      install_requires=["emzed_optimizations",
                        "guidata>=1.6.0",
                        "guiqwt>=2.3.1",
                        "requests",
                        "ipython==0.10",
                        # "spyder==2.1.13",
                        "dill",
                        "sphinx",
                        "html2text",
                        "pandas",
                        "dill",
                        "pyopenms",
                        "pyRserve",
                        "pytest",
                        "pyreadline",
                        ]
      )
