import requests
import os.path


access_token_file_name = 'access_token.json'
app_id = 'ee09784d03bfa29d76f1e1e25d5cca0ee20c33f6bbcbf3c40a256df2ec0c93ec'
app_secret = '13d2d23f8907f5557dec9b92a4ee78ad757bfc4b324a47101caf68d1e54f00b5'
call_back = 'urn:ietf:wg:oauth:2.0:oob'
authorization_code = ""

def get_authorization_code():
    import webbrowser
    print('Need to get authorization_code')
    url = "https://tower.im/oauth/authorize?client_id=%s&redirect_uri=%s&response_type=code" % (app_id, call_back)
    webbrowser.open_new(url)
    code = input("pls input authorization code: ")
    return code


def get_access_token(app_id,app_secret,authorization_code,call_back):
    url = "https://tower.im/oauth/token"
    response = requests.post(url,
            data = {
                'client_id':app_id,
                'client_secret':app_secret,
                'code':authorization_code,
                'grant_type':'authorization_code',
                'redirect_uri':call_back
                })
    return response.text


if os.path.exists(access_token_file_name):
    print("get existed access code")
else:
    authorization_code = get_authorization_code()
    text = get_access_token(app_id,app_secret,authorization_code,call_back)
    fo = open(access_token_file_name, "w")
    fo.write( text )
    fo.close()




