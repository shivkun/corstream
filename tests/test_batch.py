# tests/test_batch.py

import pytest
from corstream import Stream

@pytest.mark.asyncio
async def test_batch_even():
    result = []
    
    async def collect(batch):
        result.append(batch)
        
    await (
        Stream.from_iterable([1, 2, 3, 4])
        .batch(2)
        .for_each(collect)
    )
    
    assert result == [[1, 2], [3, 4]]
    
@pytest.mark.asyncio
async def test_batch_uneven():
    result = []
    
    async def collect(batch):
        result.append(batch)
        
    await (
        Stream.from_iterable([1, 2, 3])
        .batch(2)
        .for_each(collect)
    )
    
    assert result == [[1, 2], [3]]
    
@pytest.mark.asyncio
async def test_batch_invalid_size():
    with pytest.raises(ValueError):
        Stream.from_iterable([1, 2, 3]).batch(0)