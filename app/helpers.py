def get_page_display_name(page_name):
    return page_name.replace("_"," ").replace(".md", "")

def get_page_url_name(page_name):
    return page_name.replace(" ", "_").replace(".md", "")