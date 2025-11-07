import pandas as pd
import streamlit as st
import st_aggrid as sta
import requests

# st.set_page_config(page_title ='Taxonomy', layout='wide')

# df = pd.read_excel('C:\\Users\\werning\\IIASA\\ECE.prog - CWF\\SCIL_2024\\Taxonomy\\Taxonomy update\\taxonomy_update_v1p2.xlsx')



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

def create_github_issue(title, body, email):
    """Create a GitHub issue using REST API."""
    github_token = st.secrets["GITHUB_TOKEN"]
    repo = st.secrets["GITHUB_REPO"]
    url = f"https://api.github.com/repos/{repo}/issues"
    
    headers = {
        "Authorization": f"token {github_token}",
        "Accept": "application/vnd.github+json"
    }

    issue_data = {
        "title": title,
        "body": f"**Feedback:**\n{body}\n\n**Submitted by:** {email or 'N/A'}"
    }

    response = requests.post(url, headers=headers, json=issue_data)
    return response

def main():
    st.set_page_config(page_title='Taxonomy', layout='wide')

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



    # st.markdown("""
    # <style>
    # /* For React Select dropdown menus */
    # .rc-virtual-list-holder {
    #     font-size: 11px !important;
    # }

    # .rc-virtual-list-holder .rc-virtual-list-item {
    #     font-size: 11px !important;
    #     padding: 4px 8px !important;
    # }

    # /* BaseWeb Select dropdown menu */
    # .baseweb-select-menu {
    #     font-size: 11px !important;
    # }

    # .baseweb-select-menu-item {
    #     font-size: 11px !important;
    #     padding: 4px 8px !important;
    # }

    # /* Also shrink the selected item text in the input box */
    # .baseweb-select-value {
    #     font-size: 11px !important;
    # }
    # </style>
    # """, unsafe_allow_html=True)


    # === Load Data ===
    df = pd.read_excel('taxonomy_update_v1p4.xlsx', header=[0, 1, 2, 3], sheet_name='Taxonomy')
    print(df)

    # Flatten column names
    df.columns = [
        'Dimension', 'Category', 'Specific CID', 'Scale', 'Example', 'Scale ', 'Example ', 'Type of change', 'Example  ',
        'None/Low', 'Low/Moderate', 'High', 'Example   ',
        'None/Low ', 'Low/Moderate ', 'High ',
        'Illustrative Research Need', 'Example     ',
        'Hazard Focused', 'Vulnerability Focused', 'Exposure Focused',
        'Relevant Global Goal on Adaptation Targets',
        'Critical Global Warming Level', 'Illustrative Sectoral Emissions Reductions Potential',
        'WGI', 'WGII', 'WGI ', 'WGII '
    ]

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
        selected_category = multi_filter("Category", "Category")
        selected_specific_cid = multi_filter("Specific CID", "Specific CID")

        # Handle both 'Scale' columns
        selected_scale_1 = multi_filter("Scale (Spatial)", "Scale")
        selected_scale_2 = multi_filter("Scale (Temporal)", "Scale ")

        selected_change = multi_filter("Type of change", "Type of change")
        selected_cgwl = multi_filter("Critical Global Warming Level", "Critical Global Warming Level")

    # === Apply Filters ===
    filtered_df = df.copy()

    if selected_dimension:
        filtered_df = filtered_df[filtered_df["Dimension"].isin(selected_dimension)]

    if selected_category:
        filtered_df = filtered_df[filtered_df["Category"].isin(selected_category)]

    if selected_specific_cid:
        filtered_df = filtered_df[filtered_df["Specific CID"].isin(selected_specific_cid)]

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
                    {'field': "Category", 'headerClass': 'grey-cell', 'wrapText': True, 'autoHeight': True, 'pinned': 'left', 'type': 'extrasmall'},
                    {'field': "Specific CID", 'headerClass': 'grey-cell', 'wrapText': True, 'autoHeight': True, 'pinned': 'left', 'type': 'extrasmall'}
                ]
            },
             {'headerName': "Climate Impact Characteristics",
                       'headerClass': 'cic-header',
                       'wrapHeaderText': True,
                      'autoHeaderHeight': True,
                      'children': [
                            {'headerName': 'Spatial',
                              'children': [{'field': 'Scale', 'wrapText': True, 'autoHeight': True, 'type': 'extrasmall'},
                                      {'field': 'Example', 'filter': True, 'wrapText': True, 'autoHeight': True, 'type': 'small'}]
                            },
                            {'headerName': 'Temporal',
                             'children': [{'field': 'Scale', 'headerClass': 'grey-cell', 'wrapText': True, 'autoHeight': True, 'type': 'extrasmall'},
                                      {'field': 'Example', 'filter': True, 'headerClass': 'grey-cell', 'wrapText': True, 'autoHeight': True, 'type': 'small'}]
                            },
                            {'field': 'Type of change', 'wrapText': True, 'autoHeight': True, 'type': 'extrasmall'}],
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
                                  {'field': 'Example', 'filter': True, 'headerClass': 'grey-cell', 'wrapText': True, 'autoHeight': True, 'type': 'small'},
                                  {'field': 'CID Relevance for RKR Subsystems',
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
                            {'field': 'Illustrative Research Need', 'filter': True,'headerClass': 'grey-cell', 'wrapText': True, 'autoHeight': True, 'type': 'small'},
                            {'headerName': 'Modelling',
                             'headerClass': 'blue-cell',
                             'wrapHeaderText': True,
                             'autoHeaderHeight': True,
                             'children': 
                                [
                                    {'field': 'Example     ', 'filter': True,'wrapText': True, 'autoHeight': True, 'type': 'small'},
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
                              'children': [{'field': 'Hazard Focused', 'filter': True, 'headerClass': 'grey-cell', 'wrapText': True, 'autoHeight': True, 'type': 'bigger'},
                                      {'field': 'Vulnerability Focused', 'filter': True, 'headerClass': 'grey-cell','wrapText': True, 'autoHeight': True, 'type': 'bigger'},
                                      {'field': 'Exposure Focused', 'filter': True,'headerClass': 'grey-cell', 'wrapText': True, 'autoHeight': True, 'type': 'bigger'}]
                            },
                            {'field': 'Relevant Global Goal on Adaptation Targets', 'filter': True, 'wrapText': True, 'autoHeight': True, 'type': 'bigger'}],                            
                      'type': []},                                     
                      {'headerName': "Mitigation Linkages",
                       'headerClass': 'mit-header',
                       'wrapHeaderText': True,
                       'autoHeaderHeight': True,
                      'children': [
                            {'field': 'Critical Global Warming Level', 'headerClass': 'grey-cell', 'wrapText': True, 'autoHeight': True, 'type': 'small'},
                            {'field': 'Illustrative Sectoral Emissions Reductions Potential', 'filter': True,'headerClass': 'grey-cell', 'wrapText': True, 'autoHeight': True, 'type': 'small'}],                            
                      'type': []},
                      {'headerName': "IPCC Chapter References",
                       'headerClass': 'chap-header',
                       'wrapHeaderText': True,
                       'autoHeaderHeight': True,
                      'children': [
                            {'headerName': 'AR6',
                             'headerClass': 'green-cell',
                              'children': [{'field': 'WGI', 'filter': True, 'wrapText': True, 'autoHeight': True, 'type': 'extrasmall'},
                                      {'field': 'WGII', 'filter': True, 'wrapText': True, 'autoHeight': True, 'type': 'extrasmall'}]
                            },
                            {'headerName': 'AR7',
                             'headerClass': 'green-cell',
                              'children': [{'field': 'WGI ', 'filter': True, 'headerClass': 'grey-cell','wrapText': True, 'autoHeight': True, 'type': 'extrasmall'},
                                      {'field': 'WGII ', 'filter': True,'headerClass': 'grey-cell', 'wrapText': True, 'autoHeight': True, 'type': 'extrasmall'}]
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
        submitted = st.form_submit_button("📬 Submit Feedback")

        if submitted:
            if feedback_title.strip() == "" or feedback_text.strip() == "" or feedback_email.strip() == "":
                st.error("⚠️ Please provide a title, feedback and your email address in case we have further questions regarding your feedback.")
            else:
                with st.spinner("Submitting feedback to GitHub..."):
                    response = create_github_issue(feedback_title, feedback_text, feedback_email)
                    if response.status_code == 201:
                        st.success("✅ Feedback submitted successfully! Thank you for your contribution.")
                    else:
                        st.error(f"❌ Failed to submit feedback ({response.status_code}).")
                        st.text(response.text)

    st.markdown('<style id="final-style">div[data-baseweb="popover"] div[role="option"]{font-size:12px!important;}</style>', unsafe_allow_html=True)


if __name__ == "__main__":
    main()
