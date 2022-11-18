from operator import truediv
from turtle import Terminator
from dash import Dash
import dash_bootstrap_components as dbc

app = Dash(__name__,
            title="Supermarket Sales",
            suppress_callback_exceptions=True,
            external_stylesheets=[dbc.themes.CERULEAN])

app.scripts.config.serve_locally = True
server = app.server
