from dash import Dash, html, dcc
import dash

app = Dash(
    __name__,
    use_pages=True,
)
server = app.server
app.layout = html.Main(
    [
        html.Nav(
            [
                html.H1("Multi-page app with Dash Pages"),
                html.Div(
                    [
                        html.Div(
                            className="nav-item",
                            children=[
                                dcc.Link(
                                    f"{page['name']}",
                                    href=page["relative_path"],
                                    className="nav-link",
                                )
                            ],
                        )
                        for page in dash.page_registry.values()
                    ]
                ),
            ],
            className="navbar navbar-expand-lg navbar-light bg-light",
        ),
        html.Div(
            className="page-content",
            children=[
                dash.page_container,
            ],
        ),
    ],
    className="fluid",
)

if __name__ == "__main__":
    app.run_server(debug=True)
