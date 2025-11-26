import base64

def hyperlink_image(image_path, website):
    return f"""<a href="{website}">
    <img src="data:image/png;base64,{{}}" width=100% text-align: center>
    </a>""".format(
        base64.b64encode(open(f"{image_path}", "rb").read()).decode()
    )