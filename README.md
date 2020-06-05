<div align='center'>
    <img src="https://cdn.discordapp.com/attachments/685553321901293605/718140139632853083/e5982ce2900da24da3e4ac7c7fafc117.jpg" alt="Logo" width="100" height="100">
    <h1>Stranger Bot for Discord</h1>
    <h6>This bot is closely linked with Russian <a href='pixelstarships.com/'>Pixel Starships</a> Community</h6>
    <h6><a href='https://discord.gg/A4NETzF'>Join our Discord Server (🇷🇺)</a></h6>
</div>

___

![Python Version](https://img.shields.io/badge/python_>%3D-3.6-green) ![PyPi](https://warehouse-camo.ingress.cmh1.psfhosted.org/cd7ef4975d71b4a87a35b3c01b5b1ec8481c4549/68747470733a2f2f696d672e736869656c64732e696f2f707970692f762f7069702e737667)
![discord-py](https://img.shields.io/badge/discord.py-1.3.1-blue)     ![discord](https://img.shields.io/badge/discord-1.0.1-blue)
![License](https://img.shields.io/badge/license-MIT-green)

* ### Features
    * __Fleet Dogmas__ - type `asdogma motto` to see an example. Can cointan images.
    * __Dogmas setting__ - type `asset <name> <image link (optional)> <text (optional)>` to set your own dogma.
    * __Dogmas list__ - type `aslist` and click on the reaction to see the list of all dogmas.
    * __Mention messages__ - type `astag <@mention> <text>` and try to mention the user.
    * __Voice__ - when bot is connected to discord it also connects to `utils.variables.SAY_CHANNEL`(id). When other user joins the channel, there is random meme sound, after bot kicks the user. Requires `PyNaCl` and `ffmpeg`
    * __Ensign role giving__ - type `asbird <@mention>` to give him `utils.variables.ENSIGN` role and take out `utils.variables.GUEST` role.
    * __Taking out ensign role__ - type `asguest` (gives guest role and takes out ensign one).
    * __Databases recovering__ - bot team' command `asrecover` recovers the databases of dogmas and mention messages if bot is hosted at heroku and does not support dbs.
    * __Coronavirus statistics__ - type `asinfo <county (optional)>` to see.
    * __Pixel Starships Kickstarter__ - type `askickstart(er)` to see PSS Second Kickstarter Company statictics
* ### Running
    __(You can simply [invite](https://discord.com/api/oauth2/authorize?client_id=670692900593598530&permissions=288738624&scope=bot) the bot and acess dogmas and mention messages (it requests only those permissions it uses.)__
    1. __Paste your tokens (up to 3) into the `TOKENS.txt` file.__
    1. __Open `utils\variables.py` and set values for all options named in CAPITAL LETTERS. You can set advanturer's id to `None` if you would.__
    1. __By default, `main.py` runs bot with first token. The variable is called `tokens.ASTRANGER`. You can change it to `tokens.BSTRANGER` (second token) or `tokens.CSTRANGER` (third token)__
    __Run `main.py`.__
* ### License
    __A Stranger is licensed under the [MIT License](https://github.com/TheAmmiR/stranger-bot/blob/master/LICENSE).__