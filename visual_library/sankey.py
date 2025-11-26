import plotly.graph_objects as go
from matplotlib.cbook import flatten
from matplotlib.colors import rgb2hex, to_rgb, to_rgba

from visual_library.cwf_styles import COLOR_SCALE_RED_TO_GREEN


def sankey_plot_counts_of_values(
    title, data, columns, sorters, colors, use_src_colors, force_position, column_titles
):
    column_values = [data[column].dropna().unique() for column in columns]
    column_values = [
        (
            sorted(column, key=lambda x: sorters[i].loc[x])
            if sorters[i] is not None
            else column
        )
        for i, column in enumerate(column_values)
    ]
    ordered_colors = [
        (
            (col_colors.copy() if isinstance(col_colors, list) else [col_colors[x] for x in column])
            if col_colors is not None
            else COLOR_SCALE_RED_TO_GREEN[: len(column)]
        )
        for col_colors, column in zip(colors, column_values)
    ]

    all_labels = list(flatten(column_values))
    all_colors = list(flatten(ordered_colors))

    sources, targets, values, link_colors = [], [], [], []

    for k in range(len(columns) - 1):
        src = column_values[k]
        dst = column_values[k + 1]
        src_name = columns[k]
        dst_name = columns[k + 1]
        use_src_col = use_src_colors[k]

        node_color = ordered_colors[k if use_src_col else k + 1]

        prev_length = sum([len(column_values[i]) for i in range(k)])

        for i, src_val in enumerate(src):
            for j, dst_val in enumerate(dst):
                sources.append(prev_length + i)
                targets.append(prev_length + len(src) + j)
                values.append(
                    data.loc[data[src_name] == src_val, dst_name]
                    .value_counts()
                    .get(dst_val, 0)
                )

                idx = i if use_src_col else j
                # Add alpha value
                if "rgb" in node_color[idx]:
                    node_color[idx] = [
                        float(x) / 255
                        for x in str(node_color[idx])
                        .split("(")[1]
                        .strip(")")
                        .split(",")
                    ]
                rgb = to_rgb(node_color[idx])
                rgba = f'rgba({",".join(str(int(x*255)) for x in rgb)},0.6)'
                link_colors.append(rgba)
    x = []
    y = []

    percentages = []
    for i, col in enumerate(column_values):
        ys = [((2e-2 if i == 0 else 0) - (2e-2 if i == len(column_values) - 1 else 0) )+ float(i) / (float(len(column_values)) - 1) for _ in col]

        xs = []
        ps = []
        total = len(data[columns[i]].dropna())
        prev_pos = 0
        prev_width = 0
        for j, node in enumerate(col):
            cur_width = (data[columns[i]].dropna() == node).sum()
            new_pos = prev_pos + prev_width + cur_width/(2*total) + 2e-2
            xs.append(new_pos)
            prev_width = cur_width/(2*total)
            prev_pos = new_pos
            ps.append(cur_width/total)

        percentages.append(ps)

        if not force_position[i]:
            x.append([None for _ in col])
            y.append([None for _ in col])
            continue

        x.append(xs)
        y.append(ys)

    x = list(flatten(x))
    y = list(flatten(y))

    percentages = list(flatten(percentages))

    sankey = go.Figure(
        data=[
            go.Sankey(
                node=dict(
                    pad=15,
                    thickness=20,
                    label=[f"{label} ({p*100:.0f}%)" for label, p in zip(all_labels, percentages)],
                    color=all_colors,
                    x=y,
                    y=x,
                ),
                link=dict(
                    source=sources,
                    target=targets,
                    value=values,
                    color=link_colors,
                ),
                arrangement='perpendicular',
            )
        ],
        layout = go.Layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
                # Remove text shadow
            font_shadow='rgba(0, 0, 0, 0)',

        )
    )

    sankey.update_layout(
        title_text=title,
        font_size=15,
        font_color="black",
    )

    for i, col_title in enumerate(column_titles):
        sankey.add_annotation(
            x=i / (len(column_titles) - 1),
            y=1.1,
            text=col_title,#Text
            showarrow=False,
            font=dict(
                color="gray"
            ),
            align="left",
        )

    sankey.update_traces(textfont_color="black", selector=dict(type='sankey'))
    return sankey

def sankey_plot_from_pivot(title, data, src_column, dst_columns, pretty_names=None):
    src_values = list(data[src_column].unique())

    column_values = [src_values, list(pretty_names) if pretty_names else dst_columns]
    all_labels = list(flatten(column_values))

    sources, targets, values = [], [], []

    for i, src_val in enumerate(src_values):
        for j, dst_col in enumerate(dst_columns):
            sources.append(i)
            targets.append(len(src_values) + j)
            values.append(data.loc[data[src_column] == src_val, dst_col].sum())

    sankey = go.Figure(
        data=[
            go.Sankey(
                node=dict(
                    pad=15,
                    thickness=20,
                    label=all_labels,
                ),
                link=dict(
                    source=sources,
                    target=targets,
                    value=values,
                ),
            )
        ]
    )

    sankey.update_layout(
        title_text=title,
        font_size=15,
        font_color="white",
        font_family="",
    )

    return sankey
