# tests/test_to_list.py

import pytest
from corstream import Stream

@pytest.mark.asyncio
async def test_to_list_basic():
    result = await (
        Stream
        .from_iterable([1, 2, 3])
        .map(lambda x: x + 1)
        .to_list()
    )
    
    assert result == [2, 3, 4]
    
@pytest.mark.asyncio
async def test_to_list_empty():
    result = await (
        Stream
        .from_iterable([])
        .to_list()
    )
    
    assert result == []
    
@pytest.mark.asyncio
async def test_to_list_chained_ops():
    result = await (
        Stream
        .from_iterable(range(5))
        .filter(lambda x: x % 2 == 0)
        .map(lambda x: x * 10)
        .to_list()
    )
    
    assert result == [0, 20, 40]
    
@pytest.mark.asyncio
async def test_to_list_batches():
    result = await (
        Stream
        .from_iterable([1, 2, 3, 4])
        .batch(2)
        .to_list()
    )
    
    assert result == [[1, 2], [3, 4]]