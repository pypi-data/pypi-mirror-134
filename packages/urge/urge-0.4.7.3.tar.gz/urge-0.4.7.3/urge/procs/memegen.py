import httpx
import typing as t

url = "https://api.memegen.link/images/"


meme_list = [
    'aag',
    'ackbar',
    'afraid',
    'agnes',
    'aint-got-time',
    'ams',
    'ants',
    'apcr',
    'atis',
    'away',
    'awesome',
    'awesome-awkward',
    'awkward',
    'awkward-awesome',
    'bad',
    'badchoice',
    'bd',
    'bender',
    'bihw',
    'biw',
    'blb',
    'boat',
    'both',
    'bs',
    'buzz',
    'captain',
    'captain-america',
    'cb',
    'cbg',
    'center',
    'ch',
    'cheems',
    'chosen',
    'cmm',
    'crazypills',
    'cryingfloor',
    'db',
    'dg',
    'disastergirl',
    'dodgson',
    'doge',
    'dragon',
    'drake',
    'ds',
    'dsm',
    'dwight',
    'elf',
    'ermg',
    'fa',
    'facepalm',
    'fbf',
    'feelsgood',
    'fetch',
    'fine',
    'firsttry',
    'fmr',
    'fry',
    'fwp',
    'gandalf',
    'gb',
    'gears',
    'ggg',
    'gru',
    'grumpycat',
    'hagrid',
    'happening',
    'harold',
    'hipster',
    'home',
    'icanhas',
    'imsorry',
    'inigo',
    'interesting',
    'ive',
    'iw',
    'jd',
    'jetpack',
    'joker',
    'jw',
    'keanu',
    'kermit',
    'kk',
    'kombucha',
    'leo',
    'live',
    'll',
    'lrv',
    'mb',
    'michael-scott',
    'millers',
    'mini-keanu',
    'mmm',
    'money',
    'mordor',
    'morpheus',
    'mouth',
    'mw',
    'nice',
    'noidea',
    'ntot',
    'oag',
    'officespace',
    'older',
    'oprah',
    'patrick',
    'persian',
    'philosoraptor',
    'pigeon',
    'ptj',
    'puffin',
    'red',
    'regret',
    'remembers',
    'reveal',
    'right',
    'rollsafe',
    'sad-biden',
    'sad-boehner',
    'sad-bush',
    'sad-clinton',
    'sad-obama',
    'sadfrog',
    'saltbae',
    'same',
    'sarcasticbear',
    'sb',
    'scc',
    'sf',
    'sk',
    'ski',
    'snek',
    'soa',
    'sohappy',
    'sohot',
    'soup-nazi',
    'sparta',
    'spiderman',
    'spongebob',
    'ss',
    'stew',
    'stonks',
    'stop-it',
    'success',
    'tenguy',
    'toohigh',
    'tried',
    'trump',
    'ugandanknuck',
    'whatyear',
    'winter',
    'wkh',
    'wonka',
    'worst',
    'xy',
    'yallgot',
    'yodawg',
    'yuno',
    'zero-wing',
]


def get_meme(name: str, down: str, up: t.Optional[str] = None, target: str = "./"):

    if name not in meme_list:
        raise Exception(f"Sorry we don't have meme pic named {name} yet.")

    base = url + name
    full: str
    caps = []
    for w in [up, down]:
        if not w:
            continue
        _ = (
            # / -> ~s not succeed
            w.replace(" ", "_")
            .replace("?", "~q")
            .replace("&", "~h")
            .replace("#", "~a")
            .replace('"', "''")
            .replace("%", "~p")
            .replace("-", "--")
            .replace("<", "~l")
            .replace(">", "~g")
            .replace("\\", "~b")
        )
        caps.append(_)

    if len(caps) == 2:
        up, down = caps
        full = f"{base}/{up}/{down}.jpg"
    elif len(caps) == 1:
        down = caps[0]
        full = f"{base}/_/{down}.jpg"
    else:
        raise Exception("One meme goes with two lines: Up and Down")

    with httpx.stream("GET", full) as r:
        full_name = f"{target}{name}.jpg"
        with open(full_name, 'wb+') as f:
            for chunk in r.iter_bytes():
                f.write(chunk)

        return full_name
        
# from PIL import Image, ImageDraw, ImageFont
# import typing as t
# import os

# def get_meme(name: str, down: str, up: t.Optional[str] = None, target: str = "./"):
#     FONT_PATH = "./NotoSansTC-Bold.otf"
#     # 打开图片
#     img = Image.open(name)

#     # 调整大小
#     width, height = img.size
#     if not(150 <= width <= 1000 and 150 <= height <= 1000):
#         img.resize((500, 300),Image.ANTIALIAS)

#     # 设置文字
#     if up is None:
#         up = ""
#     font = ImageFont.truetype(font=FONT_PATH, size=50)
#     w_down, _ = font.getsize(down)
#     w_up, _ = font.getsize(up)
#     if w_down > width or w_up > width:
#         raise ValueError("The string you entered is too long, please make it shorter.")
    
#     # 添加文字
#     draw = ImageDraw.Draw(img)
#     draw.text(xy=((width - w_up) / 2, 10), text=up, fill=(255, 255, 255), font=font)
#     draw.text(xy=((width - w_down) / 2, height - 80), text=down, fill=(255, 255, 255), font=font)

#     # 保存
#     real_name, ext = os.path.splitext(name)
#     full_name = f"{target}{real_name}_new{ext}"
#     img.save(f"{target}{real_name}_new{ext}")

#     return full_name

if __name__ == "__main__":
    up = "wow "
    # % - ' < > \\   /
    down = "-"
    get_meme("tried",up,down)
