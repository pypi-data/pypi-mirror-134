import os
import pickle
from socket import *

import logging
logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(levelname)s: [%(name)s] %(message)s')
ch = logging.StreamHandler()
ch.setFormatter(formatter)
logger.addHandler(ch)
logger.setLevel(logging.ERROR)

DEF_SERVER_ADDR = '192.168.0.174'

# 서버측에서 설정할 포트와 버퍼크기임.
UDP_PORT = 21567
TCP_PORT = 21568
UDP_BUFSIZ = 65507
TCP_BUFSIZ = 1024

FILENAME = 'setting.pickle'
FULL_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), FILENAME)


class ServerSetting:
    def __init__(self):
        self.addr = DEF_SERVER_ADDR
        self._active_port = 'UDP'

    @property
    def active_port(self):
        return self._active_port

    @active_port.setter
    def active_port(self, port_type: str):
        if port_type in ['TCP', 'UDP']:
            self._active_port = port_type
        else:
            raise ValueError(f'Invalid port type: {port_type}')

    def __str__(self):
        return (f"Cybos server addr : {self.addr} / "
                f"{self.active_port} : {UDP_PORT if self.active_port == 'UDP' else TCP_PORT}")


def load() -> ServerSetting:
    try:
        with open(FULL_PATH, "rb") as fr:
            s = pickle.load(fr)
            logger.info(s)
            return s
    except (EOFError, FileNotFoundError) as e:
        logger.error(e)
        set_default()
        # 새로 만든 파일을 다시 불러온다.
        with open(FULL_PATH, "rb") as fr:
            s = pickle.load(fr)
            logger.info(s)
            return s


def chg_addr(addr: str):
    s = load()
    before = s.addr
    s.addr = addr
    if before != addr:
        print(f'Change cybos addr : {before} -> {addr}')
    with open(FULL_PATH, "wb") as fw:
        pickle.dump(s, fw)


def _switch_port_type(port_type: str):
    s = load()
    before = s.active_port
    s.active_port = port_type
    if before != port_type:
        print(f'Change port setting : {before} -> {port_type}')
    with open(FULL_PATH, "wb") as fw:
        pickle.dump(s, fw)


def set_tcp():
    _switch_port_type(port_type='TCP')


def set_udp():
    _switch_port_type(port_type='UDP')


def set_default():
    with open(FULL_PATH, "wb") as fw:
        pickle.dump(ServerSetting(), fw)


def is_srv_live() -> bool:
    s = load()
    if s.active_port == 'UDP':
        port = UDP_PORT
        try:
            sock = socket(AF_INET, SOCK_DGRAM)
            # udp는 포트 연결을 보장하지 않기 때문에 timeout으로 연결을 간접적으로 확인한다.
            sock.settimeout(1)
            try:
                from .data import CMD, AccountData
                sock.sendto(CMD.ACCOUNT.name.encode(), (s.addr, port))
                raw_data, addr = sock.recvfrom(UDP_BUFSIZ)
                result = 0
            except timeout:
                result = 1
        finally:
            sock.close()
    elif s.active_port == 'TCP':
        port = TCP_PORT
        try:
            sock = socket(AF_INET, SOCK_STREAM)
            result = sock.connect_ex((s.addr, port))
        finally:
            sock.close()
    else:
        raise
    print(f'server test : {s.addr} / {port}', end='')
    if result == 0:
        print(' : alive')
        return True
    else:
        print(' : dead')
        return False
