import typing as t
from urge import procs

# from .base import Action, action
# from .procs import weather, youdao, browser, memegen, fileoperation
from urge.base import Action, action
from urge.procs import weather, youdao, browser, memegen, fileoperation
from dataclasses import dataclass
from path import Path


class do(Action):
    """
    Do, do my work\n
    Do my dirty work, scapegoat\n
    """

    procs = []

    def __init__(self, *args) -> None:
        assert isinstance(self.procs, list)
        for f in args:
            self.procs.append(f)


# tested ok
@dataclass
class web_screenshot(Action):
    url: str
    target: str = "./"
    use_mobile: bool = True
    full_page: bool = False
    time_out: int = 2

    procs = [browser.web_screenshot]


# tested ok
@dataclass
class get_now_temp(Action):
    city: str
    lang: str = "en"
    ascii_graphs: bool = True
    procs = [weather.get_weather, weather.ret_weather]
    # Should add something like this
    # procs = [weather.get_weather, _p(weather.ret_weather,{'ascii_graphs':True})]
    # procs = [weather.get_weather, _p(weather.ret_weather,ascii_graphs=True)]
    # The idea here is turn {"ascii_graphs":True} into self.ascii_graphs=True


# tested ok 
@dataclass
class get_simple_temp(Action):
    city: str
    ascii_graphs: bool = False
    procs = [weather.get_weather, weather.ret_weather]


# tested ok
@dataclass
class translate(Action):
    q: str
    config: t.Dict[youdao.YOUDAO_PARAM_KEY,youdao.YOUDAO_PARAM_VALUE] = None
    full: bool = False
    procs = [youdao.trans_post, youdao.trans_filter]


# tested ok
@dataclass
class simple_translate(Action):
    q: str
    procs = [youdao.simple_translate]


# tested ok
@dataclass
class easy_ocr(Action):
    path: str
    procs = [youdao.pic2base64, youdao.ocr_post, youdao.ocr_ret]


# tested ok
@dataclass
class pic_translate(Action):
    path: str
    procs = [youdao.pic2base64, youdao.pictrans_post, youdao.pictrans_write]


# tested ok
@dataclass
class handwrite_ocr(Action):
    path: str
    procs = [youdao.pic2base64, youdao.ocr_post, youdao.ocr_ret]


# tested ok
@dataclass
class receipt_ocr(Action):
    path: str
    procs = [youdao.pic2base64, youdao.receipt_ocr_post, youdao.receipt_ocr_ret]


# tested ok
@dataclass
class table_ocr(Action):
    path: str
    procs = [youdao.pic2base64, youdao.table_ocr_post, youdao.table_write_excel]


# tested ok
@dataclass
class meme_gen(Action):
    name: str
    up: t.Optional[str]
    down: str
    procs = [memegen.get_meme]


# tested ok
@dataclass
class list_all(Action):
    path: str
    procs = [fileoperation.list_all]


# tested ok
@dataclass
class create(Action):
    path: str
    procs = [fileoperation.create]


# tested ok
@dataclass
class create_folder(Action):
    path: str
    procs = [fileoperation.create_folder]


# tested ok
class find:
    def __init__(self, path: t.Text, pattern: t.Text, recursive=False) -> None:
        self.handler = fileoperation.walk if recursive else fileoperation.find
        self._list = self.handler(path=path, pattern=pattern)
        if isinstance(self._list, t.Generator):
            self._list = list(self._list)
            # when self.__dict__ deepcopy it goes nuts
            # Maybe I can do self.pipe(seed) without deepcopy...
            # Already did that
    
    # tested ok
    @action([fileoperation._delete_all])
    def delete(self):
        return dict(f_list=self._list)
    

    # tested 
    # fixed ok
    @action([fileoperation._rename_all])
    def rename(self, with_suffix: str = None, with_prefix: str = None):
        return locals()

    # tested ok
    @action([fileoperation._zip_files])
    def zip(self, with_folder=False):
        return dict(f_list=self._list, with_folder=with_folder)

    @action([fileoperation])
    def unzip(self):
        ...

        
    # tested ok
    @action([fileoperation._move_all])
    def move(self, dst: str):
        return dict(f_list=self._list, dst=dst)
