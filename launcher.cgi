#!/usr/local/bin/python

# ============================================================
# Path Config
# ============================================================

import sys

sys.path.insert(0, "lib")
sys.path.insert(0, "src")

# ============================================================
# Imports
# ============================================================

import cherrypy
import main

# ============================================================
# Run Local HTTP Server
# ============================================================

cherrypy.quickstart(main.Main("http://localhost:8080","djp"))

