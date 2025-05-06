# tests/test_reduce.py

import pytest
from corstream import Stream


@pytest.mark.asyncio
async def test_reduce_sum():
    result = await (
        Stream
        .from_iterable([1, 2, 3, 4])
        .reduce(lambda acc, x: acc + x, 0)
    )
    
    assert result == 10
    
@pytest.mark.asyncio
async def test_reduce_product():
    result = await (
        Stream
        .from_iterable([1, 2, 3, 4])
        .reduce(lambda acc, x: acc * x, 1)
    )
    
    assert result == 24
    
@pytest.mark.asyncio
async def test_reduce_empty():
    result = await (
        Stream
        .from_iterable([])
        .reduce(lambda acc, x: acc + x, 100)
    )
    
    assert result == 100
    
@pytest.mark.asyncio
async def test_reduce_with_filter():
    result = await (
        Stream
        .from_iterable(range(10))
        .filter(lambda x: x % 2 == 0)
        .reduce(lambda acc, x: acc + x, 0)
    )
    
    assert result == 20  # 0 + 2 + 4 + 6 + 8 = 20