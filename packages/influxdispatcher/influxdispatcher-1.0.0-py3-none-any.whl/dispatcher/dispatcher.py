import aiohttp
import requests
from typing import Tuple
from loguru import logger
import asyncio


class Dispatcher:
    @staticmethod
    def _attempt_resend(func, *args, **kwargs):
        result = func(second_run=True, *args, **kwargs)
        return result

    @staticmethod
    def send(
        req_path: str,
        req_method: str,
        headers: dict = None,
        payload: dict = None,
        use_logger: bool = True,
        _second_run: bool = False,
    ) -> Tuple[requests.Response, bool]:
        try:
            retrieved_method = getattr(requests, req_method)
            response = retrieved_method(req_path, headers=headers, json=payload)
            return response, True
        except requests.exceptions.ConnectionError:

            if not _second_run:
                result = Dispatcher._attempt_resend(
                    req_path, req_method, headers, payload
                )
                return result
            else:
                if use_logger:
                    logger.warning(
                        f"Failed {req_path} | {req_method.upper()} | {response.status}, {response.reason}"
                    )
                return response, False
        except requests.exceptions.Timeout:
            if use_logger:
                logger.warning(f"Timeout {req_path} | {req_method.upper()}")
            return response, False


class AsyncDispatcher:
    @staticmethod
    async def _attempt_resend(func, *args, **kwargs):
        result = await func(second_run=True, *args, **kwargs)
        return result

    @staticmethod
    async def send(
        req_path: str,
        req_method: str,
        headers: dict = None,
        payload: dict = None,
        use_logger: bool = True,
        _second_run: bool = False,
    ) -> Tuple[bytes, bool]:
        try:
            async with aiohttp.ClientSession() as session:
                retrieved_method = getattr(session, req_method)
                async with retrieved_method(
                    req_path, headers=headers, json=payload
                ) as response:
                    read_resp = await response.read()
            return read_resp, True
        except aiohttp.ClientResponseError:

            if not _second_run:
                result = await AsyncDispatcher._attempt_resend(
                    req_path, req_method, headers, payload
                )
                return result
            else:
                if use_logger:
                    logger.warning(
                        f"Failed {req_path} | {req_method.upper()} | {response.status}, {response.reason}"
                    )
                return response, False
        except asyncio.TimeoutError:
            if use_logger:
                logger.warning(f"Timeout {req_path} | {req_method.upper()}")
            return response, False
