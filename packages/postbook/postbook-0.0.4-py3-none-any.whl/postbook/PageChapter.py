from postbook.update_index import HtmlChapter

class PageChapter(HtmlChapter):
    def __init__(self, index_name:str,title: str):
        super().__init__(title)
        self.index_name = index_name
    def get_chapter_path(self):
        current_directory = os.getcwd()
        with open(f"{current_directory}/.plog","rb") as f:
            meta_data = pickle.load(f)
            self.abstract = meta_data[self.title.replace('_',' ')]['abstract']
            self.published_on = meta_data[self.title.replace('_',' ')]['published_on']
        if(meta_data['domain']):
            path = f"http://{meta_data['domain']}/{self.index_name}/" + self.title+'.html'
        else:
            path = f"http://{meta_data['ip_address']}/{self.index_name}/" + self.title+'.html'
        return path