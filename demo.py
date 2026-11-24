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

This is a simple demonstration script for my module, python3-luanti. It requires the module to be in the same folder or in your site-packages directory.
THIS IS NOT MAINTAINED BY ANY LUANTI DEVELOPERS. AS THUS, IT DOES NOT REFLECT THE INTENTIONS OF THE LUANTI CREW. I DO NOT CLAIM OWNERSHIP OF LUANTI.

You can find Luanti at the following GitHub repository:
  https://www.github.com/luanti-org/luanti/
(Note that Luanti, before version 5.10.0, was called Minetest)
'''

import luanti

'''
Possible Errors:
luanti.startluanti can return the following errors:
  luanti.WorldNotFound: The specified world could not be found.
  luanti.LuantiError: An error occured with Luanti (non-zero exit code).
(Note that no error will occur if the client crashes, and luanti.startluanti is a non-blocking process).
'''

name = 'name'
password = 'password'
#luanti.luantipath = '/someplace/luanti' # Change the luanti path globally for the entire luanti module. Useful if you manually compiled luanti. This expects the binary at the end, not a directory.
print(luanti.getworlds()) # get a list of all worlds
print(luanti.getservers()) # get a list of all servers (requires internet access)
luanti.startluanti(remoteserver=True,address='vivo-medicare.tun.ply.gg',port=27788,name=name,password=password) # Join a server (the server shown is DreamPi, a server I host)
#luanti.startluanti(world='test') Join a singleplayer world
#luanti.startluanti(world='test',singleplayer=False,name=name,password=password) Locally host a server (you currently cannot change the port or specify --server)