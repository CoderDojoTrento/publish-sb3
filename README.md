
# Sb3 to TurboWarp

Given a folder like `projects/`, creates an index.html page with links to scratch .sb3 projects hosted on a custom server other than official scratch site. Can be useful if you don't want students to create accounts on Scratch

Links will open in [turbowarp.org](https://turbowarp.org) scratch fork, as original scratch can't open links from URL. Turbowarp doesn't require nor allows creating accounts.


## Demo (English):

https://coderdojotrento.github.io/sb3-to-turbowarp/demo


## Demo (Italian):

https://coderdojotrento.github.io/sb3-to-turbowarp/demo-it

## Usage

Reads all projects in root folder `demo` and creates `demo/index.html`, supposing the file will be hosted on `https://coderdojotrento.github.io/sb3-to-turbowarp/demo`

```bash
python3 sb3_to_turbowarp.py -r demo  -s https://coderdojotrento.github.io/sb3-to-turbowarp/demo/ 
```


## Deployment

All needed js and css files are packaged in a single `index.html` file for deployment convenience.


## Requirements

Python version: >= 3.6

See [requirements.txt](requirements.txt)



## Credits:

David Leoni  info@davidleoni.it

CoderDojo Trento  coderdojotrento.it


**Libraries:**

- JSLists

**Graphics:**

-  file.svg from [svgrepo](https://www.svgrepo.com/svg/6994/file)      (CC0 License)
-  folder.svg from [svgrepo](https://www.svgrepo.com/svg/22198/folder)   (CC0 License)

