from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Callable, List, Union

import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.development.base_component import Component

ItemLayoutClass = Union[dcc.Link, dbc.Accordion]


class BaseMenuItem(ABC):
    @abstractmethod
    def get_menu_item_layout(self) -> ItemLayoutClass:
        ...  # pragma: no cover

    @property
    @abstractmethod
    def pages(self) -> List["MenuItem"]:
        ...  # pragma: no cover


@dataclass
class MenuItem(BaseMenuItem):
    name: str
    layout: Union[Component, Callable[[None], Component]]
    route: str
    icon: str = None

    def get_menu_item_layout(self) -> ItemLayoutClass:
        return html.Li(
            className="nav-item",
            children=[
                dcc.Link(
                    href=self.route,
                    className="nav-link",
                    children=[html.I(className=self.icon), html.Span(self.name)],
                )
            ],
        )

    def get_layout(self) -> Component:
        return self.layout() if callable(self.layout) else self.layout

    @property
    def pages(self) -> List["MenuItem"]:
        return [self]


@dataclass
class MenuGroup(BaseMenuItem):
    name: str
    items: List[MenuItem]

    def get_menu_item_layout(self) -> ItemLayoutClass:
        return html.Li(
            className="nav-item",
            children=[
                html.H6(
                    className="sidebar-heading px-3 mt-4 mb-1 text-muted",
                    children=self.name,
                ),
                html.Ul(
                    className="nav flex-column mb-3 px-3",
                    children=[item.get_menu_item_layout() for item in self.items],
                ),
            ],
        )

    @property
    def pages(self) -> List["MenuItem"]:
        return self.items


def get_main_layout(navigation_layout: List[Component]) -> Component:
    return html.Div(
        className="container-fluid",
        children=[
            dcc.Location(id="url", refresh=False),
            html.Nav(
                className="d-flex flex-column col-4 col-md-3 col-lg-2 bg-white sidebar",
                children=navigation_layout,
            ),
            html.Div(
                className="ms-auto col-8 col-md-9 col-lg-10 px-md-4 py-3",
                id="content",
            ),
        ],
    )


Menu = List[BaseMenuItem]
