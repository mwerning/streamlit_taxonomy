import pandas as pd
import streamlit as st
import st_aggrid as sta
import requests
from visual_library.hyperlink_image import hyperlink_image
import streamlit.components.v1 as components


def load_data(file_path):
    return pd.read_excel(file_path)

#Define custom CSS
custom_css = {
    # ".ag-row-hover": {"background-color": "red !important"},
    # ".ag-header-cell-label": {
    #     "background-color": "white"
    #     },
    # #".ag-header-cell-text": {"font-size": "60px", "color": "red", "background-color": "red"},
    ".ag-header-cell": {
        "font-size": "11px", "color": "black", "background-color": "white",
        "padding": "5px !important"
        },
    ".ag-header-group-cell": {
        "font-size": "11px", "color": "black", "background-color": "white",
        "padding": "5px !important"
        },
    ".ag-header-cell-label": {
        "white-space": "normal !important",
        "overflow-wrap": "break-word !important",
         "padding": "5px !important",  # Optional: adds visual spacing
        "line-height": "1.0"
    },
    ".ag-row": {
        "font-size": "11px"
        },
    ".ag-cell": {
        "display": "flex", "align-items": "center",
        "white-space": "normal !important",
        "overflow-wrap": "break-word !important",
        "padding": "4px !important",  # Optional: adds visual spacing
        "line-height": "1.0"
        },
    ".ag-menu": {
        "font-size": "11px",
        "padding": "5px"
    },
    ".ag-menu-option": {
        "font-size": "11px"
    },
    ".ag-filter": {
        "font-size": "11px"
    },
    ".ag-input-field-input": {
        "font-size": "11px"
    },
    ".ag-popup": {
        "font-size": "11px",
        "line-height": "15px"
    },
    ".ag-set-filter-list": {
        "font-size": "12px",
        "line-height": "15px"
    },
    ".ag-set-filter-item": {
        "font-size": "11px",
        "line-height": "15px"
    },
    ".ag-checkbox-label": {
        "font-size": "11px"
    },
    "ag-filter-body-wrapper": {
        "font-size": "11px"
    },
    ".rkr-header": {
        "background-color": "lightblue !important",
        "color": "black !important",
        "font-weight": "bold"
    },
    ".cid-header": {
        "background-color": "lightblue !important",
        "color": "black !important",
        "font-weight": "bold"
    },
    ".cic-header": {
        "background-color": "lightcoral !important",
        "color": "black !important",
        "font-weight": "bold"
    },
    ".cia-header": {
        "background-color": "lightsalmon !important",
        "color": "black !important",
        "font-weight": "bold"
    },
    ".adap-header": {
        "background-color": "lightcoral !important",
        "color": "black !important",
        "font-weight": "bold"
    },
    ".mit-header": {
        "background-color": "lightsalmon !important",
        "color": "black !important",
        "font-weight": "bold"
    },
    ".chap-header": {
        "background-color": "lightcoral !important",
        "color": "black !important",
        "font-weight": "bold"
    },
    ".grey-cell": {
        "background-color": "whitesmoke !important",
        "color": "black !important",
        "font-weight": "bold"
    },
    ".green-cell": {
        "background-color": "paleturquoise !important",
        "color": "black !important",
        "font-weight": "bold"
    },
    ".yellow-cell": {
        "background-color": "lightyellow !important",
        "color": "black !important",
        "font-weight": "bold"
    },
    ".blue-cell": {
        "background-color": "powderblue !important",
        "color": "black !important",
        "font-weight": "bold"
    },
    }

def create_github_issue(title, body, email, institution, rkr, cid):
    """Create a GitHub issue using REST API."""
    github_token = st.secrets["GITHUB_TOKEN"]
    repo = st.secrets["GITHUB_REPO"]
    url = f"https://api.github.com/repos/{repo}/issues"
    
    headers = {
        "Authorization": f"token {github_token}",
        "Accept": "application/vnd.github+json"
    }

    rkr = 'not specified' if not rkr else rkr
    cid = 'not specified' if not cid else cid


    issue_data = {
        "title": title,
        "body": f"**Feedback:**\n{body}\n\n**Relates to RKR(s)** {rkr} and **CID(s)** {cid}\n\n**Submitted by** {email or 'N/A'} **from** {institution}"
    }

    response = requests.post(url, headers=headers, json=issue_data)
    return response

