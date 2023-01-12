
import sys
import os, stat, types
from xml.sax.saxutils import escape 
import argparse
from bs4 import BeautifulSoup


translations = {
    'en': {
        'view-animation' : 'Visualize animation',
        'view-code' : 'Visualize code',
        'download-file' : 'Download file',
        'title' : 'Scratch Projects',
    },
    'it': {
        'view-animation' : 'Vedi animazione',
        'view-code' : 'Vedi codice',
        'download-file' : 'Scarica file',
        'title' : 'Progetti Scratch',
    },
}

def walk_tree(args, ret, top, level):   
    
    unrooted_dir = top[len(args.root)+1:]    
    space = '&emsp; ' * level    
    
    if args.root == top:
        the_id = 'id=albero'
        label = ''
    else:
        the_id = ''
        label = f'<div class="folder-img"></div> {escape(unrooted_dir)}'
    
    ret.append(f'''
               <ul {the_id}> 
                    
                    <li class="directory">{label}
                        <ul>
                ''')

    
    
    dirs = []
    files = []
        
    for name in sorted(os.listdir(top)):
        try:
            p = os.path.join(top, name)
            st = os.lstat(p)
        except os.error:
            print('Error, skipping', p)
            continue
        
        unrooted_dir = top[len(args.root)+1:]
        space = '&emsp; ' * level
        
        
        if stat.S_ISDIR(st.st_mode):
            dirs.append(name)   
        else:
            #TODO better filter
            if name.endswith('.sb3'):
                files.append(name)
    
    dirs.sort()
    files.sort()
    
    
    for name in dirs:                
        walk_tree (args, ret, os.path.join(top, name), level + 1)                        

    if len(files) > 0:
        ret.append('''
                   <li>                        
                   ''')
        ret.append('<table class="fileList">\n')
        for name in files:
            prj_url = f'{args.server_url}{os.path.join(unrooted_dir,name)}'
            ret.append(f'''
                        <tr>
                                
                                <td class="file">
                                    <div class="file-img"></div>
                                    {escape(name)}
                                </td>
                                
                                <td class="file">
                                    <a href="https://turbowarp.org/embed.html?project_url={prj_url}">
                                        {escape(translations[args.locale]['view-animation'])}
                                    </a>
                                </td>
                                <td class="file">
                                    <a href="https://turbowarp.org/editor?project_url={prj_url}">
                                    {escape(translations[args.locale]['view-code'])}</a>
                                </td>
                                <td class="file">
                                    <a href="{prj_url}">
                                        {escape(translations[args.locale]['download-file'])}
                                    </a>
                                </td>
                        </tr>''')
        ret.append('''
                            </table>
                        </li>                    
                   ''')
    ret.append('''      
                        </ul>
                    </li>
                </ul>
                ''')
    

def make_html_dirs(args):
    
    ret = []
    walk_tree(args, ret, args.root, 0)
    return ''.join(ret)

def make_html_page(args):

    preamble = f'''
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
    <html>
        <head>
            <title>{escape(args.title)}</title>
            <meta charset="utf-8">
            <link rel="stylesheet" href="js-lists.css">
            <link rel="stylesheet" href="publish-sb3.css">            
            <script src="js-lists.js"></script>            
        </head>
        <body>
        <h1>{escape(args.title)}</h1>\n'''
    
    return '\n'.join([preamble,
                      make_html_dirs(args),
                      '''                            
                            <script src="publish-sb3.js"></script>
                        </body>
                      </html>
                      '''])
                   
if __name__ == '__main__':
    

    parser = argparse.ArgumentParser(
                    prog = 'Sb3 to TurboWarp',
                    description = 'Creates an index.html page with links to scratch .sb3 projects hosted on a server other than officai scratch site. Links will open in turbowarp.org scratch clone.')

    parser.add_argument('-d', '--debug', 
                        dest='debug',
                        action='store_true')  
    
    parser.add_argument('-r', '--root', 
                        dest='root',
                        default='projects') 
    
    parser.add_argument('-s', '--server', 
                        dest='server_url',
                        default='')  

    # Overrides default title regardless of the locale
    parser.add_argument('-t', '--title', 
                        dest='title',
                        default='')
    
    # Forces a locale (currently browser locale is not considered)
    parser.add_argument('-l', '--locale',
                        dest='locale',
                        default='en')
    
    
    args = parser.parse_args()    
    
    
    if not args.title:
        args.title = translations[args.locale]['title']
        
        
    res = make_html_page(args)
    
    with open(f'{args.root}/index.html', 'w', encoding='utf8') as write_f:

        if not args.debug:
            print('packing...')

            soup = BeautifulSoup(res, "lxml")    
            links = list(soup.select("link"))
            for tag in links:
                print('Reading link', tag['href'])
                with open(tag['href'], 'r', encoding='utf8') as link_f:
                    t = link_f.read()
                    #print(t)
                    new_tag = soup.new_tag("style")
                    new_tag.string = t
                    tag.replace_with(new_tag)
            
            scripts = list(soup.select('script["src"]'))
            for tag in scripts:
                print('Reading script', tag['src'])
                with open(tag['src'], 'r', encoding='utf8') as link_f:
                    t = link_f.read()
                    #print(t)
                    new_tag = soup.new_tag("script")                    
                    new_tag.string = t
                    tag.replace_with(new_tag)
                
            processed_res = soup.prettify('utf8').decode()
            
        else:
            processed_res = res
         
        write_f.write(processed_res)
        print(f'Wrote {write_f.name}')
