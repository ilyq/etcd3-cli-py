import asyncio
import logging
from typing import Dict, Union, Tuple

import grpc
import click

from rpc_pb2 import PutRequest, RangeRequest, DeleteRangeRequest
from rpc_pb2_grpc import KVStub

logging.basicConfig(level=logging.INFO,
                    format="%(levelname)s:%(name)s:%(lineno)s:%(message)s")
# logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)


class Etcd:

    def __init__(self, stub: KVStub) -> None:
        self.stub = stub

    async def put(self, key: bytes, value: bytes):
        response = await self.stub.Put(PutRequest(
            key=key,
            value=value
        ))
        # logger.info(response)
        logger.info('ok')
        return response

    async def get(self, key: bytes, range_end: bytes, limit: int = 0):
        response = await self.stub.Range(RangeRequest(
            key=key,
            range_end=range_end,
            limit=limit
        ))
        # logger.info(response)
        for item in response.kvs:
            logger.info(to_string(item.key))
            logger.info(to_string(item.value))
        return response

    async def delete(self, key: bytes, range_end: bytes):
        response = await self.stub.DeleteRange(DeleteRangeRequest(
            key=key,
            range_end=range_end
        ))
        # logger.info(response)
        logger.info(response.deleted)
        return response


def to_bytes(key: Union[str, bytes]):
    if key is None:
        return key
    if isinstance(key, bytes):
        return key
    return bytes(key, encoding="utf8")


def to_string(key: Union[str, bytes]):
    if key is None:
        return key
    if isinstance(key, str):
        return key
    return str(key, encoding="utf8")


def prefix_range_end(prefix):
    """
    https://github.com/kragniz/python-etcd3/blob/master/etcd3/utils.py
    """
    s = bytearray(prefix)
    for i in reversed(range(len(s))):
        if s[i] < 0xff:
            s[i] = s[i] + 1
            break
    return bytes(s)


async def etcd_command(method, *args: Tuple[bytes], **kwargs: Dict):
    async with grpc.aio.insecure_channel("localhost:2379") as channel:
        stub = KVStub(channel=channel)
        etcd = Etcd(stub=stub)

        if method == "get" or method == "del":
            if len(args) > 1:
                key, range_end = to_bytes(args[0]), args[1]
            else:
                key, range_end = to_bytes(args[0]), None
            prefix = kwargs.get("prefix")
            if prefix:
                range_end = prefix_range_end(key)
            key, range_end = to_bytes(key), to_bytes(range_end)

            if method == "get":
                await etcd.get(key=key, range_end=range_end, limit=kwargs.get("limit", 0))
            elif method == 'del':
                await etcd.delete(key=key, range_end=range_end)

        elif method == "put":
            key, value = to_bytes(args[0]), to_bytes(args[1])
            await etcd.put(key, value)

        else:
            logger.error("Unknown command")


@click.group()
def cli():
    pass


@click.command(help="Gets the key or a range of keys")
@click.argument("key", metavar="key", nargs=-1, type=str)
@click.option("--limit", default=0, help="Maximum number of results", type=int)
@click.option("--prefix", is_flag=True, show_default=True, help="Get keys with matching prefix", type=bool)
def get(key, limit, prefix):
    asyncio.run(etcd_command("get", *key, **
                {"limit": limit, "prefix": prefix}))


@click.command(help="Puts the given key into the store")
@click.argument("key", metavar="key")
@click.argument("value", metavar="value")
def put(key, value):
    asyncio.run(etcd_command("put", key, value))


@click.command(name="del", help="Removes the specified key or range of keys [key, range_end)")
@click.argument("key", metavar="key", nargs=-1, type=str)
@click.option("--prefix", is_flag=True, show_default=True, help="delete keys with matching prefix", type=bool)
def delete(key, prefix):
    asyncio.run(etcd_command("del", *key, **{"prefix": prefix}))


cli.add_command(get)
cli.add_command(put)
cli.add_command(delete)


if __name__ == '__main__':
    cli()
