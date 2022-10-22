from dash import Dash, html, dcc, Input, Output, callback
from pages import index, ParallelCategories, TimeRiver, CiteSpaceCir, CiteSpace, WordCloud, PublicationMap

base_url = "/demo"
app = Dash(__name__, suppress_callback_exceptions=True, url_base_pathname=base_url+'/')
server = app.server


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content'),
])

@callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    pathname = pathname[len(base_url):]
    if pathname == '/':
        return index.layout
    elif pathname == '/ParallelCategories':
        return ParallelCategories.layout
    elif pathname == '/TimeRiver':
        return TimeRiver.layout
    elif pathname == '/CiteSpaceCir':
        return CiteSpaceCir.layout
    elif pathname == '/CiteSpace':
        return CiteSpace.layout
    elif pathname == '/WordCloud':
        return WordCloud.layout
    elif pathname == '/PublicationMap':
        return PublicationMap.layout
    else:
        return '404 Not Found'

if __name__ == '__main__':
    app.run_server(debug=False)
