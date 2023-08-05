#django direct render


render a simple html without wirting view function. 


## INSTALLATION

    pip install django_direct_render

### INSTALLED_APP

in INSTALLED_APP, add the following entry


    'direct_render'


### project urls.py 

add the folowing line at top
	
	import direct_render.urls

add the following url configuration in your urls.py

    url(r'^direct_render/', include(direct_render.urls)), 
    
the abover the regular expression can change with your desire

### Usage

* put xxx.html in templates. 
* browse file directly from 'direct_render/xxx.html'
	
