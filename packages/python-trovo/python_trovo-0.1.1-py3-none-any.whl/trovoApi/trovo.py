import json
import requests
from logging import Logger, getLogger
from typing import List, Optional

from trovoApi.types import RequestParametersException


TROVO_API_URL = "https://open-api.trovo.live/openplatform"
TROVO_CATEGORIES_MAX_LIMIT = 100
TROVO_OBJECTS_MAX_LIMIT = 100
TROVO_VIEWERS_MIN_LIMIT = 20
TROVO_VIEWERS_MAX_LIMIT = 10000
TROVO_FOLLOWERS_MAX_LIMIT = 100


class TrovoClient:
    client_id: str = None

    __logger: Logger = None

    def __init__(self,
                 client_id):
        self.client_id = client_id
        self.__logger = getLogger('trovoApi.trovo')

    '''
      MAIN APIs
    '''
    def get_all_game_categories(self) -> dict:
        url = self.__generate_url("categorys/top")
        response = self.__perform_get_request(url)
        return response.json()

    def get_game_categories(self,
                            query: str,
                            limit: Optional[int] = None) -> dict:
        params = {"query": query}
        if limit:
            if limit > TROVO_CATEGORIES_MAX_LIMIT:
                raise ValueError(" ".join(["Limit cannot be higher than",
                                           str(TROVO_CATEGORIES_MAX_LIMIT)]))
            params["limit"] = limit
        url = self.__generate_url("searchcategory")
        response = self.__perform_post_request(url, params)
        return response.json()

    def get_top_channels(self,
                         limit: Optional[int] = None,
                         after: Optional[bool] = None,
                         token: Optional[str] = None,
                         cursor: Optional[int] = None,
                         category_id: Optional[str] = None) -> dict:
        params = {}
        if limit:
            if limit > TROVO_OBJECTS_MAX_LIMIT:
                raise ValueError(" ".join(["Limit cannot be higher than",
                                           str(TROVO_OBJECTS_MAX_LIMIT)]))
            params["limit"] = limit
        if after:
            params["after"] = after
        if token:
            params["token"] = token
        if cursor:
            params["cursor"] = cursor
        if category_id:
            params["category_id"] = category_id
        url = self.__generate_url("gettopchannels")
        response = self.__perform_post_request(url, params)
        return response.json()

    def get_users(self,
                  users: List[str] = []) -> dict:
        params = {"user": users}
        url = self.__generate_url("getusers")
        response = self.__perform_post_request(url, params)
        return response.json()

    def get_channel_info_by_id(self,
                               channel_id: Optional[str] = None,
                               username: Optional[str] = None) -> dict:
        if not (channel_id or username):
            raise RequestParametersException(("Neither channel_id nor username"
                                              " were provided."))
        elif channel_id and username:
            self.__logger.warn(("Both channel_id and username are provided. "
                                "The API will prioritize the channel_id."))
        params = {}
        if channel_id:
            params["channel_id"] = channel_id
        if username:
            params["username"] = username
        url = self.__generate_url("channels/id")
        response = self.__perform_post_request(url, params)
        return response.json()

    def get_emotes(self,
                   emote_type: int,
                   channel_id: List[int]) -> dict:
        params = {"emote_type": emote_type, "channel_id": channel_id}
        url = self.__generate_url("getemotes")
        response = self.__perform_post_request(url, params)
        return response.json()

    def get_channel_viewers(self,
                            channel_id: int,
                            limit: Optional[int] = None,
                            cursor: Optional[int] = None) -> dict:
        params = {}
        if limit:
            if limit not in range(TROVO_VIEWERS_MIN_LIMIT,
                                  TROVO_VIEWERS_MAX_LIMIT+1):
                raise ValueError("".join(["Limit must be on range(",
                                          str(TROVO_VIEWERS_MIN_LIMIT),
                                          ", ",
                                          str(TROVO_VIEWERS_MAX_LIMIT),
                                          ")"]))
            params["limit"] = limit
        if cursor:
            params["cursor"] = cursor
        url = self.__generate_url("/".join(["channels", str(channel_id),
                                            "viewers"]))
        response = self.__perform_post_request(url, params)
        return response.json()

    def get_channel_followers(self,
                              channel_id: int,
                              limit: Optional[int] = None,
                              cursor: Optional[int] = None,
                              descending: Optional[bool] = False) -> dict:
        params = {}
        if limit:
            if limit > TROVO_FOLLOWERS_MAX_LIMIT:
                raise ValueError(" ".join(["Limit cannot be higher than",
                                           str(TROVO_FOLLOWERS_MAX_LIMIT)]))
            params["limit"] = limit
        if cursor:
            params["cursor"] = cursor
        if descending:
            params["direction"] = "desc"
        url = self.__generate_url("/".join(["channels", str(channel_id),
                                            "followers"]))
        response = self.__perform_post_request(url, params)
        return response.json()

    def get_livestream_urls(self,
                            channel_id: int) -> dict:
        params = {"channel_id": channel_id}
        url = self.__generate_url("livestreamurl")
        response = self.__perform_post_request(url, params)
        return response.json()

    def get_clips_info(self,
                       channel_id: int,
                       category_id: Optional[str] = None,
                       period: Optional[str] = None,
                       clip_id: Optional[str] = None,
                       limit: Optional[int] = None,
                       cursor: Optional[int] = None,
                       descending: Optional[bool] = False) -> dict:
        params = {"channel_id": channel_id}
        if category_id:
            params["category_id"] = category_id
        if period:
            if period not in ["day", "week", "month", "all"]:
                raise ValueError("Period is not day, week, month or all")
            params["period"] = period
        if clip_id:
            params["clip_id"] = clip_id
        if limit:
            if limit > TROVO_OBJECTS_MAX_LIMIT:
                raise ValueError(" ".join(["Limit cannot be higher than",
                                           str(TROVO_OBJECTS_MAX_LIMIT)]))
            params["limit"] = limit
        if cursor:
            params["cursor"] = cursor
        if descending:
            params["direction"] = "desc"
        url = self.__generate_url("clips")
        response = self.__perform_post_request(url, params)
        return response.json()

    def get_past_streams_info(self,
                              channel_id: int,
                              category_id: Optional[str] = None,
                              period: Optional[str] = None,
                              past_stream_id: Optional[str] = None,
                              limit: Optional[int] = None,
                              cursor: Optional[int] = None,
                              descending: Optional[bool] = False) -> dict:
        params = {"channel_id": channel_id}
        if category_id:
            params["category_id"] = category_id
        if period:
            if period not in ["day", "week", "month", "all"]:
                raise ValueError("Period is not day, week, month or all")
            params["period"] = period
        if past_stream_id:
            params["past_stream_id"] = past_stream_id
        if limit:
            if limit > TROVO_OBJECTS_MAX_LIMIT:
                raise ValueError(" ".join(["Limit cannot be higher than",
                                           str(TROVO_OBJECTS_MAX_LIMIT)]))
            params["limit"] = limit
        if cursor:
            params["cursor"] = cursor
        if descending:
            params["direction"] = "desc"
        url = self.__generate_url("paststreams")
        response = self.__perform_post_request(url, params)
        return response.json()

    '''
    Local methods
    '''
    def __perform_get_request(self, url):
        headers = self.__generate_headers()
        resp = requests.get(url, headers=headers)
        return resp

    def __perform_post_request(self, url, params: dict = None):
        headers = self.__generate_headers()
        self.__logger.debug("".join(["Contacting url: ", url]))
        if params:
            payload = self.__generate_payload(params)
            self.__logger.debug("".join(["Using as parameters: ", payload]))
            resp = requests.post(url, data=payload, headers=headers)
        else:
            resp = requests.post(url, headers=headers)
        return resp

    def __generate_headers(self):
        return {"Accept": "application/json", "Client-ID": self.client_id}

    def __generate_payload(self, payload: dict):
        return json.dumps(payload)

    def __generate_url(self, endpoint: str):
        return "/".join([TROVO_API_URL, endpoint])
