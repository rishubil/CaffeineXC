# -*- coding: utf-8 -*-

from cx_Freeze import setup, Executable

buildOptions = dict(packages=["numpy.core", "numpy.lib"])

executables = [Executable("xbox-keep-on.py")]

setup(
    name="xbox-keep-on",
    version="0.8",
    description="xbox-keep-on",
    options=dict(build_exe=buildOptions),
    executables=executables,
)
