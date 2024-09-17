
# Publish sb3 

If you have Scratch .sb3 projects hosted on a custom server and want to publish them outside official Scratch website, this python script creates a single `index.html` page with browsable folders and links to easily run projects, view their code and download sb3 files.

Since original Scratch can't open links from URL, links will open in [turbowarp.org](https://turbowarp.org) scratch fork. 

This tool can be useful if you don't want students to create accounts on Scratch, note also Turbowarp doesn't require (nor allows) creating accounts.


## Demo (English):

https://coderdojotrento.github.io/publish-sb3/demo


## Demo (Italian):

https://coderdojotrento.github.io/publish-sb3/demo-it

## Example usage

Reads all projects in root folder `demo` and creates `demo/index.html`, supposing the file will be hosted on `https://coderdojotrento.github.io/publish-sb3/demo/` (REMEMBER trailing slash)

```bash
python3 publish_sb3.py -r demo  -s https://coderdojotrento.github.io/publish-sb3/demo/ 
```

## Deployment

All needed js and css files are packaged in a single `index.html` file for deployment convenience.

## Requirements

- Python version: >= 3.6
- Pyhton dependencies: see [requirements.txt](requirements.txt)
- Javascript dependencies (already included): JSLists
- **Hosting server needs to allow [CORS calls](https://docs.turbowarp.org/url-parameters#project_url)**


## Credits:

David Leoni  info@davidleoni.it

CoderDojo Trento  coderdojotrento.it


**Graphics:**

-  file.svg from [svgrepo](https://www.svgrepo.com/svg/6994/file)      (CC0 License)
-  folder.svg from [svgrepo](https://www.svgrepo.com/svg/22198/folder)   (CC0 License)

