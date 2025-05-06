# tests/test_core.py

import pytest
from corstream import Stream

@pytest.mark.asyncio
async def test_from_iterable_sync():
    result = []

    async def collect(x):
        result.append(x)

    await Stream.from_iterable([1, 2, 3]).for_each(collect)

    assert result == [1, 2, 3]

@pytest.mark.asyncio
async def test_from_iterable_async():
    async def gen():
        for i in range(3):
            yield i

    result = []

    async def collect(x):
        result.append(x)

    await Stream.from_iterable(gen()).for_each(collect)

    assert result == [0, 1, 2]