def main():
    st.set_page_config(page_title='Climate Impact Taxonomy', layout='wide')

    st.markdown("""
        <style>
            /* Reduce the blank space between sidebar and main content */
            .block-container {
                padding-left: 0.5rem !important;   /* default is ~3rem */
                padding-right: 0.5rem !important;
                padding-top: 1rem !important;      /* optional */
                padding-bottom: 2rem !important;   /* optional */
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("""
        <style>

        /* Global override for dropdown options anywhere */
        div[role="option"] {
            font-size: 12px !important;
            line-height: 1.2em !important;
            padding-top: 2px !important;
            padding-bottom: 2px !important;
        }

        /* If there is an outer container with .css-… classes that wraps the options */
        div[data-baseweb="popover"] div[role="option"] {
            font-size: 12px !important;
            padding: 0.2rem 0.3rem !important;
        }

        /* Override the input/selected area in multiselect */
        div[data-baseweb="select"] > div {
            font-size: 12px !important;
        }

        /* Override the tags (chips) for selected items */
        div[data-baseweb="tag"] {
            font-size: 11px !important;
            margin: 1px !important;
            padding: 1px 3px !important;
        }

        /* For sidebar text generally */ 
        section[data-testid="stSidebar"] * {
            font-size: 12px !important;
        }

        /* Make dropdown search box smaller too */
        div[data-baseweb="popover"] input {
            font-size: 12px !important;
        }

        </style>
        """, unsafe_allow_html=True)

    # === Load Data ===
    df = pd.read_excel('climate_impact_taxonomy.xlsx', header=[0, 1, 2, 3], sheet_name='Taxonomy')

    # Flatten column names
    df.columns = [
        'Dimension', 'Type', 'Category', 'Scale', 'Example', 'Scale ', 'Example ', 'Type of change', 'Example  ',
        'None/Low', 'Low/Moderate', 'High', 'Example   ',
        'None/Low ', 'Low/Moderate ', 'High ',
        'Illustrative Research Need', 'Example     ',
        'Hazard Focused', 'Vulnerability Focused', 'Exposure Focused',
        'Relevant Global Goal on Adaptation Targets',
        'Critical Global Warming Level', 'Illustrative Sectoral Emissions Reductions Potential',
        'WGI', 'WGII', 'WGI ', 'WGII '
    ]

    info_table_1 = pd.read_excel('assets/info_table_1.xlsx')
    info_table_1.columns = ['Category group', 'Category component', 'Description', 'Background information']

    info_table_2 = pd.read_excel('assets/info_table_2.xlsx', header=[0,1])
    info_table_2.columns = ['Representative Key Risks (RKRs)', 'Core subsystems/assets', 'Complementary subsystems/assets']

    # === Sidebar Filters ===
    st.sidebar.header("🔍 Filter Options")

    st.markdown("""
        <style>

            /* Apply smaller font size to all elements inside the feedback form */
            div[data-testid="stForm"] * {
                font-size: 11px !important;
            }

            /* Compact spacing for inputs and textarea */
            div[data-testid="stForm"] div[data-baseweb="input"] > div,
            div[data-testid="stForm"] textarea {
                min-height: 1.5em !important;
                padding: 0.25rem 0.5rem !important;
            }

            /* Make labels smaller */
            div[data-testid="stForm"] label p {
                font-size: 11px !important;
                margin-bottom: 0.2rem !important;
            }
                
            div[role="listbox"] div[role="option"] {
                font-size: 12px !important;
                line-height: 1.2em !important;
                padding-top: 0.25rem !important;
                padding-bottom: 0.25rem !important;
            }

            </style>
    """, unsafe_allow_html=True)

    with st.sidebar.expander("Filters", expanded=True):
        # Helper to build consistent dropdowns
        def multi_filter(label, column_name):
            options = sorted(df[column_name].dropna().unique())
            return st.multiselect(label, options=options, default=[])

        selected_dimension = multi_filter("Dimension", "Dimension")
        selected_category = multi_filter("Type", "Type")
        selected_specific_cid = multi_filter("Category", "Category")

        # Handle both 'Scale' columns
        selected_scale_1 = multi_filter("Scale (Spatial)", "Scale")
        selected_scale_2 = multi_filter("Scale (Temporal)", "Scale ")

        selected_change = multi_filter("Type of change", "Type of change")
        selected_cgwl = multi_filter("Critical Global Warming Level", "Critical Global Warming Level")

    with st.sidebar:
        
        with st.columns([0.2, 0.8, 0.2])[1]:
            st.markdown(
                hyperlink_image(
                    "assets/iiasa-logo.png", "https://iiasa.ac.at/"
                ),
                unsafe_allow_html=True,
            )
        st.write("")

        with st.columns([0.2, 0.8, 0.2])[1]:
            st.markdown(
                hyperlink_image(
                    "assets/cwf-logo.png",
                    "https://www.climateworks.org/",
                ),
                unsafe_allow_html=True,
            )

        st.write("***")

    # === Apply Filters ===
    filtered_df = df.copy()

    if selected_dimension:
        filtered_df = filtered_df[filtered_df["Dimension"].isin(selected_dimension)]

    if selected_category:
        filtered_df = filtered_df[filtered_df["Type"].isin(selected_category)]

    if selected_specific_cid:
        filtered_df = filtered_df[filtered_df["Category"].isin(selected_specific_cid)]

    if selected_scale_1:
        filtered_df = filtered_df[filtered_df["Scale"].isin(selected_scale_1)]

    if selected_scale_2:
        filtered_df = filtered_df[filtered_df["Scale "].isin(selected_scale_2)]

    if selected_change:
        filtered_df = filtered_df[filtered_df["Type of change"].isin(selected_change)]

    if selected_cgwl:
        filtered_df = filtered_df[filtered_df["Critical Global Warming Level"].isin(selected_cgwl)]

    # st.sidebar.markdown(f"**Rows shown:** {len(filtered_df)} / {len(df)}")

    st.markdown("""
        <style>
        /* General font size inside sidebar */
        section[data-testid="stSidebar"] * {
            font-size: 12px !important;
        }

        /* Adjust dropdown menu text */
        div[data-baseweb="select"] {
            font-size: 12px !important;
        }

        /* Dropdown menu items */
        ul[role="listbox"] li {
            font-size: 12px !important;
            padding: 0.25rem 0.5rem !important;
        }

        /* Selected items (chips in multiselect) */
        div[data-baseweb="tag"] {
            font-size: 11px !important;
            padding: 0.1rem 0.3rem !important;
        }

        /* Input box inside dropdown */
        div[data-baseweb="input"] input {
            font-size: 12px !important;
        }

        /* Label text */
        section[data-testid="stSidebar"] label p {
            font-size: 12px !important;
            margin-bottom: 0.1rem !important;
        }
        </style>
        """, unsafe_allow_html=True)

    st.markdown(
    """
    <style>
    div.stButton > button > div {
        font-size: 12px !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)


    left_logo = hyperlink_image("assets/iiasa-logo.png", "https://iiasa.ac.at/")
    right_logo = hyperlink_image("assets/cwf-logo.png", "https://www.climateworks.org/")

    # === Header row with 4 columns ===
    col1, col2, col3, col4, col5 = st.columns([2, 0.6, 0.6, 4, 1])  # Adjust ratios as needed

    with col1:
        st.markdown(
            "**Climate Impact Taxonomy** ",
            # "<span style='font-size:12px; color:gray'>developed by IIASA & CWF</span>",
            unsafe_allow_html=True
        )

    # with col2:
    #     st.markdown(left_logo, unsafe_allow_html=True)

    # with col3:
    #     st.markdown(right_logo, unsafe_allow_html=True)

    with col5:

        infoGridOptions1 = {
            'defaultColDef': {
                'resizable': True,
                'wrapText': True,
                'autoHeight': True
            },

            'columnDefs': [
                {'field': 'Category group', 'spanRows': True,},
                {'field': 'Category component', 'spanRows': True,},
                {'field': 'Description', 'spanRows': False,},
                {'field': 'Background information', 'spanRows': False,},
            ],
            'enableCellSpan': True,
        }

        infoGridOptions2 = {
            'defaultColDef': {
                'resizable': True,
                'wrapText': True,
                'autoHeight': True,
                'cellStyle':{
                    'whiteSpace': 'pre-wrap'
                }
            },

            'columnDefs':[
                {
                    'headerName': '',
                    'wrapHeaderText': True,
                    'children': [
                        {'field': 'Representative Key Risks (RKRs)'}
                    ]
                },
                {
                    'headerName': 'Relevant subsystems/assets from IPCC AR6 WGI Table 12.2',
                    'wrapHeaderText': True,
                    'children': [
                        {'field': 'Core subsystems/assets'},
                        {'field': 'Complementary subsystems/assets'}
                    ]   
                },
            ],
            'enableCellSpan': True,


        }

        info_table_css = {
            ".ag-root-wrapper": {"border": "none"},
            ".ag-cell": {"border": "none","white-space": "pre-wrap !important"},
            ".ag-header-cell": {"border": "none"},
            ".ag-row": {"border": "none"},
        }

        @st.dialog("Climate impact taxonomy - additional information", width='large')
        def open_modal():
            st.write("**Taxonomy description**")
            st.write("This taxonomy was developed by the International Institute for Applied Systems Analysis (IIASA) as part of the Scoping the Climate Impact Landscape (SCIL) project, funded by ClimateWorks. It is designed to capture the breadth of climate impacts and to map them onto different risk dimensions, while pointing to adaptation and mitigation linkages. The taxonomy uses the IPCC AR6 Working Group I and II assessments as main references and applies the IPCC concepts of Climatic Impact-Drivers (CIDs) and Representative Key Risks (RKRs) as guiding taxonomy categories. The taxonomy does NOT provide a comprehensive or exhaustive analysis of all climate impacts, but is intended to help the user improve their understanding of the diverse climate impact landscape and to facilitate a more targeted exploration of research engagement opportunities")
            st.write("**Taxonomy use**")
            st.write("The taxonomy is targeted at users from philanthropies engaging in the climate space and any non-experts interested in learning more about the climate impact landscape. For each RKR-specific ensemble of CIDs, the taxonomy provides more specific climate impact information grouped in five broad categories: Climate Impact Characteristics; Climate Impact Assessment; Adaptation Linkages; Mitigation Linkages, IPCC AR6 & AR7 Chapter References. More details on the individual taxonomy categories can be found in the table below, including information which categories can be used to sort and filter the full set of RKR-CID combinations.")
            st.write("**Taxonomy details**")
            #st.table(data=st.dataframe(readme, hide_index=True))
            sta.AgGrid(info_table_1, gridOptions=infoGridOptions1, custom_css=info_table_css, fit_columns_on_grid_load=True) 
            st.write('The table below shows which core subsystems/assets were used for the IPCC AR6 Assessment of CID Relevance for Natural and Human Systems. ')
            sta.AgGrid(info_table_2, gridOptions=infoGridOptions2, custom_css=info_table_css, fit_columns_on_grid_load=True) 
            st.write("**Taxonomy analysis**")
            st.write("To be added")
            st.caption("Click outside or press Esc to close")

        if st.button("More information"):
            open_modal()

    # === Grid Options ===
    gridOptions = {
        'columnTypes': {
            'small': { 
                'width': 100,
            },
            'extrasmall': { 
                'width': 75,
            },
            'bigger': { 
                'width': 175,
            }
        },        
        'columnDefs': [
            {
                'headerName': "Representative Key Risk (RKR)",
                'headerClass': 'rkr-header',
                'wrapHeaderText': True,
                'autoHeaderHeight': True,
                'children': [{
                    'field': "Dimension",
                    'headerTooltip': "Eight RKR categories as defined and assessed in IPCC AR6 WGII",
                    'wrapText': True,
                    'autoHeight': True,
                    'pinned': 'left',
                    'type': 'extrasmall'
                }]
            },
            {
                'headerName': "Climatic Impact Driver (CID)",
                'headerClass': 'cid-header',
                'wrapHeaderText': True,
                'autoHeaderHeight': True,
                'children': [
                    {
                        'field': "Type", 
                        'headerTooltip': "Seven CID types as defined and assessed in IPCC AR6 WGI",
                        'headerClass': 'grey-cell', 
                        'wrapText': True, 
                        'autoHeight': True, 
                        'pinned': 'left', 
                        'type': 'extrasmall'},
                    {''
                        'field': "Category", 
                        'headerTooltip': "Total of 35 CIDs as defined and assessed in IPCC AR6 WGI",
                        'headerClass': 'grey-cell', 
                        'wrapText': True, 
                        'autoHeight': True, 
                        'pinned': 'left', 
                        'type': 'extrasmall'}
                ]
            },
            {'headerName': "Climate Impact Characteristics",
                       'headerClass': 'cic-header',
                       'wrapHeaderText': True,
                      'autoHeaderHeight': True,
                      'children': [
                            {'headerName': 'Spatial',
                              'children': [{
                                            'field': 'Scale', 
                                            'headerTooltip': "Distinction between local, regional, and global scale of CID",
                                            'wrapText': True, 
                                            'autoHeight': True, 
                                            'type': 'extrasmall'},
                                        {
                                            'field': 'Example',
                                            'headerTooltip': "Example to contextualize the spatial scale of climate impact", 
                                            'filter': True, 
                                            'wrapText': True, 
                                            'autoHeight': True, 
                                            'type': 'small'}]
                            },
                            {'headerName': 'Temporal',
                             'children': [{
                                            'field': 'Scale ', 
                                            'headerTooltip': "Distinction between seven duration levels of climate impact (minutes to hours; hours to days; days to weeks; weeks to months; months to years; years to decades; decades to centuries)", 
                                            'headerClass': 'grey-cell', 
                                            'wrapText': True, 
                                            'autoHeight': True, 
                                            'type': 'extrasmall'},
                                        {
                                            'field': 'Example', 
                                            'headerTooltip': "Example to contextualize the temporal scale of climate impact", 
                                            'filter': True, 
                                            'headerClass': 'grey-cell', 
                                            'wrapText': True, 
                                            'autoHeight': True, 
                                            'type': 'small'}]
                            },
                            {
                                'field': 'Type of change', 
                                'headerTooltip': "Distinction between change in climate mean and change in climate extremes",
                                'wrapText': True, 
                                'autoHeight': True, 
                                'type': 'extrasmall'
                            }],
                      'type': []},
                       {'headerName': "Climate Impact Assessment",
                        'headerClass': 'cia-header',
                        'wrapHeaderText': True,
                      'autoHeaderHeight': True,
                        'children': 
                        [
                            {'headerName': 'Natural Systems',
                             'headerClass': 'green-cell',
                             'wrapHeaderText': True,
                             'autoHeaderHeight': True,
                              'children': 
                              [
                                  {
                                        'field': 'Example', 
                                        'headerTooltip': "Climate impact examples specific to RKR context for natural and/or human systems; N/A is used when specific RKR-CID combinations could not be directly related to IPCC AR6 WGI Table 12.2",
                                        'filter': True, 
                                        'headerClass': 'grey-cell', 
                                        'wrapText': True, 
                                        'autoHeight': True, 
                                        'type': 'small'},
                                  {'field': 'CID Relevance for RKR Subsystems',
                                   'headerTooltip': "Evidence is gathered from IPCC AR6 WGI Table 12.2, with core subsystems (referred to as assets in the table) directly linked to RKRs with complementary subsystems added from relevant other sectors (max. 2 per sector); N/A is used when specific RKR-CID combinations could not be directly related to IPCC AR6 WGI Table 12.2",
                                   'wrapText': True,
                                    'autoHeight': True,
                                        'children': 
                                            [
                                                {'field': 'None/Low', 'filter': True, 'wrapText': True, 'autoHeight': True, 'type': 'bigger'},
                                                {'field': 'Low/Moderate', 'filter': True, 'wrapText': True, 'autoHeight': True, 'type': 'bigger'},
                                                {'field': 'High', 'filter': True, 'wrapText': True, 'autoHeight': True, 'type': 'bigger'}
                                            ]
                                    }
                                ],                                      
                            },
                            {'headerName': 'Human Systems',
                             'headerClass': 'yellow-cell',
                             'wrapHeaderText': True,
                             'autoHeaderHeight': True,
                             'children': 
                                [
                                    {'field': 'Example', 'filter': True, 'headerClass': 'grey-cell', 'wrapText': True, 'autoHeight': True, 'type': 'small'},
                                    {'field': 'CID Relevance for RKR Subsystems',
                                     'headerTooltip': "Evidence is gathered from IPCC AR6 WGI Table 12.2, with core subsystems (referred to as assets in the table) directly linked to RKRs with complementary subsystems added from relevant other sectors (max. 2 per sector); N/A is used when specific RKR-CID combinations could not be directly related to IPCC AR6 WGI Table 12.2",
                                     'wrapText': True,
                                     'autoHeight': True,
                                        'children': 
                                            [
                                                {'field': 'None/Low ', 'filter': True, 'wrapText': True, 'autoHeight': True, 'type': 'bigger'},
                                                {'field': 'Low/Moderate ', 'filter': True, 'wrapText': True, 'autoHeight': True, 'type': 'bigger'},
                                                {'field': 'High ', 'filter': True, 'wrapText': True, 'autoHeight': True, 'type': 'bigger'}
                                            ]
                                    }
                                ],
                            },
                            {
                                'field': 'Illustrative Research Need', 
                                'headerTooltip': "Example of topics where more research is needed",
                                'filter': True,'headerClass': 'grey-cell', 
                                'wrapText': True, 
                                'autoHeight': True, 
                                'type': 'small'},
                            {'headerName': 'Modelling',
                             'headerClass': 'blue-cell',
                             'wrapHeaderText': True,
                             'autoHeaderHeight': True,
                             'children': 
                                [
                                    {
                                        'field': 'Example     ', 
                                        'headerTooltip': "Example of a modeling approach or framework used in the context of the specific CID-RKR combination",
                                        'filter': True,
                                        'wrapText': True, 
                                        'autoHeight': True, 
                                        'type': 'small'},
                                ],
                            },
                        ]
                     }, 
                     {'headerName': "Adaptation Linkages",
                      'headerClass': 'adap-header',
                      'wrapHeaderText': True,
                      'autoHeaderHeight': True,
                      'children': [
                            {'headerName': 'Illustrative Adaptation Response by Risk Component',
                             'wrapText': True,
                             'autoHeight': True,
                             'headerClass': 'yellow-cell',
                              'children': [{''
                                            'field': 'Hazard Focused', 
                                            'headerTooltip': "Illustrative adaptation response targeting the hazard component of the IPCC 'risk propeller' (see also IPCC AR6 WGII Chapter 16)",
                                            'filter': True, 
                                            'headerClass': 'grey-cell', 
                                            'wrapText': True, 
                                            'autoHeight': True, 
                                            'type': 'bigger'},
                                        {
                                            'field': 'Vulnerability Focused', 
                                            'headerTooltip': "Illustrative adaptation response targeting the vulnerability component of the IPCC 'risk propeller' (see also IPCC AR6 WGII Chapter 16)",
                                            'filter': True, 
                                            'headerClass': 'grey-cell',
                                            'wrapText': True, 
                                            'autoHeight': True, 
                                            'type': 'bigger'},
                                        {
                                            'field': 'Exposure Focused', 
                                            'headerTooltip': "Illustrative adaptation response targeting the exposure component of the IPCC 'risk propeller' (see also IPCC AR6 WGII Chapter 16)",
                                            'filter': True,
                                            'headerClass': 'grey-cell', 
                                            'wrapText': True, 
                                            'autoHeight': True, 
                                            'type': 'bigger'}]
                            },
                            {
                                'field': 'Relevant Global Goal on Adaptation Targets', 
                                'headerTooltip': "Examples of targets from the UNFCCC's Global Goal on Adaptation relevant for each RKR-CID combination",
                                'filter': True, 
                                'wrapText': True, 
                                'autoHeight': True, 
                                'type': 'bigger'}],                            
                      'type': []},                                     
                      {'headerName': "Mitigation Linkages",
                       'headerClass': 'mit-header',
                       'wrapHeaderText': True,
                       'autoHeaderHeight': True,
                      'children': [
                            {
                                'field': 'Critical Global Warming Level', 
                                'headerTooltip': "Assessed global warming levels (GWLs) beyond which changes in climate impacts become critical; for cold related impacts, current GWL are used with specifier on expected changes with increasing warming",
                                'headerClass': 'grey-cell', 
                                'wrapText': True, 
                                'autoHeight': True, 
                                'type': 'small'},
                            {
                                'field': 'Illustrative Sectoral Emissions Reductions Potential', 
                                'headerTooltip': "Illustrative example of how emissions reductions in sectors relevant to the CID-RKR combination could be achieved",
                                'filter': True,
                                'headerClass': 'grey-cell', 
                                'wrapText': True, 
                                'autoHeight': True, 
                                'type': 'small'}],                            
                      'type': []},
                      {'headerName': "IPCC Chapter References",
                       'headerClass': 'chap-header',
                       'wrapHeaderText': True,
                       'autoHeaderHeight': True,
                      'children': [
                            {'headerName': 'AR6',
                             'headerClass': 'green-cell',
                              'children': [{
                                                'field': 'WGI', 
                                                'headerTooltip': "Chapter references for AR6 WGI down to chapter subsection levels that allow for exploring the assessment related to CID-RKR combination in greater depth",
                                                'filter': True, 
                                                'wrapText': True, 
                                                'autoHeight': True, 
                                                'type': 'extrasmall'
                                                },
                                            {
                                                'field': 'WGII', 
                                                'headerTooltip': "Chapter references for AR6 WGII down to chapter subsection levels that allow for exploring the assessment related to CID-RKR combination in greater depth",
                                                'filter': True, 
                                                'wrapText': True, 
                                                'autoHeight': True, 
                                                'type': 'extrasmall'
                                                }]
                            },
                            {'headerName': 'AR7',
                             'headerClass': 'green-cell',
                              'children': [{''
                                                'field': 'WGI ',
                                                'headerTooltip': "Chapter references for AR7 WGI based on the outlined chapter structure for AR7", 
                                                'filter': True, 
                                                'headerClass': 'grey-cell',
                                                'wrapText': True, 
                                                'autoHeight': True, 
                                                'type': 'extrasmall'
                                                },
                                            {
                                                'field': 'WGII ', 
                                                'headerTooltip': "Chapter references for AR7 WGII based on the outlined chapter structure for AR7",
                                                'filter': True,
                                                'headerClass': 'grey-cell', 
                                                'wrapText': True, 
                                                'autoHeight': True, 
                                                'type': 'extrasmall'
                                            }]
                            }],                            
                      'type': []},
            # (keep all your existing column groups unchanged)
        ],
        'rowVerticalPaddingScale': 3.0,
        # 'autoSizeStrategy': {'type': 'fitGridWidth'},
        'skipHeaderOnAutoSize': True
    }

    # === Display Grid ===
    sta.AgGrid(
        filtered_df,
        gridOptions=gridOptions,
        update_mode=sta.GridUpdateMode.MODEL_CHANGED,
        custom_css=custom_css,
        height=800,
        width='100%'
    )

        # === Feedback Form ===
    st.markdown(
        '<p style="font-size:16px; font-weight:600; margin-bottom:0.5rem;">💬 Provide Feedback</p>',
        unsafe_allow_html=True
    )

    st.markdown(
    """
    <p style="
        font-size:14px;
        line-height:1.5;
        margin-top:0.5rem;
        margin-bottom:1.2rem;
    ">
        If you found an issue, have a suggestion, or want to comment on the taxonomy,
        please submit your feedback below. It will automatically create a GitHub issue
        in the repository that hosts this app.
    </p>
    """,
    unsafe_allow_html=True
    )

    st.markdown("""
    <style>
    /* Target the specific submit button inside the form */
    div[data-testid="stForm"] div[data-testid="baseButton-secondaryFormSubmit"] button {
        font-size: 12px !important;      /* adjust this number */
        padding: 0.4rem 0.9rem !important;
        font-weight: 500 !important;
        border-radius: 4px !important;
    }

    /* Optional: Adjust hover effect */
    div[data-testid="stForm"] div[data-testid="baseButton-secondaryFormSubmit"] button:hover {
        opacity: 0.9 !important;
        transform: scale(1.01);
    }
    </style>
    """, unsafe_allow_html=True)

    with st.form("feedback_form", clear_on_submit=True):
        feedback_title = st.text_input("**Title**")
        feedback_text = st.text_area("**Feedback**")
        feedback_email = st.text_input("**Your email**")
        feedback_institution = st.text_input("**Your institution**")
        feedback_rkr = st.text_input("**RKR(s) (optional)**")
        feedback_cid = st.text_input("**CID(s) (optional)**")
        submitted = st.form_submit_button("📬 Submit Feedback")

        if submitted:
            if feedback_title.strip() == "" or feedback_text.strip() == "" or feedback_email.strip() == ""  or feedback_institution.strip() == "":
                st.error("⚠️ Please provide a title, feedback and your email address in case we have further questions regarding your feedback.")
            else:
                with st.spinner("Submitting feedback to GitHub..."):
                    response = create_github_issue(feedback_title, feedback_text, feedback_email, feedback_institution, feedback_rkr, feedback_cid)
                    if response.status_code == 201:
                        st.success("✅ Feedback submitted successfully! Thank you for your contribution.")
                    else:
                        st.error(f"❌ Failed to submit feedback ({response.status_code}).")
                        st.text(response.text)

    st.markdown('<style id="final-style">div[data-baseweb="popover"] div[role="option"]{font-size:12px!important;}</style>', unsafe_allow_html=True)


if __name__ == "__main__":
    main()
