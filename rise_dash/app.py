from dash import Dash

external_stylesheets = ["https://rsms.me/inter/inter.css"]

app = Dash(
    __name__, external_stylesheets=external_stylesheets, assets_folder="../assets"
)
