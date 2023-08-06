import typer
import os,shutil
import pickle
app = typer.Typer()
from postbook.get_list_of_files import get_files
from postbook.write_html import write_html
from postbook.send_files import send_files
from postbook.update_index import update_index
from postbook.setting_the_host import host_setup
from datetime import datetime
from jinja2 import Template, Environment, FileSystemLoader
from postbook.PageChapter import PageChapter
import re

@app.command()
def hello(name: str):
    typer.echo(f"Hello {name}")


@app.command()
def goodbye(name: str, formal: bool = False):
    if formal:
        typer.echo(f"Goodbye Ms. {name}. Have a good day.")
    else:
        typer.echo(f"Bye {name}!")

@app.command()
def start(name: str):
    current_directory = os.getcwd()
    
    


    final_directory = os.path.join(current_directory, r'{}'.format(name))
    final_directory_with_posts = os.path.join(final_directory, r'posts')
    if not os.path.exists(final_directory):
        os.makedirs(final_directory)
        os.makedirs(final_directory_with_posts)
    
    email = typer.prompt("What's your email ?")
    ip_address = typer.prompt("Whats'your host ip ?")
    username = typer.prompt("What's your host username ?")
    password = typer.prompt("What's your host password ?")
    domain_flag = typer.prompt("Do you have a domain name ? (y/n)")

    domain = None
    if(domain_flag=='y' or domain_flag=='Y'):
        domain = typer.prompt("What's your domain address ? ")
    default_author = typer.prompt("Default Authors Name ?")
    with open(f"{final_directory}/.plog","wb") as f:
        pickle.dump({'name':name,'email':email,'ip_address':ip_address,'username':username,'password':password,'domain':domain,'default_author':default_author},f)

    
@app.command()
def getfiles():
    current_directory = os.getcwd()
    html_files = [x for x in get_files(current_directory+'/posts/') if '.html' in x ]
    return html_files


    
    final_directory = os.path.join(current_directory, r'{}'.format(meta_data['name']))
    #send_files(path_to_file,)




@app.command()
def publish(path_to_file:str):
    post_title = re.search('([a-zA-Z0-9_]*).ipynb',path_to_file).group(1).replace('_',' ')
   
    current_directory = os.getcwd()
    published_on = datetime.now().strftime("%d-%B-%Y (%I:%M %p)")
   
    with open(f"{current_directory}/.plog","rb") as f:
        meta_data = pickle.load(f)
    with open(f"{current_directory}/.plog","wb") as f: 
        meta_data[post_title]={'published_on':published_on}   
        pickle.dump(meta_data,f)
    
    html_file_location = write_html(path_to_file,post_title)
    published_on = datetime.now().strftime("%d-%B-%Y (%I:%M %p)")
    
    
    send_files(html_file_location,'/root/blog/{}.html'.format(post_title.replace(' ','_')))
    
    update_index()
    send_files('index.html','/root/blog/index.html')

@app.command()
def html(path_to_file:str):
    print("hello html file generation")
    post_title = re.search('([a-zA-Z0-9_]*).ipynb',path_to_file).group(1).replace('_',' ')
   
    current_directory = os.getcwd()
    published_on = datetime.now().strftime("%d-%B-%Y (%I:%M %p)")
   
    with open(f"{current_directory}/.plog","rb") as f:
        meta_data = pickle.load(f)
    with open(f"{current_directory}/.plog","wb") as f: 
        meta_data[post_title]={'published_on':published_on}   
        pickle.dump(meta_data,f)
    
    html_file_location = write_html(path_to_file,post_title)
    published_on = datetime.now().strftime("%d-%B-%Y (%I:%M %p)")
    
    
    # send_files(html_file_location,'/root/blog/{}.html'.format(post_title.replace(' ','_')))
    
    # update_index()
    # send_files('index.html','/root/blog/index.html')
@app.command()
def index(index_name):
    current_directory = os.getcwd()
    final_directory = os.path.join(current_directory, r'{}'.format(index_name))
    final_directory_with_posts = os.path.join(final_directory, r'posts')
    if not os.path.exists(final_directory):
        os.makedirs(final_directory)
        os.makedirs(final_directory_with_posts)
        file_path_list = os.path.realpath(__file__).split('/')[:-1]

    # the below code if for rendering the data to create the index file for the page.
    posts = [PageChapter(index_name,x) for x in get_files(current_directory+f'/{index_name}'+'/posts/')]
    with open(f"{current_directory}/.plog","rb") as f:
        meta_data = pickle.load(f)
    file_path = '/'.join(file_path_list)
    template_location  = file_path+'/templates/'
    env = Environment(loader=FileSystemLoader(template_location))
    index_template = env.get_template('index.j2')
    output_from_parsed_template = index_template.render(posts=posts, blog_name=meta_data['name'],author_name=meta_data['default_author'])
   
    # write the parsed template
    with open(f"{final_directory}/"+"index.html", "w") as chap_page:
        chap_page.write(output_from_parsed_template)

@app.command()
def setup():
    current_directory = os.getcwd()
    with open(f"{current_directory}/.plog","rb") as f:
        meta_data = pickle.load(f)
    host_setup(meta_data['ip_address'],meta_data['username'],meta_data['password'])

@app.command()
def notebooks(nb_path):
    onlyfiles = [f for f in os.listdir(nb_path) if os.path.isfile(os.path.join(nb_path, f))]
    nb_files = [f for f in onlyfiles if re.search('\.ipynb',f)]
    for filename in os.listdir('posts'):
        file_path = os.path.join('posts', filename)
        print(file_path)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
    for nb_file in nb_files:
        publish(os.path.join(nb_path, nb_file))



app()
    
    

