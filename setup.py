# -*- coding: utf-8 -*-

from cx_Freeze import setup, Executable

build_exe_options = dict(packages=["numpy.core", "numpy.lib"])
bdist_msi_options = dict(upgrade_code="{1cfd8d39-2c74-4deb-b402-ba5c7ec7f045}")

executables = [Executable("caffeinexc.py")]

setup(
    name="CaffeineXC",
    version="0.9",
    description="Caffeine for Wireless Xbox Controller",
    options=dict(build_exe=build_exe_options, bdist_msi=bdist_msi_options),
    executables=executables,
)
