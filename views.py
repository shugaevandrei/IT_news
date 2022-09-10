from __init__ import app
import requests
from flask import render_template, request, url_for, flash, redirect
from util import get_db_connection, get_post
