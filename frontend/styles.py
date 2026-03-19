CYAN = '#00f5d4'
AMBER = '#ff9100'
RED = '#ff003c'
DIM_CYAN = '#004d43'

COLORS = {'cyan': CYAN, 'amber': AMBER, 'red': RED, 'dim_cyan': DIM_CYAN}

CSS = f"""
    Screen {{
        layout: vertical;
        background: #000000;
        padding: 1;
    }}
    #header {{
        height: 5;
        dock: top;
        margin-bottom: 1;
    }}
    #node-container {{
        layout: horizontal;
        height: 1fr;
    }}
    MagiNode {{
        width: 1fr;
        height: 100%;
        margin: 0 1;
    }}
    Input {{
        dock: bottom;
        border: tall {AMBER};
        background: #000000;
        color: {CYAN};
    }}
    Input:focus {{
        border: tall {CYAN};
    }}
    """
