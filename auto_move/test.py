#!/usr/bin/python3
#coding:utf-8
from main import main, logger, LOGS, LOG_PATH


if __name__ == '__main__':
    try:
        LOGS.append(logger('INFO: Test Running....'))
        with open('test.txt','r',encoding='utf-8') as f:
            for line in f.readlines():
                line = line.strip()
                save_path, file_name = line.split(',')
                LOGS.append(logger(f"INFO: 接受到{save_path=}"))
                LOGS.append(logger(f"INFO: 接受到{file_name=}"))
                main(save_path, file_name, True)
    except Exception as e:
        LOGS.append(logger(f"WARNING: {e}"))
    finally:
        print("\n".join(LOGS))
        LOGS.append("\n")
        with open(LOG_PATH, "a+", encoding='utf-8') as f:
            f.write("\n".join(LOGS))
