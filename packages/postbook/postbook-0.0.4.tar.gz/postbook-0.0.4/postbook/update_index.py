from jinja2 import Template, Environment, FileSystemLoader
from postbook.get_list_of_files import get_files
import os
import pickle
import paramiko
class HtmlChapter:
    def __init__(self, title: str):
        self.title = title.split('.')[0]
        self.path = self.get_chapter_path()

    def get_chapter_path(self):
        current_directory = os.getcwd()
        with open(f"{current_directory}/.plog","rb") as f:
            meta_data = pickle.load(f)
            self.abstract = meta_data[self.title.replace('_',' ')]['abstract']
            self.published_on = meta_data[self.title.replace('_',' ')]['published_on']
        if(meta_data['domain']):
            path = f"http://{meta_data['domain']}/blog/" + self.title
        else:
            path = f"http://{meta_data['ip_address']}/blog/" + self.title
        return path

    def __str__(self):
        return self.path
def update_index():
    current_directory = os.getcwd()
    file_path_list = os.path.realpath(__file__).split('/')[:-1]
    file_path = '/'.join(file_path_list)
    template_location  = file_path+'/templates/'

    posts = [HtmlChapter(x) for x in get_files(current_directory+'/posts/')] 
    
    for post in posts:
        print("abstract of ", post, post.abstract)
    # load templates folder to environment (security measure)
    env = Environment(loader=FileSystemLoader(template_location))
   
    with open(f"{current_directory}/.plog","rb") as f:
        meta_data = pickle.load(f)
    
    
    # load the `index.jinja` template
    
    index_template = env.get_template('index.html.j2')
   
    # Have to write a validator function to make sure no error occurs during rendering
    output_from_parsed_template = index_template.render(posts=posts, blog_name=meta_data['name'],author_name=meta_data['default_author'])
    
        
    # write the parsed template
    with open("index.html", "w") as chap_page:
        chap_page.write(output_from_parsed_template)