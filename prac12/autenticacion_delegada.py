from bottle import run, get,request
import  urllib

import json
import os,binascii
# Credenciales. 
# https://developers.google.com/identity/protocols/OpenIDConnect#appsetup
# Copiar los valores adecuados.
CLIENT_ID     = "995083380325-asserdnmin1hgvafl574qvag8sd82qaq.apps.googleusercontent.com"
CLIENT_SECRET = "tepb9QzLDk7JglwcWvhP-yz1"
REDIRECT_URI  = "http://localhost:8080/token"

# Fichero de descubrimiento para obtener el 'authorization endpoint' y el 
# 'token endpoint'
# https://developers.google.com/identity/protocols/OpenIDConnect#authenticatingtheuser
DISCOVERY_DOC = "https://accounts.google.com/.well-known/openid-configuration"


# Token validation endpoint para decodificar JWT
# https://developers.google.com/identity/protocols/OpenIDConnect#validatinganidtoken
TOKEN_VALIDATION_ENDPOINT = "https://www.googleapis.com/oauth2/v3/tokeninfo"


@get('/login_google')
def login_google():
   
    state= os.urandom(16)
    state = "security_token"+ binascii.hexlify(state) +REDIRECT_URI 
    
  
    
    pagina= "https://accounts.google.com/o/oauth2/v2/auth?client_id="+ CLIENT_ID + "&response_type=code&scope=openid%20email&redirect_uri=http://localhost:8080/token&state=" + state
    return "<a href=" + pagina + ">Continuar</a>"


@get('/token')
def token():
   codigo= request.GET.get('code')
   state=request.GET.get('state')
   
  # if state<>  session['state'] :
     #  return "<p>Ha habido un error en la autoticacion</p>"
  # else:
   campos = urllib.urlencode({"code":codigo,"client_id": CLIENT_ID ,"client_secret":CLIENT_SECRET,"redirect_uri":REDIRECT_URI,"grant_type":"authorization_code"})
   sitio = urllib.urlopen("https://www.googleapis.com/oauth2/v4/token", campos)
   texto= sitio.read()
   a = json.loads(texto)
   
  
   id_token= a['id_token']
   json1=urllib.urlopen("https://www.googleapis.com/oauth2/v3/tokeninfo?id_token="+id_token)   
   data = json.loads(json1.read())
   return "<p>bienvenido " + data['email']+"</p>"
   
  
   

        
  


if __name__ == "__main__":
    run(host='localhost',port=8080,debug=True)
