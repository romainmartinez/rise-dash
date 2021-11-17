import numpy as np
from dash import html
from dash_dangerously_set_inner_html import DangerouslySetInnerHTML  # type: ignore

from . import icons
from ..services import processing_service


def sparkline_svg_line_component(
    values: list, xmax: int = 500, ymax: int = 100, className: str = None
) -> str:
    values_array = np.array(values)
    x_normalized_values = np.linspace(start=0, stop=xmax, num=values_array.shape[0])
    y_normalized_values = processing_service.min_max_normalisation(values_array) * ymax
    polyline_points = f'-100,{ymax+100} {" ".join(f"{x},{ymax - y}" for x, y in zip(x_normalized_values, y_normalized_values))} {xmax+100},{ymax+100}'
    return f"""<svg class="{className}" viewBox="0 0 {xmax} {ymax}">
	<polyline points="{polyline_points}" fill="currentColor" fill-opacity="0.1" stroke="currentColor" stroke-width="5" />
	<g fill='currentColor' stroke='white' stroke-width='3'>
	{[f"<circle cx='{x}' cy='{ymax - y}' r='6' />" for x, y in zip(x_normalized_values, y_normalized_values)]}
	</g>
" />
</svg>
"""


def sparkline_component(label: str, change: str, color: str, values: list) -> html.Div:
    description = html.Div(
        [
            html.Dt(label, className="text-sm font-medium text-gray-500 truncate"),
            html.Span(
                [
                    getattr(
                        icons, f"arrow_{'up' if change[0] == '+' else 'down'}_icon"
                    )("self-center flex-shrink-0 w-4 h-4"),
                    change[1:],
                ],
                className="inline-flex items-center text-sm font-semibold "
                + ("text-green-600" if color == "green" else "text-red-600"),
            ),
        ],
        className="flex items-center justify-between gap-2",
    )
    graph = html.Div(
        DangerouslySetInnerHTML(
            sparkline_svg_line_component(values, className="w-full h-16")
        ),
        className="mt-1 text-gray-500",
    )
    return html.Div([description, graph])
