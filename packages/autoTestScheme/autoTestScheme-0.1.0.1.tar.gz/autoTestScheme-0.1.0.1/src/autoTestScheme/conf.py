import dynaconf
from dynaconf.vendor.toml.decoder import TomlDecodeError
from .common import constant, common
from .common import logger
from .configuration.wb import webSocket
from .configuration.sql import MySql
from .configuration.request import requestBase
from rediscluster import RedisCluster
from redis import StrictRedis
from autoTestScheme.configuration import robot
import os, copy


class BaseDynaconf(dynaconf.Dynaconf):
    _session_list = {}
    _redis_list = {}
    _mysql_list = {}
    _feishu_list = {}
    _ws_list = {}

    def __getattr__(self, item: str):
        try:
            result = super().__getattr__(item)
        except TomlDecodeError as e:
            raise TypeError("toml文件格式错误，{}".format(e))
        except Exception as e:
            raise KeyError("配置文件内未定义{}".format(item))
        if item.startswith("redis"):
            return self.get_redis(item, result) if item not in self._redis_list else self._redis_list[item]
        elif item.startswith("request"):
            return self.get_session(item, result) if item not in self._session_list else self._session_list[item]
        elif item.startswith("sql"):
            return self.get_sql(item, result) if item not in self._mysql_list else self._mysql_list[item]
        elif item.startswith("feishu"):
            return self.get_feishu(item, result) if item not in self._feishu_list else self._feishu_list[item]
        elif item.startswith("ws"):
            return self.get_websocket(item, result) if item not in self._ws_list else self._ws_list[item]
        return result

    def get_redis(self, item, config):
        new_config = copy.deepcopy(config)
        is_colony = new_config.get('is_colony', True)
        if 'is_colony' in new_config:
            del new_config['is_colony']
        obj = None
        if is_colony is True:
            if 'db' in new_config:
                del new_config['db']
            obj = RedisCluster(**new_config)
        else:
            obj = StrictRedis(**new_config)
        self._redis_list[item] = obj
        return obj

    def get_session(self, item, config) -> requestBase:
        request = requestBase()
        if config.get("base_url", None) is not None:
            request.base_url = config['base_url']
            request.kwargs = config
            for i in config.get('api', []):
                request.read_api_folder(*i)
        else:
            logger.error("{} 注册request失败, 配置信息:{}".format(item, config))
        self._session_list[item] = request
        logger.info('注册{}'.format(item))
        return request

    def get_sql(self, item, config) -> requestBase:
        sql = MySql()
        sql.connect(config)
        self._mysql_list[item] = sql
        return sql

    def get_feishu(self, item, config):
        access_token = config.get('access_token')
        secret = config.get('secret', "")
        url = config.get('url', "https://open.feishu.cn/open-apis/bot/v2/hook/")
        feishu = robot.Feishu(access_token, secret, url)
        self._feishu_list[item] = feishu
        return feishu

    def get_websocket(self, item, config):
        ws = webSocket(config)
        for i in config.get('api', []):
            ws.read_api_folder(*i)
        self._ws_list = ws
        return ws


default_settings = {'test_tags': ['info'], 'test_case': 'all', 'is_debug': False, 'process_num': 1,
                    'tag_name_list': {'all': '其他'}, 'tag_env_list': {'all': 'all'}, 'is_locust': False}
settings = BaseDynaconf(envvar_prefix=False, merge_enabled=True, environments=True, load_dotenv=True,
                        env_switcher="ENV", root_path=constant.CONFIG_FOLDER, includes=['*.toml'])
if settings.exists('run'):
    settings.set('run', {})
for key, value in default_settings.items():
    if key not in settings.run:
        setattr(settings.run, key, value)
