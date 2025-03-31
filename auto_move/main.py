#!/usr/bin/python3
#coding:utf-8
import os
import re
import sys
import shutil
from time import sleep, strftime, localtime, time


LOGS = []
LOG_PATH = f"{os.path.dirname(os.path.abspath(__file__))}/auto_anime_move.log"


def logger(message):
    message = f'[{strftime("%Y-%m-%d %H:%M:%S",localtime(time()))}] {message}'
    return message


def get_season(save_path, video):
    prefix = f"{video}.S"
    pattern = prefix + r"\d{2}"
    files = os.listdir(save_path)
    seasons = [1]
    for file in files:
        match = re.search(pattern, file)
        if match:
            seasons.append(int(match.group().replace(prefix, '')))

    season = str(max(seasons))
    return season.zfill(2)


def get_episode(save_path, video, season):
    prefix = f"{video}.S{season}E"
    pattern = prefix + r"\d{2}"
    files = os.listdir(save_path)
    episodes = [0]
    for file in files:
        match = re.search(pattern, file)
        if match:
            episodes.append(int(match.group().replace(prefix, '')))

    episode = str(max(episodes) + 1)
    return episode.zfill(2)


def main(save_path, file_name, debug=False):
    if debug or save_path.startswith('/share/Video/Anime'):
        video = save_path.split('/')[-1]
        LOGS.append(logger(f"INFO: 获得{video=}"))

        season = get_season(save_path, video)
        LOGS.append(logger(f"INFO: 获得{season=}"))

        episode = get_episode(save_path, video, season)
        LOGS.append(logger(f"INFO: 获得{episode=}"))

        file_type = file_name.split('.')[-1]
        LOGS.append(logger(f"INFO: 获得{file_type=}"))

        new_name = f"{video}.S{season}E{episode}.{file_type}"
        if not debug:
            sleep(2)
            shutil.move(f"{save_path}/{file_name}",f"{save_path}/{new_name}")
        LOGS.append(logger(f"INFO: 创建 {save_path}/{new_name} 完成...一切已经准备就绪"))


if __name__ == "__main__":
    try:
        LOGS.append(logger('INFO: Running....'))
        save_path, file_name = sys.argv[1], sys.argv[2]
        LOGS.append(logger(f"INFO: 接受到{save_path=}"))
        LOGS.append(logger(f"INFO: 接受到{file_name=}"))
        main(save_path, file_name)
    except Exception as e:
        LOGS.append(logger(f"WARNING: {e}"))
    finally:
        LOGS.append("\n")
        with open(LOG_PATH, "a+", encoding='utf-8') as f:
            f.write("\n".join(LOGS))
