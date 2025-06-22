import streamlit as st
import streamlit.components.v1 as components
import os

_build_dir = os.path.join(os.path.dirname(__file__), "frontend", "build")

_menu = components.declare_component(
    "menu_custom",
    path=_build_dir
)

def render_menu():
    return _menu()
