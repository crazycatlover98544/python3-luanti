'''
Copyright (c) 2026 @crazycatlover98544

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

You may also read these terms at the following website: https://opensource.org/license/mit

My GitHub account is located at https://github.com/crazycatlover98544
My MistWarp account is located at https://mistwarp.org/users/crazycatlover98544

Please note that this code is not written by an expert.
I am not responsible if this harms your computer or deletes Luanti worlds (it should not).

This is still early in development. I will develop this more as I attempt to make a GUI for this (custom Luanti launcher).
However, do not expect this to be regularly maintained and be updated as Luanti changes things

THIS IS NOT MAINTAINED BY ANY LUANTI DEVELOPERS. AS THUS, IT DOES NOT REFLECT THE INTENTIONS OF THE LUANTI CREW. I DO NOT CLAIM OWNERSHIP OF LUANTI.

You can find Luanti at the following GitHub repository:
  https://www.github.com/luanti-org/luanti/
(Note that Luanti, before version 5.10.0, was called Minetest)
'''

import subprocess
import requests
import os

luantipath = 'luanti' # add this globally for the module so that way people can go [name].luantipath to change the luanti path globally without having to add it for every command
_luantidebug_randominput = False # Enable the debug mode where the Luanti client inputs random inputs

class WorldNotFound(Exception): # custom errors
    def __init__(self,message='World not found. This is a default message. If you wish to change it, add a string when you raise WorldNotFound (like this: WorldNotFound(str)).'): # is self even required here?
        super().__init__(message)

class LuantiError(Exception):
    def __init__(self,message='A luanti error occured. This is a default message. If you wish to change it, add a string when you raise LuantiError (like this: LuantiError(str)).'):
        super().__init__(message)

def getworlds(luanti_path=''): # I added the underscore because otherwise, an error would occur
    '''
    Returns the list of worlds from a Luanti installation
    Returns the following:
        [(True if command succeded else False),(World list if command succeded else string of what went wrong)
    '''
    if luanti_path == '': # doing luanti_path=luantipath inside the function definition does not work; here is the alternative
        luanti_path = luantipath
    
    try:
        luantiout = subprocess.run(
            [luanti_path,'--worldlist','name'],
            capture_output=True,
            text=True,
            check=False # likely does not need to be there, just in case
        )
    except FileNotFoundError: # if the luanti path is invalid
        return [False,'Luanti path not found.']
    
    if not luantiout.returncode == 0:
        return [False,luantiout.stderr] # return stderr so that way a program can process it if needed

    worldlist = []
    for item in luantiout.stdout.split('\n'):
        if not 'Available worlds:' in item.strip(): # luanti adds \t to the end of most lines
            worldlist.append(item.replace('\t',''))

    if worldlist[-1] == '': # for some reason, the for loop adds an extra '' to the end of the list; not sure if this is for everyone, so check first if it is there
        del worldlist[-1]
    
    del luantiout # free ram
    
    return [True,worldlist]

def getservers():
    try:
        response = requests.get('https://servers.luanti.org/list.json')
    except Exception as e:
        return [False,e]
    
    try:
        allservers = response.json().get('list',{}) # this is a BIG list (get list because that has all the servers)
    except MemoryError: # is this possible? (I do not know the size of allservers)
        return [False,'While attempting to convert the recieved response from "https://servers.luanti.org/list.json", this program ran out of memory.']
    
    if allservers == {}: # response failed?
        return [False,'The response failed or "https://servers.luanti.org/list.json" returned an unexpected error.']
    
    servers = []
    
    for server in allservers:
        servers.append({'name': server.get('name',''),
                            'address': server.get('address',''),
                            'port': server.get('port',0),
                            'version': server.get('version','')})
    
    return [True,servers]

def startluanti(luanti_path='',world='',singleplayer=True,name='',password='',remoteserver=False,address='',port=30000):
    if luanti_path == '': # doing luanti_path=luantipath inside the function definition does not work; here is the alternative
        luanti_path = luantipath
    
    if remoteserver:
        assembled_list = [luanti_path,'--go','--address',address,'--port',str(port),'--name',name,'--password',password]
        if _luantidebug_randominput:
            assembled_list.append('--random-input')
        subprocess.Popen(
            assembled_list,
            stdout=subprocess.DEVNULL,
            stdin=subprocess.DEVNULL,
            start_new_session = True # if this script ends, keep luanti running
        )
    else:
        if world == '':
            raise WorldNotFound('The world was not specified. Add the following keyword argument to startluanti(): world=[world] (expects a str object).')
        
        worldlist = getworlds(luanti_path=luanti_path)
        
        if worldlist[0]:
            if world in worldlist[1]:
                if singleplayer:
                    assembled_list = [luanti_path,'--go','--worldname',world]
                else:
                    assembled_list = [luanti_path,'--go','--worldname',world,'--name',name,'--password',password]
                if _luantidebug_randominput:
                    assembled_list.append('--random-input')
                subprocess.Popen(
                    assembled_list,
                    stdout=subprocess.DEVNULL,
                    stdin=subprocess.DEVNULL,
                    start_new_session = True # if this script ends, keep luanti running
                )
            else:
                raise WorldNotFound(f'The world "{world}" could not be found. Is it a correct world? Run {__name__}.getworlds() to get a list of all worlds.')
        else:
            if worldlist[1] == ['Luanti path not found.']:
                raise FileNotFoundError('Luanti path not found.')
            else:
                raise LuantiError(worldlist[1])