import pandas as pd
import streamlit as st
import st_aggrid as sta

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
        "font-size": "30px", "color": "black", "background-color": "white",
        "padding": "10px !important"
        },
    ".ag-header-group-cell": {
        "font-size": "30px", "color": "black", "background-color": "white",
        "padding": "10px !important"
        },
    ".ag-header-cell-label": {
        "white-space": "normal !important",
        "overflow-wrap": "break-word !important",
         "padding": "10px !important",  # Optional: adds visual spacing
        "line-height": "1.0"
    },
    ".ag-row": {
        "font-size": "30px"
        },
    ".ag-cell": {
        "display": "flex", "align-items": "center",
        "white-space": "normal !important",
        "overflow-wrap": "break-word !important",
        "padding": "4px !important",  # Optional: adds visual spacing
        "line-height": "1.0"
        },
    ".ag-menu": {
        "font-size": "20px",
        "padding": "10px"
    },
    ".ag-menu-option": {
        "font-size": "20px"
    },
    ".ag-filter": {
        "font-size": "20px"
    },
    ".ag-input-field-input": {
        "font-size": "20px"
    },
    ".ag-popup": {
        "font-size": "20px",
        "line-height": "30px"
    },
    ".ag-set-filter-list": {
        "font-size": "20px",
        "line-height": "30px"
    },
    ".ag-set-filter-item": {
        "font-size": "20px",
        "line-height": "30px"
    },
    ".ag-checkbox-label": {
        "font-size": "20px"
    },
    "ag-filter-body-wrapper": {
        "font-size": "20px"
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

def main():

    st.set_page_config(page_title ='Taxonomy', layout='wide')

    df = pd.read_excel('C:\\Users\\werning\\IIASA\\ECE.prog - CWF\\SCIL_2024\\Taxonomy\\Taxonomy update\\taxonomy_update_v1p2.xlsx', header=[0,1,2,3])

    df.columns = ['Dimension', 'Category', 'Specific CID', 'Scale', 'Example', 'Scale ', 'Example ', 'Duration', 'Example  ', 'Low/No Confidence', 
                  'Moderate Confidence', 'High Confidence', 'Example   ', 'Low/No Confidence ', 'Moderate Confidence ', 'High Confidence ',
                  'Illustrative Research Needs', 'Example     ',
                  'Hazard Focused', 'Vulnerability Focused', 'Exposure Focused', 'Relevant Global Goal on Adaptation Targets',
                  'Critical Global Warming Level','Illustrative Sectoral Emissions Reductions Potential',
                  'WGI', 'WGII', 'WGI ', 'WGII ']

    gridOptions = {'columnDefs': [
                     {'headerName': "Representative Key Risk (RKR)", 
                      'headerClass': 'rkr-header', 
                      'wrapHeaderText': True,
                      'autoHeaderHeight': True,
                      'children': [{'field': "Dimension", 'filter': True, 'wrapText': True, 'autoHeight': True, 'pinned': 'left'}],
                      'type': []}, 
                     {'headerName': "Climatic Impact Driver (CID)",
                      'headerClass': 'cid-header',
                      'wrapHeaderText': True,
                      'autoHeaderHeight': True,
                      'children': [{'field': "Category", 'filter': True,'headerClass': 'grey-cell', 'wrapText': True, 'autoHeight': True, 'pinned': 'left'},
                                   {'field': "Specific CID", 'filter': True, 'headerClass': 'grey-cell','wrapText': True, 'autoHeight': True, 'pinned': 'left'}],
                      'type': []}, 
                      {'headerName': "Climate Impact Characteristics",
                       'headerClass': 'cic-header',
                       'wrapHeaderText': True,
                      'autoHeaderHeight': True,
                      'children': [
                            {'headerName': 'Spatial',
                              'children': [{'field': 'Scale', 'filter': True, 'wrapText': True, 'autoHeight': True},
                                      {'field': 'Example', 'filter': True, 'wrapText': True, 'autoHeight': True}]
                            },
                            {'headerName': 'Temporal',
                             'children': [{'field': 'Scale', 'filter': True, 'headerClass': 'grey-cell', 'wrapText': True, 'autoHeight': True},
                                      {'field': 'Example', 'filter': True, 'headerClass': 'grey-cell', 'wrapText': True, 'autoHeight': True}]
                            },
                            {'field': 'Duration', 'filter': True, 'wrapText': True, 'autoHeight': True}],
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
                                  {'field': 'Example', 'filter': True, 'headerClass': 'grey-cell', 'wrapText': True, 'autoHeight': True},
                                  {'field': 'IPCC AR6 assessment of Relevant Subsystems',
                                   'wrapText': True,
                                    'autoHeight': True,
                                        'children': 
                                            [
                                                {'field': 'Low/No Confidence', 'filter': True, 'wrapText': True, 'autoHeight': True},
                                                {'field': 'Moderate Confidence', 'filter': True, 'wrapText': True, 'autoHeight': True},
                                                {'field': 'High Confidence', 'filter': True, 'wrapText': True, 'autoHeight': True}
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
                                    {'field': 'Example', 'filter': True, 'headerClass': 'grey-cell', 'wrapText': True, 'autoHeight': True},
                                    {'field': 'IPCC AR6 assessment of Relevant Subsystems',
                                     'wrapText': True,
                                     'autoHeight': True,
                                        'children': 
                                            [
                                                {'field': 'Low/No Confidence', 'filter': True, 'wrapText': True, 'autoHeight': True},
                                                {'field': 'Moderate Confidence', 'filter': True, 'wrapText': True, 'autoHeight': True},
                                                {'field': 'High Confidence', 'filter': True, 'wrapText': True, 'autoHeight': True}
                                            ]
                                    }
                                ],
                            },
                            {'field': 'Illustrative Research Need', 'filter': True,'headerClass': 'grey-cell', 'wrapText': True, 'autoHeight': True},
                            {'headerName': 'Modelling',
                             'headerClass': 'blue-cell',
                             'wrapHeaderText': True,
                             'autoHeaderHeight': True,
                             'children': 
                                [
                                    {'field': 'Example     ', 'filter': True,'wrapText': True, 'autoHeight': True},
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
                              'children': [{'field': 'Hazard Focused', 'filter': True, 'headerClass': 'grey-cell', 'wrapText': True, 'autoHeight': True},
                                      {'field': 'Vulnerability Focused', 'filter': True, 'headerClass': 'grey-cell','wrapText': True, 'autoHeight': True},
                                      {'field': 'Exposure Focused', 'filter': True,'headerClass': 'grey-cell', 'wrapText': True, 'autoHeight': True}]
                            },
                            {'field': 'Relevant Global Goal on Adaptation Targets', 'filter': True, 'wrapText': True, 'autoHeight': True}],                            
                      'type': []},                                     
                      {'headerName': "Mitigation Linkages",
                       'headerClass': 'mit-header',
                       'wrapHeaderText': True,
                       'autoHeaderHeight': True,
                      'children': [
                            {'field': 'Critical Global Warming Level', 'filter': True, 'headerClass': 'grey-cell', 'wrapText': True, 'autoHeight': True},
                            {'field': 'Illustrative Sectoral Emissions Reductions Potential', 'filter': True,'headerClass': 'grey-cell', 'wrapText': True, 'autoHeight': True}],                            
                      'type': []},
                      {'headerName': "IPCC Chapter References",
                       'headerClass': 'chap-header',
                       'wrapHeaderText': True,
                       'autoHeaderHeight': True,
                      'children': [
                            {'headerName': 'AR6',
                             'headerClass': 'green-cell',
                              'children': [{'field': 'WGI', 'filter': True, 'wrapText': True, 'autoHeight': True},
                                      {'field': 'WGII', 'filter': True, 'wrapText': True, 'autoHeight': True}]
                            },
                            {'headerName': 'AR7',
                             'headerClass': 'green-cell',
                              'children': [{'field': 'WGI ', 'filter': True, 'headerClass': 'grey-cell','wrapText': True, 'autoHeight': True},
                                      {'field': 'WGII ', 'filter': True,'headerClass': 'grey-cell', 'wrapText': True, 'autoHeight': True}]
                            }],                            
                      'type': []},
                     ],
                    'rowVerticalPaddingScale': 3.0,
                    #  'rowHeight': 50,
                    #  'headerHeight': 50,
                    #  'groupHeaderHeight': 50,
                     } 
                    #  'autoSizeStrategy': {'type': 'fitCellContents', 'skipHeader': False}}

        # Create GridOptionsBuilder to customize grid options
    gob = sta.GridOptionsBuilder.from_dataframe(df)

    # Configure column filters for all columns
    for column in df.columns:
        gob.configure_column(column, filter=True)

    # gridOptions = gob.build()
    # print(gridOptions)

    # Display the table using streamlit-aggrid
    sta.AgGrid(df, gridOptions=gridOptions, update_mode=sta.GridUpdateMode.MODEL_CHANGED, custom_css=custom_css, height=1000)

if __name__ == "__main__":
    main()

#st.dataframe(df)
#AgGrid(df)

